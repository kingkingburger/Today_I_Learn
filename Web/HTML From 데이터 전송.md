## HTML From 데이터 전송

HTML From 전송은 GET, POST만 지원이 됩니다.

form안의 정보들은 GET방식으로 요청하면 쿼리스트링으로 들어가고 POST방식으로 요청하면 컨탠츠-바디 부분에 들어가게 됩니다.



## HTML API 데이터 전송

POST, PUT, PATCH를 사용해 메시지 바디를 사용해 데이터 전송합니다.



## 클라이언트에서 서버로 데이터 전송

#### 데이터 전달 방식은 크게 2가지

• 쿼리 파라미터를 통한 데이터 전송

#### • GET

• 주로 정렬 필터(검색어)
• 메시지 바디를 통한 데이터 전송

#### • POST, PUT, PATCH

• 회원 가입, 상품 주문, 리소스 등록, 리소스 변경



## 클라이언트에서 서버로 데이터 전송

#### 4가지 상황

#### • 정적 데이터 조회

• 이미지, 정적 텍스트 문서

#### • 동적 데이터 조회

• 주로 검색, 게시판 목록에서 정렬 필터(검색어)

#### • HTML Form을 통한 데이터 전송

• 회원 가입, 상품 주문, 데이터 변경

#### • HTTP API를 통한 데이터 전송

• 회원 가입, 상품 주문, 데이터 변경
• 서버 to 서버, 앱 클라이언트, 웹 클라이언트(Ajax)





## 회원 관리 시스템

리소스를 식별해야합니다. 미네랄 그 자체를 식별해야하는 것이죠

• 회원 목록 /members -> GET
• 회원 등록 /members -> POST
• 회원 조회 /members/{id} -> GET
• 회원 수정 /members/{id} -> PATCH, PUT, POST
• 회원 삭제 /members/{id} -> DELETE



#### 컬렉션(Collection)

• 서버가 관리하는 리소스 디렉토리
• 서버가 리소스의 URI를 생성하고 관리
• 여기서 컬렉션은 /members

서버에 요청하는 것 /members가 post로 들어오면 서버가 알아서 100번째 자리에 넣으라고 /members/100을 넣습니다.



#### 스토어(Store)

• 클라이언트가 관리하는 리소스 저장소
• 클라이언트가 리소스의 URI를 알고 관리
• 여기서 스토어는 /files

리소스 URI를 다 알고 적어야 하니 클라이언트가 알아야 합니다. 서버는 시키는 일을 할 뿐입니다.



#### HTML FORM 사용

• 회원 목록 /members -> GET
• 회원 등록 폼 /members/new -> GET
• 회원 등록 /members/new, /members -> POST
• 회원 조회 /members/{id} -> GET
• 회원 수정 폼 /members/{id}/edit -> GET
• 회원 수정 /members/{id}/edit, /members/{id} -> POST
• 회원 삭제 /members/{id}/delete -> POST

**HTML FORM은 GET, POST만 지원**



#### 컨트롤 URI

• GET, POST만 지원하므로 제약이 있음
• 이런 제약을 해결하기 위해 동사로 된 리소스 경로 사용
• POST의 **/new, /edit, /delete가 컨트롤 URI**
• HTTP 메서드로 해결하기 애매한 경우 사용(HTTP API 포함)



## 참고하면 좋은 URI 설계 개념

#### • 문서(document)

• 단일 개념(파일 하나, 객체 인스턴스, 데이터베이스 row)
• 예) /members/100, /files/star.jpg

#### • 컬렉션(collection)

• 서버가 관리하는 리소스 디렉터리
• 서버가 리소스의 URI를 생성하고 관리
• 예) /members

#### • 스토어(store)

• 클라이언트가 관리하는 자원 저장소
• 클라이언트가 리소스의 URI를 알고 관리
• 예) /files

#### • 컨트롤러(controller), 컨트롤 URI

• 문서, 컬렉션, 스토어로 해결하기 어려운 추가 프로세스 실행
• 동사를 직접 사용
• 예) /members/{id}/delete