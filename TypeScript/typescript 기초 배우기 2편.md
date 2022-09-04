# typescript 기초 배우기 2편



## 함수에 관해서

```tsx
function hello(name: string){
    return `hello, ${name || 'word'}`;
}
const result = hello();
```

이렇게 name에 어떤 값이 들어가도 되고 안들어가도 되는 것을 설정하고 싶을 때는 `?` 를 붙여주면 됩니다.

```tsx
function hello(name?: string){
    return `hello, ${name || 'word'}`;
}
const result = hello();
```

이를 **선택적 매개변수**라고 합니다

사실 js에서 매개변수를 초기화 해놓을 수 있습니다.

```tsx
function hello(name = 'word'){
    return `hello, ${name} `;
}
const result = hello();
```



```tsx
function hello(name: string, age?: number){
    if(age !== undefined){
        return `Hello ${name}. You are ${age}`;
    }else{
        return `Hello ${name}`;
    }
}
const result = hello('Sam',30);
```

age는 들어와도 되고 안들어와도 되는 매개변수 입니다. 안들어 올 때는 undefined가 들어올 태니 예외처리를 해두었습니다.

age를 name보다 앞에 쓰면 안됩니다. 왜냐하면 들어와되고 안되는 매개변수가 있다면 무조건 undefined로 판단 할 것이기 때문입니다. 만약 앞에 쓴다면

```tsx
function hello(age: number | undefined, name: string){
    if(age !== undefined){
        return `Hello ${name}. You are ${age}`;
    }else{
        return `Hello ${name}`;
    }
}
const result = hello(undefined,'sam');
```

optional하게 쓰지말고 명확하게 number 또는 undefined 타입인것을 명시해줘야 합니다.



#### 나머지 매개변수에 대해

```tsx
function add(...nums: number[]){
    return nums.reduce((result, num) => result + num, 0);
}

add(1,2,3); // 6
add(1,2,3,4,5,6,7,8,9,10) //55
```

`...`은 갯수가 매변 바뀔 수 있습니다. `...`으로 받은 변수는 배열로써 동작하게 됩니다.



#### this 사용법

```tsx
interface Userr{
    name: string;
}
const Same :Userr = {name: 'Same'};

function showName(this:Userr){
    console.log(this.name)
}
const ab = showName.bind(Same);
```

this에 타입을 지정해주고 쓰면 됩니다. 무조건 매개변수 첫 번째에 타입을 지정합니다.



#### 오버로딩

```ts
interface Userc{
    name: string,
    age: number,
}

function join(name:string, age: number): Userc ;
function join(name:string, age: string): string;
function join(name:string, age: number | string): Userc | string{
    if(typeof age === "number"){
        return {
            name,
            age,
        };
    }else{
        return "나이는 숫자로 입력해주세요"
    }
}

const ss: Userc = join("S",25);
const tt: string = join("JJ", "666")
```

함수의 타입에 따라 원하는 리턴값이 다를 때 함수 위에다가 명확한 타입을 지정해주면 됩니다.





## 리터럴, 유니온/ 교차타입

const 로 선언된 변수를 리터럴 타입이라고 합니다. **변하지 않는 값**이죠

`|`를 쓰는 변수를 유니온 타입이라고 합니다. **여러가지 값**이 들어갈 수 있는 것이죠

```ts
interface Car {
  name: "car";
  color: string;
  start(): void;
}

interface Mobile {
  name: "mobile";
  color: string;
  call(): void;
}

function getGift(gift: Car | Mobile) {
  if (gift.name === "car") {
    gift.start();
  } else {
    gift.call();
  }
}
```

getGift의 함수를 보시면 매개변수 gift가 무슨 타입인지 name변수를 통해 확인하고 있습니다. 이와 같이 인터페이스를 구분해 주는 함수는 `식별 가능한 유니온 타입` 이라고 합니다

```ts
interface Car {
  name: string;
  color: string;
  start(): void;
}
interface Toy {
  name: string;
  color: string;
  price: number;
}

const toyCar: Toy & Car = {
  name: "타요",
  start() {},
  color: "blue",
  price: 1000,
};
```

교차타입으로 필요한 클래스를 모두 담은 클래스를 만들 수 있습니다. 만약 price를 주석처리 한다면 에러가 발생합니다.



## 클래스에 대해서

```ts
class Car {
  color: string;
  constructor(color: string) {
    this.color = color;
  }
  start() {
    console.log("start");
  }
}

const bmw = new Car("red");
```

class 안에서 color 매개변수를 쓰면 꼭 **먼저 맴버변수로 등록**되어 있어야 합니다.

```ts
class Car {
  #name: string = "car";
  color: string;
  constructor(color: string) {
    this.color = color;
  }
  start() {
    console.log("start");
    console.log(this.#name);
  }
}

class Bmw extends Car {
  constructor(color: string) {
    super(color);
  }
  showName() {
    console.log(super.name);
  }
}
```

타입스크립트에서는 private 속성을 `#` 으로 써도 됩니다. 이 때 자식 클래스에서는 접근이 안되기 때문에 에러가 발생합니다.

