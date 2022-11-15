## Typescript에서 momentjs 대신 day.js 사용하기

#### dayjs 설치하기

```shell
npm install dayjs
```

npm을 통해서 설치합니다. 

#### 불러오기

```ts
import dayjs from 'dayjs' // ES 2015
```

import를 통해서 가져옵니다. ES2015부터 된다고 나와있습니다.

```ts
const dayjs = require('dayjs')
```

require를 통해서 가져올 수 있습니다.



#### 한국 시간으로 맞추기

```ts
import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';

dayjs.extend(utc);
dayjs.extend(timezone);
```

dayjs는 타임존과 관련된 기능이 기본으로 깔려있지 않스빈다. 그래서 timzone 플러그인을 추가해줘야 합니다.

그런데 `timezone` 플러그인을 추가할 때 반드시 `utc` 플러그인도 함께 추가해줘야 합니다. `timezone` 플러그인이 `utc` 플러그인에 의존성을 갖고 있기 때문에 `utc` 플러그인을 추가해주지 않으면 타임존 기능을 사용할 때 에러가 발생합니다.



```ts
dayjs.tz.setDefault("Asia/Seoul"); //dayjs.tz의 timezone만 변경된것 dayjs는 여전히 utc를 따른다.
```

dayjs.tz.setDefault()로 timezone을 변경하고 나면 dayjs의 timezone이 서울로 변할거 같습니다만 변하지 않습니다. 

dayjs.tz의 timezone이 변한것입니다. 

```
console.log(dayjs().tz());

M {
  '$L': 'en',
  '$d': 2022-11-15T02:17:41.381Z,
  '$x': { '$timezone': 'Asia/Seoul' },
  '$y': 2022,
  '$M': 10,
  '$D': 15,
  '$W': 2,
  '$H': 11,
  '$m': 17,
  '$s': 41,
  '$ms': 381,
  '$offset': 540,
  '$u': false
}
```

결과를 보시면 dayjs().tz()의 date도 timezone이 적용이 안될걸 볼 수 있습니다. 하지만 year, month, date 등등은 변했습니다. 

```js
console.log(dayjs().tz().format());
// 2022-11-15T11:18:24+09:00
```

format()으로 보면은 +9시간이 되서 string형태로  잘 나온것을 확인할 수 있습니다.





#### 현재 날짜 및 시간 - dayjs().tz()

```ts
const now = dayjs().tz();
console.log(now.format()); //2022-11-15T11:22:12+09:00
```



#### 날짜 지정 생성 - dayjs().tz()

```ts
let date1 = dayjs("2022-11-15").tz();
console.log(date1.format()); // 2022-11-15T00:00:00+09:00
let date2 = dayjs("2022-11-16 10:00:00");
console.log(date2.format()); // 2022-11-16T10:00:00+09:00
let date3 = dayjs("2022-11-17 11:00");
console.log(date3.format()); // 2022-11-17T11:00:00+09:00
let date4 = dayjs("2022-11-18 10:30:25");
console.log(date4.format()); // 2022-11-18T10:30:25+09:00
```

**dayjs()**함수를 사용해 원하는 날짜 및 시간을 입력하여 객체를 생성할 수 있습니다.



#### 포맷 지정 - format()

```ts
const now = dayjs().tz();
console.log(now.format()); //2022-11-15T11:32:21+09:00
console.log(now.format("YY-MM-DD")); // 22-11-15
console.log(now.format("DD/MM/YY")); // 15/11/22
console.log(now.format("YYYY.MM.DD HH:mm:ss")); // 2022.11.15 11:32:21
```

**format()** 함수를 사용하여 원하는 형태를 입력하고 원하는 형태의 **문자열**로 변경할 수 있습니다.



#### **날짜 객체에서 지정 시간 단위의 시작, 마지막으로 설정 - startOf() / endOf()**

