## Sequelize select문 조건 알아보기

#### ▶ 기본

```js
Post.findAll({
  where: {
    authorId: 2
  }
});
// SELECT * FROM post WHERE authorId = 2;
```

where문을 걸어주는 방법입니다.

**연산자**가 지정되지 않으면  Sequelize는 **기본적으로 같음('=') 비교**를 합니다

```js
const { Op } = require("sequelize");
Post.findAll({
  where: {
    authorId: {
      [Op.eq]: 2
    }
  }
});
// SELECT * FROM post WHERE authorId = 2;
```

**연산자**를 넣어주려면 **[Op]**를 사용해야합니다. Operator의 줄임말 입니다.



#### ▶ 다중 조건(AND)

```js
Post.findAll({
  where: {
    authorId: 12,
    status: 'active'
  }
});
// SELECT * FROM post WHERE authorId = 12 AND status = 'active';
```

**연산자**가 지정되지 않으면  Sequelize는 **기본적으로 같음('=') 비교**를 합니다



```js
const { Op } = require("sequelize");
Post.findAll({
  where: {
    [Op.and]: [
      { authorId: 12 },
      { status: 'active' }
    ]
  }
});
// SELECT * FROM post WHERE authorId = 12 AND status = 'active';
```

이것도 Op.and를 사용해서 연상자를 넣어 줄 수 있습니다.



#### ▶ 조건 모음집

```js
const { Op } = require("sequelize");
Post.findAll({
  where: {
    [Op.and]: [{ a: 5 }, { b: 6 }],            // (a = 5) AND (b = 6)
    [Op.or]: [{ a: 5 }, { b: 6 }],             // (a = 5) OR (b = 6)
    someAttribute: {
      // Basics
      [Op.eq]: 3,                              // = 3
      [Op.ne]: 20,                             // != 20
      [Op.is]: null,                           // IS NULL
      [Op.not]: true,                          // IS NOT TRUE
      [Op.or]: [5, 6],                         // (someAttribute = 5) OR (someAttribute = 6)

      // Using dialect specific column identifiers (PG in the following example):
      [Op.col]: 'user.organization_id',        // = "user"."organization_id"

      // Number comparisons
      [Op.gt]: 6,                              // > 6
      [Op.gte]: 6,                             // >= 6
      [Op.lt]: 10,                             // < 10
      [Op.lte]: 10,                            // <= 10
      [Op.between]: [6, 10],                   // BETWEEN 6 AND 10
      [Op.notBetween]: [11, 15],               // NOT BETWEEN 11 AND 15

      // Other operators

      [Op.all]: sequelize.literal('SELECT 1'), // > ALL (SELECT 1)

      [Op.in]: [1, 2],                         // IN [1, 2]
      [Op.notIn]: [1, 2],                      // NOT IN [1, 2]

      [Op.like]: '%hat',                       // LIKE '%hat'
      [Op.notLike]: '%hat',                    // NOT LIKE '%hat'
      [Op.startsWith]: 'hat',                  // LIKE 'hat%'
      [Op.endsWith]: 'hat',                    // LIKE '%hat'
      [Op.substring]: 'hat',                   // LIKE '%hat%'
      [Op.iLike]: '%hat',                      // ILIKE '%hat' (case insensitive) (PG only)
      [Op.notILike]: '%hat',                   // NOT ILIKE '%hat'  (PG only)
      [Op.regexp]: '^[h|a|t]',                 // REGEXP/~ '^[h|a|t]' (MySQL/PG only)
      [Op.notRegexp]: '^[h|a|t]',              // NOT REGEXP/!~ '^[h|a|t]' (MySQL/PG only)
      [Op.iRegexp]: '^[h|a|t]',                // ~* '^[h|a|t]' (PG only)
      [Op.notIRegexp]: '^[h|a|t]',             // !~* '^[h|a|t]' (PG only)

      [Op.any]: [2, 3],                        // ANY (ARRAY[2, 3]::INTEGER[]) (PG only)
      [Op.match]: Sequelize.fn('to_tsquery', 'fat & rat') // 문자열 'fat' 및 'rat'에 대한 텍스트 검색 일치(PG만 해당)

      // Postgres에서 Op.like/Op.iLike/Op.notLike는 Op.any에 결합될 수 있습니다.:
      [Op.like]: { [Op.any]: ['cat', 'hat'] }  // LIKE ANY (ARRAY['cat', 'hat'])
    }
  }
});
```

Postgres 에서는 다른 문법이 존재하는거 같습니다.



#### ▶ in 사용하기

```js
Post.findAll({
  where: {
    id: [1,2,3] // Same as using `id: { [Op.in]: [1,2,3] }`
  }
});
// SELECT ... FROM "posts" AS "post" WHERE "post"."id" IN (1, 2, 3);
```

배열을 where 옵션에 직접 전달하면 암묵적으로 **IN 연산자**가 사용됩니다.



#### ▶ And와 Or 동시에 사용하기

```js
const { Op } = require("sequelize");

Foo.findAll({
  where: {
    rank: {
      [Op.or]: {
        [Op.lt]: 1000,
        [Op.eq]: null
      }
    },
    // rank < 1000 OR rank IS NULL

    {
      createdAt: {
        [Op.lt]: new Date(),
        [Op.gt]: new Date(new Date() - 24 * 60 * 60 * 1000)
      }
    },
    // createdAt < [timestamp] AND createdAt > [timestamp]

    {
      [Op.or]: [
        {
          title: {
            [Op.like]: 'Boat%'
          }
        },
        {
          description: {
            [Op.like]: '%boat%'
          }
        }
      ]
    }
    // title LIKE 'Boat%' OR description LIKE '%boat%'
  }
});
```

- rank는 or로 묶었습니다.
- createdAt은 and로 묶고 범위를 지정했습니다.
- title 칼럼과 descriptino 칼럼은 or할 수 있습니다. 둘다 like문을 사용했습니다.
  - title은 Boat로 시작하는 단어 또는 description은 boat가 들어간 단어를 찾게됩니다.



#### ▶ Not 하용하기

```js
Project.findAll({
  where: {
    name: 'Some Project',
    [Op.not]: [
      { id: [1,2,3] },
      {
        description: {
          [Op.like]: 'Hello%'
        }
      }
    ]
  }
});
```

위 쿼리는 id가 1,2,3이 없고 description칼럼에 Hello로 시작하는 것이 없어야 합니다.

```sql
SELECT *
FROM `Projects`
WHERE (
  `Projects`.`name` = 'Some Project'
  AND NOT (
    `Projects`.`id` IN (1,2,3)
    AND
    `Projects`.`description` LIKE 'Hello%'
  )
)
```

이런 형태가 됩니다.