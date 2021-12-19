## JPA(Java Persistence API) 기초

- JPA는 기존의 반복 코드는 물론이고, 기본적인 SQL도 JPA가 직접 만들어서 실행해준다.
- JPA를 사용하면, SQL과 데이터 중심의 설계에서 객체 중심의 설계로 패러다임을 전환을 할 수 있다.
- JPA를 사용하면 개발 생산성을 크게 높일 수 있다.

**jpa**는 `인터페이스`이고 `구현체`로는 **hibernate**를 사용합니다.





## JPA에서 ORM하는 방법은?

`@Entity`를 붙혀줍니다. 이걸 붙히면 이제부터 JPA에서 관리하는 객체다! 라고 선언하는 것 입니다.

다음 `PK(Primary key, 기본키)`를 설정해야 합니다.`@Id`로 설정해줍시다.

DB에 값을 넣으면 DB가 자동으로 값을 생성해 주는 것을 `Identity 전략` 이라고 합니다.

```java
@Id
@GeneratedValue(strategy= GenerationType.IDENTITY)
private Long id;

@Column(name="username")
private String name;
```

db에 `Column`명이 username이라고 하면 `name=username`이라고 적어줍니다. 그러면 username 컬럼과 연결이 됩니다.





## EntityManager

jpa는 EntityManager로 뭐든것이 동작합니다. 처음에 라이브러리를 받아오면 springboot가 알아서 db정보를 가지고 EntityManager를 생성합니다. 내부적으로 DataSource도 들고 있어서 db와 통신까지 가능합니다.





## 객체를 조회하기

```java
public List<Member> findAll() {
	//(sql, 조회타입)
	return em.createQuery("select m from Member as m", Member.class)
			.getResultList();
}

public Optional<Member> findByName(String name) {
    List<Member> result = em.createQuery("select m from Member as m where m.name = :name", Member.class)
        .setParameter("name", name)
        .getResultList();

    return result.stream().findAny();
}
```

jpql이라는 쿼리 언어입니다. **객체**를 대상으로 쿼리를 날리는 것입니다. Member객체 자체를 select합니다

jpa를 쓰러면 항상 트랜젝션이 있어야 합니다. 모든 변경이 트랜젝션 안에서 실행되어야 합니다.







## 스프링 데이터 JPA

> 스프링 부트와 JPA만 사용해도 개발 생산성이 정말 많이 증가하고, 개발해야할 코드도 확연히 줄어듭니다. 여기에 스프링 데이터 JPA를 사용하면, 기존의 한계를 넘어 마치 마법처럼, 리포지토리에 구현 클래스 없이 인터페이스 만으로 개발을 완료할 수 있습니다. 그리고 반복 개발해온 기본 CRUD 기능도 스프링 데이터 JPA가 모두 제공합니다. 스프링 부트와 JPA라는 기반 위에, 스프링 데이터 JPA라는 환상적인 프레임워크를 더하면 개발이 정말 즐거워집니다. 지금까지 조금이라도 단순하고 반복이라 생각했던 개발 코드들이 확연하게 줄어듭니다. 따라서 개발자는 핵심 비즈니스 로직을 개발하는데, 집중할 수 있습니다. 실무에서 관계형 데이터베이스를 사용한다면 스프링 데이터 JPA는 이제 선택이 아니라 필수 입니다.



```java
//인터페이스가 인터페이스를 상속받으려면 extends를 써야합니다.          T는 member, Id는 식별자,pk
public interface SpringDataJpaMemberRepository extends JpaRepository<Member, Long>, MemberRepository{

    @Override
    Optional<Member> findByName(String name);
}
```

인터페이스로 만들었지만 spring이 자동으로 구현체를 만들어 줍니다.



#### springconfig

```java
private final MemberRepository memberRepository;

@Autowired
public SpringConfig(MemberRepository memberRepository) {
    this.memberRepository = memberRepository;
}

@Bean
public MemberService memberService(){
    return new MemberService(memberRepository());
}
```

인터페이스만 만들었는데 스프링 컨테이너에서 `MemberRepository`를 찾습니다. 그런데 컨테이너 안에 레포지토리가 없습니다 그러면 `memberRepository`에 어떻게 구현이 될까요?  `스프링 데이터 JPA`는 인터페이스를 가지고 알아서 구현채를 만듭니다. 그리고 스프링 빈에 등록합니다.

**스프링 데이터 JPA가 SpringDataJpaMemberRepository 를 스프링 빈으로 자동 등록해준다.**





```
Could not autowire. There is more than one bean of 'MemberRepository' type.
Beans: memoryMemberRepository   (MemoryMemberRepository.java) springDataJpaMemberRepository   (SpringDataJpaMemberRepository.java) 
```

 이라는 오류가 떳습니다. 스프링에 등록되어있는 MemberRepository가 2개 이상일 때 @Autowired를 하면 충돌이 나는거 같습니다.

MemoryMemberRepository에서 `@Repository`로 자동 빈 등록(컴포넌트 스캔의 대상)되었습니다. MemberRepository를 구현하고 있는 구현채가 2개이기 때문에 오류가 발생했습니다.

```java
@Primary
//인터페이스가 인터페이스를 상속받으려면 extends를 써야합니다.          T는 member, Id는 식별자,pk
public interface SpringDataJpaMemberRepository extends JpaRepository<Member, Long>, MemberRepository {
    Optional<Member> findByName(String name);
}
```

`@Qualifire`를 하는데도 2개가 중복되었다고 나와서 `@Primary`를 사용했습니다. @Primary가 붙은 Bean은 최우선적으로 의존주입이 됩니다.



![image](https://user-images.githubusercontent.com/65094518/146664521-91d51f5d-3dad-4317-84bd-24e9fce77490.png)

우리가 생각하는 CRUD가 기본적으로 만들어져 있습니다. ex) findAll, save, deleteAll 등등....

그런데 우리가 Name으로 찾고 싶은데 내 프로젝트 name이지만 다른 곳에서는 user_name이렇게도 쓸 수 있습니다. 그래서 개별화 해야 합니다.

findByName()을 하면 JPQL에서 쿼리를 `select m from member as m where name =? `을 자동으로 짜줍니다.

