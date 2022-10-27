## JSON Parse와 JSON stringify 에 대해서

크게 나눠보면



## 💠**JSON 객체의 parse**  

String -> Object : **String 객체**를 **json 객체**로 변환

#### 👉파싱이란?

- 문장을 문법적 부분으로 나눕니다.
- 나누어진 부분을 식별하는 것입니다.
- Json은 문장을 **<key>:<value>** 관계로 식별합니다.

```js
const jsonStr = '{"Age": "30"}';
const obj = JSON.parse(jsonStr);

console.log(obj);
```

![[JavaScript]JSON parse 와 JSON stringify 차이 - undefined - JSON.parse](https://blog.kakaocdn.net/dn/b1U3oe/btrmKDWLDpD/wqXNOAPaB1KkheNRHZ4zwK/img.png)

reviver라는 매개변수도 있습니다. JSON.parse(text, reviver)



#### 👉reviver를 쓰는 예시입니다.

```js
const jsonStr = '{"Age": "30", "Name": "Kang"}';
const obj = JSON.parse(jsonStr, (key, value) => key ==='Age' ? value * 2 : value);

console.log(obj);

```

**key**의 이름이 **Age**라면 x2하는 reviver입니다. 변환되는 방식을 지정하는 매개변수 입니다.



#### 👉실행결과

![[JavaScript]JSON parse 와 JSON stringify 차이 - undefined - JSON.parse](https://blog.kakaocdn.net/dn/AeugE/btrmMgapYSi/ZiMMqSfxkxFIe4b5bPmUnk/img.png)



#### 👉key 뿐만아니라 value도 조건에 걸 수 있습니다.

```js
JSON.parse(
  '{"p": 5}',
  (key, value) =>
    typeof value === "number"
      ? value * 2 // return value * 2 for numbers
      : value, // return everything else unchanged
);

// { p: 10 }
```

JSON 문자열에서 뒤에 쉼표가 있는 경우 JSON.parse()에서 구문 오류가 발생합니다.

![[JavaScript]JSON parse 와 JSON stringify 차이 - undefined - JSON.parse](https://blog.kakaocdn.net/dn/k6zwp/btrmEift4Rj/vCdaQD2Kx5AJ0ayHUiUufK/img.png)





## 💠**JSON 객체의 stringify**

Object -> String : **json 객체**를 **String 객체**로 변환

```js
const obj = {Age: 30, Name: "Kang"};
const jsonStr = JSON.stringify(obj);

console.log(jsonStr);
//{"Age":30,"Name":"Kang"}
```



#### 👉3가지 매개변수가 쓰일 수 있습니다.

```js
JSON.stringify(value)
JSON.stringify(value, replacer)
JSON.stringify(value, replacer, space)
```

- 첫 번째 매개변수는 JSON 문자열로 변환할 Object입니다.
- 두 번째 매개변수는 **replacer** 함수입니다. 
  - **replacer** 함수는 key와 value 두 개의 매개변수를 받으며, 필터링 용도로 사용할 수 있습니다.
  - **replacer** 함수에서 undefined를 반환하면, 해당 속성은 JSON 문자열에 포함되지 않습니다.

#### 👉replacer를 이용한 예시 입니다.

```js
const obj = {Age: 30, Name: "Kang"};

const replacerFunc =(key: string, value: any) =>{
    if(key === "Name") {
        return undefined;
    }
    return value;
}
const jsonStr = JSON.stringify(obj, replacerFunc);
console.log(jsonStr);
//{"Age":30}
```

- 세 번째 매개변수는 JSON 문자열의 가독성을 위해 공백을 삽입하는데 사용됩니다. 
- 세 번째 매개변수가 생략되거나 빈 문자열("") 또는 null이면, 공백이 추가되지 않습니다.

```js
const obj = {Age: 30, Name: "Kang"};
const jsonStr = JSON.stringify(obj, null, 'tt ');

console.log(jsonStr);
//{
//tt "Age": 30,
//tt "Name": "Kang"
//}
```

