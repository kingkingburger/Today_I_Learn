## 🟩 sequelize에서 model에서 지정한 json에 값 추가하기

```ts
purchaseResult = await purchaseRequestDao.selectDeepInfo(params);
```

위와 같은 명령어로 purchaseResult를 출력하면 

```sh
{
  status: 200,
  code: 'SUCCESS',
  message: 'Selected data successfully',
  data: PurchaseRequest {
    dataValues: {
      id: 49,
    },
    _previousDataValues: {
      id: 49,
    },
    _changed: Set(0) {},
    _options: {
      isNewRecord: false,
      _schema: null,
      _schemaDelimiter: '',
      raw: true,
      attributes: [Array]
    },
    isNewRecord: false
  },
  remark: null
}
```

sequelize는 이런형태로 객체를 json으로 반환해줍니다. 이렇게되면 테이블에 있는것과 연관관계로 되어있는것 말고는 json에 값을 넣을 수 없습니다.

sequelize의 제어에서 벋어나려면 우리가 다룰 수 있는 객체로 만들어야 합니다.

```ts
// 우리가 원하는 대로 보여줄 Json 객체 선언
let result: Record<string, any> | null;

// sequelize에서 불러온 객체
purchaseResult = await purchaseRequestDao.selectDeepInfo(params);

// sequelize객체를 JSON.parse()로 typecript의 객체로 만들어주기
result = JSON.parse(JSON.stringify(purchaseResult)) as Record<string, any>;
```

이렇게 result 객체는 우리가 아는 typescript 객체로 변했습니다. 이제 내가 원했던 객체 값을 JSON 형태로 넣어주면 됩니다.

```ts
result.want = wantData;
```

