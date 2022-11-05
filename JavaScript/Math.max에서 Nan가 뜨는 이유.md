## Math.max에서 Nan가 뜨는 이유

If at least one of arguments cannot be converted to a number, the result is NaN.

배열에 하나라도 진짜 숫자형(number) 가 아니면 Nan이 뜨게 됩니다.

아래와 같은 경우에 혼란스럽습니다

```
Math.max([1,2,3])
```

분명 배열을 주고 max를 돌렸으니 최대 값을 찾아주는거 아닌가? java에서는 바로 찾아줬는데?

하지만 js에서는` [1,2,3]`을 **"1,2,3"**으로 convert합니다. "1,2,3"중에 최대값을 찾으라 하니 NaN이 뜨게됩니다.

```
 Math.max([23]) // return 23
```

이건 재대로 작동합니다. 왜냐하면 `[23] -> "23" -> 23` 숫자로 재대로 변형하기 때문입니다.



우리가 Math.max()에서 배열사용하려면 

```js
Math.max.apply(Math,[1,2,3])
```

[apply() 메서드](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)는 주어진 this 값과 배열(또는 배열과 유사한 객체)로 제공된 인수로 지정된 함수를 호출합니다.



더 쉬운 방법이 있습니다!

```js
Math.max(...[1,2,3]) // ...[1,2,3] => 1,2,3
```

바로 [spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)를 이용하는 것입니다.

...을 사용하면 배열이 분해 될것 입니다.