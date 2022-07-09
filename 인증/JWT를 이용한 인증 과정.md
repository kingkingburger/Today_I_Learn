

#### JWT (JSON Web Token)

![개발 지식/WEB 지식](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbmtdsy%2FbtrqApuPlmS%2FgEE45964H9LPXwm2OxROSk%2Fimg.png)

JWT(JSON Web Token)란 `인증에 필요한 정보들을 암호화시킨 JSON 토큰`을 의미한다.
그리고 JWT 기반 인증은 JWT 토큰(Access Token)을 `HTTP 헤더`에 실어 `서버가 클라이언트를 식별하는 방식`이다

JWT는 JSON 데이터를 **Base64 URL-safe Encode** 를 통해 인코딩하여 직렬화(일자로 쭉)한 것이며, 토큰 내부에는 위변조 방지를 위해 개인키를 통한 **전자서명**도 들어있다.
따라서 사용자가 JWT 를 서버로 전송하면 **서버는 서명을 검증하는 과정**을 거치게 되며 검증이 완료되면 요청한 응답을 돌려준다.

> Base64 URL-safe Encode란?
>
> Base64 URL-safe Encode 는 일반적인 Base64 Encode 에서 URL 에서 오류없이 사용하도록 '+', '/' 를 각각 '-', '_' 로 표현한 것이다.



#### JWT 구조

JWT는 . 을 구분자로 나누어지는 세 가지 문자열의 조합이다.
. 을 기준으로 좌측부터 Header, Payload, Signature를 의미한다.

![json-web-token](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbwmwBq%2FbtrqGVel5Qk%2FnPIPkduUJk2xT8Lv00FPb0%2Fimg.png)

**Header** 에는 JWT 에서 사용할 타입과 해시 알고리즘의 종류가 담겨있습니다 

**Payload** 는 서버에서 첨부한 사용자 권한 정보와 데이터가 담겨있습니다.

**Signature** 에는 Header, Payload 를 Base64 URL-safe Encode 를 한 이후 Header 에 명시된 해시함수를 적용하고, 개인키(Private Key)로 서명한 전자서명이 담겨있습니다.

전자서명에는 **비대칭 암호화 알고리즘**을 사용하므로 암호화를 위한 키와 복호화를 위한 키가 다르다. 암호화(전자서명)에는 개인키를, 복호화(검증)에는 공개키를 사용한다.



자세히 알아봅시다.

#### **Header**

![json-web-token](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbxGWdp%2FbtrqApn8yE5%2FjWJFUxLUAGKW4qncSKUcyk%2Fimg.png)

- alg : 서명 암호화 알고리즘(ex: HMAC SHA256, RSA)
- typ : 토큰 유형



**Payload**

![json-web-token](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FSsJJz%2FbtrqAVmHOSN%2F65OmpdL0CxUJwvhDgncaI1%2Fimg.png)

토큰에서 사용할 정보의 조각들인 **Claim** 이 담겨있다. `(실제 JWT 를 통해서 알 수 있는 데이터)`
즉, 서버와 클라이언트가 주고받는 **시스템에서 실제로 사용될 정보에 대한 내용을 담고 있는 섹션**이다.

페이로드는 정해진 데이터 타입은 없지만, 대표적으로 Registered claims, Public claims, Private claims 이렇게 세 가지로 나뉜다.

출처: https://inpa.tistory.com/entry/WEB-📚-JWTjson-web-token-란-💯-정리 [👨‍💻 Dev Scroll:티스토리]

![json-web-token](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmgfVm%2FbtrqCTBYYnU%2FC8HHxa7hhNu94ivkq2xKK1%2Fimg.png)

- Registed claims : 미리 정의된 클레임.

  - iss(issuer; 발행자), 

  - exp(expireation time; 만료 시간), 

  - sub(subject; 제목), 

  - iat(issued At; 발행 시간), 

  - jti(JWI ID)

- Public claims : 사용자가 정의할 수 있는 클레임 공개용 정보 전달을 위해 사용.
- Private claims : 해당하는 당사자들 간에 정보를 공유하기 위해 만들어진 사용자 지정 클레임. 외부에 공개되도 상관없지만 해당 유저를 특정할 수 있는 정보들을 담는다

출처: https://inpa.tistory.com/entry/WEB-📚-JWTjson-web-token-란-💯-정리 [👨‍💻 Dev Scroll:티스토리]

#### **Signature**

![json-web-token](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmfFwR%2FbtrqGscsGzU%2Fj4kxvr7ZQKbJgxQLOBJIP0%2Fimg.png)

- 시그니처에서 사용하는 알고리즘은 헤더에서 정의한 **알고리즘 방식(alg)**을 활용한다.
- 시그니처의 구조는 (헤더 + 페이로드)와 서버가 갖고 있는 유일한 key 값을 합친 것을 헤더에서 정의한 알고리즘으로 암호화를 한다.

