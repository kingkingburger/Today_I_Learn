## Cleanup function

컴포넌트가 없어질 때 분석 결과를 보내고 싶어할 때 분석 api를 보내려면 컴포넌트가 사라질 때 return문을 넣어주면 됩니다.

```react
function Hello() {
  function destoryFn() {
    console.log("bye");
  }
  function effectFn() {
    console.log("created:");
    return destoryFn;
  }
  useEffect(effectFn, []);
  return <h1>Hello</h1>;
}
```

**useEffect**는 []로 지켜보는애가 없으니 한번만 실행될 것입니다. 그러면 **effectFn**이 실행이 될것이고 컴포넌트가 사라질 때 **destoryFn**을 **return**할 것(**실행**)입니다. return되는 함수를 `Cleanup 함수`라고 합니다.

deps([])가 비어있으면 자동으로 컴포넌트가 파괴될 때 cleanup함수가 실행되는데 그 과정이 리렌더링으로 useEffect함수가 실행되고 클린업하면서 이전에 있던 이펙트인 console.log(“created : )가 삭제되고 새로운 이펙트 함수인 return함수가 실행되기 때문이다.

리엑트가 컴포넌트를 띄우는 순서는 `리렌더링 -> 이전 이펙트 클린업 -> 이펙트 실행`

**클린업**: 새로 렌더링한 이후 실행된다.(불확실한 정보 => 초기값이 return null로 되어있다 생각하자)
\- 이 때 렌더링은 값이 변하여 새로운 것을 그려주거나, 컴포넌트를 없애는 경우가 있다.
\- useEffect는 리렌더링 이후 클린업을 마치고 실행된다.

ex) **디펜던시**가 counter 일 경우(최초 counter는 0)
화면에 0이 렌더링 되어있는 상황에 counter가 1로 값이 바뀌면 "일단" 리렌더링을 한다.
이후에 0을 정리(클린업)한다, 그리고 useEffect가 실행된다.

ex) **디펜던시**가 없을 경우
화면에 0이 렌더링 되어있고, 해당 컴포넌트를 지울 경우 일단 0을 지운다(**리렌더링**).
이후 정리(클린업)한다.
\* 이 때 컴포넌트가 지워졌고 실행할 useEffect가 없기에 정리(클린업)만하고 끝난다.
