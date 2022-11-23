## ✅ Sequelize에서 서브쿼리를 써야할 때!

```ts
// subQuery
    const setSubQueryCustomer: CustomerSelectListQuery = {};
    if (params.ttt) {
      setSubQueryCustomer.where = {
        ...setSubQueryCustomer.where,
        ttt: params.ttt,
      };
    }
    return new Promise((resolve, reject) => {
      AlarmList.findAndCountAll({
        ...setQuery,
        attributes: { exclude: ['causeJson'] }, // 해당 필드 제외
        include: [
          {
            model: Mobile,
            attributes: MobileAttributesInclude,
          },
          {
            model: C,
            attributes: ['id', 'code'],
            include: [
              {
                model: M,
                attributes: ['id', 'code'],
                include: [
                  {
                    model: Customer,
                    attributes: ['id', 'name', 'ccIdCompany'],
                    ...setSubQueryCustomer,
                  },
                ],
              },
            ],
          },
```

#### ✅ subQeuery라는 객체를 만듭니다. 

```ts
    const setSubQueryCustomer: CustomerSelectListQuery = {};
    if (params.ttt) {
      setSubQueryCustomer.where = {
        ...setSubQueryCustomer.where,
        ttt: params.ttt,
      };
    }
```

이 객체에는 parameter에서 가져온 where문을 집어 넣습니다.



#### ✅ include(Fk)인 객체 모델에다가 서브쿼리를 넣습니다.

```ts
AlarmList.findAndCountAll({
        ...setQuery,
        attributes: { exclude: ['causeJson'] }, // 해당 필드 제외
        include: [
          {
            model: Mobile,
            attributes: MobileAttributesInclude,
          },
          {
            model: C,
            attributes: ['id', 'code'],
            include: [
              {
                model: M,
                attributes: ['id', 'code'],
                include: [
                  {
                    model: Customer,
                    attributes: ['id', 'name', 'ccIdCompany'],
                    ...setSubQueryCustomer,
                  },
                ],
              },
            ],
          },
```

AlarmList는 findAndCountAll ()을 합니다.

첫번째 include는 Mobile입니다.

두번째 include는 C입니다. C에서 M을 또 include하고 M에서 또 Customer를 include합니다.

즉, C -> M -> Customer로 종속관계가 되어있습니다. 

#### include된 속성을 살펴봅시다.

**model**은 include된 객체를 의미합니다. sequelize에 설정된 table을 모델로 설정해줍니다.

**attributes**는 출력될 속성을 의미합니다. M을 예시로 보겠습니다. M안에 'id' 와 'code' 만 가져와서 출력하겠다는 의미 입니다.(select id, code ) 랑 똑같습니다.



