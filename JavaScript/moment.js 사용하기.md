## moment.js 사용하기

**moment.js**는 JavaScript에서 사용되는 날짜관련 라이브러리 중 가장 많이 사용되었던 라이브러리입니다.

현재는 더이상의 업데이트가 없을 것이라 하였지만, 2011년부터 가장 많이 사용된 날짜 관련 라이브러리입니다.



#### **현재 날짜 및 시간 - moment()**

```js
var now = moment();
now.format(); // 2021-10-09T00:01:13+09:00
```

**moment()** 함수를 사용해 현재 날짜와 시간 객체를 생성할 수 있습니다.

 

#### **날짜 지정 생성 - moment()**

```js
var date = moment("2021-10-09");
date.format();	// 2021-10-09T00:00:00+09:00
var date = moment("2021.10.09", "YYYY.MM.DD");
date.format();	// 2021-10-09T00:00:00+09:00
var date = moment("10/09/21", "MM/DD/YY");
date.format();	// 2021-10-09T00:00:00+09:00
var date = moment("2021-10-09 10:30:25", "YYYY-MM-DD HH:mm:ss");
date.format();	// 2021-10-09T10:30:25+09:00
```

**moment()** 함수를 사용해 원하는 날짜 및 시간을 입력하여 객체를 생성할 수 있습니다.

 

#### **포맷 지정 - format()**

```js
var now = moment();
now.format();	// 2021-10-09T00:09:45+09:00
now.format("YY-MM-DD");	// 21-10-09
now.format("DD/MM/YY");	// 09/10/21
now.format("YYYY.MM.DD HH:mm:ss");	// 2021.10.09 00:09:45
```

**format()** 함수를 사용하여 원하는 형태를 입력하고 원하는 형태의 문자열로 변경할 수 있습니다.

 

#### **날짜 객체에서 지정 시간 단위의 시작, 마지막으로 설정 - startOf() / endOf()**

```js
moment("2021-10-09 10:30:25").format(); // 2021-10-09T10:30:25+09:00

moment("2021-10-09 10:30:25").startOf("day").format(); // 2021-10-09T00:00:00+09:00
moment("2021-10-09 10:30:25").endOf("day").format(); // 2021-10-09T23:59:59+09:00

moment("2021-10-09 10:30:25").startOf("year").format(); // 2021-01-01T00:00:00+09:00
moment("2021-10-09 10:30:25").endOf("year").format(); // 2021-12-31T23:59:59+09:00

moment("2021-10-09 10:30:25").startOf("hour").format(); // 2021-10-09T10:00:00+09:00
moment("2021-10-09 10:30:25").endOf("hour").format(); // 2021-10-09T10:59:59+09:00

moment("2021-10-09 10:30:25").startOf("minute").format(); // 2021-10-09T10:30:00+09:00
moment("2021-10-09 10:30:25").endOf("minute").format(); // 2021-10-09T10:30:59+09:00
```

**startOf()** 함수를 사용하여 지정 시간 단위에서의 시작 날짜 및 시간,

**endOf()** 함수를 사용하여 지정 시간 단위에서의 마지막 날짜 및 시간으로 설정할 수 있습니다.

 

#### **날짜 및 시간 더하기 - add()**

```js
moment().format(); // 2021-10-09T00:32:12+09:00

moment().add(1, "years").format(); // 2022-10-09T00:32:12+09:00
moment().add(1, "y").format(); // 2022-10-09T00:32:12+09:00

moment().add(1, "months").format();  // 2021-11-09T00:32:12+09:00
moment().add(1, "M").format(); // 2021-11-09T00:32:12+09:00

moment().add(1, "weeks").format(); // 2021-10-16T00:32:12+09:00
moment().add(1, "w").format(); // 2021-10-16T00:32:12+09:00

moment().add(1, "days").format();  // 2021-10-10T00:32:12+09:00
moment().add(1, "d").format(); // 2021-10-10T00:32:12+09:00

moment().add(1, "hours").format(); // 2021-10-09T01:32:12+09:00
moment().add(1, "h").format(); // 2021-10-09T01:32:12+09:00

moment().add(1, "minutes").format(); // 2021-10-09T00:33:12+09:00
moment().add(1, "m").format(); // 2021-10-09T00:33:12+09:00

moment().add(1, "seconds").format(); // 2021-10-09T00:32:13+09:00
moment().add(1, "s").format(); // 2021-10-09T00:32:13+09:00

moment().add(1000, "milliseconds").format(); // 2021-10-09T00:32:13+09:00
moment().add(1000, "ms").format(); // 2021-10-09T00:32:13+09:00
```

**add()** 함수를 사용하여 원하는 날짜 및 시간을 더할 수 있습니다.

#### **날짜 및 시간 빼기 - subtract()**

