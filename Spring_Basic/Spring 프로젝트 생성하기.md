## Spring 프로젝트 생성하기



#### 버전

```
 java 11
 intellij(2020.3)
```



요즘에는 스프링부트로 스프링을 만들면 됩니다.
너무 편리하기 때문입니다.

[스프링 부트 스타터 사이트](https://start.spring.io/)로 이동해서 스프링 프로젝트를 생성

![image](https://user-images.githubusercontent.com/65094518/145711357-50866b5c-19a9-4ac7-89f7-5fddb309d666.png)

스프링을 만들어주는 사이트 입니다.

스프링에서 운영중 입니다.



#### Maven VS Gradle

필요한 라이브러리를 땡겨와서 빌드까지 해주는 툴입니다.

요즘에는 Gradle으로 많이 넘어오는 추세입니다.



#### Spring Boot

버전을 정해줘야 합니다.

SNAPSHOT - 아직 만들고 있는 버전입니다.
M1 - 정식 배포가되지 않은 것 입니다.



#### Group

보통 기업 도메인 명을 적어줍니다.



#### Artiface

빌드되어 나올 때 결과물 입니다.



#### Dependencies

내가 스프링을 쓸 때 **어떤 라이브러리**를 땡겨쓸 꺼냐 선택하는 곳 입니다.

**Thymeleaf**  - HTML을 만들어주는 템플릿 엔진

**Spring Web** - 웹 프로젝트를 만들 때 기본!



- **Generate**를 눌러서 다운 받습니다.
- **IntelliJ**를 사용해 폴더를 열여줍니다.



#### 폴더 구조를 봐봅시다.

![image-20211212185315654](https://user-images.githubusercontent.com/65094518/145711380-cf588d75-9a02-45a1-97e8-6b5338d22b6b.png)

src 보면 요즘 main이랑 test 폴더가 나눠져 있습니다.

main에는 실제 파일이 들어가고 test에는 test코드 파일이 들어갑니다.

test코드는 무척이나 중요합니다.

java 파일을 제외한건 resources에 들어가 있습니다.



**build.gralde** 를 보면 버전설정하고 라이브러리를 땡겨온 것을 확인할 수 있습니다.

내가 어떤~ 라이브러리를 쓴다고 적어놓으면 **mavenCentral** 에가서 다운받아 옵니다.



기본 main 을 실행하면

Spring이 내장된 **Tomcat 웹서버**를 실행시켜 줍니다.

##### **Gradle**을 통해서 실행하지 않고 Intell J로 바로 실행하게 만듭시다



## Spring의 라이브러리 맛보기



intell J를 보면 **External libraries**폴더에 밖에서 땡겨온 라이브러리들이 있습니다.



Grandle이나 maven 같이 빌드툴 들은 의존관계를 **관리** 해줍니다.

의존 관계 있는 것들을 쭈욱 땡겨옵니다.



intell J 오른쪽에 Gradle을 보면 Dependencies를 보면 라이브러리 들을 계속 들어간 다는 것을 알 수 있습니다.



고대의 선배님들은

tomcat같은 것을 설치해서 java 코드를 밀어 넣는 방식으로 동작시켰습니다.

요즘은 소스 라이브러리에서 이런 웹 서버를 들고 있습니다.(임배디드, 내장)

그냥 실행만 하는대도 웹 서버가 뜹니다.



스프링 부트와 관련된 라이브러리를 쓰면 core까지 땡겨 씁니다.



##### loggin?

현업에서는 꼭 log로 출력해야 합니다.System.out.println()을 쓰면 안됩니다.

꼭 log로 남겨놔야 하기 때문이죠



**스프링 부트 라이브러리**

- spring-boot-starter-web
  - spring-boot-starter-tomcat: 톰켓 (웹서버)
  - spring-webmvc: 스프링 웹 mvc

- spring-boot-starter-thyleaf:타임리프 템플릿 엔진(View)



**테스트 라이브러리**

- spring-boot-starter-test
  - junit: 테스트 프레임워크



## View 환경설정

#### Welcome페이지

도메인만 누르고 들어왔을 때 처음 보여지는 화면입니다.

**resources/static/index.html** 에 들어가는 것이  웰컴 페이지 입니다.



만약 웰컴페이지를 만들고 싶다면

- [spring.io](https://spring.io/)에 들어간다.
- Projects에 Spring Boot 클릭 
- Learn을 누르고
- Reference Doc를 봅니다.
- 주제에 맞는 것을 고르고 검색을 해서 찾습니다.



index.html을 못찾으면 index templete을 검색한다고 나와있습니다.



html을 던져주는 것을 그냥 파일을 주는 것 입니다.

여기서 **템플릿 엔진**을 쓰면 파일의 모양을 바꿀 수 있습니다.

우리는 **Thymeleaf**를 씁니다.





웹 에플리케이션에서 첫 번째 진입점이 **Controller** 입니다.

![image-20211212202720001](https://user-images.githubusercontent.com/65094518/145711396-1157e350-5241-47d2-b832-62bc4840f80e.png)



/hello요청이 들어오면 이 함수를 실행 시킵니다.

key는 data이고 value는 hello 입니다.



![image-20211212202708952](https://user-images.githubusercontent.com/65094518/145711388-56de5b2f-2bce-4db5-a7bb-a0ad4492a1b4.png)

```
<html xmlns:th="http://www.thymeleaf.org">
```

한줄 넣어주면 `thymeleaf` 문법을 쓸 수 있습니다.





#### 동작환경 그림

![image-20211212203256268](https://user-images.githubusercontent.com/65094518/145711404-dcb589da-051f-44d8-8495-03f7aa74c4b1.png)

우리가 url을 치면 GET방식으로 넘어옵니다.

spring이 model을 만들어서 넘겨줍니다.

return hello는 `resource/templates에 가라` 라는 뜻입니다.

찾아가서 hello를 찾습니다.



스프링 부트 템플릿엔진이  

resources:templates/ + {ViewName} +.html 으로 매핑합니다.



data는 키 값이니 그 안에있는 hello를 꺼냅니다.



## 빌드하고 실행하기

저는 window 사용자여서 해당 폴더에 가서 cmd를 치고 `gradlew build`를 해서 build를 했습니다.

다음 `cd build`를 해서 build폴더로 넘어간 다음 `cd libs`으로 들어가 줍니다.

그안에 `.jar`파일이 들어있을 것입니다.



#### jar 실행시키기

`java -jar ***.jar` 로 실행시킵시다.



서버를 배포할 때 build를 하고 jar파일만 실행시키면 된다는 걸 알았습니다.

그러면 서버에서 spring이 동작합니다!





`gradelew clean build` 하면 clean build를 해줍니다.

