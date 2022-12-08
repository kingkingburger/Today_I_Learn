## ✅ Swagger를 Typescript적용하기

express에서 swagger를 적용해보려고 합니다. 



#### 1. 모듈 설치

```bash
npm install swagger-cli swagger-ui-express
npm install -D @types/swagger-ui-express
```

- swagger-ui-express 는 swagger화면을 보여주게 도와주는 모듈입니다.



#### 2. swagger 적용

우리는 swagger에 우리들의 라우터(컨트롤러)를 적용시켜서 화면에 띄워봐야 합니다.

```
import swaggerUi from 'swagger-ui-express'; //ui 설정할 수 있는 모듈 불러오기
import swaggerJson from '../src/swagger.json'; // api가 세팅된 json파일, yaml 방식도 가능!

const app = express();

// swagger 문서 UI 설정
app.use('/docs', swaggerUi.serve, swaggerUi.setup(swaggerJson));
```

위 코드를 최상위 폴더인 `index.ts`에 넣어서 실행시키면 아래와 같은 화면이 나옵니다.

![image](https://user-images.githubusercontent.com/112359150/206358914-ae91c0d1-de64-4124-ac5f-9b377061a928.png)

#### json import 안될 때 



#### 3. swagger 자동생성 - swagger-autogen

그러면 이제 내가 만든 라우터(컨트롤러)들을 화면에 띄와야 합니다. 하지만 이미 만들어진 라우터를 일일이 json 파일로 만들기에는 힘듭니다. 그래서 이미 만들어둔 라우터를 자동으로 만들어주는 모듈을 쓰면 됩니다. `sagger-autogen`이라는 모듈입니다.

```sh
npm i swagger-autogen
```

swagger-autogen의 모듈을 설치해주면 됩니다.

![image](https://user-images.githubusercontent.com/112359150/206359655-269ec0a2-250e-4d91-84ec-4540a0f5d251.png)

공식문서에서 보여주는 예시입니다. 

우리는 ts 문서로 써야하니 swagger.ts 파일을 만들어야 합니다.

![image](https://user-images.githubusercontent.com/112359150/206360302-f4f67c13-0676-4228-866d-7f0443ba6afd.png)

swagger.ts 파일 입니다.  여기서 import 에러가 날 수도 있습니다. 그러면 `tsconfig.json`에 가서 `compilerOptions`안에 `esModuleInterop`, `resolveJsonModule`를 true로 해주시면 됩니다.

최상위 index.ts(express가 선언된 곳) 문서와 같은 위치에 swagger라는 폴더를 만들고 그안에 swagger 설정파일을 만들었습니다. 

- **outputFile**은 swagger-autogen이 라우터를 돌아다니면서 json파일을 출력할 곳을 정합니다. 
- **endpointsFiles**는 swagger-autogen이 어떤 파일을 돌아다닐까 설정하는 곳입니다.

endpointsFiles에 routes폴더 안에 있는 모든 ts파일들을 돌아다니라고 명령했습니다.

이제 이 파일을 node가 실행하라고 명령을 내려주면 됩니다. ts파일을 swagger-autogen로 실행시키는 방법은 

```js
ts-node ./src/swagger/swagger.ts
```

ts-node를 써주면 됩니다. ts 파일을 실행시키기 위해서는 `ts-node` 명령어를 써야합니다.

계속 콘솔창에 쓰면 귀찮으니깐 package.json 파일에 스크립트로 등록합니다.



package.json 파일

```json
"swagger-autogen": "ts-node ./src/swagger/swagger.ts"
```

```sh
npm run swagger-autogen
```

으로 swagger를 자동생성해줍시다.



#### 출처

- https://rsbh.dev/blogs/rest-api-with-express-typescript