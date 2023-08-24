# nest에서 typeorm을 활용해서 db 2개 연결하는법

nestjs를 사용하고 typeorm 0.3 버전을 기준으로 설명하겠습니다. 2개 이상의 데이터베이스를 설정하고 연결할 준비가 되었다고 생각하고 진행하겠습니다.

보통은 nest에 1개의 db를 연결하는데요. 여러개의 db를 같이 활용하고 싶을 때가 있습니다. 그러면 typeorm의 설정을 알려드리겠습니다.

### 기존연결의 문제

```tsx
...
@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'mysql',
      host: 'localhost',
      port: 3306,
      username: 'root',
      password: 'root',
      database: 'test',
      entities: [Customer],
      synchronize: true,
    }),
  ],
})
...
```

기본적인 세팅방법입니다. 여기에 env 파일 설정하고 싶다면 아래와 같이 하면 됩니다

```tsx
...
@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
    }),
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService],
      useFactory: async (configService: ConfigService) => {
        return {
          type: 'mssql',
          host: configService.get('MAIN_DB_HOST'),
          port: parseInt(configService.get('MAIN_DB_PORT')),
          database: configService.get('MAIN_DB_DATABASE'),
          username: configService.get('MAIN_DB_USERNAME'),
          password: configService.get('MAIN_DB_PASSWORD'),
          schema: configService.get('MAIN_DB_SCHEMA'),
          entities: [Customer],
          synchronize: false,
        };
      },
    }),
...
```

이렇게 연결하면 typeorm에서 configService를 사용할 수 있습니다.

여기서 중요한 점은 연결의 이름을 정의할 필요가 없습니다. 기본적으로 `default` 로 연결이 됩니다.

[nest 문서](https://docs.nestjs.com/techniques/database#multiple-databases)에서 name 설정을 다른 database 설정과 같은 레벨 안에 넣으라고 했습니다.

```tsx
const defaultOptions = {
  type: 'postgres',
  port: 5432,
  username: 'user',
  password: 'password',
  database: 'db',
  synchronize: true,
};

@Module({
  imports: [
    TypeOrmModule.forRoot({
      ...defaultOptions,
      host: 'user_db_host',
      entities: [User],
    }),
    TypeOrmModule.forRoot({
      ...defaultOptions,
      name: 'albumsConnection',
      host: 'album_db_host',
      entities: [Album],
    }),
  ],
})
export class AppModule {}
```

중요한 점이 있습니다. multiple datablae를 사용하려면 forRootAsync를 사용해야 합니다.

forRootAsync를 사용하기 위해 name을 useFactory 바깥에다가 넣어야 합니다.

app.module.ts

```tsx
import { Module } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AccessLog } from './access-log/access-log.entity';
import { AccessLogModule } from './access-log/access-log.module';
import { CustomerModule } from './customer/customer.module';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
    }),
    // MAIN DB CONNECTION
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService],
      useFactory: async (configService: ConfigService) => {
        return {
          type: 'mssql',
          host: configService.get('MAIN_DB_HOST'),
          port: parseInt(configService.get('MAIN_DB_PORT')),
          database: configService.get('MAIN_DB_DATABASE'),
          username: configService.get('MAIN_DB_USERNAME'),
          password: configService.get('MAIN_DB_PASSWORD'),
          schema: configService.get('MAIN_DB_SCHEMA'),
          entities: [Customer],
          synchronize: false,
        };
      },
    }),
    // SECONDARY DB CONNECTION
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService],
      name: 'secondaryDB',
      useFactory: async (configService: ConfigService) => {
        return {
          type: 'mssql',
          database: configService.get('SECONDARY_DB_DATABASE'),
          host: configService.get('SECONDARY_DB_HOST'),
          authentication: {
            type: 'default',
            options: {
              userName: configService.get('SECONDARY_DB_USERNAME'),
              password: configService.get('SECONDARY_DB_PASSWORD'),
            },
          },
          entities: [AccessLog],
        };
      },
    }),
    CustomerModule,
    AccessLogModule,
  ],
})
export class AppModule {}
```

mysql과 mssql이 있는데요. mssql에는 secondaryDB라는 connection name을 붙여주었습니다.

### 기존 DB 사용방법

기존 방법과 똑같이 사용해도 됩니다.

```tsx
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Customer} from './entity';
import { CustomerController } from './customer.controller';
import { CustomerService } from './customer.service';

@Module({
  imports: [
    TypeOrmModule.forFeature([Customer]),
  ],
  controllers: [CustomerController],
  providers: [CustomerService],
})
export class CustomerModule {}
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Customer } from './entity/customer.entity';

@Injectable()
export class CustomerService {
  constructor(
    @InjectRepository(Customer)
    private customerRepository: Repository<Customer>,
  ) {}

  async getCustomerById(id: number, user: any) {
    return await this.customerRepository.findOne({ ID: id });
  }
}
```

### 두 번재 DB 사용방법

```tsx
import { Global, Module } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AccessLogController } from './access-log.controller';
import { AccessLog } from './access-log.entity';
import { AccessLogService } from './access-log.service';

@Global()
@Module({
  imports: [TypeOrmModule.forFeature([AccessLog], 'secondaryDB')],
  providers: [AccessLogService, ConfigService],
  controllers: [AccessLogController],
  exports: [AccessLogService],
})
export class AccessLogModule {}
import { Injectable, Logger } from '@nestjs/common';
import { CreateAccessLogDto } from './dto/create-access-log.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { AccessLog } from './access-log.entity';
import { Repository } from 'typeorm';

@Injectable()
export class AccessLogService {
  private readonly logger = new Logger(AccessLogService.name);

  constructor(
    @InjectRepository(AccessLog, 'secondaryDB')
    private accessLogRepository: Repository<AccessLog>,
  ) {}

  create(createAccessLogDto: CreateAccessLogDto) {
    try {
      this.accessLogRepository
        .createQueryBuilder()
        .insert()
        .into(AccessLog)
        .values([createAccessLogDto])
        .execute();
    } catch (error) {
      this.logger.error(`Failed to create access log record. ${error.message}`);
    }
  }
}
```

typerom 객체를 만들 때 connection이 secondaryDB라는 것을 꼭 적어주셔야 합니다. 적지 않으면 typeorm 객체는 default connection을 사용하게 됩니다.