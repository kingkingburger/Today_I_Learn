## 22/09/13

#### 오늘할 일

- 순회점검 물려서 들어가는 것들 변수명 고치기
- 레거시 db 부서, 유저 순으로 스케쥴러 만들어보기

GSP_USER 테이블

- 고객, 열량계, 기계실이 합쳐저 있는 테이블이다.
- 이걸 가져와서 고객, 열량계, 기계실로 나누어 저장해보자





gsp-htms-server:v.0.2.4-a-mh

https://github.com/uvcdev/gsp-htms-server/pull/46

검토부탁드립니다.

#### 사용자 데이터 연동

- department테이블의 companyCode 칼럼의 이름을 -> ccIdCompany로 변경

  ```
  EXEC htms.sys.sp_rename N'htms.dbo.departments.compnay_code' , N'cc_id_company', 'COLUMN';
  ```

- 레거시DB와 최신DB를 동기화하는 api 2종 추가

  - 레거시부서와 최신DB를 동기화(**GET /legacy/sync_dept**)
  - 레거시유저와 최신DB를 동기화(**POST /legacy/sync_user**)

- department테이블의 upsert를 위해 model의 **dept_code(부서코드)**를 unique로 변경

- getYearStartEndDateTime() 메서드를 해당 년도 기준으로 1년 가져오는 것으로 변경













1. 사번id(emp_id)를 user_id로 사용
   - 기존에 쓰던 id가 없기 때문
   - 기존에 쓰던 password도 없다 => default로 `@gsPower1` 형태로 password 설정함
2. **레거시유저테이블(TB_HR_USER_CODES)**에는 있는 부서번호가 **부서테이블(department)**에 없는 경우에는 continue(다음 레거시유저찾기)를 해놨음
   - ex) N01000은 **레거시부서** 에는 있지만 **레거시유저** 에는 없음 => (해결) null값 너흐면 됨
3. ccIdTask에서 R은 설비이고 C는 고객인가?
   - 현직 구분은 어떻게?? 레거시에서는 Y or N으로 구분했다. 현직구분 코드로는 어떻게 구분을 하는지?





## Upsert를 할 때 주의해야할 점

upsert는 insert + update를 합친 말입니다. 즉, 원래 테이블에 있다면 update를 하고 없다면 insert를 하라는 뜻입니다.

쿼리는 

```sql
INSERT INTO user_refresh_token (user_id, refresh_token)
VALUES (#{userId}, #{refreshToken}) ON DUPLICATE KEY
UPDATE refresh_token = #{refreshToken}
```

이런형태로 나옵니다.

user_refresh_token 테이블에다가 user_id와 refresh_token을 넣을 껀데 

`ON DUPLICATE KEY UPDATE`의 의미는 데이터 삽입시 Primery key나 Unique key가 중복되었을 경우 지정한 데이터만 Update하는 명령어 입니다.

예시를 보겠습니다. 만약 refreshToken이 없다면 value()안에 들어있는 토큰을 넣을 것입니다. 하지만 userId, refreshToken 둘중에 하나가 존재한다면 refreshToken을 새로 업데이트할 것 입니다.



또 하나 예시를 보겠습니다.

**Member 테이블 생성**

```sql
CREATE TABLE member (
	id INT AUTO_INCREMENT primary KEY,
	NAME VARCHAR(50) UNIQUE KEY,
	price INT NOT NULL DEFAULT 0,
	cnt INT NOT NULL DEFAULT 0
);
```

**데이터 삽입**

```sql
INSERT INTO member (NAME, price, cnt) VALUES ('kim', 1000, 0) 
ON DUPLICATE KEY UPDATE 
  price = price * 2, 
  cnt = cnt + 1;
```

![img](https://blog.kakaocdn.net/dn/63swQ/btqF0RvlaDW/EhRWghfiErwlkA6XTKRIKk/img.png)



한번 더 데이터를 삽입 할 경우



![img](https://blog.kakaocdn.net/dn/bEIt2N/btqFZ4Pe4zR/MSBiaVxzBPhQBqj4LKKpAk/img.png)



새로운 행이 삽입 되지 않고, price와 cnt가 변경된 것을 볼 수 있습니다.

즉, 데이터 삽입 시, 중복키 제약조건에 위배 되면 **ON DUPLICATE KEY UPDATE** 아래에 지정한 필드가 수정됩니다.

위 테이블에 경우 **name 값이 중복** 되므로 price와 cnt 필드가 지정한 값으로 수정되었습니다.