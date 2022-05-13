## @Transactional 의 계념

테스트 케이스에 이 애노테이션이 있으면, **테스트 시작 전**에 `트랜잭션을 시작`하고, **테스트 완료 후**에 항상`롤백`한다. 이렇게 하면 DB에 데이터가 남지 않으므로 다음 테스트에 영향을 주지 않는다.

db는 query가 오면 commit을 해야 적용이 됩니다. 이것을 auto로 하냐 안하냐의 차이가 있을 뿐입니다. 만약 commit을 하지 않으면 적용이 되지 않겠지요?

예를들어 회원가입 테스트를 할 때 DB에 값이 적용이 된다면 이전에 있던 값이 DB에 남아있게 됩니다.  `@Transactional`을 붙혀주면 db query를 다시 rollback합니다. 그러면 다음 테스트에 반영이 안됩니다.



## @Transactional 은 어디에 사용되는가? (22.05.13)

**@Transactional** 이라는 어노테이션이 어떤 역할을 하는지 궁금해서 글을 써봅니다.



일단 **트랜잭션**에 대해 알아봐야 합니다.



#### **트랜잭션(Transaction)이란?**

트랜잭션(Transaction)의 정의를 내려보자면, 트랜잭션은 Database의 상태를 변환시키는 하나의 논리적 기능을 수행하기 위한 작업 단위나 한번에 수행되어야할 일련의 연산을 의미한다.



**@Transactional**은 **트랜잭션**을 처리하는 어노테이션 입니다.

스프링 환경에서는 @Transactional을 이용하여 메서드, 클래스, 인터페이스의 트랜잭션 처리가 가능합니다. 이러한 방식을 **선언적 트랜잭션**이라고 부릅니다.

**프록시 객체**가 생성되어 자동적으로 커밋이나 롤백을 해준다고 생각해봅시다.



#### **Spring @Transactonal 기능제공 방식**

JPA 의 객체 변경감지는 transacton 이 commit 될 때, 작동합니다.

그렇기에 Spring 은 @Transactonal 어노테이션을 선언한 메서드가 **실행되기전,** **transaction begin** **코드를 삽입**하며

메서드가 **실행된 후,** **transaction commit** **코드를 삽입**하여, 객체 변경감지를 수행하게 유도합니다.



```
public class BooksProxy {
  private final Books books;
  private final TransactonManager manager = TransactionManager.getInstance();
  
  public BooksProxy(Books books) {
    this.books = books;
  }
  
  public void addBook(String bookName) {
    try {
      manager.begin();
      books.addBook(bookName);
      manager.commit();
    } catch (Exception e) {
      manager.rollback();
    }
  }
}
```





jpa의 save같은 메소드 안에는 @Transactional이 기본적으로 달려있습니다.

**begin, commit, rollback 같은 트랜잭션의 처리**를 별도의 모듈로 만드는 **AOP**(Aspect Oriented Programming, 관점 지향 프로그래밍)을 고안 및 적용하게 되고 **어노테이션(@Transaction)이 탄생**한것 입니다.



간단한 예시로 MemberService에서 MemberDTO 클래스를 insert를 하는 Service 내부의 메서드를 만든다고 가정해보면 아래처럼 구현을 할 수가 있습니다.

```
@Service 
public class MemberService { 
	@Transactional
	public void addMember(MemberDto memberDto) throws Exception { 
    	// 멤버 삽입 로직 구현 
  	  } 
}
```



#### @Transactional의 주요한 옵션 2가지

- isolation
- propagation

공부를 하다보니 2개의 옵션에 대한 글들이 정말 많았습니다. 이 주로 2개로 트랜잭션의 흐름을 결정하는거 같습니다.



#### Isolation

먼저 **isloation(격리수준)**은 트랜잭션이 **실행하고 있는 동안에 데이터의 lock을 어떤식**으로 잠글지 정하는 옵션같습니다.



Level 0 ~ Level 3까지 있습니다.

1️⃣ **Level 0(Read_UNCOMMITED)** -> 커밋되지 않는 데이터를 다른사용자가 읽을 수 있다!

2️⃣ **Level 1(Read_COMMITED)** -> 커밋되지 된 데이터만 읽을 수 있다! -> A사용자가 데이터를 변경하는 동안에는 접근불가

3️⃣ **Level 2(Repeatable_Read)** -> 트랜잭션이 완료될 때 까지 select 문장에 사용되는 모든 데이터들에 대해 Shared Lock을 걸어 그 데이터에 접근 불가능하게 만듭니다.

4️⃣ **Level 3(Serializable)** -> 데이터의 일관성과 동시성을 유지하는것을 목표로 합니다. 트랜잭션이 완료될 때 까지 select 문장에 사용되는 모든 데이터들에 대해 Shared Lock을 걸어 그 데이터에 접근 불가능하게 만듭니다.



#### Propagation

propagation(전파)는 **트랜잭션이 동작할 때 다른 트랜잭션이 호출되면 어떻게 처리할지**를 정하는 옵션입니다.

**7개**의 옵션이 있습니다.



**1️⃣ Required**

**이미 진행중인 트랜잭션**이 있다면 해당 트랜잭션 속성을 따르고, 진행중이 아니라면 새로운 트랜잭션을 생성합니다.



**2️⃣ Requires_new** 

**항상 새로운 트랜잭션을 생성**한다. 이미 진행중인 트랜잭션이 있다면 **잠깐 보류**하고 해당 트랜잭션 작업을 먼저 진행한다



**3️⃣ Support**

**이미 진행 중인 트랜잭션이 있다면 해당 트랜잭션 속성을 따르고**, 없다면 트랜잭션을 설정하지 않는다.



**4️⃣ Not_support**

이미 진행중인 트랜잭션이 있다면 **보류하고, 트랜잭션 없이 작업을 수행**한다.



**5️⃣ Mandatory**

**이미 진행중인 트랜잭션이 있어야만, 작업을 수행**한다. 없다면 Exception을 발생시킨다.



**6️⃣ Never**

**트랜잭션이 진행중이지 않을 때 작업을 수행**한다. 트랜잭션이 있다면 Exception을 발생시킨다.



**7️⃣ Nested**

진행중인 트랜잭션이 있다면 **중첩된 트랜잭션이 실행**되며, 존재하지 않으면 REQUIRED와 동일하게 실행된다.





#### 참고

https://mommoo.tistory.com/92

https://devkingdom.tistory.com/287

propagation의 옵션을 참조한 글입니다: [ https://bamdule.tistory.com/51](https://bamdule.tistory.com/51)

https://mangkyu.tistory.com/154

트랜잭션의 흐름을 참고한 블로그입니다 : https://wookim789.tistory.com/60
