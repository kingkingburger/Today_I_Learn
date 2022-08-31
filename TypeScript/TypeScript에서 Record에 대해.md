## TypeScript에서 Record에 대해

#### Record Type이란?

TypeScript는 Version 2.1부터 Utility Type인 Record Type을 도입했습니다. Record Type은  

**Record <Key, Type> 형식**으로 키가 Key이고 값이 Type인 객체 타입입니다.



어디서 많이 본 형식 입니다. 마치 **java**에서 **Map**과 비슷한 형상을 띄었습니다. 



### **Record Type vs Index Signature(기존)**

TypeScript에서 **인덱스 시그니처(Index Signature)**는 **대괄호**로 객체를 접근하는 방법입니다.

다음은 **인덱스 시그니처**를 사용하여 객체를 생성해봅시다.

```js
type humanInfo = { 
  [name: string]: number 
};

let human:humanInfo = {
  '홍길동': 20,
  '둘리': 30,
  '마이콜': 40
};
```

위에서 작성한 인덱스 시그니처 예제는 **Record Type**으로 바꿔 봅시다.

```js
type humanInfo = Record<string, number>

let human:humanInfo = {
  '홍길동': 20,
  '둘리': 30,
  '마이콜': 40
};
```

**Record Type**과 **인덱스 시그니처**는 상당히 비슷해 보입니다. 그러나 구문 관점에서 **인덱스 시그니처**가 더 좋습니다. **인덱스 시그니처**에서 **name이라는 Key**가 의도를 명확하게 표현하기 때문입니다. Record Type 에서는 <key, value> 로 앞에 있는 것은 무조건 key로 생각하면 됩니다.



 **▶ Record Type이 유용한 이유**

인덱스 시그니처의 단점으로 **문자열 리터럴을 Key로 사용하는 경우 오류**가 발생합니다.

```js
type humanInfo = { 
  [name: '홍길동' | '둘리' | '마이콜']: number 
};
```

이런식으로 key의 타입을 정하면 오류가 납니다.

**실행 결과**

![[TypeScript]Record Type 사용 방법 - undefined - Record Type vs Index Signature](https://blog.kakaocdn.net/dn/dfS6mE/btrotlUYUS8/C74QRiRso0q9kJnKOVNqvk/img.png)



 

하지만, **Record Type**은 Key로 **문자열 리터럴**을 허용합니다. **Record Type**은 속성을 제한하고 싶은 경우 문자열 리터럴을 사용하여 Key에 허용 가능한 값을 제한합니다.

```js
type names = '홍길동' | '둘리' | '마이콜';

type humanInfo = Record<names, number>

let human:humanInfo = {
  '홍길동': 20,
  '둘리': 30,
  '마이콜': 40
};
```

또 다른 기능으로는 **TypeScript Version 2.9**부터 **열거형을 Key**로 사용할 수 있습니다. 문자열 리터럴보다 코드가 깔끔하다는 장점이 있습니다.

```js
enum names {
  "홍길동" = 1,
  "둘리" = 2,
  "마이콜" = 3
}

type humanInfo = Record<names, number>;

let human: humanInfo = {
  1: 20,
  2: 30,
  3: 40
};
```

------

### **keyof와 Record Type을 같이 사용**

`keyof` 키워드는 타입 또는 인터페이스에 존재하는 **모든 키 값을** **union 형태**로 가져옵니다.

```js
type keyType = {
  a: string,
  b: number
};

// Key의 타입은 "a" | "b"
type Key = keyof keyType;
```

 

다음은 Record Type을 `keyof`와 같이 사용하는 예제입니다.

```js
type humanType = {
  name: string;
  age: number;
  address: string;
};

type humanRecordType = Record<keyof humanType, string>;

let human: humanRecordType = {
  name: "또치",
  age: "20",
  address: "서울"
};
```

위 예제처럼 기존 타입의 속성 이름을 **Reocrd Type**의 Key 타입으로 하고 싶은 경우 `keyof`와 함께 사용할 수 있습니다.



#### 출처

 https://developer-talk.tistory.com/296 [평범한 직장인의 공부 정리:티스토리]