## useEffect

우리는 state를 변화시킬 때마다 return의 모든 것을 다시 render했습니다. api같이 한번만 끌어오게끔 만들려면useEffect()를 사용하면됩니다.

2개의 매개변수를 가진다.

첫 번째 매개변수는 한번만 실핼된 **함수**를 넣어줍니다.

```react
import { useState, useEffect } from "react";
 
const iRunOnlyOnce = () => {
    console.log("Call the Api");
};

useEffect(iRunOnlyOnce, []);
```

이러면 `iRunOnlyOnce`는 state가 변해도 한번만 실행됩니다.





#### 그런데 input을 넣었을 때 state를 변화시키면?

```react
const [keyword, setKyeword] = useState("");


<input
        value={keyword}
        onChange={onChange}
        type="text"
        placeholder="Serch here..."
/>

const onChange = (event) => {
    setKyeword(event.target.value);
};
```

`keyword`에 값을 입력하면 `onChange()`가 동작하고 state가 변화됩니다. 그러면 입력할 때마다 페이지를 새로고칩니다. 이를 어떻게 해결할까요.





#### 코드의 특정한 부분만이 변화했을 때 원하는 코드들을 실행할 수 있는 방법

useEffect의 2번째 매개변수를 쓰면 됩니다. 빈 arrary를 써주었는데 여기에 **변화를 원하는 state**를 써주면 됩니다.

```react
useEffect(() => {
    console.log("Search for", keyword);
}, [keyword]);
```

**keyword가 변할 때마다 console.log()를 찍어라.** 만약 [keywrod]가 없이 []를 넣었다면 react는 지켜볼것이 없기 때문에 1번만 실행할 것입니다.

그렇지만 화면이 시작할 때 빈`keyword`를 가지고 console.log을 합니다.





```react
useEffect(() => {
    if (keyword !== "" && keyword.length > 5) {
      console.log("Search for", keyword);
    }
  }, [keyword]);
```

조건울 줘서 `빈 문자열`이 아니거나 `keyword의 길이가 5이상`일 때만 console.log를 찍게 하면 됩니다.

2번 째 매개변수는 **react가 지켜보는 것**입니다. 2개이상 적어주어도 되겠죠