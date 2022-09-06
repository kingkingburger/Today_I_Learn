

## Mssql에서 한글이 깨질 때 

```sql
select * from sys.databases where name = ‘DB명’;

alter database DB명 set single_user with rollback immediate;

alter database DB명 collate Korean_Wansung_CI_AS;

alter database DB명 set multi_user;
```

#### 참고

https://hyzoon.com/archives/2169

#### Collatino 이란?

collation은 데이터 정렬, 비교하는 방식을 지정하는 명령어로

collation 설정에 따라 작업 결과가 다르게 나타날 수 있습니다.

```
SELECT name, collation_name FROM sys.databases;  
```

위 쿼리문을 실행하면 아래와 같은

결과를 확인할 수 있습니다.

|      | name   | collation_name       |
| ---- | ------ | -------------------- |
| 1    | master | Korean_Wansung_CI_AS |
| 2    | sample | Korean_Wansung_CI_AS |

master와 sample은 **데이터베이스의 이름** 그리고

collation_name은 해당 **데이터베이스가 사용하고 있는 collation 설정값**입니다.

**'Korean_Wansung_CI_AS'**라는 값은 '**한국어 사전 정렬 규칙**'을

사용해 데이터를 비교, 정렬한다는 의미입니다.

