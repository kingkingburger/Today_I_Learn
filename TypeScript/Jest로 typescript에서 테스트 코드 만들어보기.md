## ✅ Jest로 typescript 테스트 코드 만들어보기

테스팅 도구인 jest를 사용하면 javascript, typescript파일에서 작성한 코드를 테스트 할 수 있습니다

jest와 Mocha라는 테스트 프레임워크가 있다고 합니다.  Jest는 추가 종속성이 필요하지 않은 단일 독립 테스트 프레임워크로 작동하도록 되어 있습니다. 반면에 Mocha는 제대로 작동하기 위해 함께 통합된 여러 라이브러리가 필요합니다.

jest가 배우기 쉽다고 하여 jest로 테스트를 진행해보기로 하겠습니다.





#### 🔷초기 설정

### 👉 jest를 위한 라이브러리 설치하기

```shell
npm i jest @types/jest ts-jest typescript -D
```

1. jest

   단위 테스트 프레임워크

2. @types/jest

   - jest 의 타입스크립트 버전

3. ts-jest

   - jest의 ts 모듈

4. typescript

   - 타입 스크립트 모듈



### 👉 Jest 설정

- jest.config.js를 루트 폴더에 만듭니다.

```ts
//jest.config.js
module.exports = {
  preset: "ts-jest", //trypeScript파일은 ts-jest에서 CommonJS구문으로 변환
  testEnvironment: "node", //테스트 환경
  testMatch: ["**/*.spec.[jt]s?(x)", "**/*.test.[jt]s?(x)"], //테스트 파일 위치
};
```



### 👉 테스트용 파일 만들기

