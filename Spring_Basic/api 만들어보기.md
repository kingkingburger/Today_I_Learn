```
@Getter
@NoArgsConstructor(access= AccessLevel.PROTECTED)
@Entity
public class Usersdata {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // PK
    private LocalDateTime createdDate = LocalDateTime.now(); //생성일
    private LocalDateTime modifiedDate; //수정일
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

이렇게 생긴 **entity**가 있습니다. mysql에서 데이터를 가져옵니다!





```
@Getter
@NoArgsConstructor(access = AccessLevel.PACKAGE)
public class UserDataResponseDto {


    private Long id; // PK
    private LocalDateTime createdDate = LocalDateTime.now(); //생성일
    private LocalDateTime modifiedDate; //수정일
    private String category; //카테고리
    private String username; //작성자
    private int price; //경매 가격
    private int immediatelyprice; // 즉시구매가
    private String title; //제목
    private String location; //지역
    private String imgsrc; //이미지 경로
    private char deleteYn; //삭제 여부

    public UserDataResponseDto(Usersdata usersdata) {
        this.id = usersdata.getId();
        this.category = usersdata.getCategory();
        this.username = usersdata.getUsername();
        this.price = usersdata.getPrice();
        this.immediatelyprice = usersdata.getImmediatelyprice();
        this.title = usersdata.getTitle();
        this.location = usersdata.getLocation();
        this.imgsrc = usersdata.getImgsrc();
        this.deleteYn = usersdata.getDeleteYn();
    }

}
```

**응답DTO(ResponseDto)** 입니다. api를 반환할 때 json 형식으로 보내려고 DTO 객체를 만들었습니다.



```
@CrossOrigin(origins="*")
@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
public class UserdataController {

    private final UserService userService;


    @GetMapping("/b")
    public List<UserDataResponseDto> findAll(){
        return userService.findAll();
    }
}
```

컨트롤러 입니다. 테스트로 react(포트3000)에서 spring(포트8080)으로 요청하기 때문에 @CrossOrigin(origins="*")으로 CORS문제를 피했습니다.

 

**@RestController**로 return 그대로를 http 응답 body에 박아줍ㄴ디ㅏ.

 

**@RequestMapping("/api")**를 클래스 레벨에 박아서 /api로 시작하는 url이 오면 이 컨트롤러를 찾게 됩니다.

 

**@RequiredArgsConstructor**로 클래스의 final이 붙은 멤버변수에 spring이 자동으로 객체를 넣어줍니다. 

 

@GetMapping("/b")로 Get요청으로 "/api/b"라는 url이 왔을 때 동작하는 메서드 입니다.

List를 반환하는데 안에는 ResponseDto로 꽉꽉 차있을것 입니다. 그럼 요청이 들어오면 Service에서 나가야겠죠?





```
@Service
@RequiredArgsConstructor
public class UserService {

    //final 붙여야지 생성자 만들어줌
    private final UserdataRepository userdataRepository;

    //게시글 리스트 조회
    public List<UserDataResponseDto> findAll(){
        Sort sort = Sort.by(Sort.Direction.DESC , "id", "createdDate");
        List<Usersdata> list = userdataRepository.findAll(sort);
        return list.stream().map(UserDataResponseDto::new).collect(Collectors.toList());
    }

}

```

**@Service** 로 이 클래스는 서비스를 담당한다고 spring에게 알려줍니다.



```
public interface UserdataRepository extends JpaRepository<Usersdata, Long> {

}
```

**Repository**는 JpaRepository를 상속받습니다. 그러니 이 객체를 만들면 Jpa가 대신 쿼리를 써줍니다. 

자 이제 Jpa가 어떤식으로 **쿼리를 짜야하는지 지정**해 줘야 합니다.

**Sort 객체**를 만드는데 **id**와 **createdDate**를 **DECS(내림차순)**으로 정렬시키는 객체입니다. **spring**에서 지원해줍니다.

따라서 정렬 방향을 direction으로 지정하고 properties를 통해 해당 정렬을 사용할 컬럼 이름(properties)을 나열해 주면 됩니다. 그럼 id와 createdDate를 기준으로 정렬이되는 sort객체를 만들었습니다.

이제 이걸 jpa에 넣어주면 

```
Hibernate: 
    /* select
        generatedAlias0 
    from
        Usersdata as generatedAlias0 
    order by
        generatedAlias0.id desc,
        generatedAlias0.createdDate desc */ 
        
select
    usersdata0_.id as id1_0_,
    usersdata0_.category as category2_0_,
    usersdata0_.created_date as created_3_0_,
    usersdata0_.delete_yn as delete_y4_0_,
    usersdata0_.imgsrc as imgsrc5_0_,
    usersdata0_.immediatelyprice as immediat6_0_,
    usersdata0_.location as location7_0_,
    usersdata0_.modified_date as modified8_0_,
    usersdata0_.price as price9_0_,
    usersdata0_.title as title10_0_,
    usersdata0_.username as usernam11_0_ 
from
    usersdata usersdata0_ 
order by
    usersdata0_.id desc,
    usersdata0_.created_date desc
```

이런식으로 쿼리가 완성됩니다.

```
return list.stream().map(UserDataResponseDto::new).collect(Collectors.toList());
```

자바8부터 **Stream** 을 사용 할 수 있습니다.

기존에 자바 컬렉션이나 배열의 원소를 가공할떄, for문, foreach 등으로 원소 하나씩 골라내여 가공을 하였다면,

**Stream** 을 이용하여 **람다함수형식**으로 간결하고 깔끔하게 요소들의 처리가 가능

배열의 원소를 가공하는데 있어

 

**map**, **filter**, **sorted** 등 이 있습니다.

 

**map은 요소들을 특정조건에 해당하는 값으로 변환해 줍니다.**

요소들을 대,소문자 변형 등 의 작업을 하고 싶을떄 사용 가능 합니다.

여기서는 **Dto 클래스를 새로 생성해서 변환**했습니다. 

 

**filter는 요소들을 조건에 따라 걸러내는 작업을 해줍니다.**

길이의 제한, 특정문자포함 등 의 작업을 하고 싶을때 사용 가능합니다.

 

**sorted는 요소들을 정렬해주는 작업을 해줍니다.**

 

요소들의 가공이 끝났다면 리턴해줄 결과를 **collect** 를 통해 만들어줍니다. 

요소들을 대문자로 가공하였다면 collect 를 이용하여 결과를 리턴받을 수 있습니다.

Collectors.toList 를 이용해 리스트로 리턴 받을 수 있습니다.

 

출처:https://dpdpwl.tistory.com/81