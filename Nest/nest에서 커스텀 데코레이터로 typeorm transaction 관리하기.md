# nest에서 커스텀 데코레이터로 typeorm transaction 관리하기

기존에 코드로 typeorm의 transaction을 관리해야 한다면

```jsx
try {
			// ..doing
      await queryRunner.commitTransaction();
      return;
    } catch (e) {
      await queryRunner.rollbackTransaction();
    } finally {
      await queryRunner.release();
    }
```

이런 형태가 되었을 것 입니다.

connection을 생성하고 일일이 commit과 rollback, release를 하는 과정은 복잡했습니다. 이 과정을 축소시키고자 transaction interceptor 와 custom decorator를 만들어 보겠습니다.



transaction.interceptor.ts

```jsx
@Injectable()
export class TransactionInterceptor implements NestInterceptor {
  constructor(private readonly dataSource: DataSource) {}
  async intercept(
    context: ExecutionContext,
    next: CallHandler,
  ): Promise<Observable<any>> {
    const req = context.switchToHttp().getRequest();
    const queryRunner: QueryRunner = await this.dbInit();

    req.queryRunnerManager = queryRunner.manager;

    return next.handle().pipe(
      catchError(async (e) => {
        await queryRunner.rollbackTransaction();
        await queryRunner.release();

        if (e instanceof HttpException) {
          throw new HttpException(e.message, e.getStatus());
        } else {
          throw new InternalServerErrorException(e.message);
        }
      }),
      tap(async () => {
        await queryRunner.commitTransaction();
        await queryRunner.release();
      }),
    );
  }

  private async dbInit(): Promise<QueryRunner> {
    const queryRunner = this.dataSource.createQueryRunner();
    await queryRunner.connect();
    await queryRunner.startTransaction();

    return queryRunner;
  }
}
```

nest에서 interceptor는 서비스 로직의 실행 전, 후 어떠한 행동을 실행할 수 있게 해줍니다.

우선 요청이 들어오면

```tsx
async intercept(
  context: ExecutionContext,
  next: CallHandler,
): Promise<Observable<any>> {
const req = context.switchToHttp().getRequest();
const queryRunner: QueryRunner =await this.dbInit();

  req.queryRunnerManager = queryRunner.manager;

  ...
```

위 부분을 통해 request 객체를 가져오고,

**connection을 생성한 후 transaction을 시작하는 공통된 작업을 수행합니다. 새로운 connection pool을 만드는 것이죠.**

**queryRunner의 manager를 request 객체에 담아둡니다.**

**그다음 next.handle()을 통해 interceptor가 감싼 메서드를 실행한 후, pipe()를 통해 메서드 실행 후의 작업을 정의합니다.**

```tsx
return next.handle().pipe(
  catchError(async (e) => {
await queryRunner.rollbackTransaction();
await queryRunner.release();

if (e instanceof HttpException) {
throw new HttpException(e.message, e.getStatus());
    }else {
throw new InternalServerErrorException(e.message);
    }
  }),
  tap(async () => {
await queryRunner.commitTransaction();
await queryRunner.release();
  }),
);
```

**catchError를 통해 에러가 발생했다면 transaction을 rollback 하고, connection을 release 한 후 잡은 에러를 처리합니다.**

**에러 없이 잘 끝났다면 transaction을 commit 하고, release 한 후 작업이 종료되도록 합니다.**

자, 이제 이렇게 구현한 Interceptor를 통해 코드를 개선하기 전에 request 객체에 담아둔  query manager를 사용하기 위한 커스텀 데코레이터를 만듭시다.



transaction.decorator.ts

```jsx
import { createParamDecorator, ExecutionContext } from '@nestjs/common';

export const TransactionManager = createParamDecorator(
  (data: unknown, ctx: ExecutionContext) => {
    const req = ctx.switchToHttp().getRequest();
    return req.queryRunnerManager;
  },
);
```

이 데코레이터는 request 객체에 접근한 후, 담아뒀떤 manager를 반환하도록 하는 데코레이터 입니다.



### 사용방법

🟩 controller

```jsx
  @UseInterceptors(TransactionInterceptor)
  @Post('/')
  create(
    @Body() body: ApiRequest,
    @TransactionManager() queryRunnerManager: EntityManager,
  ) {
    return this.resultService.create(
      body,
      queryRunnerManager,
    );
  }
```

controller 에서는 Interface를 사용하기 위해서는 @UseInterceptors(TransactionInterceptor)

를 넣어주셔야 합니다.

service메서드에 데코레이터로 만든 queryRunnerManager를 넣어줍니다.



🟩 service

```jsx
@Injectable()
export class TestService{
constructor(
		...
    private dataSource: DataSource,
  ) {}

  async create(
    apiRequest: ApiRequest,
    queryRunnerManager: EntityManager,
  ) {
    // const queryRunner = this.dataSource.createQueryRunner();
    const queryRunner = queryRunnerManager.queryRunner;
    await queryRunner.connect();
    await queryRunner.startTransaction();
   
    try {
      const OrderResult = await queryRunner.manager
        .getRepository(OutOrder)
        .upsert(OutOrderParamArray, ['Asrs', 'Awb']);
      if (asrsOutOrderResult) {
        const simulatorResultBody: CreateSimulatorResultDto = {
          startDate: new Date(),
          endDate: new Date(),
          version: bodyResult.version,
          simulation: mode,
        };
        const simulatorResultResult = await queryRunner.manager
          .getRepository(SimulatorResult)
          .save(simulatorResultBody);

        const joinParamArray: CreateJoinDto[] = [];
        const historyParamArray: CreateHistoryDto[] = [];

        const joinResult = queryRunner.manager
          .getRepository(CreateJoinDto)
          .save(joinParamArray);
        const historyResult = queryRunner.manager
          .getRepository(CreateHistoryDto)
          .save(historyParamArray);
        await Promise.all([joinResult, historyResult]); 
      }

      // await queryRunner.commitTransaction();
      return psResult;
    } catch (error) {
      // await queryRunner.rollbackTransaction();
      throw new TypeORMError(`rollback Working - ${error}`);
    } finally {
      // await queryRunner.release();
    }
  }
```

이전의 썻던 queryRunner의 값을 매개변수로 들어오는 queryRunnerManager의 queryRunner로 바꿔줍니다.

try, catch, finally에서 사용하던 commit, rollback, release 하는 로직은 interceptor에서 대신 실행해 줍니다.



🟥 만약 그대로 실행시킨다면 finally의 release 부분에서 2번 relase하냐는 오류가 나오게 됩니다.

```jsx
if (this.isReleased) throw new QueryRunnerAlreadyReleasedError()
QueryRunnerAlreadyReleasedError: Query runner already released. Cannot run queries anymore.
```



참고:

- [NestJS - Transaction Interceptor 적용하기 (tistory.com)](https://hou27.tistory.com/entry/NestJS-Transaction-Interceptor-적용하기)
- [Interceptor 사용하여 TypeORM Transaction 적용하기 (tistory.com)](https://sol-devlog.tistory.com/17)