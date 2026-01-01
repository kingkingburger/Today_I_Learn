## 스프링 데이터 JPA에서 fetch join이 들어간 경우 Count 쿼리를 정상적으로 만들어내지 못한다!

스프링 데이터 JPA에서 fetch join이 들어간 경우 Count 쿼리를 정상적으로 만들어내지 못합니다.

@EntityGraph를 사용하는 경우에는 Count 쿼리를 정상적으로 만들어낼 수 있습니다.

따라서 이 경우 countQuery 부분을 별도로 분리해주시면 됩니다.

조인 대상을 필터링하는 경우에도 countQuery를 똑같이 사용해주시면 됩니다.



#### 참고

https://stackoverflow.com/questions/21549480/spring-data-fetch-join-with-paging-is-not-working

https://www.inflearn.com/questions/39776

https://velog.io/@jayjay28/JPA%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%8B%A8%EC%88%9C-%EA%B2%8C%EC%8B%9C%EB%AC%BC-%EC%B2%98%EB%A6%AC