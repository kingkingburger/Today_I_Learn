## Spring boot로 Id, Name을 가진 도메인과 리포지토리 만들기

정말 간단한 도메인을 만들어 보겠습니다.

회원은 id, name을 가지고있고 `src - main - java`아래 `domain`, `repository` 패키지를 만들어서 그 안에 코드를 입력합니다.







## Member정보

```java
package hello.hellospring.domain;

public class Member {
    private Long id;
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }
}

```

인텔리j에서 `private Long id`, `private String name`을 입력하고 `Alt + insert` 누르면 getter와 setter를 편리하게 만들 수 있습니다.







## MemberRopository 인터페이스

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    Member save(Member member);
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();
}
```

인터페이스에는 리포지토리에 필요한 기능을 넣습니다. 구현은 구현체에서 해야죠

여기서 Optional이라는 타입이 나오는데 이것은 `Java8`에 나온 기능 입니다. 
null을 처리할 때 Optional로 감쌉니다, Optional 객체를 사용하면 예상치 못한 NullPointerException 예외를 제공되는 메소드로 간단히 회피할 수 있습니다.

즉, 복잡한 조건문 없이도 널(null) 값으로 인해 발생하는 예외를 처리할 수 있게 됩니다.

[참고](http://www.tcpschool.com/java/java_stream_optional)







## MemberRepository 구현채

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.*;

public class MemoryMemberRepository implements MemberRepository{


    private static Map<Long, Member> store = new HashMap<>();
    //sequence는 key값을 생성해 주는 애
    private static Long sequence = 0L;

    @Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {

        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values());
    }
}
```

각 기능을 구현한 것을 하나하나 보겠습니다.







#### save(Member)

```
@Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }
```

Member 객체를 구별하기 위해 sequence 변수를  1씩 늘려가며 저장합니다.
store 객체에 <id, (id, name)> 형태로 저장합니다.







#### findById(id)

```
    @Override
    public Optional<Member> findById(Long id) {

        return Optional.ofNullable(store.get(id));
    }
```

Optional 객체는 of()메소드나 ofNullable()메소드를 사용하여 Optional 객체를 생성할 수 있습니다. 

매개변수의 값이 null이 된다면 비어있는 Optional 객체를 반환 합니다. null이 안된다면 그냥 매개변수를 반환합니다.





#### findById(name)

```java
@Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny();
    }
```

**name**을 주면 member객체를 반환해야 합니다.

이건 [람다](http://www.tcpschool.com/java/java_lambda_concept)형식으로 작성했습니다. 

- `values() 메소드`는 해당 Map에 value들만 모아 Collection으로 리턴합니다.
- `stream() 메소드`는 Map안에 있는 값을 모두 출력합니다.

모든 출력값을 filter()를 통해 필터링을 해서 **Map**안에 있는 **member**가  매개변수로 들어온 name과 같다면 해당 store를 반환합니다.

