## 에플리케이션에서 db에 연결하기

java와 db에 연결하려면 `jdbc`드라이버가 꼭 필요합니다. 





## 환경설정을 할 때 

`build.gradle`에서 새로운 라이브러리를 추가하면 intelliJ의 오른쪽에 있는 gradle을 열어서 Refash를 해주어야 합니다. 그래야 새로운 라이브러리가 들어왔는지 압니다.

Spring JDBC를 사용하려면 먼저, DB Connection을 가져오는 DataSource를 Spring IoC 컨테이너의 공유 가능한 Bean으로 등록해야 한다.







## Spring으로 DB에 연결하기

#### DB Connection Pooling이란?

자바 프로그램에서 데이터베이스에 연결(**Connection 객체를 얻는 작업**)은 시간이 많이 걸린다.
만약, 일정량의 Connection을 미리 생성시켜 **저장소**에 저장했다가 프로그램에서 요청이 있으면 저장소에서 Connection 꺼내 제공한다면 시간을 절약할 수 있다. 이러한 프로그래밍 기법을 **Connection Pooling**이라 한다.





#### 커넥션 풀링이란?

미리 정해진 갯수만큼의 DB 커넥션을 풀에 준비해두고, 어플리케이션이 요청할 때마다 Pool에서 꺼내서 하나씩 할당해주고 다시 돌려받아서 Pool에 넣는 식의 기법.

db에 접근하려면 DataSource가 필요합니다.





####  **DataSource란?**

- **connectionPool**은 경우에 따라 여러개가 생성될 수 있으며, DataSource는 connectionPool을 관리하는 목적으로 사용되는 **객체**이다.
- DataSource를 이용해 **커넥션을 얻어오고 반납하는 등의 작업을 수행**한다.
- DataSource로 부터 얻은 connection의 **close 메서드**는 커넥션을 반납하는 작업을 수행한다.





```java
spring.datasource.url = jdbc:h2:tcp://localhost/~/test
spring.datasource.driver-class-name=org.h2.Driver
```

spring에 driver를 설치해두고 연결을 해두면 DataSource가 Connection을 관리하게 됩니다. 그 DataSource에서 진자로 연결되게 하는 Connection을 가지고 오면 됩니다.





## Spring에서 Connection가져올 때 팁

```java
private Connection getConnection() {
        return DataSourceUtils.getConnection(dataSource);
}
```

DataConnection의 똑같은 것을 유지하면서 db를 사용하려면 DatasourceUtils를 사용합니다.