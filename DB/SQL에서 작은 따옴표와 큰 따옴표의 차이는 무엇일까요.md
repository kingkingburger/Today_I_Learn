## **SQL에서 작은 따옴표와 큰 따옴표의 차이는 무엇일까요?**

환경은 mssql입니다.

```
SELECT * from TB_HR_DEPT_CODE thdc where dept_id = '000000';
SELECT * from TB_HR_DEPT_CODE thdc where dept_id = "000000";
```

위의 sql문은 서치가 되었지만 아래 sql문은

```
SQL Error [207] [S0001]: Invalid column name '000000'.
```

에러가 납니다.

차이점을 알아보겠습니다.

- 작은 따옴표는 문자열 상수 또는 날짜 / 시간 상수를 구분합니다.
- 큰 따옴표는 테이블 이름 또는 열 이름과 같은 식별자를 구분합니다.

즉, 작은 따옴표로는 문자열을 판단하고 큰 따옴표는 테이블과 열 이름 같은 문자열을 구별합니다.