## URL 다루기

**보내줄 때** 

```react
<Link to={`/movie/${id}`}>{title}</Link>
```

/movie/1234 형태로 보내지게 됩니다.

백틱(`)을 보면 ${}(플레이스 홀더)를 사용해 변수를 넣고 문자열을 사용합니다. ES6부터 사용됐다고 하네요 더 변리하게 문자열을 쓰기 위해 만들어진거 같습니다.



**받는 쪽에서는** 

```react
<Route path="/movie/:id">
          <Detail />
</Route>
```

/movie/123~ 형태로 들어오는 것은 <Detail/> 컴포넌트를 수행시킵니다.

그럼 이제 Detail컴포넌트는 id를 어떻게 파악할까요?



```react
function Detail() {
  const { id } = useParams();
  console.log(id);
  return <h1>Detail</h1>;
}
```

`uesParams`라는 것을 react가 제공해주고 있습니다. 이건 url을 Object로 끌고 오는데요 변수에 {}를 붙힌 이유는 바로 Object안에 침투하기 위함입니다.

ex) const x = useParams()     결과: { id : 385959 }
      const {x} = useparams()   결과:  385959

