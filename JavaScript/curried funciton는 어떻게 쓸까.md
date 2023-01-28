#### 🟦 curried funciton는 어떻게 쓸까?

```
ItemDataFind: (state) => (id) => {
  return state.ItemList.rows.find(row => {
    if (row.id === id) {
      return 1
    }
  })
}
```

다른사람의 코드를 보다가 이게 어떻게 동작하는거지??

스택오버플로우에서 가져왔습니다.

수학과 컴퓨터 과학에서 **커링**이란 **다중 인수을 갖는 함수**를 **단일 인수를 갖는 함수들의 함수열로 바꾸는 것**을 말한다. 예를 들어, 세 개의 인수를 가지는 함수f를 커링하면 다음과 같은 세 개의 함수가 만들어진다.

이걸 function에 적용한게  **[curried function](https://en.wikipedia.org/wiki/Currying) 이라고 합니다.**



먼저 아래 함수는 2개의 매개변수를 가집니다.

```
const add = (x, y) => x + y
add(2, 3) //=> 5
```

curried 형태로 바꾼 함수입니다.

```
const add = x => y => x + y
```

curried 형태의 함수와 똑같은 함수 입니다.

```
const add = function (x) {
  return function (y) {
    return x + y
  }
}
```

**`return` 을 자세히 봅시다.**

`add`함수는 함수를 반환합니다 *.* 명확성을 더하기 위해 괄호를 사용할 수 있습니다.

```
const add = x => (y => x + y)
```

몇개의 `add` 함수는 함수 자체를 리턴합니다.

```
add(2) // returns (y => 2 + y)
```

------

#### 🟦 **커리 함수 호출** (**Calling curried functions**)

따라서 커리 함수를 사용하려면 조금 다르게 호출해야 합니다.

```
add(2)(3)  // returns 5
```

이는 첫 번째(외부) 함수 호출이 두 번째(내부) 함수를 반환하기 때문입니다. 두 번째 함수를 호출한 후에야 실제로 결과를 얻습니다. 통화를 두 줄로 분리하면 더 분명해집니다.

```
const add2 = add(2) // returns function(y) { return 2 + y }
add2(3)             // returns 5
```



#### Typescript에서 예시 입니다.

```
interface person {
    name: string;
    age: number;
}

const twoFunctionTest = (state: person) => (married: boolean) => {
    console.log(state, married); // { name:'won', age:26 } true
    return 5;
}

const minho: person = {name: 'won', age: 26};
const tta = twoFunctionTest(minho);
console.log(tta(true)) // 5
console.log(tta(false)) // 5
```

이걸왜 쓰냐라고 보면 첫 번재 매개변수를 미리 저장해두고 2번째 매개변수를 가지가지 변화시킬 때 유용하게 쓰일수 있다고 생각합니다. 

예를들어 한 인물의 신상 정보를 받아야 될 때 tta의 매개변수만 바꿔끼면 되지 않을까 싶습니다. 첫번째 매개변수를 고정하거나 다른 변수드를 유연하게 쓰기 위해 이런 문법이 나온거 같습니다.



출처:

[What do multiple arrow functions mean in JavaScript?](https://stackoverflow.com/questions/32782922/what-do-multiple-arrow-functions-mean-in-javascript)