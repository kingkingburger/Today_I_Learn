## JavaScript에서 null과 undefined 타입의 차이점 알아보기

java를 할 때는 객체에 무조건 null값을 주었습니다. js를 배우다 보니 undefined 타입 에러를 자주 만나게 되서 정리를 해보려고 합니다.

js엔진에서 소스코드가 실행되기 위한 과정을 먼저 이해 해보겠습니다.

1. `소스코드의 평가`와 `소스코드의 실행` 2가지 과정으로 나누어 처리합니다.
2. 엔진은 코드를 실행하려면 **필요한 환경**을 먼저 만들고 코드가 실행되면서 생긴 **실행 결과를 관리하는 영역**이  필요합니다.
3. 이 모든 것을 관리하는 것(개념적, 물리적 영역)을 **실행 컨텍스트** 라고 말합니다.
4. 엔진은 소스코드를 평가해서 실행 컨텍스트를 생성합니다.
5. 실행 컨텍스트는 크게 두 가지를 관리하는데 하나는 `식별자를 등록하고 스코프를 생성하는 관리`와 `코드의 실행 순서 관리`입니다.
6. 실행 컨텍스트는 **식별자를 등록하고 스코프를 생성할 때**는 **렉시컬 환경**으로 관리합니다.
   - 실행 컨텍스트의 변수 객체를 생성하고 관리하는 것이 **렉시컬 환경**입니다.
7. 코드의 실행 순서는 **실행 컨텍스트 스택**으로 관리합니다.



#### undefined와 null의 공통점

- 둘다 각각의 타입명(undefined, null)의 값이 유일합니다.
- undefined 타입의 값은 undefined가 유일합니다.
- null 타입의 값은 null이 유일합니다.

-----



#### undefined 타입에 대해서

- undefined는 ‘아무 값도 할당받지 않은 상태’를 의미합니다.
- 변수 선언에 의해 확보된 메모리 공간을 처음 할당이 이뤄질 때까지 빈 상태(*대부분 비어 있지 않고 쓰레기 값이 들어 있다.)로 내버려두지 않고 자바스크립트 엔진이 undefined로 초기화합니다.
- 변수를 참조했을 때 undefined가 반환된다면 선언 이후 값이 할당되지 않은 즉, 초기화되지 않은 변수라는 것을 알 수 있습니다.

완전 깡통 변수를 메모리도 아니고 어딘가(실행 컨텍스트의 스코프)에 저장해 놓는거 같습니다.

-----



#### null 타입에 대해서

- 자바스크립트는 대소문자를 구분하므로 null은 Null, NULL 등과는 다릅니다.
- null은 ‘비어있는, 존재하지 않는 값'(값의 부재)을 의미합니다.

메모리에 객체를 만들고  null이라는 값을 넣어주니 메모리에 존재하는 변수라고 생각됩니다.

----



### **👉 실행 컨텍스트를 구성하는 렉시컬 환경의 객체 형태의 스코프**

- 소스코드를 실행하기 전 **변수, 함수 등의 선언문만 먼저 실행**하여 생성된 변수나 함수 식별자를 키로 만들어서 실행 컨텍스트가 관리하는 **스코프에 등록**한다.
- 그리고 소스코드가 실행되면서 생긴 실행 결과도 실행 컨텍스트가 관리한다. (변수에 값 할당 및 변경 등)
- 이때 소스코드를 실행하면서 필요한 정보(변수, 함수 참조)를 실행 컨텍스트가 관리하는 **스코프**에서 검색해서 취득한다.
- 스코프에 등록한다는 말은 정확히 말해서 **실행 컨텍스트의 변수 객체에 등록되고 초기화되고 할당되는 것**이다.
- 실행 컨텍스트의 **변수 객체를 생성하고 관리하는 것이 렉시컬 환경**이다.
- 렉시컬 환경은 식별자와 식별자에 바인딩 된 값, 그리고 상위 스코프에 대한 참조를 기록하는 자료구조이고 실행컨텍스트를 구성하는 컴포넌트이다.
- 앞서 말한 실행 컨텍스트가 관리하는 스코프에 등록, 검색이란 말을 정확하게 말하자면 **실행 컨텍스트를 구성하는 렉시컬 환경이 생성한 객체에서 등록하고 검색하다**는 말이고 이러한 객체는 **스코프 생성**을 의미하는 것이다.
- 렉시컬 환경은 **스코프를 구분하여 식별자를 등록하고 관리하는 저장소**이기 때문이다.
- 그래서 **스코프를 생성한다고 한 것**이다. **결국 객체를 생성한 것**이다. 이것이 스코프의 실체이다.
- 이러한 렉시컬 환경이 스코프와 식별자를 관리한다.
- 즉, 렉시컬 환경은 스코프를 구분하여 식별자를 등록하고 관리하는 저장소 역할을 한다.



### **👉 스코프의 실체**

- 렉시컬 환경은 렉시컬 스코프의 실체이다.
- 렉시컬 스코프란 함수를 어디서 호출했는지가 아닌 **함수를 어디서 정의했는지에 따라 스코프를 결정**하는 것을 말한다.
- 스코프라는 개념의 실체는 **실행 컨텍스트의 렉시컬 환경**이다.
- 렉시컬 환경은 외부 렉시컬 환경에 대한 참조를 통해 **상위 렉시컬 환경과 연결**된다.
- 이것이 바로 **스코프 체인**이다.
- 따라서 함수의 상위 스코프를 결정한다는 것은 렉시컬 환경의 외부 렉시컬 환경에 대한 참조에 저장할 참조값을 결정한다는 것과 같다.
- 렉시컬 환경의 외부 렉시컬 환경에 대한 참조에 저장할 참조값이 바로 상위 렉시컬 환경에 대한 참조이며, 이것이 상위 스코프이기 때문이다.
- 다시 한 번 렉시컬 환경을 정의해보면 다음과 같다.
- 렉시컬 환경의 외부 렉시컬 환경에 대한 **참조에 저장할 참조값**, 즉 상위 스코프에 대한 참조는 **함수 정의가 평가되는 시점에 함수가 정의된 환경(위치)에 의해 결정**된다. 이것이 바로 렉시컬 스코프이다.



### **👉 var, let 키워드와 undefined**

- var 키워드로 선언된 변수는 실행 컨텍스트 객체에 등록(즉, 렉시컬 횐경 등록, 즉, 실행컨텍스트의 렉시컬 환경이라는 객체 형태의 자료구조, 스코프에 등록)과 동시에 초기화 단계도 진행한다. 초기화 단계에서는 등록된 변수를 위한 메모리 공간을 확보한다. 이 단계에서 undefined로 초기화된다.
- let 키워드로 선언된 변수는 실행 컨텍스트 객체에 등록되고 소스코드가 실행후 선언문을 만났을 때 비로소 undefined로 초기화된다. 즉, 변수를 위한 메모리 공간을 확보한다.
- 그리고 할당 단계에서 undefined로 초기화된 변수에 실제 값을 할당한다.
- 그런데 이때 변수에 값이 없다는 것을 명시하고 싶다면 null 값을 할당한다.
- undefined는 변수가 생성되는 단계에서 메모리 공간을 확보하기 위해 변수를 초기화하기 위해 사용되는 자료형이기 때문이다.



#### 참고

- https://hanamon.kr/javascript-undefined-null-%EC%B0%A8%EC%9D%B4%EC%A0%90/
- https://2ssue.github.io/common_questions_for_Web_Developer/docs/Javascript/13_undefined&null.html#undefined