```ts
console.log(dayjs("2022-11-15 11:35:25").startOf("day").format()); // 2022-11-15T00:00:00+09:00
console.log(dayjs("2022-11-15 11:35:25").endOf("day").format()); // 2022-11-15T23:59:59+09:00

console.log(dayjs("2022-11-15 11:35:25").startOf("year").format()); // 2022-01-01T00:00:00+09:00
console.log(dayjs("2022-11-15 11:35:25").endOf("year").format()); // 2022-12-31T23:59:59+09:00

console.log(dayjs("2022-11-15 11:35:25").startOf("hour").format()); // 2022-11-15T11:00:00+09:00
console.log(dayjs("2022-11-15 11:35:25").endOf("hour").format()); // 2022-11-15T11:59:59+09:00

console.log(dayjs("2022-11-15 11:35:25").startOf("minute").format()); // 2022-11-15T11:35:00+09:00
console.log(dayjs("2022-11-15 11:35:25").endOf("minute").format()); // 2022-11-15T11:35:59+09:00
```

**startOf()** 함수를 사용하여 지정 시간 단위에서의 시작 날짜 및 시간,

**endOf()** 함수를 사용하여 지정 시간 단위에서의 마지막 날짜 및 시간으로 설정할 수 있습니다.

| Unit      | Shorthand | Description                                                  |
| --------- | --------- | ------------------------------------------------------------ |
| `year`    | `y`       | January 1st, 00:00 this year                                 |
| `quarter` | `Q`       | beginning of the current quarter, 1st day of months, 00:00 ( dependent [`QuarterOfYear` ](https://day.js.org/docs/en/plugin/quarter-of-year)plugin ) |
| `month`   | `M`       | the first day of this month, 00:00                           |
| `week`    | `w`       | the first day of this week, 00:00 (locale aware)             |
| `isoWeek` |           | the first day of this week according to ISO 8601, 00:00 ( dependent [`IsoWeek` ](https://day.js.org/docs/en/plugin/iso-week)plugin ) |
| `date`    | `D`       | 00:00 today                                                  |
| `day`     | `d`       | 00:00 today                                                  |
| `hour`    | `h`       | now, but with 0 mins, 0 secs, and 0 ms                       |
| `minute`  | `m`       | now, but with 0 seconds and 0 milliseconds                   |
| `second`  | `s`       | now, but with 0 milliseconds                                 |

각 속성들이 가질 수 있는 값들과 설명입니다.



#### **날짜 및 시간 더하기 - add()**

```ts
console.log(dayjs().add(1, "year").format()); // 2023-11-15T11:40:57+09:00
console.log(dayjs().add(1, "y").format()); // 2023-11-15T11:40:57+09:00

console.log(dayjs().add(1, "M").format()); // 2022-12-15T11:42:21+09:00
console.log(dayjs().add(1, "months").format()); // 2022-12-15T11:42:21+09:00

console.log(dayjs().add(1, "weeks").format()); // 2022-11-22T11:42:21+09:00
console.log(dayjs().add(1, "w").format()); // 2022-11-22T11:42:21+09:00

console.log(dayjs().add(1, "days").format()); // 2022-11-16T11:42:21+09:00
console.log(dayjs().add(1, "d").format()); // 2022-11-16T11:42:21+09:00

console.log(dayjs().add(1, "hours").format()); // 2022-11-15T12:42:21+09:00
console.log(dayjs().add(1, "h").format()); // 2022-11-15T12:42:21+09:00

console.log(dayjs().add(1, "minutes").format()); // 2022-11-15T11:43:21+09:00
console.log(dayjs().add(1, "m").format()); // 2022-11-15T11:43:21+09:00

console.log(dayjs().add(1, "seconds").format()); // 2022-11-15T11:42:22+09:00
console.log(dayjs().add(1, "s").format()); // 2022-11-15T11:42:22+09:00

console.log(dayjs().add(1000, "milliseconds").format()); // 2022-11-15T11:42:22+09:00
console.log(dayjs().add(1000, "ms").format()); // 2022-11-15T11:42:22+09:00
```



#### **날짜 및 시간 빼기 - subtract()**

```ts
console.log(dayjs().subtract(1, "year").format()); // 2023-11-15T11:42:21+09:00
console.log(dayjs().subtract(1, "y").format()); // 2023-11-15T11:42:21+09:00

console.log(dayjs().subtract(1, "M").format()); // 2022-12-15T11:42:21+09:00
console.log(dayjs().subtract(1, "months").format()); // 2022-12-15T11:42:21+09:00

console.log(dayjs().subtract(1, "weeks").format()); // 2022-11-22T11:42:21+09:00
console.log(dayjs().subtract(1, "w").format()); // 2022-11-22T11:42:21+09:00

console.log(dayjs().subtract(1, "days").format()); // 2022-11-16T11:42:21+09:00
console.log(dayjs().subtract(1, "d").format()); // 2022-11-16T11:42:21+09:00

console.log(dayjs().subtract(1, "hours").format()); // 2022-11-15T12:42:21+09:00
console.log(dayjs().subtract(1, "h").format()); // 2022-11-15T12:42:21+09:00

console.log(dayjs().subtract(1, "minutes").format()); // 2022-11-15T11:43:21+09:00
console.log(dayjs().subtract(1, "m").format()); // 2022-11-15T11:43:21+09:00

console.log(dayjs().subtract(1, "seconds").format()); // 2022-11-15T11:42:22+09:00
console.log(dayjs().subtract(1, "s").format()); // 2022-11-15T11:42:22+09:00

console.log(dayjs().subtract(1000, "milliseconds").format()); // 2022-11-15T11:42:22+09:00
console.log(dayjs().subtract(1000, "ms").format()); // 2022-11-15T11:42:22+09:00
```

**subtract()** 함수를 사용하여 원하는 날짜 및 시간을 뺄 수 있습니다.



#### **날짜 및 시간 차이 구하기 - diff()**

```ts
const date1 = dayjs(); //현재 날짜 2022-11-15
const date2 = dayjs("2020-02-17");

console.log(date1.format()); // 2022-11-15T11:45:38+09:00
console.log(date2.format()); // 2020-02-17T00:00:00+09:00

console.log(date1.diff(date2)); // 86615162745
console.log(date1.diff(date2, "year")); // 2
console.log(date1.diff(date2, "month")); // 32
console.log(date1.diff(date2, "week")); // 143
console.log(date1.diff(date2, "day")); // 1002
console.log(date1.diff(date2, "hour")); // 24059
console.log(date1.diff(date2, "minute")); // 1443586
console.log(date1.diff(date2, "second")); // 86615209
console.log(date1.diff(date2, "millisecond")); // 86615209305
```

년도는 xx년도 차이, month는 xx 개월 차이... 이렇게 지정된 타입으로 차이 갯수가 나오게 됩니다.

| Unit          | Shorthand | Description                              |
| ------------- | --------- | ---------------------------------------- |
| `day`         | `d`       | Day of Week (Sunday as 0, Saturday as 6) |
| `week`        | `w`       | Week of Year                             |
| `quarter`     | `Q`       | Quarter                                  |
| `month`       | `M`       | Month (January as 0, December as 11)     |
| `year`        | `y`       | Year                                     |
| `hour`        | `h`       | Hour                                     |
| `minute`      | `m`       | Minute                                   |
| `second`      | `s`       | Second                                   |
| `millisecond` | `ms`      | Millisecond                              |

들어갈 수 있는 요소들과 설명 입니다.



#### **지정한 날짜 및 시간을 기준을 기준으로 상대적인 시간 구하기 - from()**

dayjs에서 from을 사용하려면 또 다른 플러그인이 필요합니다.  `RelativeTime`이란 플러그인이죠

```ts
import relativeTime from "dayjs/plugin/relativeTime";
dayjs.extend(utc);
dayjs.extend(timezone);
dayjs.extend(relativeTime);
```

import로 불러오고 extend로 추가해줍시다. dayjs가 용량이 작은 이유가 플러그인들을 다 빼놔서인가? 생각도 듭니다.

```ts
console.log(dayjs().format()); // 2022-11-15T11:55:08+09:00
console.log(dayjs().from(dayjs())); // a few seconds ago
console.log(dayjs().from(dayjs().startOf("day"))); // in 12 hours
console.log(dayjs().from(dayjs().endOf("day"))); // 12 hours ago
console.log(dayjs().from(dayjs("2022-10-08"))); // in a month
console.log(dayjs().from(dayjs("2022-10-01"))); // in a month
console.log(dayjs().from(dayjs("2022-10-25"))); // in 21 days
console.log(dayjs().from(dayjs("2022-08-09"))); // in 3 months
console.log(dayjs().from(dayjs("2022-12-25"))); // a month ago
console.log(dayjs().from(dayjs("2021-10-09"))); // in a year
console.log(dayjs().from(dayjs("2023-10-09"))); // a year ago
```

**from()** 함수를 사용하여 날짜 객체를 기준으로 또 다른 날짜 객체로부터의 차이를 구할 수 있습니다.





#### **날짜가 지정한 시간 단위에서 특정 날짜와 일치하는지 구하기 - isSame()**

```ts
const date = dayjs("2022-10-09");
console.log(date.isSame("2022-10-09")); // true
console.log(date.isSame("2022-10-09", "year")); // true
console.log(date.isSame("2022-10-09", "month")); // true
console.log(date.isSame("2020-10-09", "month")); // false
console.log(date.isSame("2022-10-09", "day")); // true
console.log(date.isSame("2022-11-09", "day")); // false
```

**isSame()** 함수를 사용하여 날짜 객체가 지정한 시간 단위에서 특정 날짜와 일치하는지 구할 수 있습니다.

**isSame()** 함수에서 시간단위를 입력하여 사용할때 주의할 점은, 

입력한 시간 단위가 같다고 해도 입력한 시간 단위보다 더 큰 시간 단위에서 이미 서로가 다르면 false를 반환합니다.

ex) 비교할 시간 단위를 [day] 로 지정했을 때, true가 나오기 위해서는 year, month, day가 모두 일치해야 합니다.



#### **날짜가 지정한 시간 단위에서 특정 날짜보다 이전 인지, 이전 이거나 같은지 구하기 - isBefore() / isSameOrBefore()**

dayjs에서 isSameOrBefore()을 사용하려면 또 다른 플러그인이 필요합니다.  `isSameOrBefore`이란 플러그인이죠

```ts
import isSameOrBefore from "dayjs/plugin/isSameOrBefore";
dayjs.extend(utc);
dayjs.extend(timezone);
dayjs.extend(relativeTime);
dayjs.extend(isSameOrBefore);
```

import로 불러오고 extend로 추가해줍시다.

```ts
let date = dayjs("2022-11-15");

console.log(date.isBefore("2022-10-09")); // false
console.log(date.isSameOrBefore("2022-11-15")); // true

console.log(date.isBefore("2021-10-20", "year")); // false
console.log(date.isSameOrBefore("2021-10-20", "year")); // false

console.log(date.isBefore("2022-11-16", "month")); // false
console.log(date.isSameOrBefore("2022-11-15", "month")); // true

console.log(date.isBefore("2022-11-15", "day")); // false
console.log(date.isSameOrBefore("2022-11-15", "day")); // true
```

**isBefore()** 함수를 사용하여 날짜 객체가 지정한 시간 단위에서 특정 날짜보다 이전인지 확인할 수 있습니다.

**isSameOrBefore()** 함수를 사용하여 날짜 객체가 지정한 시간 단위에서 특정 날짜보다 이전이거나 같은지 확인할 수 있습니다.



#### **날짜가 지정한 시간 단위에서 특정 날짜보다 이후 인지, 이후 이거나 같은지 구하기 - isAfter() / isSameOrAfter()**

마찬가지로 dayjs에서 isSameOrAfter()을 사용하려면 또 다른 플러그인이 필요합니다.  `isSameOrAfter`이란 플러그인이죠

```ts
import isSameOrAfter from "dayjs/plugin/isSameOrAfter";
dayjs.extend(utc);
dayjs.extend(timezone);
dayjs.extend(relativeTime);
dayjs.extend(isSameOrBefore);
dayjs.extend(isSameOrAfter);
```

import로 불러오고 extend로 추가해줍시다

```ts
let date = dayjs("2022-11-15");

console.log(date.isAfter("2022-10-09")); //  true
console.log(date.isSameOrAfter("2022-11-15")); //  true

console.log(date.isAfter("2021-10-20", "year")); //  true
console.log(date.isSameOrAfter("2021-10-20", "year")); //  true

console.log(date.isAfter("2022-11-16", "month")); //  false
console.log(date.isSameOrAfter("2022-11-15", "month")); //  true

console.log(date.isAfter("2022-11-15", "day")); //  false
console.log(date.isSameOrAfter("2022-11-15", "day")); //  true
```





#### **날짜가 지정한 시간 단위에서 특정 날짜들 사이에 있는지 구하기 - isBetween()**

 dayjs에서 isBetween()을 사용하려면 또 다른 플러그인이 필요합니다.  `isBetween`이란 플러그인이죠

```ts
import isBetween from "dayjs/plugin/isBetween";
dayjs.extend(utc);
dayjs.extend(timezone);
dayjs.extend(relativeTime);
dayjs.extend(isSameOrBefore);
dayjs.extend(isSameOrAfter);
dayjs.extend(isBetween);
```

import로 불러오고 extend로 추가해줍시다

```tsx
let date = moment("2022-11-09");

console.log(date.isBetween("2022-11-09", "2022-11-09")); // false
console.log(date.isBetween("2022-11-08", "2022-11-10")); // true
console.log(date.isBetween("2022-11-08", "2022-11-09")); // false
console.log(date.isBetween("2022-11-09", "2022-11-10")); // false
console.log(date.isBetween("2022-11-09", undefined)); // false

console.log(date.isBetween("2022-11-08", "2022-11-10", "year")); // false
console.log(date.isBetween("2020-11-09", "2022-11-09", "year")); // false
console.log(date.isBetween("2022-11-08", "2022-11-10", "month")); // false
console.log(date.isBetween("2022-11-09", "2022-11-09", "month")); // false
console.log(date.isBetween("2022-10-09", "2022-12-09", "month")); // true
console.log(date.isBetween("2022-11-09", "2022-11-09", "day")); // false
console.log(date.isBetween("2022-11-08", "2022-11-10", "day")); // true

console.log(date.isBetween("2022-11-09", "2022-11-09", undefined, "()")); // false
console.log(date.isBetween("2022-11-09", "2022-11-09", undefined, "[)")); // false
console.log(date.isBetween("2022-11-09", "2022-11-10", undefined, "[)")); // true
console.log(date.isBetween("2022-11-09", "2022-11-09", undefined, "(]")); // false
console.log(date.isBetween("2022-11-08", "2022-11-09", undefined, "(]")); // true
console.log(date.isBetween("2022-11-09", "2022-11-09", undefined, "[]")); // true
```

**isBetween()** 함수를 사용하여 날짜 객체가 특정 날짜들 사이에 있는지 확인할 수 있습니다.

**isBetween()** 함수에서 첫번째와 두번째에 날짜를 넣는 부분에 **undefined**를 입력하면 **오늘 날짜로 대체**됩니다.

**세번째 인수**에는 시간 단위를 지정할 수 있습니다. month면 month만 비교하고 day면 day날짜만 비교합니다.

**네번째 인수**에서 **'('**와 **')'**는 **입력한 시작날짜와 마지막 날짜를 포함하지 않고 비교하도록 하고,**

**'['와 ']'는 입력한 시작날짜와 마지막 날짜를 포함하여 비교하도록 설정**합니다.







#### 공식문서

https://day.js.org/docs/en/timezone/converting-to-zone

공식문서에 더욱 다양한 내용이 있습니다.



moment에는 기본으로 탑재되어있는 기능들이 dayjs에서는 import해야와 하는 불편함이 있습니다. 이 때문에 용량이 작다고 말할 수 있는거 같습니다.



















