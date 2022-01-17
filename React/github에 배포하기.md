## github에 배포하기

일단 터미널에 `npm i gh-pages`를 쳐서 다운을 받습니다. github에서 무료로 호스팅을 해준다고 합니다.

그리고 `build`를 해야하는데 buile를 하면 **production ready code**를 생성하게 됩니다. production ready code란 코드가 압축되고 모든것이 최적화 된다는 것입니다.

`npm run build`를 하면 build를 하고 build 폴더를 제공합니다. 브라우저가 읽을 수 있게 최적화 되어있어 사람이 읽기에는 어렵습니다.



이제 github에 push해야 합니다.





## 첫 번째 단계

```
},

 "homepage": "https://kingkingburger.github.io/react-for-beginners"

}
```

package.json의 마지막부분에 `"homepage":"https://github이름.github.io/레포지토리이름"`을 적어줍시다.





## 두 번째 단계

다른 스크립트를 만들어줘야 합니다.

```
"scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "deploy": "gh-pages -d build",
    "predeploy": "npm run build"
  },
```

"deploy라는 명령어는 gh-pages를 실행시키고 **build**라는 디렉토리를 가져가 주세요" 하는 것입니다.

predeploy라는 명령어는 **Node.js**가 deploy라는 명령어가 실행되기 전에 predeploy를 먼저 실행시킵니다. 

build 폴더를 지우고 `npm run deploy`를 하면 predeploy가 build 폴더를 만들고 deploy가 실행될 것 입니다.

gh-pages는 자동으로 page를 업데이트 해줄 것입니다.