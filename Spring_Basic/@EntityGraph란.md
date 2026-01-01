## @EntityGraph란?

연관관계가 있는 엔티티를 조회할 경우 지연 로딩으로 설정되어 있으면 연관관계에서 종속된 엔티티는 쿼리 실행 시 select 되지 않고 **proxy 객체**를 만들어 엔티티가 적용시킵니다.

그 후 해당 **proxy 객체**를 호출할 때마다 그때 그때 **select 쿼리가 실행**됩니다.

위 같은 연관관계가 지연 로딩으로 되어있을 경우 fetch 조인을 사용하여 여러 번의 쿼리를 한 번에 해결할 수 있습니다.

**@EntityGraph는** Data JPA에서 fect 조인을 어노테이션으로 사용할 수 있도록 만들어 준 기능입니다.

 

#### Entity(Member)

```java
@Entity
@Getter @Setter
@NoArgsConstructor(access = AccessLevel.PROTECTED) // 기본생성자를 만들어 주는 기능
public class Member extends BaseEntity{

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "member_id")
    private Long Id;
    private String username;
    private int age;

    @ManyToOne(fetch = LAZY)
    @JoinColumn(name = "team1_id")
    private Team team;


    public Member( String username) {
        this.username = username;
    }

}
```

 Member 객체가 Team을 ManyToOne으로 연관관계가 되어 있습니다.

#### Entity(Team)

```java
@Entity
@Getter
@Setter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Team {

    @Id
    @GeneratedValue
    @Column(name = "team_id")
    private Long id;
    private String name;

    @OneToMany(mappedBy = "team",cascade = ALL,orphanRemoval = true)
    private List<Member> members = new ArrayList<>();

    public Team(String name) {
        this.name = name;
    }
}
```

 Team객체는 member에게 종속되어 있습니다. 

 

 

#### Test Class

```java
   @Test
    public void basicCRUD() {
        Member member1 = new Member("member1");
        Member member2 = new Member("member2");
        memberRepository.save(member1);
        memberRepository.save(member2);


        List<Member> all = memberRepository.findAll();
        assertThat(all.size()).isEqualTo(2);

    }
```

 

실행 시 쿼리를 확인해 보면 

![img](https://blog.kakaocdn.net/dn/bQ7Qba/btq7iOSDYhv/mC8HnwryBbcRWnDv0BvZTk/img.png)

위처럼 지연로딩 의 경우 member 객체만 조회하고 team 객체는 프락시 객체가 대체되어 들어갑니다. 

 select쿼리가 한 번만 이루어집니다. 이는 `Member` 객체 내에서 `Team` 객체에 접근하기 전까지는 `Team`에 대한 쿼리를 수행하지 않기 때문이고 `FetchType.LAZY`가 하는 일이기도 합니다.



####  Repository

```java
    public interface MemberRepository extends JpaRepository<Member,Long> ,MemberRepositoryCustom{
    
      @Override //기본 적으로 findAll 을 제공하기 때문에 Override 하여 재정의 후 사용 
      @EntityGraph(attributePaths = {"team"}) // DataJpa 에서 fetch 조인을 하기 위한 설정
      List<Member> findAll();

    }
```

Repository에서 findAll코드를 재정의 한 다음 실행시켜 보면

 



![img](https://blog.kakaocdn.net/dn/cgEfWT/btq7fcNKCGX/21DljSIPNrfbmdk8kGZSmK/img.png)

team 엔티티를 함께 조회하는 것 을 확인할 수 있습니다.

```java
@Query("select m from Member m")
@EntityGraph(attributePaths = {"team"})
List<Member> findAllMembers(); // JPQL을 이용해도 가능

@EntityGraph(attributePaths = {"team"})
Member findByUsername(String username); // 메서드 쿼리를 이용해도 가능
```

jpql을  중첩으로 사용도 동작이 됩니다.



### @NamedEntityGraph

`@Query`와 마찬가지로 `@EntityGraph`도 `@NamedEntityGraph`를 지원합니다.

실제로 사용하는 방법도 동일합니다.

`Entity` 클래스에 `@NamedEntityGraph`를 추가하고 `Repository` 내 메서드에 `@EntityGraph`의 속성으로 앞에서 정의한 이름을 넣어주면 됩니다.

```java
// 생략
@NamedEntityGraph(name = "member.findAll", attributeNodes = @NamedAttributeNode("team"))
public class Member {
    // 생략
}
@Query("select m from Member m")
@EntityGraph("member.findAll")
List<Member> findAllMembers();
```

개인적인 생각은 기본 메서드를 Override 하는 경우가 아니면 `@EntityGraph`는 사용하지 않을 거 같습니다.

`JPQL`을 사용할 경우 그냥 쿼리 뒤에 `join fetch` 만 붙여주면 되는데 굳이 번거롭게 애너테이션과 그 속성을 추가할 필요가 없기 때문이죠.

`@NamedEntityGraph` 역시 `@NamedQuery`를 잘 쓰지 않을 거 같은 느낌과 동일한 느낌을 받았습니다.





## @EntityGraph의 type

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findById(Long userId);

    @EntityGraph(attributePaths = {"addresses"}, type = EntityGraph.EntityGraphType.LOAD)
    Optional<User> findWithAddressesById(Long userId);
}
```

`@EntityGraph`의 type은 `EntityGraph.EntityGraphType.FETCH`와 `EntityGraph.EntityGraphType.LOAD` 2가지가 있습니다.

- `FETCH`: entity graph에 명시한 attribute는 `EAGER`로 패치하고, 나머지 attribute는 `LAZY`로 패치
- `LOAD`: entity graph에 명시한 attribute는 `EAGER`로 패치하고, 나머지 attribute는 entity에 명시한 fetch type이나 디폴트 FetchType으로 패치 (e.g. `@OneToMany`는 `LAZY`, `@ManyToOne`은 `EAGER` 등이 디폴트입니다.)



## 참고

https://blog.leocat.kr/notes/2019/05/26/spring-data-using-entitygraph-to-customize-fetch-graph

https://itmoon.tistory.com/77

https://jaime-note.tistory.com/54