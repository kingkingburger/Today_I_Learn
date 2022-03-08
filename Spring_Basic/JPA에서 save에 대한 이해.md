## JPA에서 save에 대한 이해

서비스 계층해서

```java
@Transactional
public Long save(final UserDataRequestDto params){
    Usersdata entity = userdataRepository.save(params.toEntity());
    return entity.getId();
}
```

이런식으로 객체를 저장해봅니다. 요소들을 가지고 insert 하면 되겠죠. ReuquestDto를 보면 

```java
@Getter
@NoArgsConstructor(access = AccessLevel.PACKAGE)
public class UserDataRequestDto {

    private String title; // 제목
    private String username; //작성자
    private String category; //카테고리
    private String location; //지역
    private String imgsrc; //이미지 경로
    private int price; //경매 가격
    private int immediatelyprice; // 즉시구매가
    private char deleteYn; //삭제 여부

    public Usersdata toEntity() {
        return Usersdata.builder()
                .title(title)
                .username(username)
                .category(category)
                .location(location)
                .imgsrc(imgsrc)
                .price(price)
                .immediatelyprice(immediatelyprice)
                .deleteYn(deleteYn)
                .build();
    }
}
```

Usersdata 란 entity에다가 build로 값을 집어넣습니다. **요소들을 만들어서 반환하는 과정**입니다.



Usersdata를 보면

```java
public class Usersdata {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // PK
    private LocalDateTime createdDate = LocalDateTime.now() ; //생성일
    private LocalDateTime modifiedDate ; //수정일
    private String category; //카테고리
    private String username; //작성자
    private int price; //경매 가격
    private int immediatelyprice; // 즉시구매가
    private String title; //제목
    private String location; //지역
    private String imgsrc; //이미지 경로
    private char deleteYn; //삭제 여부

    //빌더 패턴을 이용하면 어떤 멤버에 어떤 값을 세팅하는지 직관적으로 확인이 가능합니다.
    //인자의 순서에 관계없이 객체를 생성할 수 있습니다.
    @Builder
    public Usersdata(String title, String category, String username, int price, int immediatelyprice,
                     String location, String imgsrc, char deleteYn){
        this.category = category;
        this.username = username;
        this.price = price;
        this.immediatelyprice = immediatelyprice;
        this.title = title;
        this.location = location;
        this.imgsrc = imgsrc;
        this.deleteYn = deleteYn;

    }
}
```

build()로 매개변수에 있는 값으로 멤버변수를 채웁니다. 요소들을 만들 때 순서와 상관없이 만들 수 있게해줘서 편합니다. **이 멤버변수는 곧 테이블의 한 행**과 같습니다. entity는 테이블 그 자체라는 말을 이해할 수 있게되었습니다.