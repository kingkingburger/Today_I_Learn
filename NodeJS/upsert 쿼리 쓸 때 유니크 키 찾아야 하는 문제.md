## **Error: Primary Key or Unique key should be passed to upsert query**

upsert 쿼리를 쓰는데 key를 못찾는 문제

```
const MaintenanceParams: MaintenanceInsertParams = {
        machineRoomId: calMeterInfo.machineRoomId,
        calMeterId: calMeterInfo.id,
        coolerId: null,
        compactUnitId: null,
        meterGaugeId: null,
        maintPriceDtlId: null,
        ccIdMaintType: 371, // MAINT_TYPE_09
        ccIdHeatDia: null,
        sapQ: null,
        sapF: null,
        sapV: null,
        content: null,
        priceType: MaintenanceDefaults.priceType,
        customerName: null,
        customerSign: null,
        userSign: null,
        confirmUserSign: null,
        // state: req.body.state || MaintenanceDefaults.state,
        state: MaintenanceDefaults.state,
        note: null,
        workDate: null,
        userId: null,
        imageList: null,
      };
// 4. 유지보수 테이블에 객체 적용
const maintenanceid = await maintenanceDao.upsert(MaintenanceParams, transaction);
```

db에 넣으려는 객체는 위와 같습니다. 그 다음 Dao 에 있는 upsert 객체를 호출 합니다.

```
upsert(params: MaintenanceInsertParams, transaction: Transaction | undefined = undefined): Promise<UpsertResult> {
    return new Promise((resolve, reject) => {
      Maintenance.upsert(params, {
        transaction: transaction !== undefined ? transaction : undefined,
      })
        .then((result) => {
          resolve({ upsertedId: result[0].id });
        })
        .catch((err) => {
          reject(err);
        });
    });
  }
```

여기서 직접적으로 db와 소통을 합니다. **MaintenanceInsertParams 객체**를 넘겨주면 Sequeilze가 알아서 **Maintenance 테이블**에 가서 **machineRoomId** 값을 찾아서 있다면 **update**를 하고 없다면 **insert를 하는 동작**을 원했습니다.

근데 Sequelize는 **Maintenance테이블**의 **어떤 키값을 기준으로 update를 하고 insert를 하는지 모르는거** 같습니다. 나는 **machineroomId 값**을 기준으로 동작하라고 명령하고 싶습니다.

![https://user-images.githubusercontent.com/112359150/187834989-dbe7fd4d-50c3-4895-9641-344df9fd3b01.png](https://ci3.googleusercontent.com/proxy/yKtm2yFCKVqWnntmKWo0Vk9eoTvqC3rx59d5igBb0dWwgBXvUQQvWSYfHRXrX7WEu901sg4pDeOCnxw6aTwEPazf1mcalZzaGsZ1inhMuzu5jAY_OBu0sNrmldm3tHom2CYMWSCTxKowb-Rz9_nJmNa7qhIMompa0g=s0-d-e1-ft#https://user-images.githubusercontent.com/112359150/187834989-dbe7fd4d-50c3-4895-9641-344df9fd3b01.png)

그러면 Table 세팅에서 객체를 생성할 때 **machineRoomId를 유니크 키**로 지정합시다.

즉, **table Model**의 유니크한 키를 하나 지정을 해주면 Sequilze가 알아서 그걸로 upsert()를 실행합니다.