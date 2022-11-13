주소: https://www.youtube.com/watch?v=b0ImUEsqaAA&t=25s

vue/cli

- vue 프로젝트를 빠르게 생성해주는 명령어
  - 프로그램을 구동하기 위한 파일, 초기설정



vue 사용할 때 유용한 vscode extension

- vetur



vue create project01

- project01이라는 vue 프로젝트를 생성합니다.

![image](https://user-images.githubusercontent.com/65094518/201467404-749a5c87-af55-453b-b96b-987b6d538a94.png)

vue3 쓸꺼냐 vue2 쓸꺼냐 고르게 됩니다.



#### vue 시작하기 

- **npm run serve** 로 시작합니다.



#### vue 폴더 이해하기

![image](https://user-images.githubusercontent.com/65094518/201467690-a47084b6-2f03-4712-a771-8944a5e4eaaf.png)

- package.json에는 프로젝트에 대한 정보를 다 가지고 있습니다.
  - private: true -> 만약 우리가 npm 사이트에 등록하게 되면 private을 걸꺼냐 안걸꺼냐(나는 개인용도로 쓸꺼다)
  - scripts: cli명령어를 scripts에 넣고 쓸 수 있습니다. 약간 단축키같은 느낌입니다.
  - dependencies: 운영환경에 필요한 모듈들
  - devDependencies: 개발할 때 필요한 모듈들
    - 모듈도 또 다른 모듈이 필요할 수 있습니다. 그런거는 package-lock.json에 들어가 있습니다.
  - borwsersList: 전세계에 1%이상 사용자들이 사용하는 브라우저만 지원한다.

#### main.js

![image](https://user-images.githubusercontent.com/65094518/201467842-8f87ca93-627e-4718-b0eb-016b6b40e5d6.png)

제일 먼저 실행되는 파일 입니다. public에 index.jhtml 파일을  하나만 두고 실행하게 됩니다.

- id가 app인 것에 mount를 시키겠다.



#### App.vue

![image](https://user-images.githubusercontent.com/65094518/201467940-cccf1f21-02d1-4741-acf0-3c3e975a310c.png)

template 태그 안에 html 같은게 들어갑니다.

script 태그 안에 js 들이 들어갑니다.





#### vue create [프로젝트이름] Manually 설치

![image](https://user-images.githubusercontent.com/65094518/201468224-23f52ca5-b742-46ba-8d20-cbc53ecec265.png)

- Babel: 옛날 브라우저에서 최신 문법을 바꿔주는 것
- pwa 모바일 환경같이 만들어 주는것
- Router: 화면이동을 해주는 모듈
- Vuex: vue컴포넌트 내에서 공통으로 접근 가능한 저장소

 Use history mode for router? (Requires proper server setup for index fallback in production) 

ESLint: 국물로 가자

Lint: 저장할 때마다 문법 검사

설정 파일을 별도로 관리할래? package.json으로 관리할래?





#### vue router와 store로 관리할 수 있다

router로 화면을 이동할 수 있게합니다

![image](https://user-images.githubusercontent.com/65094518/201468684-4506456c-7986-45af-b7d4-1d067ab85664.png)

주소에서 path를 받아서 component 에서 해당 vue페이지를 끌고 옵니다.

<router-view>라는 태그가 현재 연결되어있는 컴포너트로 교체가 됩니다.



#### component와 views의 관계

![image](https://user-images.githubusercontent.com/65094518/201468783-22e186ec-58ec-4bb1-bd74-44ab8e8af796.png)

HelloWorld.vue 컴포넌트의 {{ msg }} 라는 값에 값이 들어가게 됩니다.

router -> views -> component 형태로 불러오는거 같습니다.