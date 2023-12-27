#### 🟩 왜 flatMap에 관심을 가지셨나요?

프로젝트나 코딩하다가 쓸일이 있어서 알게된건 아닙니다. [next에 유용한 12가지 라이브러리](https://medium.com/@nitinmaurya969543/top-12-libraries-for-your-nextjs-project-29ab2c44e745)들 이라는 글을 읽고 있었는데 **lodash** 라는 라이브러리를 소개해주었습니다. 소개 문구에서 flatMap이라는 것을 지원해주기 전에 이 라이브러리를 써서 유용하게 썻다 라고 이해했습니다. "어? flatMap이 뭐지? 하다가 찾아본 것입니다."





# ✅ js의 flatMap에 대해서

**✨ map은 알고있다고 가정하겠습니다**



[Array.prototype.flatMap() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap)

map와 flatMap은 차이가 있습니다. map을 이미 알고있다면 한번에 이해가 갈 예시가 있는데요.

```
const arr1 = ["it's Sunny in", "", "California"];

arr1.map((x) => x.split(" "));
// [["it's","Sunny","in"],[""],["California"]]

arr1.flatMap((x) => x.split(" "));
// ["it's","Sunny","in", "", "California"]
```

위 예시 입니다.

예시를 보고 한방에 알았습니다. "아하 map의 결과 배열을 1차원으로 만들어주는 함수구나"



```
// 음수를 모두 제거하고
// 홀수를 짝수와 1로 분할한다고 가정해 보겠습니다.
const a = [5, 4, -3, 20, 17, -33, -4, 18];
//         |\\  \\  x   |  | \\   x   x   |
//        [4,1, 4,   20, 16, 1,       18]

const result = a.flatMap((n) => {
  if (n < 0) {
    return [];
  }
  return n % 2 === 0 ? [n] : [n - 1, 1];
});
console.log(result); // [4, 1, 4, 20, 16, 1, 18]
```

flatMap은 filter와 반대되게 사용할 수 있답니다.

- 음수 제거
- 홀수를 짝수와 1로 분할

2가지 기능을 한번에 합니다.

짝수 맞을 때 [n]으로 반환하는데 그냥 n으로 반환해도 됩니다.



### ✅ map와 flatMap이 다른점

```
console.log([1, 2, , 4, 5].flatMap((x) => [x, x * 2])); // [1, 2, 2, 4, 4, 8, 5, 10]
console.log([1, 2, 3, 4].flatMap((x) => [, x * 2])); // [2, 4, 6, 8]

console.log([1, 2, , 4, 5].map((x) => [x, x * 2])); // [ [ 1, 2 ], [ 2, 4 ], <1 empty item>, [ 4, 8 ], [ 5, 10 ] ]
console.log([1, 2, 3, 4].map((x) => [, x * 2])); // [[ <1 empty item>, 2 ],[ <1 empty item>, 4 ],[ <1 empty item>, 6 ],[ <1 empty item>, 8 ]]
```

flat은 빈 슬롯을 무시합니다. map은 원본배열의 빈 슬롯을 무시합니다.

위 패턴도 typescript로 바꾸었더니 에러가 납니다.

TS18048: x is possibly undefined x의 추정값에 undefined가 되어있어서 소스 배열에 undefined 값이 있으면 컴파일 타임에서 잡아줍니다.

반환 배열에 빈 슬롯이 있는건 js와 똑같이 동작합니다.





### 🟩 객체에서 flatMap() 사용하기

```
const arrayLike = {
  length: 2,
  0: 7,
  1: 8,
  2: 9, // length가 2이므로 flatMap()에 의해 무시됩니다.
  3: 10, // length가 2이므로 flatMap()에 의해 무시됩니다.
};
console.log(
  Array.prototype.flatMap.call(arrayLike, (x) => {
    return [x, x * 2];
    // console.log(x);
    // return x;
  })
);
// [7, 14, 8, 16]

// 콜백에서 반환된 유사 배열은 평탄화되지 않습니다.
console.log(
  Array.prototype.flatMap.call(arrayLike, (x) => ({
    length: 1,
    0: x,
  }))
);
// [ { '0': 7, length: 1 }, { '0': 8, length: 1 } ]
```

여기서 처음 안건대 object 첫 번 재에 length를 적어두면 배열처럼 되나봐요. 아니였습니다😥

정확한 계념은 아래와 같습니다.

> flatMap() 메서드는 this의 length 속성을 읽은 다음 키가 length보다 작은 음수가 아닌 정수인 각 속성에 접근합니다.

말을 잘 풀어 보면

1. flatMap() 메서드는 호출된 배열(this)의 length 속성을 읽습니다.
2. 그런 다음, 배열의 각 요소에 대해 콜백 함수를 호출합니다.
3. 콜백 함수는 각 요소에 대해 적용되며, 이때 키(인덱스)가 배열의 길이(length)보다 작은 음수가 아닌 정수인 경우에만 적용됩니다.



그래서 key 값을 바꾸면 배열처럼 동작을 안합니다.

```
const arrayLike = {
  length: 2,
  q: 7,
  w: 8,
  e: 9, 
  r: 10, 
};
```

length가 2여도 q,w를 인식 못합니다. flatMap을 실행시키면 빈배열([])이 출력됩니다.