![json-web-token](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FciuEZW%2FbtrqGUNpW5k%2FtTa44GLQ4LzQhgD9gpb4j1%2Fimg.png)

요약하면 위 그림과 같습니다

```
Header와 Payload는 단순히 인코딩된 값이기 때문에 제 3자가 복호화 및 조작할 수 있지만, Signature는 서버 측에서 관리하는 비밀키가 유출되지 않는 이상 복호화할 수 없다.
따라서 Signature는 토큰의 위변조 여부를 확인하는데 사용된다.
```

### **JWT를 이용한 인증 과정**

![json-web-token](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ft2DrY%2FbtrqGTOykhT%2FbpeE1EZ0YeP9xIec1uU9g0%2Fimg.png)

1. 사용자가 ID, PW를 입력하여 서버에 로그인 인증을 요청한다.
2. 서버에서 클라이언트로부터 인증 요청을 받으면, Header, PayLoad, Signature를 정의한다.Hedaer, PayLoad, Signature를 각각 Base64로 한 번 더 암호화하여 JWT를 생성하고 이를 쿠키에 담아 클라이언트에게 발급한다.
3. 클라이언트는 서버로부터 받은 JWT를 로컬 스토리지에 저장한다. (쿠키나 다른 곳에 저장할 수도 있음)API를 서버에 요청할때 **Authorization header에 Access Token**을 담아서 보낸다.
4. 서버가 할 일은 클라이언트가 Header에 담아서 보낸 JWT가 내 서버에서 발행한 토큰인지 일치 여부를 확인하여 일치한다면 인증을 통과시켜주고 아니라면 통과시키지 않으면 된다.인증이 통과되었으므로 페이로드에 들어있는 유저의 정보들을 select해서 클라이언트에 돌려준다.
5. 클라이언트가 서버에 요청을 했는데, 만일 액세스 토큰의 시간이 만료되면 클라이언트는 리프래시 토큰을 이용해서
6. 서버로부터 새로운 엑세스 토큰을 발급 받는다.



#### 토큰 인증 신뢰성을 가지는 이유

유저 JWT: A(Header) + B(Payload) + C(Signature) 일 때 (만일 임의의 유저가 B를 수정했다고 하면 B'로 표시한다.)

1. 다른 유저가 B를 임의로 수정 -> 유저 JWT: A + **B'** + C
2. 수정한 토큰을 서버에 요청을 보내면 서버는 유효성 검사 시행
   - 유저 JWT: A + **B'** + C
   - 서버에서 검증 후 생성한 JWT: A + **B'** + C' => (signature) 불일치
3.  대조 결과가 일치하지 않아 유저의 정보가 임의로 조작되었음을 알 수 있다.

정리하자면, 서버는 토큰 안에 들어있는 정보가 무엇인지 아는게 중요한 것이 아니라 해당 토큰이 유효한 토큰인지 확인하는 것이 중요하기 때문에, 클라이언트로부터 받은 JWT의 헤더, 페이로드를 서버의 key값을 이용해 시그니처를 다시 만들고 이를 비교하며 일치했을 경우 인증을 통과시킨다.



#### JWT 장점

1. Header와 Payload를 가지고 Signature를 생성하므로 **데이터 위변조를 막을 수 있다.**
2. 인증 정보에 대한 **별도의 저장소가 필요없다.**
3. JWT는 토큰에 대한 기본 정보와 전달할 정보 및 토큰이 검증됬음을 증명하는 서명 등 필요한 모든 정보를 자체적으로 지니고 있다.
4. 클라이언트 인증 정보를 저장하는 세션과 다르게, **서버는 무상태(StateLess)**가 된다.
5. 확장성이 우수하다.
6. 토큰 기반으로 **다른 로그인 시스템에 접근 및 권한 공유가 가능하다. (쿠키와 차이)**
7. OAuth의 경우 Facebook, Google 등 소셜 계정을 이용하여 다른 웹서비스에서도 로그인을 할 수 있다.
8. 모바일 어플리케이션 환경에서도 잘 동작한다. (모바일은 세션 사용 불가능)

```
서버에서 가장 피해야 할 것은 데이터베이스 조회이다.
서버 자체가 죽는 경우도 있지만, 대부분 DB가 터져서 서버도 같이 죽는 경우가 허다하기 때문이다.
이런 점에서, JWT 토큰은 DB조회를 안해도 되는 장점을 가지고 있다는 점이다.
만일 payload에 유저이름과 유저등급 을 같이 두고 보내면, 서버에서는 유저이름을 가지고 DB를 조회해서 유저 등급을 얻지않아도 바로 원하는 정보를 취할수 있다.
```



#### 출처

https://inpa.tistory.com/entry/WEB-📚-JWTjson-web-token-란-💯-정리 [👨‍💻 Dev Scroll:티스토리]