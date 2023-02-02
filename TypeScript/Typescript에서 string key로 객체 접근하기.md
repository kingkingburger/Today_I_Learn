# Typescript에서 string key로 객체 접근하기

```tsx
interface Person {
  name: string,
  age: number,
}
const testFunction = (testObj:Person, objectName: string) =>{
	console.log(testObj); // { name:'minho', age:25 }
}

constmin= { name: 'minho', age: 25};

testFunction(min, 'age');
```

위와 같은 상태에 있습니다.

testFunction()을 호출했을 때 저는 매개변수로 들어온 testObj의 name만 필요한 상황입니다. 어떻게 할까요?

물론 `[testObj.name](<http://testObj.name>)` 을 하면 됩니다. 저는 매개변수로 들어오는 `objectName` 로 객체안의 요소를 뽑아내고 싶습니다.

### 🟩 접근 1. 배열 접근자

javascript에서도 **점(.) 표기법**과 **대괄호( [] ) 표기법**을 사용하여 접근합니다.

```jsx
var objProperties = 'title'

var obj = {
  title : 'Java'
}

// 점 표기법
console.log(obj.title);
// Java

// 대괄호 표기법 1. 문자열로 접근
console.log(obj['title']);
// Java

// 대괄호 표기법 2. 변수로 접근
console.log(obj[objProperties]);
// Java
```

이런 방식에서 대괄호 표기법으로 접근해보면

```tsx
interface Person {
  name: string;
  age: number;
}

const testFunction = (
  testObj: Person | { objectName: string },
  objectName: string
) => {
console.log(testObj[objectName]); // 에러발생!
};

constmin= { name: "minho", age: 25 };

testFunction(min, "age");
```

에러가 발생합니다.

TS7053: Element implicitly has an 'any' type because expression of type 'string' can't be used to index type 'Person | { objectName: string; }'. No index signature with a parameter of type 'string' was found on type 'Person | { objectName: string; }'.

위 에러는 Typescript의 `string literal` 타입만 들어갈 수 있는 곳에 `string` 을 넣었기 때문입니다.

### 🥽 string literal vs string 에 대해서

다음과 같은 TypeScript 코드가 있다. `b`와 `c`은 string 타입이 맞지만, `a`은 `"Hello World"` 타입입니다.(string literal) [Type Script Playground](https://www.typescriptlang.org/play?#code/MYewdgzgLgBAFgUwDZJAdRAJyQEwIwwC8MARABLKowbY4kCwAUEgrIiulrgExGkUdqXOk1CQ2lTrQDMALhjRMASzABzPuUlDaJIA)에서 각 변수명에 mouse over하면 타입을 확인할 수 있습니다.

```jsx
const a = "Hello World"
let b = "Hello World"
const c: string = "Hello World"
```

`b` 변수는 `let`으로 선언되어 재할당될 수 있을 경우 어떤 문자열이든 넣을 수 있으며 그 경우의 수가 무한대입니다. 그렇기 때문에 컴파일러는 이 변수를 string 타입으로 추론합니다.

`c` 변수는 명시적으로 string 타입으로 선언했으므로 그냥 string 타입입니다.

`a`의 경우는 컴파일러는 이 변수를 `string`이 아닌 조금 더 좁은 타입(narrowed type)으로 선언한 것으로 추론합니다. 이 것을 [Literal Narrowing](https://www.typescriptlang.org/docs/handbook/literal-types.html#literal-narrowing)이라고 합니다.

`a`의 타입은 string이 아니라 string타입을 좁혀 만든 [string literal type](https://www.typescriptlang.org/docs/handbook/literal-types.html)이라고 합니다. 여기서 "타입을 좁힌다"는 말의 의미는 무한대의 경우의 수를 가질 수 있는 string타입보다 훨씬 구체적인 string의 부분집합, `"Hello World"`만을 허용하는 타입이 됩니다. 즉, `a` 의 타입은 `"Hello World"` 입니다.

따라서 아래와 같이 명시적으로 literal type을 선언하면 `let`으로 선언된 변수도 `"Hellow World"` 타입만을 허용하도록 만들 수도 있습니다.

```jsx
type HelloWorldType = "Hello World"; // literal type

let a: HelloWorldType = "Hello World"; // ok
a = "minho"; // TS2322: Type '"minho"' is not assignable to type '"Hello World"'.
```

### 그러면 우리는 string 대신 string literral을 써야합니다.

typescript의 ****`Index Signature`** 기능이 있습니다.

```tsx
type ObjType = {
  [key: string]: string  
  foo: string
  bar: string
}

const obj: ObjType = {
  foo: "hello",
  bar: "world",
}

const propertyName1 = "foo"
const propertyName2: string = "foo"

console.log(obj[propertyName1]) // ok
console.log(obj[propertyName2]) // ok
```

이런식으로 쓰는데요. `ObjType` 의 **key는 string**이고 **value는 string**이라는 것을 알려줍니다.



## 🟩 접근2. string literral 사용하기

제가 생각해낸 방법은

```tsx
interface Person {
  name: string;
  age: number;
}

const testFunction = (testObj: Person, objectName: string) => {
  const inFunctionTestObj = testObj as Person & { [key: string]: string };
  console.log(inFunctionTestObj[objectName]);
};

constmin= { name: "minho", age: 25 };

testFunction(min, "age");
```

함수 내부에서 interface안에다가 타입을 하나 더 끼워넣는 것입니다. 

다른 변수를 선언하면서 타입 단언(as)를 하는것이지요.

Person `& ` 를하면 뒤에 있는 객체를 상속받습니다. 



처음에는 이렇게 했습니다. 하지만 이렇게하면 호출하는 쪽에 서 에러가 납니다. 

```tsx
interface Person {
  name: string;
  age: number;
}

const testFunction = (
  testObj: Person & { [key: string]: string },
  objectName: string
) => {
  const inFunctionTestObj = testObj as Person;
  console.log(inFunctionTestObj[objectName]);
};

const min = { name: "minho", age: 25 };
testFunction(min, "age"); // 에러발생!
```

typescript 컴파일러가 testObj: Person & { [key: string]: string } 에서 **분명 Person안에 key는 string이 맞는데 value는 string | number인데 너는 string만 적었어!** 라고 에러를 보냅니다.

그렇기 때문에 `testObj: Person & { [key: string]: string | numbre }`, 라고 하면 에러는 잡힙니다. 하지만 이건 type을 쓰는 의미가 없어보여서 쓰지 않았습니다. Person이라는 interface가 무시되기 때문입니다.



#### 🟩 결론

- typescript에서 string을 key로 넣으려면 `index signature`를 사용하자



#### 출처

- https://soopdop.github.io/2020/12/01/index-signatures-in-typescript/