## JPA에서 findBy 메소드 생성해보기

기본적인 jpa 판은 아래와 같습니다.

```
public interface MemberRepository extends JpaRepository<Member_table, Long>{

}
```

여기에 **jpa가 기본**으로 놔둔 save, findAll, count... 등등을 쓸 수 있습니다. 하지만 내가 id로  table을 찾아보고싶다고 하면 findById를 생성하면 됩니다. 

```
public interface MemberRepository extends JpaRepository<Member_table, Long>{
    MemberResponseDto findByEmailAndPasswd(final String email, final String passwd);
}
```

만약 Email, Passwd 컬럼2개로 db를 찾아보고 싶다하면 **findByEmailAndPasswd**를 사용하면 됩니다. 주의할 점은 메서드 이름입니다. 

위 예시로는 Email and Passwd를 where-and 쿼리로 만들어버립니다. 만약 다른 명칭으로 매서드를 만든다면 jpa가 쿼리를 생성할 수 없습니다. 

And뿐만 아니라 Or, Between 등 다양한 매서드로 where문을 만들 수 있습니다.



[참고:](https://devfunny.tistory.com/426)