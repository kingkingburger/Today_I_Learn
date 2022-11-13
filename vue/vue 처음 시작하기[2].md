주소: https://www.youtube.com/watch?v=b0ImUEsqaAA&t=25s



#### 컴포넌트 불러오는법

```js
import HomeView from "../views/HomeView.vue";
```

```js
 component: () => import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
```

2가지 다 import 해오는거지만 큰 차이가 있다고 합니다.

![image](https://user-images.githubusercontent.com/65094518/201472526-9e4929f0-0c83-4d74-a899-3a6c75e99f92.png)

외부 js 파일은 chunk-vendors.js에 모두다 들어가 있습니다.

1번 import형태는 app.js에 모두 들어가게 됩니다.

![image](https://user-images.githubusercontent.com/65094518/201472612-f01c3831-f6b2-4474-b59d-4d2b6beb2cd4.png)

about을 눌렀을 때 app.js 파일로부터 왔습니다.



처음 설치할 때 standard prettier은 무조건 홑따옴표('')로 문자열을 묶어야 합니다.

#### prettier 를 vue의 standard 코드포멧으로 바꾸기

1. 루트폴더에다가 `.prettierrc`를 만들고

```
{
  "semi": false,
  "bracketSameLine": true,
  "singleQuote": true,
  "useTabs": false,
  "trailingComma": "none",
  "printWidth": 80
}
```

이렇게 내용을 채워줍니다.

vue는 semi콜론을 안쓰게 합니다.

2. package.json파일열고

```js
  "eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/vue3-essential",
      "@vue/standard"
    ],
    "parserOptions": {
      "parser": "@babel/eslint-parser"
    },
    "rules": {
      "space-before-function-paren": "off"
    }
  },
```

pretter는 함수를 작성할 때 function myFucntion () {} 처럼 함수명과 ()를 한칸 안띄워야 합니다.

vue는 한칸 안띄워야 해서 prettier의 옵션을 끈것입니다.





#### webpackPrefetch

```js
component: () =>
import(
/* webpackChunkName: "about", webpackPrefetch: true */ '../views/AboutView.vue'
)
```

webpackPrefetch는 당장 쓸껀아닌데 바로 미래에 쓸 가능성이 높으니 `브라우저 캐시`에 리소스를 저장합니다.

사이즈가 작아서, 많이 쓰일거 같은거 들을 prefetch를 넣는 것이 좋겠죠?