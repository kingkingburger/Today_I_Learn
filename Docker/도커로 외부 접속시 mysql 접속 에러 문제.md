## 도커로 외부 접속시 mysql 접속 에러 문제

계정의 비밀번호 오류 및 네크워크 허용 설정 때문입니다.

접근 host 별로 비밀번호가 다르게 설정되어 있을 수 있습니다!

Mysql은 같은 이름의 계정이라도, 접속지에 다라 다른 패스워드를 줄 수 있습니다.



host 별 패스워드가 동일한지 확인하기 위해서는 mysql.user 테이블을 조회하면 된다. 

아래 쿼리로 host, user 별로 동일하게 패스워드가 설정되어있는지 확인할 수 있다.





```null
mysql> grant all privileges on test.* to 'admin'@'%';
mysql> flush privileges;
mysql> show grants for 'admin'@'%';
```

`test`라는 데이터베이스에 대한 모든 권한을 `admin` 계정에게 준 것이다.
그리고 `flush privileges`는 `grant`라는 테이블을 즉시 리로드해서 변경 사항을 즉시 반영하게 하는 명령어이다.
이로써 `admin`은 `test`에 대한 모든 권한을 가지게 되었다.