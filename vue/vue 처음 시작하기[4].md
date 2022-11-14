주소: https://www.youtube.com/watch?v=b0ImUEsqaAA&t=25s



#### 클릭 이벤트

```vue
<button @click="increaseCount">Add 1</button>
    <p>{{ counter }}</p>

  methods: {
    increaseCount() {
      this.counter += 1
    }
  }
```

@click 하면 = onclick 과 똑같은 효과 입니다.

`v-on:change`처럼 v-on을 @ 처럼 쓸 수 있습니다.

#### 변화

앞에서 선택하는거에 따라 뒤에 따라오는 select가 바뀌는 경우

```vue
<template>
  <div>
    <select name="" id="" @change="changeCity" v-model="selectedCity">
      <option value="">===도시선택===</option>
      <option
        :value="city.cityCode"
        :key="city.cityCode"
        v-for="city in cityList"
      >
        {{ city.title }}
      </option>
    </select>
    <select name="" id="">
      <option
        :value="dong.dongCode"
        :key="dong.dongCode"
        v-for="dong in selectedDongList"
      >
        {{ dong.dongTitle }}
      </option>
    </select>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      selectedCity: '',
      cityList: [
        { cityCode: '01', title: '서울' },
        { cityCode: '02', title: '부산' },
        { cityCode: '03', title: '제주' }
      ],
      dongList: [
        { cityCode: '01', dongCode: '1', dongTitle: '서울1동' },
        { cityCode: '01', dongCode: '2', dongTitle: '서울2동' },
        { cityCode: '01', dongCode: '3', dongTitle: '서울3동' },
        { cityCode: '01', dongCode: '4', dongTitle: '서울4동' },
        { cityCode: '02', dongCode: '1', dongTitle: '부산1동' },
        { cityCode: '02', dongCode: '2', dongTitle: '부산2동' },
        { cityCode: '02', dongCode: '3', dongTitle: '부산3동' },
        { cityCode: '02', dongCode: '4', dongTitle: '부산3동' },
        { cityCode: '03', dongCode: '1', dongTitle: '제주1동' },
        { cityCode: '03', dongCode: '2', dongTitle: '제주2동' },
        { cityCode: '03', dongCode: '3', dongTitle: '제주3동' }
      ],
      selectedDongList: []
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    changeCity() {
      this.selectedDongList = this.dongList.filter(
        (dong) => dong.cityCode === this.selectedCity
      )
    }
  }
}
</script>

```

selectedCity 라는 문자열에 처음에 고른 문자를 넣어줍니다. (:value="city.cityCode")

그 고유값을 가지고 dongList에 filter를 돌려서 그 아래에 있는 Object를 모두 가져와서 보여줍니다.

```vue
    <select name="" id="">
      <option
        :value="dong.dongCode"
        :key="dong.dongCode"
        v-for="dong in dongList.filter(
          (dong) => dong.cityCode === selectedCity
        )"
      >
        {{ dong.dongTitle }}
      </option>
```

사실 changed 함수를 거치지 않고 할 수 있습니다. 

데이터 바인딩의 원리로 selectdCity의 값이 바로 들어오기 때문에 바로 dongList에서 값을 찾을 수 있습니다.



```js
<select name="" id="" @change="changeCity($event)" v-model="selectedCity">
```

메서드에 $event로 event를 파라미터 형식으로 보낼 수 있습니다.

```vue
changeCity(event) {
      console.log(event.target.tagName)
    }
```

받는곳에서는 이렇게 받습니다.



#### key인식하기

```vue
    <input
      type="search"
      name=""
      id=""
      @keyup="checkEnter($event)"
      v-model="searchText"
    />
```

무언가 키를 인식하려면 keyup으로 인식합시다.

```vue
methods: {
  doSearch() {
    console.log(this.searchText)
  },
  checkEnter(event) {
    if (event.keyCode === 13) {
      this.doSearch()
    }
  }
}
```

keyCode가 13인 이유는 엔터기 값이기 때문입니다.



#### 더 쉽게

```vue
    <input
      type="search"
      name=""
      id=""
      @keyup.enter="doSearch"
      v-model="searchText"
    />
    <button @click="doSearch">조회</button>
```

@keyup.enter를 하면 enter키를 인식해줍니다. 그리고 doSearch를 실행시켜주죠.

@keyup. 속성들을 보면 다양한 것이 있습니다. delete, down(키 아래) 등등 주요키를 자동으로 설정해줘서 편합니다.

.ctrl 하면 ctrl을 누른 상태인지 까지 확인합니다.



```vue
<button type="submmit" @click.prevent="doSearch"></button>
```

event.preventDefault()가 실행된 후에 `doSearch` 메서드가 실행될 것입니다.
