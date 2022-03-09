## React 시계 만들어보기

```react
  const [time, setTime] = useState(moment());

  useEffect(() => {
    const id = setInterval(() => {
      setTime(moment());
    }, 1000);
    return () => clearInterval(id);
  }, []);
  
  return ( <div>남은 시간:{time.format("HH-mm-ss")}</div> )
```

useEffect(첫 번째, 두 번째)를 사용하면  두 번재 매개변수가 변할 때마다 useEffect가 실행이 됩니다.

아무것도 안넣어줬으니 프로그램이 실행될 때 한번만 실행됩니다.

여기서 setInterval과 clearInterval을 잘 모르겠습니다.

JavaScript 에서 setInterval 함수는 기준 간격을 두고 주기적으로 이벤트를 발생 시키고 싶을 때 사용합니다.

그리고 중지하고 싶을 때는 clearInterval 함수를 사용합니다.

clearInterval 함수의 매개변수는 setInterval 함수가 리턴해주는 값을 사용합니다. 리턴받은 timer 값을 매개변수로 보내주면 됩니다.



일단 

```react
  const [time, setTime] = useState(moment());

    const id = setInterval(() => {
    	setTime(moment());
    }, 1000);
  
  return ( <div>남은 시간:{time.format("HH-mm-ss")}</div> )
```

이렇게 해도 실행이 되긴 됩니다. 하지만 useState 특성상 set()이 동작하면 화면 전체를 리랜더링 하는 규칙이 있습니다. 그럼 time만 리랜더링이 되는게 아니라 다른 거까지 리랜더링이 되니 성능이 저하될 것 입니다.

임의의 변수를 만들어서 `setInterval()`을 저장해두고 `useEffect()`가 이 변수를 참조하도록 하면..? 역시나 렌더링 될 때마다 새로운 `setInterval()`을 만드는 건 마찬가지
👉 `useEffect()`를 사용해서 처음 마운트되었을 때 한 번만 `setInterval()`을 생성하도록 한다.

`useEffect`에 전달된 함수는 화면에 렌더링이 완료된 후에 수행되게 될 것입니다. 

마운트 = 트리에 삽입된 직후



가장 어려운 부분이 `useEffect`가 return 하는 부분이였습니다. [공식 문서](https://ko.reactjs.org/docs/hooks-reference.html#useeffect)를 보니 effect 이후에 어떻게 정리(clean-up)할 것인지 표시합니다.

 `useEffect`로 전달된 함수는 정리(clean-up) 함수를 반환할 수 있습니다. 컴포넌트가 (그냥 일반적으로 수행하는 것처럼) 여러 번 렌더링 된다면 **다음 effect가 수행되기 전에 이전 effect는 정리됩니다**. 

즉 Interval이 한번만 수행이 되고 화면을 리랜더링 하는 setTime 함수를 interval 안에 끼워놓자. 그리고 시간 측정이 끝나면 interval을 초기과 시켜봅시다.



## 컴포넌트 생명주기

DOM에 렌더링 되는 것을 마운트라고 합니다

```
  componentDidMount() {
  	//마운트 될 때 수행되는 것
  }

  componentWillUnmount() {
  	//언마운트 될 때 수행되는 것
  }
```

```
useEffect(() => {
  (컴포넌트가 생길 때 수행 작업);
  return {
      (컴포넌트가 사라질 때 수행 작업);
  }
}, [의존성])

useEffect(() => {
    console.log('user 값이 설정됨');
    console.log(user);
    return() => {
    console.log('user 값이 바뀌기 전');
    console.log(user);
  }
},[user])
```

참고 : https://handhand.tistory.com/32

https://velog.io/@chez_bono/%EB%A6%AC%EC%95%A1%ED%8A%B8-%ED%83%80%EC%9D%B4%EB%A8%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0