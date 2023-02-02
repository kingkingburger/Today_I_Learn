### [Nest] Test시 Please make sure that the argument Repository at index [0] is available in the ResultIoModule 에러 처리

```ts
import { Test, TestingModule } from "@nestjs/testing";
import { ChampionService } from "./champion.service";
import { Champion } from "./entities/champion.entity";
import { ChampionRate } from "../champion-rate/entities/champion-rate.entity";
rate.repository";

describe("ChampionService", () => {
  let service: ChampionService;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      imports: [Champion, ChampionRate],
      providers: [ChampionService]
    }).compile();

    service = app.get<ChampionService>(ChampionService);
  });

  it("should be defined", () => {
    expect(service).toBeDefined();
  });
});
```

위 코드를 테스트 하려고 했습니다. 처음이니깐 service단만 테스트 코드를 돌려보려 했습니다.

그런데 에러가 났습니다.

![image](https://user-images.githubusercontent.com/65094518/215993041-32f99993-a302-44a0-b0cf-82b0918ff477.png)

에러 코드 입니다. jest가 친절하게 어떤 부분이 에러인지 알려줍니다.

- RootTestModule은 유효한 NestJS 모듈입니까?
- ChampionRepository가 Provider인 경우 현재 RootTestModule의 일부입니까?
- 별도의 @Module에서 ChampionRepository를 내보낸 경우 해당 모듈을 RootTestModule 내에서 가져왔습니까?
  @Module({
  imports: [ /* ChampionRepository를 포함하는 모듈 */ ]
  })

여기서 저는 module을 직접 넣어줘야겠다고 생각했습니다. spring처럼 컨테이너가 어노테이션이 붙은것을 인식해서 알아서 주입시켜주는줄 알았는데 Test환경에서는 다른것같습니다.

```ts
@Injectable()
export class ChampionService {
  constructor(
    @InjectRepository(Champion)
    private readonly championRepository: Repository<Champion>,
    @InjectRepository(ChampionRate)
    private readonly championRateRepository: Repository<ChampionRate>
  ) {}
}
```

import 하고 있는 ChampionService 입니다. 보니깐 생성자에 championRepository와 championRateRepository를 넣으면 됩니다.

자, 그러면 2가지를 알아야 할거같습니다.

- **test환경에서 생성자를 직접 주입하는법**
- **TypeORM환경에서 Repository를 만드는법**

## 🟩 test환경에서 생성자를 직접 주입하는법

```ts
import { Test, TestingModule } from "@nestjs/testing";
import { ChampionService } from "./champion.service";
import { Champion } from "./entities/champion.entity";
import { ChampionRate } from "../champion-rate/entities/champion-rate.entity";
import { getRepositoryToken } from "@nestjs/typeorm";

describe("ChampionService", () => {
  let service: ChampionService;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      providers: [
        ChampionService,
        { provide: getRepositoryToken(Champion), useClass: Champion },
        { provide: getRepositoryToken(ChampionRate), useClass: ChampionRate },
      ],
    }).compile();

    service = app.get<ChampionService>(ChampionService);
  });
});
```

createTestingModule안에는 ModuleMetadata가 들어가야 합니다. ModuleMetadata안에는

![image](https://user-images.githubusercontent.com/65094518/215995413-a9a7b299-6239-4984-8a94-4bf897ef2051.png)

imports와 controllers도 있고 proviers를 넣을 수 있습니다. 저희가 넣어야 할건 proviers 입니다.

proviers란 `Nest 인젝터에 의해 인스턴스화되고 적어도 이 모듈 전체에서 공유될 수 있는 목록입니다.`

proviers안에는

![image](https://user-images.githubusercontent.com/65094518/215995896-2102ed8d-b5bd-47ca-92af-8090460ccd88.png)

ClassProvier가 들어가 있습니다. 우리가 주의해서 봐야한건 provide와 useClass 입니다.

**provide** : 어떤걸 주입시킬것인가?

**useClass:** 어떤 클래스 인가?

내가 주입시킬 정보를 provide와 useClass에 넣으면 됩니다.

![image](https://user-images.githubusercontent.com/65094518/215996491-ca002a1b-e13e-4855-a600-85e0fa12b06d.png)

**getRepositoryToken()**은 **TypeORM**에서 제공해주는 함수입니다. 객체 자체를 주입시키기 위함 입니다. **@InjectRepository**와 동일한 역할을 합니다.

이제 championRepository 클래스와 championRateRepository 클래스를 만들어야 합니다. 위에 예시는 지금 동작하지 않습니다. Champion 클래스는 아직 Repository가 없기 때문입니다.

## 🟩 **TypeORM환경에서 Repository를 만드는법**

https://typeorm.io/

공식문서에서 Repository를 만드는 법이 나와있습니다. 그중 한가지가 @Entity()를 쓰고 BaseEntity를 상속받는 것입니다.

```ts
import { Entity, PrimaryGeneratedColumn, Column, BaseEntity } from "typeorm";

@Entity()
export class User extends BaseEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  firstName: string;

  @Column()
  lastName: string;

  @Column()
  age: number;
}
```

그러면 User 클래스는 Repository 를 주입받았습니다.

```ts
const user = new User();
user.firstName = "Timber";
user.lastName = "Saw";
user.age = 25;
await user.save();

const allUsers = await User.find();
const firstUser = await User.findOneBy({
  id: 1,
});
const timber = await User.findOneBy({
  firstName: "Timber",
  lastName: "Saw",
});

await timber.remove();
```

Repository를 따로 주입받지 않아도 클래스 자체에로 repository를 사용하는 것을 볼 수 있습니다.

#### Champion

```ts
import { ChampionRate } from "src/champion-rate/entities/champion-rate.entity";
import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  JoinColumn,
  OneToOne,
  PrimaryGeneratedColumn,
  UpdateDateColumn,
  BaseEntity,
} from "typeorm";

@Entity()
export class Champion extends BaseEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  key: number; // 챔피언 고유의 id

  @Column({ unique: true })
  name: string;

  @Column()
  engName: string;

  @Column({ default: "" })
  line: string;

  @Column()
  img: string;

  @CreateDateColumn()
  createdAt: Date;
  @UpdateDateColumn()
  updatedAt: Date;
  @DeleteDateColumn()
  deletedAt: Date | null;
  @OneToOne((type) => ChampionRate, (championRate) => championRate.name)
  @JoinColumn()
  championRateName: number; // championRate에 대한 테이블 fk
}
```

#### ChampionRate

```ts
import { BaseEntity, Column, Entity, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class ChampionRate extends BaseEntity {
  @PrimaryGeneratedColumn()
  id: number;
  @Column({ unique: true })
  name: string;

  @Column()
  worst1Name: string;
  @Column()
  worst2Name: string;
  @Column()
  worst3Name: string;
  @Column()
  worst1Rate: string;
  @Column()
  worst2Rate: string;
  @Column()
  worst3Rate: string;
  @Column()
  great1Name: string;
  @Column()
  great2Name: string;
  @Column()
  great3Name: string;
  @Column()
  great1Rate: string;
  @Column()
  great2Rate: string;
  @Column()
  great3Rate: string;
}
```

BaseEntity를 상속받아서 Repository를 사용할 수 있습니다. 그러므로 useClase에 넣을 수 있게됩니다.

#### 결과

![image](https://user-images.githubusercontent.com/65094518/216001514-47c975fe-dc3b-4154-844b-a740171f71ca.png)

#### 출처

- https://www.inflearn.com/questions/397737/%ED%85%8C%EC%8A%A4%ED%8A%B8-di-%EA%B4%80%EB%A0%A8-%EC%A7%88%EB%AC%B8
  (provier,useClasse 아이디어 얻음)
- https://stackoverflow.com/questions/65570680/what-is-getrepositorytoken-in-nestjs-typeorm-and-when-to-use-it
- https://junior-datalist.tistory.com/147
  (주입 아이디어 얻음)
- https://typeorm.io/
  (Repository 만드는법 얻음)
- https://stackoverflow.com/questions/65570680/what-is-getrepositorytoken-in-nestjs-typeorm-and-when-to-use-it
  (getRepositoryToken에 대한 아이디어 얻음)
