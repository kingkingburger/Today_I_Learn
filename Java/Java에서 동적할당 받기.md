## Java에서 동적할당 받기(Java Collection 사용)

코딩테스트를 하다 배열의 길이를 자유자재로 할당을 받고 싶어졌습니다.

고정적으로 설정을하니 남은 문자에 0,빈칸 들이 채워게 됩니다. python 처럼 list 형태로 정해진 크기 없이 받아 보는것을 배워봤습니다.



#### Java Collection 사용하기

파이썬의 List 형태처럼 Java에서는 ArrayList가 있습니다. 이는 Collections 클래스에 정의되어 있습니다. (Collections랑 다릅니다.)

![99B88F3E5AC70FB419](https://user-images.githubusercontent.com/65094518/165911627-55c10a48-257d-4731-9ebe-66e7cd798dbf.png)

[공식문서](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)

List는 인터페이스이고(구현체로 구현해야함) ArrayList는 구현체 입니다. 

```java
List<XClass> myclass = new ArrayList<XClass>();
myclass.add(new XClass());
myclass.add(new XClass());
```

ArrayList 안에는 템플릿 형태로 다양한 클래스들이 들어갈 수 있습니다.(ex, String, Integer, 등등)



####  **Collection 인터페이스의 특징**

| 인터페이스 | 구현클래스                | 특징                                                         |
| ---------- | ------------------------- | ------------------------------------------------------------ |
| Set        | HashSetTreeSet            | 순서를 유지하지 않는 데이터의 집합으로 데이터의 중복을 허용하지 않는다. |
| List       | LinkedListVectorArrayList | 순서가 있는 데이터의 집합으로 데이터의 중복을 허용한다.      |
| Queue      | LinkedListPriorityQueue   | List와 유사                                                  |
| Map        | HashtableHashMapTreeMap   | 키(Key), 값(Value)의 쌍으로 이루어진 데이터으 집합으로,순서는 유지되지 않으며 키(Key)의 중복을 허용하지 않으나 값(Value)의 중복은 허용한다. |



**1. Set 인터페이스**

순서를 유지하지 않는 데이터의 집합으로 데이터의 중복을 허용하지 않는다.



- **HashSet**
  \- 가장빠른 임의 접근 속도
  \- 순서를 예측할 수 없음

  

- **TreeSet**
  \- 정렬방법을 지정할 수 있음



**2. List 인터페이스**

순서가 있는 데이터의 집합으로 데이터의 중복을 허용한다.



- **LinkedList**
  \- 양방향 포인터 구조로 데이터의 삽입, 삭제가 빈번할 경우 데이터의 위치정보만 수정하면 되기에 유용
  \- 스택, 큐, 양방향 큐 등을 만들기 위한 용도로 쓰임

  

- **Vector**
  \- 과거에 대용량 처리를 위해 사용했으며, 내부에서 자동으로 동기화처리가 일어나 비교적 성능이 좋지 않고 무거워 잘 쓰이지 않음

  

- **ArrayList**
  \- 단방향 포인터 구조로 각 데이터에 대한 인덱스를 가지고 있어 조회 기능에 성능이 뛰어남

  

**3. Map 인터페이스**

키(Key), 값(Value)의 쌍으로 이루어진 데이터으 집합으로,

순서는 유지되지 않으며 키(Key)의 중복을 허용하지 않으나 값(Value)의 중복은 허용한다.



- **Hashtable**
  \- HashMap보다는 느리지만 동기화 지원
  \- null불가

  

- **HashMap**
  \- 중복과 순서가 허용되지 않으며 null값이 올 수 있다.

  

- **TreeMap**
  \- 정렬된 순서대로 키(Key)와 값(Value)을 저장하여 검색이 빠름

