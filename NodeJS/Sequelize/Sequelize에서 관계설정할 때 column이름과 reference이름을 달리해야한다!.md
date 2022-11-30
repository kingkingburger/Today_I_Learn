## ✅ sequelize에서 관계설정할 때 column 이름과 reference 이름을 달리해야 한다!

여기서 reference이름이란 xx as minho 처럼 별명지어 출력을 할 때 쓰입니다.




I faced exactly this problem while play with Sequelize, It's happened because the **`column name` and `reference name` are same**

**잘못된 구현**

```coffeescript
module.exports = (sequelize, DataTypes) => {
  const session = sequelize.define('session', {
    menteeId: DataTypes.INTEGER,
  }, {});

  session.associate = (models) => {
    session.belongsTo(models.user, {
      foreignKey: 'menteeId',
      as: 'menteeId',
      onDelete: 'CASCADE',
    });
  };
  return session;
};
```

session은 model의 user와 연관관계를 맺고있습니다. user의 menteeId가 FK가 되겠군요. 그리고 session에서 출력할 때 **menteeId** 라는 이름으로 출력하려고 합니다.

그런데 에러가 나게됩니다. Sequelize는  `column name` (`menteeId`) 과 `alias name` (`menteeId`) 같은 것을 허용하지 않습니다. 해결방법은 **alias name만 column name과 다른것으로  바꾸면** 됩니다.

올바른 예시

```coffeescript
module.exports = (sequelize, DataTypes) => {
  const session = sequelize.define('session', {
    menteeId: DataTypes.INTEGER,
  }, {});

  session.associate = (models) => {
    session.belongsTo(models.user, {
      foreignKey: 'menteeId',
      as: 'MenteeId', // Changes applied here
      onDelete: 'CASCADE',
    });
  };
  return session;
};
```
