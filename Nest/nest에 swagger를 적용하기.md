## nest에 swagger를 적용하기

[OpenAPI (스웨거) | NestJS - 프로그레시브 Node.js 프레임워크](https://docs.nestjs.com/openapi/introduction)

공식문서를 보고 따라했습니다.

### **설치[#](https://docs.nestjs.com/openapi/introduction#installation)**

사용 시작하려면 먼저 필요한 종속성을 설치합니다.

```
$ npm install --save @nestjs/swagger
```

설치 프로세스가 완료되면 파일을 열고 클래스를 사용하여 Swagger를 초기화합니다.



main.ts

```
import { NestFactory } from '@nestjs/core';
import { SwaggerModule, DocumentBuilder } from '@nestjs/swagger';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  const config = new DocumentBuilder()
    .setTitle('Cats example')
    .setDescription('The cats API description')
    .setVersion('1.0')
    .addTag('cats')
    .build();
  const document = SwaggerModule.createDocument(app, config);
  SwaggerModule.setup('api', app, document);

  await app.listen(3000);
}
bootstrap();
```

```
$ npm run start
```

응용 프로그램이 실행되는 동안 브라우저를 열고 `http://localhost:3000/api` 로 이동합니다. Swagger UI가 표시됩니다



![swagger1.png (1349×630)](https://docs.nestjs.com/assets/swagger1.png)