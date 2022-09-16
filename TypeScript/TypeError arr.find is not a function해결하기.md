## TypeError: arr.find is not a function에 대해서

array에 find를 걸었는데 에러가 납니다.

**The "find is not a function" error occurs when we call the `find()` method on a value that is not of type array. To solve the error, convert the value to an array before calling the `find` method or make sure to only call the method on arrays.**

배열에 아무 값도 없다면 find에서 에러가 난답니다. 

```javascript
const arr = {};

// ⛔️ Uncaught TypeError: arr.find is not a function
const result = arr.find(num => num % 2 === 0);
```

이런식으로 쓰면 배열에 아무것도 들어가지 않습니다!



#### 해결방법

```javascript
const arr = [3, 6, 10];

const result = arr.find(num => num % 2 === 0);

console.log(result); // ️ 6
```

값을 넣어주던가

```javascript
const arr = null;

const result = Array.isArray(arr) ? arr.find(num => num % 2 === 0) : 0;

console.log(result); // ️ 0
```

Array.isArray()로 빈 배열인지 확인하면 됩니다.



#### js에서 배열을 만들 때 

```js
const arr = []
```

형태가 기본입니다.

#### js에서 배열 안에 object를 만들 때 

```js
const arr = [{}]
```

이런 형태로 배열 안에 객체(object)를 넣어줍시다.