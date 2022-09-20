## node.js에서 프로시져 사용하기

[1.프로시저 만들기](#1.-프로시져-만들기.)

[2. node.js와 mssql 연결하기](#2.-node.js와-mssql-연결하기)

[3. 컨트롤러 만들기(router의 역할)](3.-컨트롤러-만들기(router의-역할))

[4. 서비스 로직 만들기](4.-서비스-로직-만들기)

[5. Dao에서 db에서 값 가지고 오기](5.-Dao에서-db에서-값-가지고-오기)

#### 1. 프로시져 만들기.

```sql
CREATE  PROCEDURE dbo.test
	@CO varchar(50),
	@TOTAL int=NULL output
AS
begin
	SELECT @TOTAL = COUNT(*) from cal_meters cm2 ;
	SELECT * FROM cal_meters cm WHERE code = @CO;
end

exec dbo.test'10002-03-01';
```

`create procedure` 문으로 프로시저를 만들 수 있습니다.

함수의 매개변수 처럼 `@변수명` + `타입`을 써서 프로시저 안에 **변수**를 받을 수 있습니다.

![image](https://user-images.githubusercontent.com/112359150/191213395-0f22b44a-83bf-4811-96a9-cd952592aa76.png)

calmeter의 code칼럼입니다. where문에 code를 넣어서 calmeter 전체를 가져와보겠습니다.

#### 2. node.js와 mssql 연결하기

```ts
const config: config = {
  user: 이름,
  password: 패스워드,
  server: db주소,
  port: db포트,
  database: db데이터베이스이름,
  pool: { //커넥션 풀 설정
    max: 30,
    min: 1,
    idleTimeoutMillis: 30000,
  },
};

export const poolPromise = new sql.ConnectionPool(configHtms)
  .connect()
  .then((pool) => {
    console.log('Connected to MSSQL');
    return pool;
  })
  .catch((err) => console.log('Database Connection Failed! Bad Config: ', err));

module.exports = {
  sql,
  poolPromise,
};
```

npm -i sql을 받아서 커넥션 풀을 쓸 수 있어야 합니다. 커넥션 풀을 쓰면 한 번 db에 연결해 놓으면 커넥션 풀로 계속해서 연결 할 수 있습니다.



#### 3. 컨트롤러 만들기(router의 역할)

```ts
const router = express.Router();

// Procedure로 데이터 가져오기
router.post(
  '/procedure-test',
  async (req: Request<unknown, unknown, PROCEDURE_TESTSelectListParams, unknown>, res: Response) => {
    const logFormat = makeLogFormat(req);
    const tokenUser = (req as { decoded?: Payload }).decoded;

    try {
      logging.REQUEST_PARAM(logFormat);

      // 비즈니스 로직 호출
      const result = await PROCEDURE_TESTService.listAll(req.body, logFormat);
      console.log(result);
      // 최종 응답 값 세팅
      const resJson = resSuccess(result, resType.LIST);

      return res.status(resJson.status).json(resJson);
    } catch (err) {
      // 에러 응답 값 세팅
      const resJson = resError(err);

      return res.status(resJson.status).json(resJson);
    }
  }
);
```

컨트롤러에서 사용자의 요청을 받고 service 로직에 넘겨서 비지니스 로직을 실행시킵니다. 

POST요청으로 `/procedure-test`가 들어오면 service단의 listAll()이 동작할 것 입니다.

여기서에 제가 사용한 interface는 ` PROCEDURE_TESTSelectListParams`입니다.

```ts
// selectList
export interface PROCEDURE_TESTSelectListParams {
  CO: number;
  limit?: number;
  offset?: number;
  order?: string;
}
```

인터페이스 형태로 변수를 받아올 수 있습니다. `CO`객체를 body에서 받아와야 하니 interface로 객체타입을 지정해줍니다.



#### 4. 서비스 로직 만들기

```ts
const service = {
  // selectList
  async listAll(params: PROCEDURE_TESTSelectListParams): Promise<Array<any>> {
    let result: PROCEDURE_TESTSelectListResult | void;

    try {
      result = await PROCEDURETESTDao.selectList(params);
    } catch (err) {
      return new Promise((resolve, reject) => {
        reject(err);
      });
    }

    return new Promise((resolve) => {
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-ignore
      resolve(result);
    });
  },
};
```

컨트롤러에서 받은 req.body들을 **Dao(db와 접촉하는 layer)**에 넘겨주는 역할을 합니다.



#### 5. Dao에서 db에서 값 가지고 오기

```ts
//select All
async selectList(params: PROCEDURE_TESTSelectListParams): Promise<PROCEDURE_TESTSelectListResult | void> {
    let result: PROCEDURE_TESTSelectListResult | void;
    const pool = await poolPromise;

    if (pool) {
      result = await pool
        .request()
        .input('CO', sql.VarChar(50), params.CO)
        .output('TOTAL', sql.Int, 0)
        .execute('dbo.test')
        .then((result) => {
          const result_data: PROCEDURE_TESTSelectListResult = {
            total: result.output.TOTAL as number,
            result: result.recordset,
          };
          return result_data;
        })
        .catch((err) => {
          console.log('err', err);
        });
    }

    return result;
  }
```

여기서 **커넥션 풀**을 가져와서 db의 프로시져를 실행합니다. 물론 node.js에서 `sql`라이브러리의 도움이 필요합니다.

- 먼저 위에서 만든 pool객체를 가져옵니다.
- **input(변수명,타입,입력 값)**을 이용해 DB프로시져 안에  `CO`라는 변수에 값을 **넣습니다**.
- **output(변수명,타입,입력 값)**을 이용해 DB프로시져 에서 `TOTAL`라는 변수를 **가져옵니다**.

이제 then() 구문으로 결과(result)가 온다면 **총 개수(total)**, **실제 결과값(result)**을 반환하면 됩니다.

![image](https://user-images.githubusercontent.com/112359150/191213792-674c69c5-0558-46a5-b7e3-a76280c6c795.png)

성공적으로 total값과 cal_meter의 값을 얻을 수 있게됐습니다.



#### 🚩주의!

```sql
CREATE  PROCEDURE dbo.test
	@CO varchar(50),
	@TOTAL int=NULL output
AS
```

프로시저를 만들 때 **변수 타입,크기** 를 지정하게 됩니다.

```ts
.input('CO', sql.VarChar(50), params.CO)
```

실제 값을 넣을 때도 같은 변수 타입, 크기를 지정해줘야 합니다.

실제 db안의 칼럼 크기도 주의해서 프로시저를 만들어야 합니다. **칼럼 보다 더 작은 값으로 프로시저를 만들면 값이 안들어 갑니다.**



#### 참고

https://gameserverengineer-k.tistory.com/7

https://ahnsisters.tistory.com/7 