```js
moment().format(); // 2021-10-09T00:37:29+09:00

moment().subtract(1, "years").format(); // 2020-10-09T00:37:29+09:00
moment().subtract(1, "y").format(); // 2020-10-09T00:37:29+09:00

moment().subtract(1, "months").format(); // 2021-09-09T00:37:29+09:00
moment().subtract(1, "M").format(); // 2021-09-09T00:37:29+09:00

moment().subtract(1, "weeks").format(); // 2021-10-02T00:37:29+09:00
moment().subtract(1, "w").format(); // 2021-10-02T00:37:29+09:00

moment().subtract(1, "days").format(); // 2021-10-08T00:37:29+09:00
moment().subtract(1, "d").format(); // 2021-10-08T00:37:29+09:00

moment().subtract(1, "hours").format(); // 2021-10-08T23:37:29+09:00
moment().subtract(1, "h").format(); // 2021-10-08T23:37:29+09:00

moment().subtract(1, "minutes").format(); // 2021-10-09T00:36:29+09:00
moment().subtract(1, "m").format(); // 2021-10-09T00:36:29+09:00

moment().subtract(1, "seconds").format(); // 2021-10-09T00:37:28+09:00
moment().subtract(1, "s").format(); // 2021-10-09T00:37:28+09:00

moment().subtract(1000, "milliseconds").format(); // 2021-10-09T00:37:28+09:00
moment().subtract(1000, "ms").format(); // 2021-10-09T00:37:28+09:00
```

**subtract()** 함수를 사용하여 원하는 날짜 및 시간을 뺄 수 있습니다.

 

#### **날짜 및 시간 차이 구하기 - diff()**

```js
var date1 = moment();
var date2 = moment("2020-04-08");

date1.format(); // 2021-10-09T00:44:52+09:00
date2.format(); // 2020-04-08T00:00:00+09:00

date1.diff(date2); // 47436292714
date1.diff(date2, "years"); // 1
date1.diff(date2, "months"); // 18
date1.diff(date2, "weeks"); // 78
date1.diff(date2, "days"); // 549
date1.diff(date2, "hours"); // 13176
date1.diff(date2, "minutes"); // 790604
date1.diff(date2, "seconds"); // 47436292
date1.diff(date2, "milliseconds"); // 47436292714
```

**diff()** 함수를 사용하여 두 날짜의 차이를 구할 수 있습니다.

 

#### **현재 날짜 및 시간을 기준으로 상대적인 시간 구하기 - fromNow()**

```
moment().format(); // 2021-10-09T00:15:13+09:00
moment().fromNow(); // a few seconds ago
moment().startOf("day").fromNow(); // 15 minutes ago
moment().endOf("day").fromNow(); // in a day
moment("2021-10-08").fromNow(); // a day ago
moment("2021-10-01").fromNow(); // 8 days ago
moment("2021-10-25").fromNow(); // in 16 days
moment("2021-08-09").fromNow(); // 2 months ago
moment("2021-12-25").fromNow(); // in 3 months
moment("2020-10-09").fromNow(); // a year ago
moment("2023-10-09").fromNow(); // in 2 years
```

**fromNow()** 함수를 사용하여 날짜 객체의 현재로부터의 차이를 구할 수 있습니다.

 

#### **지정한 날짜 및 시간을 기준을 기준으로 상대적인 시간 구하기 - from()**

```js
moment().format(); // 2021-10-09T00:18:13+09:00
moment().from(moment()); // a few seconds ago
moment().from(moment().startOf("day")); // in 18 minutes
moment().from(moment().endOf("day")); // a day ago
moment().from(moment("2021-10-08")); // in a day
moment().from(moment("2021-10-01")); // in 8 days
moment().from(moment("2021-10-25")); // 16 days ago
moment().from(moment("2021-08-09")); // in 2 months
moment().from(moment("2021-12-25")); // 3 months ago
moment().from(moment("2020-10-09")); // in a year
moment().from(moment("2023-10-09")); // 2 years ago
```

**from()** 함수를 사용하여 날짜 객체를 기준으로 또 다른 날짜 객체로부터의 차이를 구할 수 있습니다.

 

#### **날짜가 지정한 시간 단위에서 특정 날짜와 일치하는지 구하기 - isSame()**

```js
var date = moment("2021-10-09");
date.isSame("2021-10-09"); // true
date.isSame("2021-10-09", "year"); // true
date.isSame("2021-10-09", "month");  // true
date.isSame("2020-10-09", "month");  // false
date.isSame("2021-10-09", "day");  // true
date.isSame("2021-11-09", "day");  // false
```

**isSame()** 함수를 사용하여 날짜 객체가 지정한 시간 단위에서 특정 날짜와 일치하는지 구할 수 있습니다.

