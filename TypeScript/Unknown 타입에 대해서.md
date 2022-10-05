## Unknown 타입에 대해서

### any vs unknown

`unknown` 타입이 도입된 배경을 보다 잘 이해하기 위해 `any` 타입을 살펴봐야 합니다. TypeScript에서 `any`는 모든 타입을 할당받을 수 있는 타입이다. 즉 `any` 타입으로 선언된 변수, argument는 모든 타입의 값이 할당될 수 있고 전달될 수 있는 것입니다. 

java의 Object와 비슷한 성격인거 같습니다.

`unknown` 타입도 `any`과 마찬가지로 모든 타입의 값이 할당될 수 있습니다.

```ts
let variable: unknown

variable = true // OK (boolean)
variable = 1 // OK (number)
variable = 'string' // OK (string)
variable = {} // OK (object)
```

하지만 조금 다른 것은 `unknown` 타입으로 선언된 변수는 `any`를 제외한 다른 타입으로 선언된 변수에 할당될 수 없다는 것입니다..

```ts
let variable: unknown

let anyType: any = variable
let booleanType: boolean = variable
// Error: Type 'unknown' is not assignable to type 'boolean'.(2322)
let numberType: number = variable
//  Error: Type 'unknown' is not assignable to type 'number'.(2322)
let stringType: string = variable
//  Error: Type 'unknown' is not assignable to type 'string'.(2322)
let objectType: object = variable
//  Error: Type 'unknown' is not assignable to type 'object'.(2322)
```

`unknown` 타입의 특징은 한 가지 더 있는데, `unknown` 타입으로 선언된 변수는 프로퍼티에 접근할 수 없으며, 메소드를 호출할 수 없으며, 인스턴스를 생성할 수도 없다. **알려지지 않은 타입**이라 그런 것입니다.



#### 타입의 범위를 쉽게 볼 수 있는 그림이 있습니다.

![type_diagram](https://jbee.io/static/f19e5096c6cc5c8682607b9886b66c88/c1b63/type_diagram.png)

**유니온(Union, |)**은 쉽게 말하면 **합집합**입니다. 따라서 unknown 타입과 다른 타입을 `|`로 유니온 타입으로 합성하게 되면 `unknown` 타입이 반환됩니다.

**인터섹션(intersection, &)**은 교집합이라고 할 수 입니다. 따라서 unknown 타입과 다른 타입을 `&`로 인터섹션 타입으로 반환하게 되면 대상이 된 타입이 반환됩니다.



```
unknown 을 사용하는 것은 컴파일러에게 "이 변수는 어떤 타입이될지몰라 너가 추론해줘" 라고 이야기해주는 것과 같습니다.
```

출처: https://sambalim.tistory.com/146 [삼바의 성장 블로그:티스토리]