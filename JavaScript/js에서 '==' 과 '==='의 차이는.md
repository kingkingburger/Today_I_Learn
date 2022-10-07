## js에서 '==' 과 '==='의 차이는?

==는 Equal Operator이고,  ===는 Strict Equal Operator이다. 

==는 a == b 라고 할때, a와 b의 값이 같은지를 비교해서, 같으면 true, 다르면 false라고 한다.(값만 같으면 true이다.)



===는 Strict, 즉 엄격한 Equal Operator로써, "엄격하게" 같음을 비교할 때 사용하는 연산자이다. 

===는 a === b 라고 할때, 값과 값의 종류(Data Type)가 모두 같은지를 비교해서, 같으면 true, 다르면 false라고 한다. 



#### <기본자료형(Primitive)> 

- 값은 똑같이 1이지만 값의 종류가 숫자냐, 문자열이냐에 따라 === 연산자를 사용할 때 결과가 false라고 나온다. 

```
var a = 1; 
var b = "1"; 
console.log(a == b); // true 
console.log(a === b); // false 
```



- null과 undefined는 공통적으로 값이 없음을 뜻하지만, 값의 종류(Data Type)가 다르기 때문에, === 연산자를 사용할 때 결과가 false라고 나온다. 

```
console.log(null == undefined); // true 
console.log(null === undefined); // false 
```





- 기본적으로 1은 true, 0은 false로 나타낼 수 있지만, 데이터 타입은 다르다. 

```
console.log(true == 1); // true 
console.log(true === 1); // false 
```



- 숫자 0과 문자열 “0”, ""

```
console.log(0 == "0"); // true 
console.log(0 === "0"); // false 
console.log(0 == ""); // true 
console.log(0 === ""); // false 
```



- NaN은 Not a Number라는 뜻으로, 숫자가 아닌 것을 의미하지만 그 값 자체끼리는 같지 않다. 

```
console.log(NaN == NaN); // false 
console.log(NaN === NaN); // false 
```





#### 배열, 또는 객체 등의 경우는 어떨까? 



**<객체형(Object type)>**

```
var a = [1,2,3]; 
var b = [1,2,3]; 
console.log(a == b); // false 
console.log(a === b); // false 
```



배열을 할당할때, 각 변수는 각 메모리의 주소를 참조한다. 

두 변수 a, b의 값과 데이터 타입이 같지만, 이와 상관없이 

참조하는 **메모리의 주소가 다르기 때문에** 두 a, b는 같지 않다. 

array, object 같은 경우에는 메모리의 주소를 참조하는 방식이다 보니, ==나 ===에 상관없이 같은 주소를 참조하면 동일한 것이고, 그게 아니면 다른 것 입니다.

```
var a = [1,2,3]; 
var b = [1,2,3]; 
var c = b; 
console.log(b === c); // true 
console.log(b == c); // ture 
```



새로운 변수 c에 변수 b를 할당해주면, 변수 c도 b가 참조하는 같은 메모리의 주소를 참조하게 되어, 

두 변수 c, b는 같다. 이때, c, b의 값과 데이터 타입이 같기 때문에, ==와 ===의 결과값이 동일하다. 



객체도 마찬가지다. 

```
var x = {}; 
var y = {}; 
var z = y; 
console.log(x == y) // false 
console.log(x === y) // false 
console.log(y === z) // true 
console.log(y == z) // true 
```







