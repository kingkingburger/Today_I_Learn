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
