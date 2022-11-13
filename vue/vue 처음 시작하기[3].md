주소: https://www.youtube.com/watch?v=b0ImUEsqaAA&t=25s

#### views와 Component

views는 화면 전체를 의미합니다. 이름을 붙힐때도 뒤에 `View`라고 붙여야 합니다.

Component는 화면의 구성요소들입니다. 



#### vue 에서 함수 만들때

function 안붙히고 그냥 `[이름]()` 이렇게 합니다.



#### 컴포넌트 만들기

html 들을 `template` 안에 들어가면 됩니다.

js코드들은 `script`안에 넣으면 되빈다.

컴포넌트 스코프에서만 쓰는 css들이 있다면 `style scoped` 태그 안에 넣을 수 있습니다.



#### template 안에서

vue 안에서 template 안에 있는 태그들은 최상의 태그 1개가 필요 합니다.

같은 레벨로 태그가 많이 있으면 안되고 **최상위 테그로 1개** 묶어야 합니다.



#### 문자열 데이터 바인딩

{{}} 안에 script 변수를 넣으면 값이 들어갑니다.



#### webpackChnkName 같은거 쓰면

같은 컴포넌트를 브라우저 캐시에 올릴 수 있습니다.



#### Html 바인딩 할 때 

vue 에서는 디랙티브가 `v-`로 시작합니다.

`v-html`을 하면 html 태그가 들어가면 string으로 인식되는게 아니라 html로 인식됩니다.

여기서 느낀건데 data() {} 컴포넌트의 이름이 고정되어있는거 같습니다. data1로 바꿔봤는데 data를 인식을 못하네요.



#### 데이터 양방향 바인딩

`v-model`이라고 하면 양방향 데이터 바인딩이 됩니다.

사용자가 화면에서 바꾸면 js안에 객체도 바뀌게 됩니다.

onclick에서 on 데신 `@` 를 쓰면 됩니다.

`v-model.number` 를  써서 데이터 바인딩 하면 자동으로 number로 받아옵니다.





#### 호출할 함수 등록하기

method란 곳에 등록하면 됩니다.



#### select로 데이터 양방향 바인딩

select로도 데이터를 주고 받고 할 수 있습니다.

```vue
    <select name="" id="" v-model="selectedCity">
      <option value=""></option>
      <option value="02">서울</option>
      <option value="051">부산</option>
      <option value="064">제주</option>
    </select>
```

v-model을 변수로 주면 js안에서 selectedCity라는 변수에 값이 바뀔 것 입니다.



#### [v-model] 체크박스(checkbox) 데이터 양방향 바인딩

```vue
  <div>
    <div>
      <input type="checkbox" name="" id="html" value="html" v-model="favoriteLang" />
      <label for="html">html</label>
    </div>
    <div>
      <input type="checkbox" name="" id="css" value="css" v-model="favoriteLang" />
      <label for="css">css</label>
    </div>
    <div>
      <input type="checkbox" name="" id="js" value="js" v-model="favoriteLang" />
      <label for="js">js</label>
    </div>
    <div>선택한 지역: {{ favoriteLang }}</div>
  </div>
```

여기서 checkbox의 이름을 같게하면 하나의 그룹으로 묶을 수 있습니다.

체크박스로 값을 선택하는건 배열로 선언해야 합니다. 왜냐하면 값이 많이 들어올 수 있으니깐요.

체크박스에 있는 value 값은 바뀌지 않습니다. html value 속성과 양방향 데이터 바인딩이 되는게 아닙니다. checked 속성과 양방향 바인딩이 되는 것입니다.



#### 라디오(radio) 데이터 양방향 바인딩

```vue
  <div>
    <div>
      <input
        type="radio"
        name=""
        id="html"
        value="html"
        v-model="favoriteLang"
      />
      <label for="html">html</label>
    </div>
    <div>
      <input type="radio" name="" id="css" value="css" v-model="favoriteLang" />
      <label for="css">css</label>
    </div>
    <div>
      <input type="radio" name="" id="js" value="js" v-model="favoriteLang" />
      <label for="js">js</label>
    </div>
    <div>선택한 지역: {{ favoriteLang }}</div>
  </div>
```

체크박스는 1개만 선택이 가능합니다. 그래서 favoriteLang 변수는 배열이 아니라 변수(string)으로 선언되어야 합니다.



#### [v-bind] html 속성에 데이터 양방향 바인딩

```vue
v-bind:value="userId"
```

v-bind:value하면 value 태그에 userId를 단방향으로 묶는다는 뜻입니다. 이러면 js -> html 으로 밖에 전달이 안됩니다. 사용자가 바꿀 수 없는 값에 넣으면 됩니다.

v-bind는 생략이 가능합니다. `:value` 와 `v-bind:value` 는 똑같은 의미 입니다.

```js
    <img :src="imgSrc" alt="" />
```

imgSrc로 img도 데이터 바인딩이 가능해집니다.



#### 반드시 입력되야 하는 상황

```
    <input type="search" name="" id="" v-model="txt1" />
    <button :disabled="txt1 === ''">조회</button>
```

txt1 값이 있다면 disable===false가 됩니다.



####  [v-for]데이터 List로 보여주기

```vue
      cities: [
        { title: '서울', code: '02' },
        { title: '부산', code: '03' },
        { title: '제주', code: '04' }
      ]
```

이런식으로 cities 배열이 있습니다.

```vue
      <select name="" id="">
        <option value="" :key="city.code" v-for="city in cities"></option>
      </select>
```

v-for을 사용하면 for문 처럼 동작하게 됩니다. 

이 때 key에는 배열에 **유일한 값**이 들어가야 합니다.

```vue
<tr :key="i" v-for="(city, i) in cities"></tr>
```

이 때 리스트에 고유한 번호가 없다 => for문 돌때 index를 지정해줍니다. 

선언했을 때 안쓰면 빨간줄 그입니다.



#### [:class] 클래스 데이터 데이터 바인딩

```css
<style scoped>
.active {
  background-color: aqua;
  font-weight: bold;
}

.text-red {
  color: red;
}
</style>
```



```vue
<template>
  <div>
    <div :class="{ 'text-red': true }">클래스 바인딩</div>
  </div>
</template>
```

클래스는 object로 들어가게 됩니다. 하나에 태그에 여러개의 클래스를 넣을 수 있습니다.

만약 false면 style이 안들어갑니다. 만약 css 이름에 `-`가 들어가게 된다면 `'[태그이름]'` 로 감싸야 인식합니다.

```vue
  <div>
    <div :class="{ 'text-red': true, active: true }">클래스 바인딩</div>
  </div>
```

아니면 `'[태그명]'`홑따옴표로 안감싸도 됩니다.

```vue
<template>
  <div>
    <div :class="{ 'text-red': isActive, active: hasError }">클래스 바인딩</div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      isActive: false,
      hasError: false
    }
  },
```

이렇게 속성값을 js로 두고 hasError 가 났을 때 함수로 true로 만들면 css가 적용되게 끔 만들 수 있습니다.



#### 스타일 바인딩

```vue
  <div>
    <div :style="style1">스타일 바인딩: 글씨는 red, 폰트 크기: 30px</div>
  </div>
```

```vue
 style1: { color: 'red', fontSize: '30px' }
```

대문자가 `-` 문자로 바뀝니다.

Object 형태로 데이터 스타일을 넣을 수 있습니다.

```vue
    <button @click="style1.color = 'blue'">클릭</button>
```

style1 Object를 버튼 클릭시 바꾸게끔 할 수 있습니다.