- public - 자식 클래스, 클래스 인스턴스 모두 접근 가능(접근 제한자 안적으면 모두 public)
- protected - 자식 클래스에서 접근 가능(인스턴스에서 접근 불가능)
- private  - 해당 클래스 내우벵서만 접근 가능

```ts
abstract class Car {
  name: string = "car";
  color: string;
  static wheels = 4;
  constructor(color: string) {
    this.color = color;
  }
  start() {
    console.log("start");
    console.log(this.name);
  }
  abstract doSomething(): void;
}

class Bmw extends Car {
  constructor(color: string) {
    super(color);
  }
  showName() {
    console.log(super.name);
  }
    doSomething(): void {}
}
```

추상클래스도 만들 수 있습니다. static으로 맴버변수를 만들면 클래스로 접근 가능합니다.

추상 클래스의 추상 메서드가 있다면 자식 클래스에서 반드시 구현을 해야 합니다.



## 제네릭에 대해서

```ts
function getSize<T>(arr: T[]): number {
  return arr.length;
}
const arr1 = [1, 2, 3];
getSize(arr1);
```

함수옆에다가 <T>를 넣으면 T안에 들어온 값을 쓸 수 있습니다. 전달되는 매개변수를 보고 알아서 T 값을 적용해줍니다.

```ts
interface Mobile<T> {
  name: string;
  option: T;
}
const m1: Mobile<Object> = {
  name: "21",
  option: {
    color: "red",
    coupon: false,
  },
};

const m2: Mobile<string> = {
  name: "22",
  option: "goog",
};
```

인터페이스에도 제네릭 타입을 쓸 수 있습니다.

```ts
interface User {
  name: string;
  age: number;
}

interface Car {
  name: string;
  age: number;
}

interface Book {
  price: number;
}

const user: User = { name: "a", age: 10 };
const car: Car = { name: "bmw", age: 2000 };
const book: Book = { price: 3000 };

function showName(data): string {
  return data.name;
}
```

이 때 Book 클래스는 name 속성이 없으니 에러가 납니다. 그러면 제네릭 타입으로 해결을 할 수 있습니다.

```ts
function showName<T extends { name: string }>(data: T): string {
  return data.name;
}
```

결국에는 book을 쓰지 못하게 막는 것입니다. data는 항상 name이  string인 객체를 확장한 타입을 받게됩니다.



## 유틸리티 타입에 대해서

```ts
interface User{
    id: number;
    name: string;
    age: number;
    gender: "m" | "f";
}

type UserKey = keyof User; // 'id' | 'name' | 'age' | 'gender'
```

keyof 를 사용하면 위와같이 id만 빼오는거 같습니다.



```ts
// interface User {
//     id?: number;
//     name?: string;
//     age?: number;
//     gender?: "m" | "f";
//   }
let admin: Partial<User> = {
  id: 1,
  name: "bob",
};
```

interface에 Partial로 감싸면 모든 인수들이 optinal하게 변하게 됩니다. 위에 주석과 같아지게 되죠

```ts
let admin: Required<User> = {
  id: 1,
  name: "bob",
};
```

반대로 Required는 필수로 바꿔줍니다.

```ts
let admin: ReadOnly<User> = {
  id: 1,
  name: "bob",
};
```

처음에만 할당가능하고 나중에는 읽기만 가능합니다.

```ts
type Grade = "1" | "2" | "3" | "4";
type Score = "A" | "B" | "C" | "D";
const score: Record<Grade, Score> = {
  1: "A",
  2: "B",
  3: "C",
  4: "D",
};
```

```ts
interface User {
  id: number;
  name: string;
  age: number;
}

function isValid(user: User) {
  const result: Record<keyof User, boolean> = {
    id: user.id > 0,
    name: user.name !== "",
    age: user.age > 0,
  };
  return result;
}
```

이런식으로 응용을 할 수 있습니다. key, value같은 형태입니다. java의 map과 비슷해보입니다.



#### Pick 사용해보기

```ts
interface User {
  id: number;
  name: string;
  age: number;
  gender: "m" | "w";
}

const admin: Pick<User, "id" | "name"> = {
  id: 0,
  name: "boc",
};
```

User에서 id와 name만 가져다가 쓸 수 있습니다.



#### Omit 사용해보기

```tsx
interface User {
  id: number;
  name: string;
  age: number;
  gender: "m" | "w";
}

const admin: Omit<User, "age" | "gender"> = {
  id: 0,
  name: "boc",
};
```

Omit은 반대로 제외하고 사용하는 것입니다. age와 gender만 제외되었죠



#### Exclude 사용해보기

```tsx
type T1 = string | number;
type T2 = Exclude<T1, number>;
```

이러면 T2는 string 타입이 됩니다.



#### NonNullable 사용해보기

```ts
type T1 = string | null | undefined | void;
type T2 = NonNullable<T1>;
```

null과 undefined도 함께 제거가 됩니다.

이러면 T2는 string,void 타입만 가지게 됩니다.