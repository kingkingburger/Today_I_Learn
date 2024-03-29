# Database Lock 종류 및 기능

DataBase는 데이터를 영속적으로 저장하고 있는 시스템입니다. 이런 시스템은 같은 자원(데이터)에 대해서 동시에 접근하는 경우가 생길 수 밖에 없습니다. 이럴 경우 데이터가 오염 될 수 있는데 그렇게 되지 않도록 데이터의 일관성과 무결성을 유지해야할 필요가 있습니다. 예를 들어 영화예매 시스템에서 1명만이 정원으로 남게되었습니다. 여기서 2사람이 거의 동시에 버튼을 눌렀습니다. 성공은 1명만 되야합니다. 이런 상황에서 DBMS(DataBase Management System)가 사용하는 공통적인 방법이 **Lock**이라는 것입니다.

Lock을 사용함으로써 여러 유저가 동시에 접근하더라도 1명씩 요청을 처리하게 됩니다. 

Lock은 하나의 트랜잭션이 완벽하게 끝날 때까지 다른 요청을 막아줍니다. 마치 하나의 화장실에 들어갔을 때 문앞을 막아주는 보디가드 처럼요.

## Lock

**Lock이란 트랜잭션 처리의 순차성을 보장하기 위한 방법**입니다. 트랜잭션이란 DB의 나누어지지 않는 최소한의 처리 단위입니다. 

그리고 중요한 것은 DBMS마다 Lock을 구현하는 방식과 세부적인 방법이 다릅니다. 따라서 DBMS를 효과적으로 이용하기 위해서는 해당 DB의 Lock에 대한 이해가 요구됩니다.

## Lock의 종류

**Lock의 종류로는 공유(Shared) Lock과 베타(Exclusive) Lock이 있습니다. 공유락은 다른 말로 Read Lock이라고 불리며 베타락은 Write Lock이라고도 불립니다.**

### 공유(Shared) Lock

**공유 Lock은 데이터를 읽을 때 사용되어지는 Lock**입니다. 이런 **공유 Lock은 공유 Lock 끼리는 동시에 접근이 가능**합니다. 즉, 하나의 데이터를 읽는 것은 여러 사용자가 동시에 할 수 있다라는 것입니다. 하지만 공유 Lock이 설정된 데이터에 베타 Lock을 사용할 수는 없습니다.

### 베타(Exclusive) Lock

**베타 Lock은 데이터를 변경하고자 할 때 사용**되며, 트랜잭션이 완료될 때까지 유지됩니다. **베타락은 Lock이 해제될 때까지 다른 트랜잭션(읽기 포함)은 해당 리소스에 접근할 수 없습니다.** 또한 해당 Lock은 다른 트랜잭션이 수행되고 있는 데이터에 대해서는 접근하여 함께 Lock을 설정할 수 없습니다.



db에서 데이터를 읽는것은 관대하고 변경하는건 굉장히 까탈스럽습니다. 깐깐한 주인장 옷가게에 들어가는것과 비슷해 보입니다.

트랜잭션이 실행되면서 동시에 자원을 가져가려는 상황이 있습니다. **블로킹**과 **교착상태** 입니다.





## 블로킹(Blocking)

**블로킹은 Lock간(베타 - 베타, 베타 - 공유)의 경합이 발생하여 특정 Transaction이 작업을 진행하지 못하고 멈춰선 상태**를 말합니다. 위에 설명했듯이 **공유락** 끼리는 블로킹이 발생하지 않지만 **베타락**은 블로킹을 발생시킵니다. 블로킹을 해소하기 위해서는 **이전의 트랜잭션이 완료(커밋 OR 롤백)**되어야 합니다. 뒤에 들어온 트랜잭션은 이전 트랜잭션이 마무리되어야 이후 진행이 가능합니다. 이런 경합은 성능에 좋지 않은 영향을 미칩니다. 따라서 경합을 최소화 할 필요가 있습니다.



![img](https://blog.kakaocdn.net/dn/Hkc78/btqL3wfemow/apZ9CtndatkDz9ATfpLYoK/img.png)



DB를 사용하는 프로그래밍을 진행하면서 몇가지 주의사항을 알아보도록 하겠습니다.

1. 한 트랜잭션의 길이를 너무 길게하는 것은 트랜잭션끼리 경합의 확률을 올립니다.
2. 처음부터 설계할 때 같은 데이터를 갱신하는 트랜잭션이 동시에 수행되지 않도록 해야합니다.
3. 트랜잭션 격리성 수준을 불필요하게 상향 조정하지 않습니다. (참고 : [트랜잭션 격리성 수준](https://sabarada.tistory.com/117))
4. 쿼리를 오랜시간 잡아두지 않도록 적절한 튜닝을 진행합니다.

이외에 DBMS에 따라서 lock 대기 시간 등을 설정할 수 있습니다.



## 교착상태(DeadLock)

**교착상태는 두 트랜잭션이 각각 Lock을 설정하고 다음 서로의 Lock에 접근하여 값을 얻어오려고 할 때 이미 각각의 트랜잭션에 의해 Lock이 설정되어 있기 때문에 양쪽 트랜잭션 모두 영원히 처리가 되지않게 되는 상태**를 말합니다. 예를 들어 보면, game_master, game_detail 테이블이 있습니다. 트랜잭션 A가 game_master 테이블에 5번 Row를 수정했고 이제 game_detail 테이블에 5번 Row를 이어서 수정하려고 합니다. 동시에 트랜잭션 B는 game_detail 테이블의 5번 Row를 수정하고 이어서 game_master 테이블의 5번 Row를 수정하려고 합니다. 이 경우 트랜잭션 A는 game_master 테이블의 5번 Row에 배타 락을 설정했고 트랜잭션 B는 game_detail 테이블의 5번 Row에 배타 락을 설정하였습니다. 그리고 교차로 트랜잭션 A는 game_detail의 5번 row의 Lock 설정을 하려고 하고 트랜잭션 B는 game_master의 5번 row에 Lock 설정을 하려고 합니다. 하지만 이미 각 row들은 서로다른 트랜잭션에 의해서 배타락 설정이 되어있습니다. 따라서 Lock이 해제되기를 서로 기다립니다. 하지만 이 Lock은 풀리지 않을 서로의 트랜잭션 기다리므로 영원히 풀리지 않을것입니다.

이미지로 나타내면 아래와 같습니다.



![img](https://blog.kakaocdn.net/dn/IAs6r/btqL39jMHtW/mzTqIspCi0K0n01KTKz0h0/img.png)



**그래서 교착상태가 발생하면 DBMS가 둘 중 한 트랜잭션에 에러를 발생시킴으로써 문제를 해결합니다. 교착상태가 발생할 가능성을 줄이기 위해서는 접근 순서를 동일하게 하는것이 중요**합니다. 즉, 위의 예제라면 프로그래밍을 할 때 game_master를 업데이트 한 후 game_detail을 업데이트 한다와 같은 규칙을 정해 테이블 접근의 교차가 일어나지 않도록 하는것이 중요할 것입니다.





#### 출처

- https://sabarada.tistory.com/121
- https://medium.com/29cm/db-postgresql-lock-%ED%8C%8C%ED%97%A4%EC%B9%98%EA%B8%B0-57d37ebe057
  -  postgresql에서 lock에 대해서 롤토체스 예시로 쉽게 알려준 고마운사이트
