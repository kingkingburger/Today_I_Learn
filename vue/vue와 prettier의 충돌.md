## vue와 prettier의 충돌

vue create [프로젝트이름] 하고 eslint를 기본(basic)으로 설정했습니다.

vue의 eslint를 사용할 때 prettier의 설정을달리해줘야 했었습니다.

왜냐하면 vue는 ''를 사용하고 prettier는 기본적으로 ""으로 문자열을 감쌉니다.

그런데 다른 프로젝트할 때는 prettier를 기본으로 사용하고 싶었스빈다. vue만 prettier를 따로 적용시키고 싶었죠.



그 방법을 찾아보니 **prettierrc라는 파일**을 만들면 되었습니다.

```
{
  "semi": false, // 끝에 세미콜론 안붙힘
  "singleQuote": true, // 홑따옴표 사용
  "useTabs": false, // 탭 사용안함
  "trailingComma": "none", //문장 끝에 콤마 안넣음
  "printWidth": 80 // 한줄에 80자만 들어가게끔, 이상이면 줄바꿈
}
```

루트폴더(최상위 폴더)에 .prettierrc 파일을 생성하고 위 내용을 넣으면 됩니다.



다른 옵션들 입니다.

```
{
  "arrowParens": "avoid", // 화살표 함수 괄호 사용 방식
  "bracketSpacing": false, // 객체 리터럴에서 괄호에 공백 삽입 여부 
  "endOfLine": "auto", // EoF 방식, OS별로 처리 방식이 다름 
  "htmlWhitespaceSensitivity": "css", // HTML 공백 감도 설정
  "jsxBracketSameLine": false, // JSX의 마지막 `>`를 다음 줄로 내릴지 여부 
  "jsxSingleQuote": false, // JSX에 singe 쿼테이션 사용 여부
  "printWidth": 80, //  줄 바꿈 할 폭 길이
  "proseWrap": "preserve", // markdown 텍스트의 줄바꿈 방식 (v1.8.2)
  "quoteProps": "as-needed" // 객체 속성에 쿼테이션 적용 방식
  "semi": true, // 세미콜론 사용 여부
  "singleQuote": true, // single 쿼테이션 사용 여부
  "tabWidth": 2, // 탭 너비 
  "trailingComma": "all", // 여러 줄을 사용할 때, 후행 콤마 사용 방식
  "useTabs": false, // 탭 사용 여부
  "vueIndentScriptAndStyle": true, // Vue 파일의 script와 style 태그의 들여쓰기 여부 (v1.19.0)
  "parser": '', // 사용할 parser를 지정, 자동으로 지정됨
  "filepath": '', // parser를 유추할 수 있는 파일을 지정
  "rangeStart": 0, // 포맷팅을 부분 적용할 파일의 시작 라인 지정
  "rangeEnd": Infinity, // 포맷팅 부분 적용할 파일의 끝 라인 지정,
  "requirePragma": false, // 파일 상단에 미리 정의된 주석을 작성하고 Pragma로 포맷팅 사용 여부 지정 (v1.8.0)
  "insertPragma": false, // 미리 정의된 @format marker의 사용 여부 (v1.8.0)
  "overrides": [ 
    {
      "files": "*.json",
      "options": {
        "printWidth": 200
      }
    }
  ], // 특정 파일별로 옵션을 다르게 지정함, ESLint 방식 사용
}
```