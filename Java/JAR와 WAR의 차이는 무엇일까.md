## JAR와 WAR의 차이는 무엇일까? 

스프링 프로젝트를 배포하려 합니다. 그러려면 프로젝트를 빌드하고 압축해서 서버에 올려야 합니다. 빌드하고 압축하는 과정 중에 의문이 들었습니다. **jar 파일**과 **war 파일**의 형태 2가지가 있었습니다. 두 개가 어떤 차이점이 있는지 알아보겠습니다.

 

#### WAR, JAR는 무엇인가??

서비스 배포시에 프로젝트는 **WAR 포맷**으로 묶어서 **Tomcat 등의 웹 컨테이너(WAS)** 에다 넣어서 deploy 하는 식으로 사용한다고 합니다. 

**jar는** Maven 이나 Gradle 가져온 라이브러리들이 보여주는 포맷입니다. Class 파일들이 묶인 jar 파일을 가져와서 그 안에 있는 서비스를 이용하는 것입니다.

 

 

#### JAR의 상세정보

JAR은 **Java Archieve** 라는 의미입니다.

.jar 확장자 파일에는 Class와 같은 Java 리소스와 속성 파일, 라이브러리 및 액세서리 파일이 포함되어 있습니다. 

 

쉽게 JAVA 어플리케이션이 동작할 수 있도록 **자바 프로젝트를 압축한 파일**로 생각하시면 되겠네요. 실제로 J**AR 파일은 플랫폼에 귀속되는 점만 제외하면 WIN ZIP파일과 동일한 구조**입니다.

 

JAR 파일은 **원하는 구조로 구성이 가능**하며 JDK(Java Development Kit)에 포함하고 있는 **JRE(Java Runtime Environment)**만 가지고도 실행이 가능합니다.

 

#### WAR의 상세정보

WAR는 **Web Application archive라는** 의미입니다.

.war 확장자 파일은 servlet / jsp 컨테이너에 배치 할 수 있는 **웹 어플리케이션(Web Application) 압축 파일 포맷**입니다. JSP, SERVLET, JAR, CLASS, XML, HTML, JAVASCRIPT 등 웹 어플리케이션이 구동되기 위한 기타 자원을 한 군데에 모아 배포하는데 사용되는 파일입니다.

 

WAR는 웹 응용 프로그램를 위한 포맷이기 때문에 **웹 관련 자원만 포함하고 있으며** **이를 사용하면 웹 어플리케이션을 쉽게 배포**하고 테스트 할 수 있습니다.

 

원하는 구성을 할 수 있는 JAR 포맷과 달리 WAR은 WEB-INF 및 META-INF 디렉토리로 **사전 정의 된 구조를 사용**하며 WAR파일을 실행하려면 Tomcat, Weblogic, Websphere 등의 웹 서버 (WEB)또는 웹 컨테이너(WAS)가 필요합니다.

 

WAR 파일도 JAVA의 JAR 옵션( java - jar)을 이용해 생성하는 JAR파일의 일종으로 웹어플리케이션 전체를 패키징하기 위한 JAR파일로 생각하시면 될 것 같습니다.

 

#### JAR와 WAR의 구동 방식 차이점

\- **JAR**는 **JRE( Java Runtime Environment )만 존재하면 프로젝트 구동이 가능합니다**

\- **WAR**는 별도의 **웹서버 또는 WAS ( 웹 컨테이너 )가 있어야 프로젝트 구동이 가능합니다.**

 

#### 결론

JAR와 WAR의 차이는 리소스들을 하나의 파일로 패키징 하는 과정의 차이가 있는 것 입니다.



![img](https://blog.kakaocdn.net/dn/clFlHg/btrH1CbBn3E/3gFhOsKnhIWrgGKvwG7zW0/img.png)



WAR 안에 JAR 가 있는 것 처럼 WAR는 실행하기 위한 모든 파일을 묶고 있다고 생각하면 되겠습니다.

 

#### 참고

https://ifuwanna.tistory.com/224

https://velog.io/@sowjd1225/JAR-vs-WAR-vs-EAR