## 👍sequelize 에서 include된 객체를 다시 가져와야 할 때

![Untitled](https://user-images.githubusercontent.com/65094518/197947860-c6b2534a-a22f-4a45-bcbf-ff67efa8c6cc.png)

이런 model이 있다고 가정합시다.

node에서 corrMeterHour를 결과로 넘겨받으면 CorrMeterHour에 대한 객체만가지고 있고 CalMeter, CorrMeterHourHistory, User는 그냥 객체로만 보입니다.

ts에서 객체로 접근이 불가능했습니다.

![Untitled 1](https://user-images.githubusercontent.com/65094518/197947880-f3e93bc6-e34d-4ad1-9b28-09fab6ce03fa.png)

이런식으로 결과는 나옵니다. 그러면 CalMeter에 접근하려고 하면

![Untitled 2](https://user-images.githubusercontent.com/65094518/197947899-e027e5da-52c6-4e6a-b604-d04e64b95beb.png)

CalMeter 라고 객채가 안나옵니다 왜why?

```
selectList(params: CorrMeterHourSelectListParams): Promise<CorrMeterHourAttributes>
```

리턴타입이 CorrMeterHourAttributes였기 때문!!

```
export interface CorrMeterHourAttributes {
  id: number;
  calMeterId: number | null;
  meterGaugeId: number | null;
  notiListId: number | null;
  userId: number | null;
  corrOk: boolean | null;
  datetime: Date | null;
  year: number | null;
  month: number | null;
  weekSeq: number | null;
  dayWeek: number | null;
  day: number | null;
  hour: number | null;
  minute: number | null;
  prevQ: number | null;
  currQ: number | null;
  deltaQ: number | null;
  prevF: number | null;
  currF: number | null;
  deltaF: number | null;
  note: string | null;
  calMeterCode: string | null;
  createdAt: Date;
  updatedAt: Date;
  deletedAt: Date | null;
}
```

CorrMeterHourATtributes 소개입니다.

그런데 여기에는 없지만 분명 반환값에는 들어가 있습니다.

![Untitled 3](https://user-images.githubusercontent.com/65094518/197947901-1b8f6b48-e961-4ca0-a263-07edac16f708.png)

이런식으로요. 저는 이게 결과 타입때문이라고 생각합니다. CalMeter와 CorrMeterHourHistories 객체를 타입에 넣어놨다면 접근이 가능했겠죠.

근데 분명 값은 있습니다. 그러면 접근이 가능하겠죠.



## 👍 결론

```
((corrMeterHour as unknown) as {CorrMeterHourHistories: CorrMeterHourHistoryAttributes;}).CorrMeterHourHistories;
```

이렇게 접근이 가능해집니다. unknown 타입으로 만들고 CorrMeterHouHistories 객체 형태로 as 합니다. 그리고 마지막에 객체를 호출하는 것이죠

as unknown으로 일단 타입을 물렁하게 한다음 as {} 객체에 이름이 똑같은 것을 캐스팅(?) 하는 형태라고 생각했습니다.그러면 corrMeterHour 객체에서 CorrMeterHourHistories만 빼올태지요.









