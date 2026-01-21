코드상에 많은 try-catch문에 의문이 들었어요. 에러를 보내는데 왜 모든 함수들마다 try-catch가 있는것인가? 계속 써야하는가? 안써도 되는 방법은 없는가? 를 살펴봐요.

이해를 쉽게하기 위해 간단한 코드를 만들어봤어요.
```
export const throwErrorFunction = () => {
    throw new Error("An error occurred");
}

const catchingFunction2 = () => {
    throwErrorFunction();
}

const catchingFunction = () => {
    try {
        catchingFunction2();
    } catch (error) {
        console.log("do nothing");
    }
}

const notCatchingFunction = () => {
    catchingFunction2();
}

catchingFunction();
notCatchingFunction();
```
### 왜 모든 함수들마다 try-catch가 있는것인가? 계속 써야하는가?
js의 에러는 catch를 만날 때 까지 호출한 곳(caller)으로 계속 던져집니다
- 1. **`throwErrorFunction()` 실행:** 에러를 `throw` 합니다.
- 2. **`catchingFunction()` 내부:**
    - `throwErrorFunction`을 호출했지만 `try-catch`가 없습니다.
    - 따라서 에러가 발생한 시점에서 **즉시 함수 실행을 중단**하고, 자신을 호출한 곳(Global scope)으로 에러를 토스합니다.
- 3. **최상위 레벨 (Global Scope):**
    - `catchingFunction()`을 호출했지만, 여기서도 `try-catch`가 없습니다.
    - 더 이상 에러를 보낼 상위 호출자가 없으므로, **런타임(Node.js 또는 브라우저)이 이 에러를 처리**합니다.


### 실행 후 어떻게 처리되냐면
- nodejs 환경: Uncauch Error 메세지가 출력되고, 프로세스가 강제 종료됩니다.(서버가 죽어요)
- 브라우저 환경: 콘솔창에 에러가 뜨고, 뒤에 있는 js 코드는 실행되지 않습니다.

### 그래서 어떤식으로 써야하는 건가?
무조건 바로 위에서 잡을 필요는 없지만, **어딘가에서는 반드시 잡아야** 안전한 프로그램이 됩
니다.

제가 쓰는 ts 서버는 여러군데에 try-catch가 많이 쓰여져 있답니다. 중요한 로직의 흐름을 보고싶은데 try-catch가 가독성을 해치는 경우가 있죠. 그래서 저는 `global error handling` 하는 방식을 찾아봤어요
bun + hono 인 서버경우에 예시를 보여드리면
```
import { Hono } from 'hono';
import { HTTPException } from 'hono/http-exception';

const app = new Hono();

// ==========================================
// 1. Service (비즈니스 로직)
// ==========================================
// 상황에 맞는 에러를 그냥 던집니다.
const getUserService = (id: string) => {
  if (id === 'error') {
    // 500 에러 테스트용
    throw new Error('의도치 않은 DB 에러 발생!');
  }
  
  if (id !== '1') {
    // 404 에러: Hono 내장 예외 사용
    throw new HTTPException(404, { message: '해당 유저를 찾을 수 없습니다.' });
  }

  return { id: '1', name: 'Gemini' };
};

// ==========================================
// 2. Controller (라우트 핸들러)
// ==========================================
// try-catch 없이 깔끔하게 작성합니다.
app.get('/users/:id', (c) => {
  const id = c.req.param('id');
  
  // 에러가 발생하면 여기서 실행이 중단되고 onError로 점프합니다.
  const user = getUserService(id);
  
  return c.json({ success: true, data: user });
});

// ==========================================
// 3. Global Error Handling (최상위 방어선)
// ==========================================
app.onError((err, c) => {
  // 1. 우리가 의도적으로 던진 HTTP 에러인 경우 (예: 404, 400)
  if (err instanceof HTTPException) {
    return c.json({
      success: false,
      message: err.message,
    }, err.status);
  }

  // 2. 예상치 못한 시스템 에러인 경우 (예: DB 연결 실패, 코드 버그) -> 500 처리
  console.error('System Error:', err); // 로깅 (Sentry 등을 여기에 연결)
  
  return c.json({
    success: false,
    message: 'Internal Server Error', // 보안상 상세 내용은 숨김
  }, 500);
});

export default app;
```
service, handler 같은 비지니스 로직을 관리하는 곳에서 에러 상황이 오면 던저버리고 최종 error 관리하는 곳에서 한번에 관리하는거에요. 
물론 에러가 발생하고 처리해야 하는 상황일 때는 try-catch를 써야죠. 저는 가독성, 관심사의 분리로 한가지 일만 잘하는 함수를 만드는게 목표였어요.

### 컴파일 타임에 throw가 없으면 잡아줄 수 없을까?
왜 런타임에서만 잡아주냐구요.  컴파일 언어에서는 throw가 있을 때 catch 하는 곳이 없다면 컴파일이 안된데요. 부럽다. 비슷하게 하는 방법을 찾아왔어요. 요즘 rust를 배우고 있어요. Rust는  Result 패턴이라는 것으로 객체 형태를 정의해서 리턴을 해줘요. go도 비슷하다고 하네요?
```
// 성공과 실패를 나타내는 타입 정의
type Success<T> = { success: true; data: T };
type Failure = { success: false; error: Error };
type Result<T> = Success<T> | Failure;

function explicitFunc(): Result<string> {
  const isError = Math.random() > 0.5;

  if (isError) {
    return { success: false, error: new Error("실패했습니다!") };
  }
  return { success: true, data: "성공 데이터" };
}

const response = explicitFunc();

// [컴파일 에러 발생!]
// success 여부를 확인하기 전에는 data에 접근할 수 없습니다.
// console.log(response.data); 

// [해결책]
if (response.success) {
  // TypeScript가 여기서 자동으로 타입을 좁혀줍니다 (Type Narrowing)
  console.log(response.data); 
} else {
  console.log(response.error.message);
}
```
성공과 실패를 나타나내는 타입을 정의하고. 반환 타입으로 Result 타입을 주는거에요. Result 타입을 받은 값은 무조건 핸들링해야되요. result안에 data를 쓰려면 sucess를 확인해야하죠. 없다면 에러처리도 해야되요. 자연스럽게 sucess라는 값으로 에러처리를 하게 됩니다.
이런 패턴을 Result 패턴이라고 해요. Result패턴도 연습해서 체화시켜야겠어요.