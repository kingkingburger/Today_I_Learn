## fetch

fetch("url")을 넣으면 요청을 보내는거 같습니다.

response을 fetch().then()으로 다룰 수 있습니다.

```react
useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
      .then((response) => response.json())
      .then((json) => {
        setCoins(json);
        setLoading(false);
      });
}, []);
```

then()안에 () => {} 형태로 람다 함수를 집어넣을 수 있는거 같습니다.





```react
 <ul>
        {coins.map((coin) => (
          <li>
            {coin.name}({coin.symbol}): {coin.quotes.USD.price}
          </li>
        ))}
 </ul>
```

coins라는 array를 map함수로 하나씩 살펴보려 합니다. 첫 번째 매개변수는 array의 요소들로 coin으로 이름을 정했습니다. coin안에는 name, symbol, quotes... 등등이 있습니다.



```react
const [coins, setCoins] = useState([]);
<h1>The Coins! ({coins.length})</h1>
```

만약 coins의 초기값이 useState()라면 undefined가 될것입니다. 그렇게 되면 undefined는 길이가 없으므로 에러가 나게되겠죠. 그래서 초기값 빈 배열을 넣는 것입니다. 





## async, await

이건 then과 같은 것입니다.

```react
useEffect(() => {
    fetch(
      `https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`
    )
      .then((response) => response.json())
      .then((json) => {
        setMovies(json.data.movies);
        setLoading(flase);
      });
  }, []);
```

처음 사용할 때는 이렇게 했습니다. fetch를 하고 fetch가 끝나면 then으로 response를 받아와서 json으로 변환작업을 했지요



```react
const getMovies = async () => {
    const response = await fetch(
      `https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`
    );
    const json = await response.jsoin();
    setMovies(json.data.movies);
    setLoading(false);
  };
 useEffect(() => {
   getMovies();
 }, []);
```

이거를 async, await로 바꾸면 async()가 들어오면 await가 순서대로 동작하는 방식같습니다.





## map을 사용할 때 

```react
<div>
    {movies.map((movie) => (
        <div key={movie.id}>
            <h2>{movie.title}</h2>
            <p>{movie.summary}</p>
            <ul>
                {movie.genres.map((g) => (
                    <li key={g}>{g}</li>
                ))}
            </ul>
        </div>
    ))}
</div>
```

map의 한 요소를 꺼낼 때 고유한 **key**값이 필요합니다. 왜냐하면 movie들 중에 어떤 movie를 가져와야하는지 모르기 때문입니다. 그래서 요소를 구분할 수 있는 **유니크**한 값이 필요합니다.

ex) movies중에 movie.id가 1,2,3,4,5,....100까지 있다고 하면 5번째를 원하는데 어떻게 접근해야하는지 모릅니다. 이  때 key가 필요합니다. 

key는 숫자가 아니더라도 고유한 값이면 다 됩니다.