## js에서 YYYY-MM-DD형태로 시간 가져오기

현재 년-월-일 을 가져와야 해야 했습니다. Date()객체로 가져올 수 있습니다.

백틱과 Date()함수를 이용해서 구할 수 있습니다.

```js
const today = new Date();
const year = today.getFullYear();
const month = `0${today.getMonth()+1}`.splice(-2);
const day = `0${today.getDate()}`.splice(-2);
const now = `${year}-${month}-${day}`;
```

이제 now에 년-월-일 데이터가 담기게 됩니다.

- splice(-2)는 월, 일은 2자리수가 있으니 앞에 0을 붙히면 3자리가 됩니다. ex)013 
- 그러면 **무조건 앞에 0을 붙히**고 **뒤에 2자리만 가지고 오게**되면 MM-DD 형태로 2자리가 됩니다.
- getMonth()는 0~11(1월~12월)입니다. 0부터 시작해서 +1을 해줍니다.



#### Moment 라이브러리 사용하기(Typescript 환경)

moment 라이브러리를 사용해서 더 쉽게 포맷을 만들 수 있습니다.

먼저 moment 라이브러리를 설치합니다.

```js
npm install moment
```



```ts
import moment from "moment";

const today = moment(new Date(),'Asia/Seoul').format('YYYY-MM-DD');
console.log(today);
```

1. moment를 import 해옵니다.
2. moment() 매개변수로 Date를 넣어주고 'Asia/Seoul' 포멧으로 합니다. 
3. 그 다음 결과값에 'YYYY-MM-DD'를 해줘서 원하는 형식을 지정합니다.
4. 그럼 today 변수에 원하는 날짜를 넣어줍니다.
