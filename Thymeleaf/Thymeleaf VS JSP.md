## Thymeleaf VS JSP

나는 왜 jsp를 쓰지 않고 Thymeleaf를 쓸까?

인프런에서 spring 강의 배울때 'view는 thymeleaf가 요즘 대세이다.' 라는 말을 듣고 자연스럽게 썼습니다. 그러면 jsp는 왜 많이 안쓰게 되었는가? 를 생각을 해보겠습니다.





## 차이점

Thymeleaf는 HTML, XML, JavaScript, CSS 및 일반 텍스트를 처리 할 수 있는 웹 및 독립형 환경에서 사용할 수 있는 Java 템플릿 엔진입니다. Thymeleaf는 **html파일을 가져와서 파싱해서 분석후 정해진 위치에 데이터를 치환**해서 웹 페이지를 생성합니다.



JSP는 서블릿으로 변환되어 실행이 되어집니다. JSP 내에서 **자바 코드**를 사용할 수도 있습니다(사용하지 못하도록 설정할 수 있습니다). Thymeleaf는 자바코드를 사용할 수 없고, jsp에서 처럼 커스텀 태그와 같은 기능도 없습니다.



## 장단점

**JSP**는 html에서 자바코드를 사용할 수 있다는것이 장점이고 **Thymelaef**는 일반적인 태그를  조작한 다는 점이 장점인거 같습니다.

#### 일반적인 태그를 조작한다는게 뭐가장점인가?

view를 수정할 때 웹서버를 실행하지 않고도 오프라인에서 수정할 수 있습니다. 그리고 일반 text를 넣고 if문을 걸어서 편리하게 사용할 수 있습니다.



#### view단에서 java코드를 사용하면

MVC 구조에서 jsp는 **뷰**만 담당해야 합니다. 여기에 자바 코드를 넣으면 비즈니스 로직이 되어버립니다. 이러면 코드를 보는데 힘들어집니다. 이러한 이유 때문에 안쓰는 거 같습니다.





## 성능

Thymeleaf 템플릿 엔진의 성능을 비교한 자료들이 있는지 찾아 봤는데, 예전 자료들이 있었습니다. Thymeleaf 템플릿 엔진은 다른 템플릿엔진이나 JSP에 비해서 속도가 떨어지는것 같았습니다.



**Freemarker > Velocity > JSP > Thymeleaf**



다음 글에서 속도 비교를 찾아볼 수 있습니다. "[Modern Type-Safe Template Engines (Part 2)](https://dzone.com/articles/modern-type-safe-template-engines-part-2)"





Thymeleaf 버전간의 성능 비교 글도 있었습니다. 버전 2에서 버전 3으로 넘어오면서 상당한 성능 개선이 있었다는 내용입니다. 그래도 JSP 보다는 느립니다. 



다음 글에서 내용을 볼 수 있습니다. "[Java: Benchmark Thymeleaf 2.1.4 vs Thymeleaf 3.0 SNAPSHOT](https://smarterco.de/java-benchmark-thymeleaf-2.1.4-vs-thymeleaf-3.0-snapshot/)"



지금까지 Thymeleaf와 JSP를 비교해 보았는데, 반드시 이걸 써야겠다 던가 하는 것은 아닌것 같습니다. 사실 성능도 상대적인 템플릿 엔진들간에 상대적인 것이지 실제 운영에서 느껴질 만큼 느린 것은 아닌것 같습니다. Thymeleaf가 쓰지 못할 만큼 느리다면 사용하는 곳이 없겠지만 Thymeleaf 공식 사이트에 가보면 사용하고 있는 사이트가 상당히 있는것 같습니다.