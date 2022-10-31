## Sequelize에서 Boolean 칼럼을 ( ㅁ= 0 OR ㅁ IS NULL) 문으로 만들어보기

#### ▶ 다중 조건(OR)

```js
const { Op } = require("sequelize");
Post.findAll({
  where: {
    [Op.or]: [
      { authorId: 12 },
      { authorId: 13 }
    ]
  }
});
// SELECT * FROM post WHERE authorId = 12 OR authorId = 13;
```

Op.or로 다중 조건을 걸 수 있습니다.

약간 다른 구조로도 할 수 있습니다.

```js
const { Op } = require("sequelize");
Post.destroy({
  where: {
    authorId: {
      [Op.or]: [12, 13]
    }
  }
});
// DELETE FROM post WHERE authorId = 12 OR authorId = 13;
```

필드별로 쪼개서 넣을 수도 있습니다.



#### ✅ Boolean을 sequelize에서 확인하기

```ts
const testparam: testParams = {
  empty: ('false' as unknown) as boolean,
};
await testDao.selectList(testparam);
```

위와같은 형식으로 selectList를 보내보겠습니다.

그러면 'false'로 empty 필드에 들어갈 것입니다.

```js
if (params.empty) {
      const realEmpty = params.empty as unknown;
      setQuery.where = {
        ...setQuery.where,
        empty: realEmpty === 'true' ? realEmpty : { [Op.or]: [false, { [Op.is]: null }] }, // '=' OR 'IS NULL'검색
      };
    }
```

boolean 형식이 문자열로 true인지 false인지를 판단하게 됩니다. if문으로 params의 empty가 있는지 없는지 확인하기 위해서 문자열 형태로 보냅니다.

#### ✅ ( ㅁ= 0 OR ㅁ IS NULL) 문 만들기

```js
 { [Op.or]: [false, { [Op.is]: null }] }, // '=' OR 'IS NULL'검색
```

Op.or를 사용해서 (empty = 0 OR empty IS NULL) 문을 만들어 줍니다.



#### 출처

- https://sequelize.org/docs/v6/core-concepts/model-querying-basics/




