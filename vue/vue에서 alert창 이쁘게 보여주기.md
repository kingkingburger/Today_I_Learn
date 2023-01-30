## vue에서 alert창 이쁘게 보여주기

바로 "sweetalert2" 입니다.

```sh
npm i vue-sweetalert2
```

위 명령어로 모듈을 다운받으 신다음 vue의 main.js에 설정을 해야 합니다.



#### Vue2에서는

```sh
// main.js
import Vue from 'vue';
import VueSweetalert2 from 'vue-sweetalert2';

// If you don't need the styles, do not connect
import 'sweetalert2/dist/sweetalert2.min.css';

Vue.use(VueSweetalert2);
```



#### Vue3에서는

```js
// main.js
import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

const app = createApp(App)

app.use(VueSweetalert2);

app.mount('#app');
```



#### npm 공식문서

- https://www.npmjs.com/package/vue-sweetalert2





이렇게 설정했으면 vueSweetalert를 쓸 수 있게됩니다. 그다음 사람들이 만들어놓은 sweetaler를 쓰기 위해서 https://sweetalert2.github.io/ 에들어갑니다. 다양한 사람들이 멋지게 만들어 놓은것들이 있습니다.

![image](https://user-images.githubusercontent.com/65094518/205477552-6c8bcbdd-ec72-47de-9dd1-b6dd6d04f511.png)

아래로 내려보면 Try me! 보라색 버튼이 있습니다. 오른쪽 코드를 실행하는 버트입니다. 눌러보면

![image](https://user-images.githubusercontent.com/65094518/205477576-a9e548fc-511f-4872-87df-a6c060341d5b.png)

어떤 알람창인지 알 수 있습니다.

save, don'tsave 하는것만 아니라 ![image](https://user-images.githubusercontent.com/65094518/205477608-aa4d9573-f42a-43d6-b47e-4dea639d5912.png)

![image](https://user-images.githubusercontent.com/65094518/205477655-d4df7dab-9087-4940-a551-42b9a82150cd.png)

경고창, 확인창, 입력창 등등... 다양한 경고 팝업창이 존재합니다. 해당주소에서 코드를 복사한 후 내가 만들고 싶은 로직을 집어넣으면 됩니다.



#### Vue에서 methods에 집어넣을때

기존 예시문

```js
Swal.fire({
  title: 'Do you want to save the changes?',
  showDenyButton: true,
  showCancelButton: true,
  confirmButtonText: 'Save',
  denyButtonText: `Don't save`,
}).then((result) => {
  /* Read more about isConfirmed, isDenied below */
  if (result.isConfirmed) {
    Swal.fire('Saved!', '', 'success')
  } else if (result.isDenied) {
    Swal.fire('Changes are not saved', '', 'info')
  }
})
```

🟥 Vue가 Swal객체를 인식하지 못합니다. Vue안에 swal객체를 인식시키려면 **this.$swal**을 붙여야 합니다.

```js
//Swal 이라고 쓰지말고 vue에서는 this.$ 를 붙여야 한다.
this.$swal.fire({
  title: 'Do you want to save the changes?',
  showDenyButton: true,
  showCancelButton: true,
  confirmButtonText: 'Save',
  denyButtonText: `Don't save`,
}).then((result) => {
  /* Read more about isConfirmed, isDenied below */
  if (result.isConfirmed) {
    this.$swal.fire('Saved!', '', 'success')
  } else if (result.isDenied) {
    this.$swal.fire('Changes are not saved', '', 'info')
  }
})
```

vue 안에 들어온 Swal객체를 인식하지 못해서 그런거같습니다. 각각 예제마다 주석으로 간단한 설명이 되어있스빈다.

**isConfirmed** (=성공하였을 때)는 save를 눌렀을 때 true가 되는거 같습니다. if문안에 로직을 넣어서 save가 눌렸을 때 동작할 로직을 넣으면 됩니다.

반대로 **isDenied**는 cancel을 눌렀을 때 동작하는 로직을 넣으면 될것입니다.

