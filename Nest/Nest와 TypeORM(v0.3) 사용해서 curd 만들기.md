# Nest와 TypeORM(v0.3) 사용해서 curd 만들기

nest와 typeorm으로 db에 연결해보겠습니다. TypeOrm이 0.3 버전으로 올라감에 따라 다른방법으로 db연결을 해야 합니다.

#### 🟩 일단 모듈이 필요합니다.

```
#npm
npm install mysql2 typeorm @nestjs/typeorm
```

1. @nestjs/typeorm - Nest.js에서 TypeORM을 사용하기 위해 연동시켜주는 모듈
2. typeorm - 실제 TypeORM(TypeORM은 JavaScript를 지원합니다)
3. mysql2 - MySQL 데이터베이스 연결 시 사용



#### 🟩 TypeORM 파일 설정

src/configs 폴더를 생성한 후에 그 안에다가 설정파일을 만듭니다.

![image](https://user-images.githubusercontent.com/112359150/207207588-01368044-8c3b-4356-a0b2-aa8bde03d586.png)

파일이름은 본인이 편한 이름으로 생성해주면 됩니다. 이 때 ts 확장자는 무조건 해주셔야 합니다. 컴파일 시 제외되기 때문입니다.



```ts
import { TypeOrmModuleOptions } from '@nestjs/typeorm';

export const TypeOrmConfig: TypeOrmModuleOptions = {
  type: 'mariadb', //Database 설정
  host: 'localhost',
  port: 3308,
  username: 'root',
  password: '1234',
  database: 'dev',
  entities: [__dirname + '/../**/*.entity.{js,ts}'], // Entity 연결, entity를 모두 찾아줘라!
  synchronize: true, //true 값을 설정하면 어플리케이션을 다시 실행할 때 엔티티안에서 수정된 컬럼의 길이 타입 변경값등을 해당 테이블을 Drop한 후 다시 생성해준다. jpa에서 create, update 의 역할입니다.
};
```

파일안에 우리가 사용할 db의 정보를 넣어줍니다.



#### 🟩 설정 파일 연결

typeOrm 정보를 Nest.js에 연결해봅시다.

**app.module.ts** 

```ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { TypeOrmConfig } from './config/typeorm.config';
import { UserModule } from './user/user.module';

@Module({
  imports: [
    TypeOrmModule.forRoot(TypeOrmConfig), // TypeORM 설정파일 연결
    UserModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}
```

app.module.ts 파일에 우리 **TypeOrmConfig**를 적용시켜달라 합니다.

방법은 imports 안에 **TypeOrmModule**를 가져와서 **forRoo**t로 typeORM  환경설정을 적용시켜줍니다.



#### 🟩 Entity 생성

typeOrm이 0.3 버전으로 올라오면서 repository를 생성하지 않고 Service에서 바로 주입받을 수 있게되었습니다. @EntityRepository같은 데코레이터를 만드는 방법이 있습니다. 여기서는 0.3버전에 맞는 예시를 들어보겠습니다. entity와 Service만 있다면 Repository는 Serivce 단에서 바로 주입받을 수 있습니다.(Repository 파일이 필요 없습니다.)

![image](https://user-images.githubusercontent.com/112359150/207484412-c86ffff3-51e9-495d-af2c-d21267411866.png)

db의 테이블을 담당하는 **entity**파일을 만듭니다.

**🚩 user.entity.ts**

```ts
import {
  Column,
  CreateDateColumn,
  DeleteDateColumn,
  Entity,
  PrimaryGeneratedColumn,
  UpdateDateColumn,
} from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  user_id: string;
  @Column()
  password: string;
  @Column()
  name: string;
  @Column()
  age: number;
  @CreateDateColumn()
  createdAt: Date;
  @UpdateDateColumn()
  updatedAt: Date;
  @DeleteDateColumn()
  deletedAt: Date | null;
}
```

- @Entity - 해당 클래스는 DB user 테이블과 매핑시킬 때 사용
- @Unique - 유니크 컬럼을 설정할 때 사용(배열 형태로 원하는 컬럼 값을 지정하면 된다)
- @PrimaryGeneratedColumn - uuid 값을 지정하면 해당 컬럼은 uuid 타입으로 설정이 되며, Auto Increment 타입으로 설정

​                          Auto_Increment : @PrimaryGeneratedColumn()

​                          UUID: @PrimaryGeneratedColumn('uuid')

- @Column - 해당 클래스 속성과 DB user 테이블 컬럼과 매핑시킬 때 사용
- @CreateDateColumn - 데이터가 생성되는 시간을 기록할 때 사용
- @UpdateDateColumn - 데이터가 수정되는 시간을 기록할 때 사용
- @DeleteDateColumn - 데이터가 삭제되는 시간을 기록할 때 사용(실제 삭제되지 않는다. 백업 서버가 없다면 해당 옵션을 사용!!)



#### 🟩 Service 생성

따로 Repository를 안만들어도 생성자에서 바로 주입받을 수 있게됩니다. **@InjectRepository(Entity)**로 Entity에 관한 Repository가 바로 만들어 지는거 같습니다.

Nest.js는 저장소 패턴(Repository Pattern)을 지원합니다. Repository 계층에서는 DB 작업을 다룹니다.

**"1. @Controller -> 2.@Service -> 3. Repository"**

@Controller 계층에서는 클라이언트 요청 정보를 처리하고 @Service 계층에서는 비즈니스 로직을 담당하며, Repository 계층에서는 DB 작업을 다룬다고 생각하시면 됩니다.

**🚩 user.service.ts 생성**

```ts
import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

import { CreateUserDto, UpdateUserDto } from './dto/user.dto';
import { User } from './entity/user.entity';

@Injectable()
export class UserService {
  //service에서 생성자로 repository를 받아온다.
  constructor(
    @InjectRepository(User) private userRepository: Repository<User>,
  ) {}
  async findALl(): Promise<User[]> {
    return this.userRepository.find();
  }
  create(createUserDto: CreateUserDto): Promise<User> {
    const newUser = this.userRepository.create(createUserDto);
    return this.userRepository.save(newUser);
  }

  // 전체 요소 모두 가져오기
  findAll() {
    return this.userRepository.find();
  }

  // 요소 1개만 가지고 오기
  findOne(id: number) {
    return this.userRepository.findOneBy({ id });
  }

  // 쿼리로 가져오기
  findByQuery(user_id: string) {
    return this.userRepository.find({ where: { user_id } });
  }
    
  // update의 2가지 방법

  // async update(id: number, updateUserDto: UpdateUserDto) {
  //   // const user = await this.findOne(id);
  //   // return this.userRepository.save({ ...user, ...updateUserDto });
  // }
  update(id: number, updateUserDto: UpdateUserDto) {
    return this.userRepository.update(id, updateUserDto);
  }

  // delete의 2가지 방법

  // async remove(id: number) {
  //   const user = await this.findOne(id);
  //   return this.userRepository.remove(user);
  // }
  remove(id: number) {
    return this.userRepository.delete(id);
  }
}
```

spring에서 JPA와 비슷한 문법을 쓰는거같습니다. 저장은 save, select은 find.. 등등 그런데 update와 delete의 설명을 읽어보면 

> Updates entity partially. Entity can be found by a given conditions. Unlike save method executes a primitive operation without cascades, relations and other operations included. Executes fast and efficient UPDATE query. Does not check if entity exist in the database.

저장 방법과 달리 캐스케이드, 관계 및 기타 작업이 포함되지 않은 기본 작업을 실행합니다. 빠르고 효율적인 UPDATE 쿼리를 실행합니다. **엔터티가 데이터베이스에 있는지 확인하지 않습니다**. 엔터티가 있는지 확인을 안하니 없다면는 pass할것이고 있다면 동작할 것입니다.

**findOneQuery**처럼 쿼리형태로 row를 가져올 수 있습니다.





####  🟩 모듈과 연결

**🚩user.module.ts**

```ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './entity/user.entity';

import { UserController } from './user.controller';
import { UserService } from './user.service';

@Module({
  imports: [TypeOrmModule.forFeature([User])], //Entity를 등록하면 알아서 Repository생성
  controllers: [UserController],
  providers: [UserService], 
})
export class UserModule {}
```

우리는 UserModule에서 사용해야하기 때문에 UserModule에 UserRepository를 등록합니다.

이렇게 등록하고 UserService에 등록하고 사용하면 됩니다.



#### 🟩 Controller 생성

TypeORM 메서드는 기본적으로 **Promise 객체**입니다. 그렇기 때문에 **async, await**를 사용할 수 있습니다.

🚩 **user.controller.ts**

```ts
import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Post,
  Query,
} from '@nestjs/common';
import { DeleteResult, UpdateResult } from 'typeorm';
import { CreateUserDto, UpdateUserDto } from './dto/user.dto';
import { UserService } from './user.service';

@Controller('/')
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post('/create_user')
  create(@Body() createUserDto: CreateUserDto): Promise<CreateUserDto> {
    return this.userService.create(createUserDto);
  }

  @Get('/user_all')
  getUserAll(): Promise<User[]> {
    return this.userService.findAll();
  }

  @Get('/user/:id')
  findByUserOne2(@Param('id') id: number): Promise<User> {
    return this.userService.findOne(id);
  }
    
  @Get('/userinfo')
  findByUser(@Query('user') user: string): Promise<User[]> {
    return this.userService.findByQuery(user);
  }
    
  @Post('/user/:id')
  setUser(
    @Param('id') id: number,
    @Body() updateUserDto: UpdateUserDto,
  ): Promise<UpdateResult> {
    return this.userService.update(id, updateUserDto);
  }

  @Delete('/user/delete')
  deleteUser(@Query('id') id: number): Promise<DeleteResult> {
    return this.userService.remove(id);
  }
}
```

@Body로 Dto를 받을 수 있습니다. 자동으로 TypeOrm이 알아서 객체로 만들고 Service단에 가서 객체로 동작하게 됩니다.

**🚩createUserDto, updateUserDto**

```ts
export class CreateUserDto {
  user_id: string; //유저 고유 아이디
  password: string; //유저 비밀번호
  name: string; //유저 이름
  age: number; //유저나이
}

export class UpdateUserDto extends CreateUserDto {
  id: number;
}
```



