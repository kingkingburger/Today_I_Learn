# Spring에서 Args 어노테이션 알아보기

생성자 매개변수에 관한 `@RequiredArgsConstructor` , `@AllArgsContructor` , `@NoArgsContructor` 에대해 알아보려고합니다.

어노테이션은 컴파일 타임에 java 코드로 변환이 되는데요. 좀더 명확하게 기억하고 사용하고자 예시코드와 함께 알아보겠습니다.



#### 1. **@RequiredArgsConstructor**

이 어노테이션은 '**필요한 최소한의 생성자**'를 자동으로 생성해줍니다. 클래스 내에 `final` 키워드가 붙거나 `@NonNull` 어노테이션이 붙은 필드에 대해 생성자를 만들어줍니다. 이를 통해 불변성을 보장하는 필드를 안전하게 초기화할 수 있습니다.

**예시 코드**:

```java
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class Coffee {
    private final String name; // final 필드에 대한 생성자를 생성
    private final int price;
}
```

위 코드에서 `@RequiredArgsConstructor`는 다음과 같은 생성자를 자동으로 생성해줍니다:

```java
public Coffee(String name, int price) {
    this.name = name;
    this.price = price;
}
```





#### **2. @AllArgsConstructor**

`@AllArgsConstructor` 어노테이션은 클래스의 **모든 필드를 매개변수로 받는 생성자**를 만들어줍니다. 이 어노테이션을 사용하면 클래스의 모든 필드를 한 번에 초기화할 수 있는 생성자가 자동으로 생성됩니다.

**예시 코드**:

```java
import lombok.AllArgsConstructor;

@AllArgsConstructor
public class Book {
    private String title;
    private String author;
    private int pages;
}
```

`@AllArgsConstructor`는 다음과 같은 생성자를 자동으로 생성해줍니다:

```java
public Book(String title, String author, int pages) {
    this.title = title;
    this.author = author;
    this.pages = pages;
}
```





### **3. @NoArgsConstructor**

`@NoArgsConstructor`는 매개변수가 없는 기본 생성자를 생성합니다. 이 어노테이션은 주로 JPA에서 엔티티의 기본 생성자를 만들 때 사용됩니다. 기본 생성자는 클래스의 모든 필드를 기본값(숫자는 0, 객체 참조는 null 등)으로 초기화합니다.

**예시 코드**:

```java
import lombok.NoArgsConstructor;

@NoArgsConstructor
public class Member {
    private String name;
    private int age;
}
```

`@NoArgsConstructor`는 다음과 같은 기본 생성자를 생성해줍니다:

```java
public Member() {
    // 모든 필드를 기본값으로 초기화
}
```

이처럼 `Args` 시리즈 어노테이션들은 생성자를 명시적으로 작성하는 수고를 덜어주고, 코드를 더 깔끔하고 명확하게 만들어줍니다. 



`@Args` 어노테이션들은 생성자를 자동으로 만들어준다! 가 요약입니다. 또한 같이 쓸 수 있습니다.

`@NoArgsConstructor` 와 `@RequiredArgsConstructor` 를 같이쓴다면 



```java
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@NoArgsConstructor
public class Coffee {
    private final String name; // final 필드에 대한 생성자를 생성
    private final int price;
}
```

2개의 어노테이션이 같이 생성자를 만듭니다.

```java
public Coffee(){
    
}

public Coffee(String name, int price) {
    this.name = name;
    this.price = price;
}
```

위 생성자를 **오버로딩**이 됩니다.

