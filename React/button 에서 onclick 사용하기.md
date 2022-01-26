## button 에서 onclick 사용하기

```react
const [filter, setFilter] = useState(0);
<button onClick={setFilter(index)} ></button>
```

아렇게 넣으면 동작하지 않습니다.`Too many re-renders. React limits the number of renders to prevent an infinite loop.`오류가 뜨죠

React는 이벤트가 발생했을 때 표현식에 정의되어 있는 함수를 자동으로 **호출**합니다. setFilter를 그대로 호출하는 것이죠. 그런데 State를 변화시키는 함수는 콜백으로 다시 렌더링을 합니다. 그러면 또 setFilter를 호출하겠죠

```react
onClick={() => setFilter(index)}
```

그러므로 함수 호출이 아닌 함수 자체를 적용해야 합니다.



[참고](https://medium.com/@su_bak/react-js-react%EC%97%90%EC%84%9C-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%A0%81%EC%9A%A9-%ED%95%98%EA%B8%B0-904015a3bb1f)

[참고2](https://anerim.tistory.com/161)