## nest와 redis를 연결

nest와 redis를 연결하는것에 초점을 맞춘 글입니다. nest에서 여러가지 방법으로 redis를 연결해도 된다고 하지만 너무 다양한 방법이 있어 오히려 혼란스러웠기 때문에 제일 간단한 방법으로 소개해드리겠습니다.

[redis에 대한 자세한 정보](https://www.zerocho.com/category/NodeJS/post/5a3238b714c5f9001b16c430)

 

 

 

### 🟩redis 설치

npm i redis를 설치하시면 됩니다. 

pnpm이면 pnpm i redis 으로 하시고 bun이면 bun i redis 로 설치하면 됩니다.

 

#### 🟩 redis 폴더 만들기

app.module.ts 파일에다가 직접 redisModule을 연결할 수도 있지만 더 깔끔한 방법을 위해 redis를 관리하는 폴더, 모듈화를 했습니다.



![img](https://blog.kakaocdn.net/dn/I1K9c/btsydpmpSzI/jJRrRFKq631gUQ6p6PYvb0/img.png)



 

🟦 redis.provider.ts

```
import { createClient } from 'redis';

export const redisProvider = [
  {
    provide: 'REDIS_CLIENT',
    useFactory: async () => {
      const client = createClient({
        url: 'redis://localhost:6379',
      });
      await client.connect();
      return client;
    },
  },
];
```

redis로 redisProvider를 만들었습니다. nest에서는 이를 커스텀 provider라고 부릅니다.

redis를 연결하면서 뭔가 어색한 부분이 있었는데요 프로토콜은 http가 아닌 redis를 사용한다는 것이었습니다. 하도 url만 보니 다른 프로토콜이 어색하게 느껴집니다.



또 이상하게 여기는 부분이 있을 수 있는데요. 바로 배열로 provider를 만들었다는 것입니다. 왜냐하면 여러개의 redis를 연결시키기 위해확장성 있게 구조화 한 것입니다.

 

예를들면

```
import { createClient } from 'redis';

export const redisProvider = [
  {
    provide: 'REDIS_CLIENT',
    useFactory: async () => {
      const client = createClient({
        url: 'redis://localhost:6379',
      });
      await client.connect();
      return client;
    },
  },
  {
    provide: 'REDIS_CLIENT2',
    useFactory: async () => {
      const client = createClient({
        url: 'redis://localhost:6380',
      });
      await client.connect();
      return client;
    },
  },
];
```

이렇게 쓸 수도 있을 것입니다.

 

 

 

🟦 redis.module.ts

```
import { Module } from '@nestjs/common';
import { redisProvider } from './redis.provider';

@Module({
  providers: [...redisProvider],
  exports: [...redisProvider],
})
export class RedisModule {}
```

redisProvider는 배열입니다.

구조분해 할당해서 nest에 주입시켜줍시다.

 

 

#### 🟩 사용할 때 

```
@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    AModule,
    BModule,
    CModule,
    RedisModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule implements NestModule {

}
```

어떤 모듈이든 상관없습니다. RedisModule을 import 시켜주기만 하면 REDIS_CLIENT 이름으로 된 redis 객체를 사용할 수 있습니다.

 

app.service.ts

```
@Injectable()
export class AppService {
  constructor(
    private readonly configService: ConfigService, // @Inject('CUSTOM_KEY') private readonly customValue,
    @Inject('REDIS_CLIENT')
    private readonly redis: RedisClientType,
  ) {}

  async redisTest() {
    this.redis.set('key', 'value');
    const value = await this.redis.get('key');
    return value;
  }

  getHello(): string {
    return this.configService.get('SECRET');
  }
  getHello2(): string {
    return 'Hello World!';
  }
}
```

이렇게요.

 

저는 한발 더 나아갔습니다... 사실 redis를 계속 주입해서 사용하면 되는데요. 저는 redis의 기능만 모아둔 redis.service를 만들고 싶었습니다. redis 역할만 가진 service를 만들어보겠습니다.

 

🟦 redis.service.ts

```
import { Inject, Injectable } from '@nestjs/common';
import { RedisClientType } from 'redis';

@Injectable()
export class RedisService {
  constructor(
    @Inject('REDIS_CLIENT') private readonly redis: RedisClientType,
  ) {}

  async set(key: string, value: string) {
    return await this.redis.set(key, value);
  }

  async get(key: string) {
    return await this.redis.get(key);
  }
}
```

provider와 별반 다를게 없는 구조같은데요. Service 클래스에 redis 객체를 주입시킵니다.

다른 모듈에서 사용할 때 RedisService 형태로만 사용할 수 있게됩니다.

 

 

🟦 redis.module.ts

```
import { Module } from '@nestjs/common';
import { redisProvider } from './redis.provider';

@Module({
  providers: [...redisProvider, RedisService],
  exports: [...redisProvider],
})
export class RedisModule {}
```

providers에 RedisService를 넣어줍니다.

 

 

#### 🟩 사용할 때 

```
@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),
    AModule,
    BModule,
    CModule
  ],
  controllers: [AppController],
  providers: [
     AppService
      RedisService,
    ...redisProvider
    ],
})
export class AppModule implements NestModule {

}
```

service는 providers에 넣어줘야 합니다. Service객체를 만들기위해서는 redisProvider를 주입시켜줘야 하기 때문에 같이 써줘야 합니다.(사용할 때 마다 계속 2개씩 같이 써줘야함)

 

```
@Injectable()
export class AService {
  constructor(
    private redisService: RedisService,
  ) {}
```

2개씩 쓰는 귀찮은 대가로 this.redisService를 쓸 수 있게됩니다.

 

 

 

#### 🧨 참고



![img](https://blog.kakaocdn.net/dn/bGzT0N/btsynDwScgz/Q2EC3QBZchNmOgmVpUIU8k/img.png)



저는 pnpm을 사용하고 있고 redis를 다운받았는데요 import 에러가 자꾸 뜨더라고요; 하지만 실행은 잘됩니다. webstorm 문제인지...