![image](https://user-images.githubusercontent.com/112359150/204428250-7a437613-b49e-4598-afc9-7e2c8934396d.png)

테스트할 파일이름을 `{파일이름}.test.js` 로 만듭니다.



```js
class Person {
  name: string;
  age: number;
  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  isAdult() {
    return this.age >= 18;
  }
}

export { Person };
```

test8.ts의 내용입니다. Person이란 사람 클래스를 만들고 export하고 있습니다.



```ts
import { Person } from "./test8";

describe("사람 유닛 테스트", () => {
  let person: Person;

  beforeEach(() => {
    person = new Person("민호", 25);
  });

  test("어른일 것이다", () => {
    expect(person.isAdult()).toBeDefined();
    expect(person.isAdult()).toBe(true);
  });
});

describe("pow 테스트", () => {
  test("주어진 숫자의 n 제곱", () => {
    const pow = Math.pow(2, 3);
    expect(pow).toEqual(8);
  });
});
```

test8.test.ts의 파일입니다.



**describe(name, function)**

-  여러 관련 테스트를 그룹화하는 블록입니다.

**beforeEach(function)**

-  테스트가 실행되기 전 실행되는 부분입니다. 객체를 초기화 할때  쓸 수 있습니다.

**test(name, fn, timeout)** 

- it(name, fn, timeout) 과 비슷합니다.
- 각각의 유닛 테스트에 필요한 가장 작은 단위의 테스트 단위입니다. 또한 4가지 메서드들은 메서드 체인을 통해 추가적인 기능을 수행할 수 있습니다.
- 테스트 이름을 적고 테스트할 function을 넣어줍니다.

**expect()**

- 말 그대로 기대하는 객체입니다. 
- 그 뒤에 있는 메서드는 정말 많습니다. toBe(value) , toBeNull().... 등등. 공식문서를 참조해서 필요한 상황에 맞는 매서드를 선택합니다.   
  - [expect() 에 대한공식문서](https://jestjs.io/docs/expect) 





### 😮 자주쓰는 문법들

### 👉 toBeTruthy(), toBeFalsy()

많이 사용되는 Matcher 함수는 아마도 `toBeTruthy()` 와 `toBeFalsy()`일 것입니다. 많은 분들이 아시다시피 느슨한 타입 기반 언어인 자바스크립트는, 자바같은 강한 타입 기반 언어처럼 `true`와 `false`가 boolean 타입에 한정되지 않습니다.

따라서 숫자 `1`이 `true`로 간주되고, 숫자 `0`이 `false`로 간주되는 것과 같이 모든 타입의 값들을 `true` 아니면 `false` 간주하는 규칙이 있습니다. `toBeTruthy()`는 검증 대상이 이 규칙에 따라 `true`로 간주되면 테스트 통과이고, `toBeFalsy()`는 반대로 `false`로 간주되는 경우 테스트가 통과됩니다.

```js
test("숫자형 0은 false고 문자열0은 true다", () => {
  expect(0).toBeFalsy();
  expect("0").toBeTruthy();
});
```





### 👉 toHaveLength(), toContain

배열에 매개변수로 들어오는 값이 있는지 없는지 확인 해줍니다. 

toHaveLength()는 **배열의 길이를 체크**하고, toContain()은 **배열안에 특정 값을 체크**합니다.

```ts
test("배열에 있는지 없는지 채크", () => {
  const colors = ["Red", "Yellow", "Blue"];
  expect(colors).toHaveLength(3);
  expect(colors).toContain("Yellow");
  expect(colors).not.toContain("Green");
});
```

자세히 보시면 마지막 테스트에  **not.toContain()**이란것이 있습니다. `not` Matcher이란 것인데요. 이처럼 어떤 Matcher함수가 불만족하는지를 테스트할 때는 앞에 not을 붙여주면 됩니다.



### 👉 toBe(), toMatch()

문자열을 테스트할 때 toBe()를 사용해서 문자열이 정확히 일치하는지 테스트합니다.

또한 문자열을 비교할 때 정규식을 사용할 때가 있습니다. **toMatch()**함수로 특정 문자열을 정규식으로 테스트할 수 있습니다.

```ts
function getUser(id: number) {
  return {
    id,
    email: `user${id}@test.com`,
  };
}

test("정규식 기반 문자열 테스트 해보기", () => {
  expect(getUser(1).email).toBe("user1@test.com");
  expect(getUser(2).email).toMatch(/.*test.com$/);
});
```



### 👉 toThrow()

```ts
function getUser(id: number) {
  if (id <= 0) throw new Error("Invalid Id");
  return {
    id,
    email: `user${id}@test.com`,
  };
}

test("예외처리 테스트", () => {
  expect(getUser(-1)).toThrow();
  expect(getUser(-1)).toThrow("Invalid Id");
});
```

예외 발생 여부도 테스트를 할 수 있습니다. getUser함수는 0이 들어올 때 Error를 반환합니다.

toThrow() 함수로 에러 발생여부를 테스트할 수 있습니다. toThrow() 함수는 인자도 받는데 문자열을 넘기면 예외 메세지를 비교하고 정규식을 넘기면 정규식 체크를 해줍니다.

하지만 위 테스트를 진행하면 테스트가 실패하게 됩니다.



```
function getUser(id: number) {
  if (id <= 0) throw new Error("Invalid Id");
  return {
    id,
    email: `user${id}@test.com`,
  };
}

test("예외처리 테스트", () => {
  expect(() => getUser(-1)).toThrow();
  expect(() => getUser(-1)).toThrow("Invalid Id");
});
```

toThrow() 함수를 사용할 때 주의해야 할 점입니다. expect() 함수에 **검증 대상을 함수로 한 번 감싸줘야** 합니다. 왜냐하면 예외 발생 여부를 체크하는 것이 아니라, 테스트 실행도중 진짜로 함수를 실행할 때 예외가 발생하기 때문에 테스트가 항상 실패하기 때문입니다.



[공식문서](https://jestjs.io/docs/getting-started)





#### 출처

- https://www.js2uix.com/frontend/jest-study-step2/ <다양한 jest의 문법을 한글로 알려주는 고마운 사이트 입니다.

- https://mong-blog.tistory.com/entry/jest%EB%A1%9C-typescript-%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%95%98%EA%B8%B0-1%EA%B8%B0%EB%B3%B8%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0
- https://yonghyunlee.gitlab.io/temp_post/jest/
- https://rutgo-letsgo.tistory.com/289
- https://www.daleseo.com/jest-basic/
