## ✅ commonjs vs Es module 뭐가 더 좋을까?

다른 코드들을 살펴보다가 import 하는 방식이 차이가난다는것을 발견했습니다.

예를들면 path 모듈같은 경우입니다. `path` 모듈은 Node.js에 내장되어 있어 있기 때문에 별도의 라이브러리 설치없이 바로 불러와서 사용할 수 있습니다.

CommonJS 모듈 시스템을 사용하는 프로젝트에서는 `require` 키워드로 불러오고, ES 모듈 시스템을 사용하는 프로젝트에서는 `import` 키워드를 사용할 수 있습니다.

```js
// CommonJS Modules
const path = require("path");
// ES Modules
import path from "path";
```

위 설명에서 프로젝트별로 **CommonJs 모듈 시스템**과 **Es모듈 시스템** 2가지를 말하고 있습니다.

브라우저 JS 환경에서, JS 모듈은 `import`, `export` 에 따라 EMCA Script modules(또는 ES modules)를 가져오기, 내보내기를 합니다.

ES module 형태는 재사용을 위한 JS 코드 패키징의 공식 표준 형식이고 대부분의 최신 웹 브라우저는 기본적으로 모듈을 지원합니다.

그러나, Node.js는 기본적으로 CommonJS 모듈을 지원합니다.
CommonJS 모듈은 `require()`를 사용해서 가져오고 변수와 함수를 내보낼 때는 `module.exports`를 사용합니다.



과연 이 차이는 무엇일까요??

#### CommonJS

```
const module = require('어쩌구');
const { func } = require('어쩌구');

module.exports = '어쩌구'; // default exports
module.exports.func = () => {}; // named exports
```

####  ES Modules

```
import a from '어쩌구';
import {func} from '어쩌구';

export const a = '어쩌구'; // default exports
export default func = () => {}; // named exports
```

다음과 같은 Node.js 프로젝트가 있다고 합시다.

```null
my-node-library
├── lib/
│   ├── browser-lib.js (iife format)
│   ├── module-a.js  (commonjs format)
│   ├── module-a.mjs  (es6 module format)
│   └── private/
│       ├── module-b.js
│       └── module-b.mjs
├── package.json
└── …
```

`package.json` 내부에서, 우리는 `exports`를 사용해서 public 모듈(module-a)을 두가지의 다른 모듈 형태로 내보내고 private 모듈(module-b)에 대한 접근을 제한할 수 있습니다.

```json
// package.json
{
  "name": "my-library",         
  "exports": {
    ".": {
        "browser": {
          "default": "./lib/browser-module.js"
        }
    },
    "module-a": {
        "import": "./lib/module-a.mjs" 
        "require": "./lib/module-a.js"
    }
  }
}
```

`my-library`패키지에 대한 다음과 같은 정보가 주어지면, 우리는 이제 다음과 같이 지원되는 모든 곳에서 사용할 수 있습니다.

```js
// For CommonJS 
const moduleA = require('my-library/module-a')

// For ES6 Module
import moduleA from 'my-library/module-a'

// This will not work
const moduleA = require('my-library/lib/module-a')
import moduleA from 'my-awesome-lib/lib/public-module-a'
const moduleB = require('my-library/private/module-b')
import moduleB from 'my-library/private/module-b'
```

`exports`경로 때문에 절대 경로를 지정하지 않고 public 모듈을 import(`reuire()`)할 수 있습니다.

`.js`와 `.mjs`에 대한 경로를 포함시켜서 비호환성 문제를 해결할 수 있습니다.
우리는 private 모듈에 접근 제한을 하면서 브라우저와 Node.js와 같은 다른 환경에 대해 패키지 모듈을 매핑할 수 있습니다.

### CommonJS 는  module imports를 유연하게 제공합니다.

ES module에서, import는 파일의 맨 처음에서만 호출되어 사용할 수 있습니다. 어디서 호출하든 파일 맨 처음으로 자동으로 옮겨지거나 에러가 뜹니다.

반면에, `require()`를 함수로 사용하면 런타임때 구문 분석이 됩니다.결과적으로 `require()`는 코드 어디에서든 호출 할 수 있습니다. 이를 사용해서 if문,조건부 루프, 함수에서 조건적으로 또는 동적으로 모듈을 불러올 수 있습니다.

예를 들어, 다음과 같이 조건문에서 `require()`를 사용할 수 있습니다.

```js
if(user.length > 0){
   const userDetails = require(‘./userDetails.js’);
  // Do something ..
}
```

### CommonJS는 동기적으로 모듈을 불러오고 ES modules은 비동기

`require()`사용의 제한 중 하나는 동기적으로 모듈을 불러온다는 것이다. 이는 모듈이 불러와지고 실행되는게 각각(하나씩) 실행된다는 뜻이다.

짐작할 수 있듯이, 수백개의 모듈이 있는 대규모 어플리케이션의 경우에 몇가지 성능 문제를 발생할 수 있습니다. 이런 경우 `import`가 비동기 동작에 근거해서 `require()` 보다 성능이 좋을 수 있습니다.

그러나, `require()`의 동기적인 특성은 몇개의 모듈을 쓰는 작은 어플리케이션에서는 큰 문제가 안될것이다.



#### 출처

- https://velog.io/@tenacious_mzzz/Node.JS%EC%97%90%EC%84%9C-CommonJS-vs-ES-modules
- https://blog.logrocket.com/commonjs-vs-es-modules-node-js/