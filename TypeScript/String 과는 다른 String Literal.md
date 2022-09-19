## String과는 다른 String Literal

다음과 같은 TypeScript 코드가 있다. `b`와 `c`은 string 타입이 맞지만, `a`은 `"Hello World"` 타입이다. [Type Script Playground](https://www.typescriptlang.org/play?#code/MYewdgzgLgBAFgUwDZJAdRAJyQEwIwwC8MARABLKowbY4kCwAUEgrIiulrgExGkUdqXOk1CQ2lTrQDMALhjRMASzABzPuUlDaJIA)에서 각 변수명에 mouse over하면 타입을 확인할 수 있스빈다

```ts
const a = "Hello World"
let b = "Hello World"
const c: string = "Hello World"
```

`b` 변수는 `let`으로 선언되어 재할당될 수 있을 경우 어떤 문자열이든 넣을 수 있으며 그 경우의 수가 무한대입니다. 그렇기 때문에 컴파일러는 이 변수를 string 타입으로 추론합니다. 그리고 `c` 변수는 명시적으로 string 타입으로 선언했으므로 그냥 string 타입입니다.

하지만 `a`의 경우는 다릅니다. 컴파일러는 이 변수를 `string`이 아닌 조금 더 좁은 타입(narrowed type)으로 선언한 것으로 추론합니다. 이 것을 [Literal Narrowing](https://www.typescriptlang.org/docs/handbook/literal-types.html#literal-narrowing)이라고 합니다. (참고로 [타입 추론](https://www.typescriptlang.org/docs/handbook/type-inference.html)은 TypeScript 컴파일러가 제공하는 뛰어난 기능 중 하나이며, 개발자가 명시적으로 타입을 선언해 주지 않을 경우 컴파일러가 할당되는 값을 기준으로 타입을 스스로 결정하는 것을 말합니다.)

따라서 `a`의 타입은 string이 아니라 **string타입을 좁혀 만든 [string literal type](https://www.typescriptlang.org/docs/handbook/literal-types.html)입니다.** 여기서 "타입을 좁힌다"는 말의 의미는 무한대의 경우의 수를 가질 수 있는 string타입보다 훨씬 구체적인 string의 부분집합, `"Hello World"`만을 허용하는 타입을 선언했다는 뜻입니다..

따라서 아래와 같이 명시적으로 literal type을 선언하면 `let`으로 선언된 변수도 `"Hellow World"` 타입만을 허용하도록 만들 수도 있습니다..

```ts
type HelloWorldType = "Hello World" // literal type

let a: HelloWorldType = "Hello World" // ok
a = "hahaha" // compile error: "hahaha"는 "Hello World"가 아니기 때문.
```