**isSame()** 함수에서 시간단위를 입력하여 사용할때 주의할 점은,

입력한 시간 단위가 같다고 해도 입력한 시간 단위보다 더 큰 시간 단위에서 이미 서로가 다르면 false를 반환합니다.

예를들어 비교할 시간 단위를 [day] 로 지정했을 때, true가 나오기 위해서는 year, month, day가 모두 일치해야 합니다.

제가 입력한 예시를 참고해주시기 바랍니다.

 

#### **날짜가 지정한 시간 단위에서 특정 날짜보다 이전 인지, 이전 이거나 같은지 구하기 - isBefore() / isSameOrBefore()**

```js
var date = moment("2021-10-09");

date.isBefore("2021-10-09"); // false
date.isSameOrBefore("2021-10-09"); // true

date.isBefore("2021-10-20"); // true
date.isSameOrBefore("2021-10-20"); // true

date.isBefore("2021-10-20", "year"); // false
date.isSameOrBefore("2021-10-20", "year"); // true

date.isBefore("2021-10-20", "month"); // false
date.isSameOrBefore("2021-10-20", "month"); // true

date.isBefore("2021-10-20", "day"); // true
date.isSameOrBefore("2021-10-20", "day"); // true
```

**isBefore()** 함수를 사용하여 날짜 객체가 지정한 시간 단위에서 특정 날짜보다 이전인지 확인할 수 있습니다.

**isSameOrBefore()** 함수를 사용하여 날짜 객체가 지정한 시간 단위에서 특정 날짜보다 이전이거나 같은지 확인할 수 있습니다.

 

#### **날짜가 지정한 시간 단위에서 특정 날짜보다 이후 인지, 이후 이거나 같은지 구하기 - isAfter() / isSameOrAfter()**

```js
var date = moment("2021-10-09");

date.isAfter("2021-10-09"); // false
date.isSameOrAfter("2021-10-09"); // true

date.isAfter("2021-10-01"); // true
date.isSameOrAfter("2021-10-01"); // true

date.isAfter("2021-10-01", "year"); // false
date.isSameOrAfter("2021-10-01", "year"); // true

date.isAfter("2021-10-01", "month"); // false
date.isSameOrAfter("2021-10-01", "month"); // true

date.isAfter("2021-10-01", "day"); // true
date.isSameOrAfter("2021-10-01", "day"); // true
```

**isAfter()** 함수를 사용하여 날짜 객체가 지정한 시간 단위에서 특정 날짜보다 이후인지 확인할 수 있습니다.

**isSameOrAfter()** 함수를 사용하여 날짜 객체가 지정한 시간 단위에서 특정 날짜보다 이후이거나 같은지 확인할 수 있습니다.

 

#### **날짜가 지정한 시간 단위에서 특정 날짜들 사이에 있는지 구하기 - isBetween()**

```js
var date = moment("2021-10-09"); // today

date.isBetween("2021-10-09", "2021-10-09"); // false
date.isBetween("2021-10-08", "2021-10-10"); // true
date.isBetween("2021-10-08", "2021-10-09"); // false
date.isBetween("2021-10-09", "2021-10-10"); // false
date.isBetween("2021-10-09", undefined); // false

date.isBetween("2021-10-08", "2021-10-10", "year"); // false
date.isBetween("2020-10-09", "2022-10-09", "year"); // true
date.isBetween("2021-10-08", "2021-10-10", "month"); // false
date.isBetween("2021-09-09", "2021-11-09", "month"); // true
date.isBetween("2021-10-09", "2021-10-09", "day"); // false
date.isBetween("2021-10-08", "2021-10-10", "day"); // true

date.isBetween("2021-10-09", "2021-10-09", undefined, "()"); // false
date.isBetween("2021-10-09", "2021-10-09", undefined, "[)"); // false
date.isBetween("2021-10-09", "2021-10-10", undefined, "[)"); // true
date.isBetween("2021-10-09", "2021-10-09", undefined, "(]"); // false
date.isBetween("2021-10-08", "2021-10-09", undefined, "(]"); // true
date.isBetween("2021-10-09", "2021-10-09", undefined, "[]"); // true
```

**isBetween()** 함수를 사용하여 날짜 객체가 특정 날짜들 사이에 있는지 확인할 수 있습니다.

**isBetween()** 함수에서 첫번째와 두번째에 날짜를 넣는 부분에 **undefined**를 입력하면 **오늘 날짜로 대체**됩니다.

**세번째 인수**에는 시간 단위를 지정할 수 있고,

**네번째 인수**에서 **'('**와 **')'**는 **입력한 시작날짜와 마지막 날짜를 포함하지 않고 비교하도록 하고,**

**'['와 ']'는 입력한 시작날짜와 마지막 날짜를 포함하여 비교하도록 설정**합니다.



