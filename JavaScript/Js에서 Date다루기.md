## Js에서 Date다루기

```js
new Date();
```

date로 Date()객체를 가져옵니다.

[`Date.prototype.getDate()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getDate)

`Date`에서 현지 시간 기준 일(`1`–`31`)을 반환합니다.

[`Date.prototype.getDay()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getDay)

`Date`에서 현지 시간 기준 요일(`0`–`6`)을 반환합니다.

[`Date.prototype.getFullYear()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getFullYear)

`Date`에서 현지 시간 기준 연도(네 자리 연도면 네 자리로)를 반환합니다.

[`Date.prototype.getHours()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getHours)

`Date`에서 현지 시간 기준 시(`0`–`23`)를 반환합니다.

[`Date.prototype.getMilliseconds()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getMilliseconds)

`Date`에서 현지 시간 기준 밀리초(`0`–`999`)를 반환합니다.

[`Date.prototype.getMinutes()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getMinutes)

`Date`에서 현지 시간 기준 분(`0`–`59`)을 반환합니다.

[`Date.prototype.getMonth()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getMonth)

`Date`에서 현지 시간 기준 월(`0`–`11`)을 반환합니다.

[`Date.prototype.getSeconds()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date/getSeconds)

`Date`에서 현지 시간 기준 초(`0`–`59`)를 반환합니다.



## Date() 생성자로 만들 때 

#### new Date(year, month, day, hour, minute, second, millisecond])

인수로 **년, 월, 일, 시, 분, 초, 밀리초**를 의미하는 숫자를 전달하면 지정된 날짜와 시간을 가지는 인스턴스를 반환합니다. 이때 년, 월은 반드시 지정하여야 한다. 지정하지 않은 옵션 정보는 0 또는 1으로 초기화된다.

| 인수        | 내용                                                         |
| ----------- | ------------------------------------------------------------ |
| year        | 1900년 이후의 년                                             |
| month       | 월을 나타내는 **0 ~ 11**까지의 정수 (주의: 0부터 시작, 0 = 1월) |
| day         | 일을 나타내는 1 ~ 31까지의 정수                              |
| hour        | 시를 나타내는 0 ~ 23까지의 정수                              |
| minute      | 분을 나타내는 0 ~ 59까지의 정수                              |
| second      | 초를 나타내는 0 ~ 59까지의 정수                              |
| millisecond | 밀리초를 나타내는 0 ~ 999까지의 정수                         |


