## ✅ Sequelize에서 값 증가,감소 update 하기

저는 입력을 할 때 마다 -1이 되는 동작이 필요했습니다. 0 이상의 값만 감소시키려고 합니다.

기존칼럼에 - 하는 쿼리을 짜봤습니다.

```sql
update inventories
set count = (select count from inventories i2 where item_id = 1) - 1
where (select count from inventories i2 where  item_id = 1) >= 0 and item_id = 1;
```

inventories라는 테이블에 count라는 기존 칼럼에 -1 을 하는 칼럼 입니다. 

item_id칼럼의 값을 주고 값이 0 이상일 때만 동작하게 됩니다. 이제 이걸 sequelize로 옮기려고합니다.

#### 👉 방법1.  **update**메서드로 하는 방법도 있습니다.

```ts
const dao ={
updateItem(params: InventoryUpdateWithItemOutflowParams): Promise<UpdatedResult> {
    return new Promise((resolve, reject) => {
      Inventory.update(
        { count: Sequelize.literal(`count-${params.count}`) },
        {
          where: {
            itemId: params.itemId,
            count: { [Op.gt]: 0 }, // '> 0' 조건
          },
        }
      )
        .then(([updated]) => {
          resolve({ updatedCount: updated });
        })
        .catch((err) => {
          reject(err);
        });
    });
  },
}
```

이 때는 Sequlize의 literal을 이용해서 칼럼을 현재 칼럼을 빼는 칼럼을 string형태로 추가해야 합니다.

**쿼리 결과**

```sh
 UPDATE "inventories" SET "count"=count-2,"updated_at"=$1 WHERE ("deleted_at" IS NULL AND ("count" > '0' AND "storage_id" = $2 AND "item_id" = $3))
```



#### 👉 방법2. increment() 메서드를 사용하는 방법도 있습니다.

```ts
const dao ={  
updateWithItemOutflow(params: InventoryUpdateWithItemOutflowParams): Promise<UpdatedResult> {
    return new Promise((resolve, reject) => {
      Inventory.increment(
        { count: -params.count },
        {
          where: {
            itemId: params.itemId,
            count: { [Op.gt]: 0 }, // '> 0' 조건
          },
        }
      )
        .then((updated) => {
          resolve({ updatedCount: updated.id });
        })
        .catch((err) => {
          reject(err);
        });
    });
  },
}
```

**쿼리 결과**

```sh
UPDATE "inventories" SET "count"=count-2,"updated_at"=$1 WHERE ("deleted_at" IS NULL AND ("count" > '0' AND "storage_id" = $2 AND "item_id" = $3))
```



명확하게 **increment()** 메서드는 '증가시켜준다' 라는 의미가 분명한거 같아 확실히 증가, 감소가 필요한 칼럼은 increment()를 쓰고 literal 자체를 변화시키면서 update를 하고 싶을 때는 **update()** 메서드를 쓰는게 좋아보입니다.





#### 참고

- https://stackoverflow.com/questions/55646233/updating-with-calculated-values-in-sequelize
- https://includecoding.tistory.com/217