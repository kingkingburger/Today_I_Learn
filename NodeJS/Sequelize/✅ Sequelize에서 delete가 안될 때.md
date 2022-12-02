## ✅ Sequelize에서 delete가 안될 때 

분명 삭제`destroy`를 쓰면 삭제된다고 하는데 Update 쿼리가 날라가는 겁니다. 이상하다...

원인을 알아보니 `destroy`는 **소프트삭제, 하드삭제** 2가지 모드가 존재했습니다.



#### 기본적으로 `destroy`는 소프트 삭제가 발생합니다.

```js
await Post.destroy({
  where: {
    id: 1
  }
});
// 실제쿼리 : UPDATE "posts" SET "deletedAt"=[timestamp] WHERE "deletedAt" IS NULL AND "id" = 1
```

테이블의 deletedAt에 삭제 시간만 update하는 쿼리를 날립니다.

하드 삭제를 정말로 원한다면 `force: true`옵션을 사용하여 강제로 삭제할 수 있습니다.

#### force: true 옵션 켜기!

```js
await Post.destroy({
  where: {
    id: 1
  },
  force: true
});
// 실제쿼리 : DELETE FROM "posts" WHERE "id" = 1
```

위의 예시는 정적 `destroy`메소드를 예로 `Post.destroy()` 를 보았습니다, 인스턴스 메소드를 사용해도 모든 것이 동일하게 동작합니다.
예시
```js
const post = await Post.create({ title: 'test' });
console.log(post instanceof Post); // true
await post.destroy(); // Would just set the `deletedAt` flag
await post.destroy({ force: true }); // Would really delete the record
```

