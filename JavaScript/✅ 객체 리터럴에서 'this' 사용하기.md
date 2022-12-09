## ✅ **객체 리터럴에서 'this' 사용하기**

함수 `makeUser`는 객체를 반환합니다.

이 객체의 `ref`에 접근하면 어떤 결과가 발생하고, 그 이유는 뭘까요?

```javascript
function makeUser() {
  return {
    name: "John",
    ref: this
  };
};

let user = makeUser();

alert( user.ref.name ); // 결과가 어떻게 될까요?
```



**에러**가 발생합니다.

직접 실행해 봅시다.

```javascript
function makeUser() {
  return {
    name: "John",
    ref: this
  };
};

let user = makeUser();

alert( user.ref.name ); // Error: Cannot read property 'name' of undefined
```

에러가 발생하는 이유는 `this` 값을 설정할 땐 객체 정의가 사용되지 않기 때문입니다. `this` 값은 호출 시점에 결정됩니다.

위 코드에서 `makeUser()` 내 `this`는 `undefined`가 됩니다. 메서드로써 호출된 게 아니라 함수로써 호출되었기 때문입니다.

`this` 값은 전체 함수가 됩니다. 코드 블록과 객체 리터럴은 여기에 영향을 주지 않습니다.

따라서 `ref: this`는 함수의 현재 `this` 값을 가져옵니다.

`this`의 값이 `undefined`가 되게 함수를 다시 작성하면 다음과 같습니다.

```javascript
function makeUser(){
  return this; // 이번엔 객체 리터럴을 사용하지 않았습니다.
}

alert( makeUser().name ); // Error: Cannot read property 'name' of undefined
```

보시다시피 `alert( makeUser().name )`와 위쪽에서 살펴본 `alert( user.ref.name )`의 결과가 같은 것을 확인할 수 있습니다.

에러가 발생하지 않게 하려면 코드를 다음과 같이 수정하면 됩니다.

```javascript
function makeUser() {
  return {
    name: "John",
    ref() {
      return this;
    }
  };
};

let user = makeUser();

alert( user.ref().name ); // John
```

이렇게 하면 `user.ref()`가 메서드가 되고 `this`는 `.` 앞의 객체가 되기 때문에 에러가 발생하지 않습니다.





#### 올라가기(`up`)와 내려가기(`down`) 메서드를 제공하는 객체 `ladder`가 있습니다.

```javascript
let ladder = {
  step: 0,
  up() {
    this.step++;
  },
  down() {
    this.step--;
  },
  showStep: function() { // 사다리에서 몇 번째 단에 올라와 있는지 보여줌
    alert( this.step );
  }
};
```

메서드를 연이어 호출하고자 한다면 아래와 같이 코드를 작성할 수 있습니다.

```javascript
ladder.up();
ladder.up();
ladder.down();
ladder.showStep(); // 1
```

`up`, `down`, `showStep`을 수정해 아래처럼 메서드 호출 체이닝이 가능하도록 해봅시다.

```javascript
ladder.up().up().down().showStep(); // 1
```

참고로 이런 방식은 자바스크립트 라이브러리에서 널리 사용됩니다.

메서드를 호출할 때마다 객체 자신을 반환하게 하면 됩니다.

```javascript
let ladder = {
  step: 0,
  up() {
    this.step++;
    return this;
  },
  down() {
    this.step--;
    return this;
  },
  showStep() {
    alert( this.step );
    return this;
  }
}

ladder.up().up().down().up().down().showStep(); // 1
```

체이닝이 길어질 땐 메서드 호출을 별도의 줄에 작성하면 가독성이 좋아집니다.

```javascript
ladder
  .up()
  .up()
  .down()
  .up()
  .down()
  .showStep(); // 1
```

