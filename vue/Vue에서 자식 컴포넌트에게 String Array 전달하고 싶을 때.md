## Vue에서 자식 컴포넌트에게 String Array 전달하고 싶을 때 

```vue
        <div class="col">
          <EasyChampion
            :greatArray="greatArray" //string[]
            :greatNameArray="greatNameArray" //string[]
            :greatRateArray="greatRateArray" //string[]
          ></EasyChampion>
        </div>
```

이게 부모 클래스 입니다. EasyChampion 이란 컴포넌트에 strign[]을 보내고 있습니다.



```
export default defineComponent({
  name: "EasyChampion",
  compatConfig: { MODE: 3 },
  props: {
    lolVersion: String,
    greatArray: Array<String>,
    greatNameArray: Array<String>,
    greatRateArray: Array<String>,
  },
  methods: {},
});
```

그리고 Array<String>으로 받았는데 에러가 납니다! typescript 조건은 맞췄는데 vue에서 랜더링이 실패합니다.



ERROR in src/components/EasyChampion.vue:25:17
TS2365: Operator '<' cannot be applied to types 'ArrayConstructor' and 'StringConstructor'.
    23 |   props: {
    24 |     lolVersion: String,
  > 25 |     greatArray: Array<String>,
  >   |                 ^^^^^^^^^^^^
  > 26 |     greatNameArray: Array as PropType<string[]>,
  > 27 |     greatRateArray: Array as PropType<string[]>,
  > 28 |   },





그래서 찾아 봤습니다. 

## Adding the type assertion `as PropType<string[]>` helps in this case:

```js
<script lang="ts">
import { PropType } from "vue"
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class MyComponent extends Vue {
  @Prop({
    type: Array as PropType<string[]>, // use PropType
    default: () => [] // use a factory function
  }) private readonly myProperty!: string[];
}
</script>
```

Array를 쓰고 as PropType<string[]>을 쓰면 해결되었습니다.

PropType은 vue에서 제공하는 Type변환 util입니다. 그래서 vue 객체에서 import를 해야합니다.



최종 코드

```ts
export default defineComponent({
  name: "EasyChampion",
  //다른 컴포넌트를 쓰고 싶을 때

  compatConfig: { MODE: 3 },
  props: {
    lolVersion: String,
    greatArray: Array as PropType<string[]>,
    greatNameArray: Array as PropType<string[]>,
    greatRateArray: Array as PropType<string[]>,
  },
  methods: {},
});
```





#### 참고

- https://stackoverflow.com/questions/63796824/vue-js-typescript-how-to-set-prop-type-to-string-array