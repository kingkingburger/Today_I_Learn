## pnpm에서 tsc-watch 사용하기

nodemon이 너무 느려서 다른방법을 찾아보았습니다. nodemon은 한 파일이 바뀌면 전체적으로 컴파일을 해줍니다.

npm의 tsc-watch라는 것이 있었습니다. 전체를 compile하지않고 바뀐부분만 컴파일 해주는 고마운 모듈입니다.

하지만 저는 pnpm이라는 패키지 매니저를 쓰고 있습니다. pnpm에서는 좀 다른방법으로 패키지를 설정해야 합니다.



#### 🔷pnpm-lock.yaml 파일에

```
lockfileVersion: 5.4

importers:

  .:
    specifiers:
      tsc-watch: ^5.0.3
      
    dependencies:
      tsc-watch: 5.0.3_typescript@4.1.3

    devDependencies:


```

tsc-watch를 넣어줍니다. yaml 파일은 들여쓰기를 범위로 인식하니 주의해주세요



그리고 

```
pnpm install
```

을 해서 pnpm을 다운받아줍니다.



package.json에 들어가서 `script`부분을 조정해줍니다.

```
  "scripts": {
    "mi": "tsc-watch --onSuccess \"node build/index.js\""
  },
```

`pnpm mi`라고 루트폴더 터미널에 쓰면 tsc-watch가 동작합니다.

#### ❗이때!

`node [빌드된index.js위치] `를 주의해야합니다. tsconfig.json 폴더에 `outDir`부분에 적혀진 경로에 index.js가 컴파일 되어들어가있을 것입니다. 그 컴파일된 index.js를 node로 실행시켜야 하므로 정확한 경로를 적어줍시다.

#### 참고

- https://gkqlgkql.tistory.com/89





참고할만한 글

- https://gkqlgkql.tistory.com/entry/4%EB%85%84%EC%B0%A8-%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%9D%98-%EC%84%B1%EC%9E%A5-%EB%B0%A9%EB%B2%95%EB%A1%A0-%EC%A1%B0%EA%B8%88%E2%80%A6
- https://marcosong.notion.site/4ab952c8766547b5ac2a9cd6de774228?v=2dcf17e887a54e229cdac807ca49acd2

node로 셀레리움 자세한 예제

- https://goodmemory.tistory.com/98
