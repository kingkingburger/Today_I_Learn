## typescript 기초 배우기 1편



#### 배열 타입은 2가지가 있습니다

```js
let a:number[] = [1,2,3];
let a2:Array<number> = [1,2,3];
```

흔히 아니 number[]를 써도 되고 Array<> 처럼 객체에다 템플릿을 넣어도 됩니다.

number가 아닌 string을 넣어도 됩니다.



#### 튜플에 관해서

```js
//튜플
let b:[string, number];

b = ['z',1];
```

배열에 어러가지 타입을 담을 수 있는거 같습니다.



#### void와 never에 관해서

```js
//void, never
function example():void{

}

function showError():never{
    throw new Error();
}

function infLoop():never{
    while(true){
        //do something....
    }
}
```

void는 아무것도 반환하지 않는 함수입니다.

never는 **에러만 반환하는 함수**나, **무한 루프를 도는 함수**에 쓸 수 있습니다.



#### enum에 관해서

```tsx
enum Os{
    Window,
    Ios,
    Android
}
```

window부터 인덱스가  0으로 시작됩니다.(0,1,2) 만약 Window = 3을 했다면 인덱스가 3,4,5가 됩니다.

중간에 Ios를 10으로 바꾸면 Android는 11이 됩니다.

```tsx
enum Os{
    Window,
    Ios,
    Android
}

let myOs:Os;

myOs = Os.Window;
```

한 변수에  enum타입을 넣으면 그 변수는 enum타입의 변수밖에 쓰지 못합니다.



#### interface 알아보기

```tsx
let user:object;

user = {
    name : 'xx',
    age : 30
}

console.log(user.name);
```

여기서 console.log는 에러를 나타냅니다. 

왜냐하면 object 타입에는 name이라는 멤버변수가 없기 때문이죠

그래서 우리는 interface로 타입을 지정해줘야 합니다.



```tsx
interface User{
    name: string;
    age: number;
}

let user:User;

user = {
    name : 'xx',
    age : 30
}

console.log(user.name);
```

interface로 내가 원하는 타입을 가지는 변수를 만들었습니다.



```tsx
interface User{
    name: string;
    age: number;
    gender?: string;
}

let user:User;

user = {
    name : 'xx',
    age : 30
}

user.gender = 'male';

console.log(user.name);
```

gender같은 경우는 optional한 타입입니다. 있어도 되고 없어도 되고, `?`로 판별합니다.



```tsx
interface User{
    name: string;
    age: number;
    gender?: string;
    readonly birthYear: number;
}

let user:User;

user = {
    name : 'xx',
    age : 30,
    birthYear : 15,
}
```

readonly 타입은 생성자에서만 생성이 되고 그 후에는 변환이 불가능 합니다.



```tsx
interface User{
    name: string;
    age: number;
    gender?: string;
    readonly birthYear: number;
    [grade:number] : string;
}
```

[grade]를 key로하고 value를 string으로 받는 변수를 선언한것 입니다.

```tsx
type Score = 'A' | 'B'

interface User{
    name: string;
    age: number;
    gender?: string;
    readonly birthYear: number;
    [grade:number] : Score;
}
```

value에 내가 원하는 type을 넣어줄 수 있습니다.



```tsx
interface Add{
    (num1:number, num2:number): number;
}

const add: Add = function(x,y){
    return x+ y;
}
```

interface를 함수에 넣을 수도 있습니다. (number,number) 타입을 가진 메게변수와 number 리턴타입을 가져야 하는 함수 입니다.



```tsx
interface IsAdult{
    (age:number) : boolean;
}
const aa:IsAdult = (age) =>{
    return age > 18;
}
```

화살표 함수로도 적용할 수 있습니다.



```tsx
interface Car{
    color:string;
    whells:number;
    start():void;
}

class Bmw implements Car{
    color;
    whells = 4;

    constructor(c:string){
        this.color = c;
    }
    start(){
        console.log("go...");
    }
}

const bbmw = new Bmw("red");
```

interface를 class에 적용할 수 있습니다. 이 때는 `implements`라는 키워드를 씁니다. 

class에서 constructor()를 만드는 것을 볼 수 있습니다. java와 비슷하네요.

```tsx
interface Benz extends Car{
    door: number;
    stop(): void;
}

const benz: Benz = {
    door: 5,
    stop(){
        console.log('stop');
    },

    color:"green",
    whells:4,
    start(){

    },
}
```

interface를 다른 interface에다가 확장 할 수도 있습니다.

`extends`를 쓰면 확장이 가능합니다. 2개의 interface를 동시에 extend를 할 수 있습니다