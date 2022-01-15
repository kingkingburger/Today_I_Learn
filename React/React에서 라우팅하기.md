## React에서 라우팅하기

```react
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Detail from "./routes/Detail";
import Home from "./routes/Home";
function App() {
  return (
    <Router>
      <Switch>
        <Route path="/movie">
          <Detail />
        </Route>
        <Route path="/">
          <Home />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
```

BrowserRouter는 url로 홈페이지를 옮겨다닐 수 있게합니다.

**Switch컴포넌트**는 한번에 하나의 Route만 렌더링 하기 위함입니다. React Router는 2개의 Route를 한버에 렌더링 할 수 있거든요.

모든 컴포넌트는 url을 감시하고 있습니다. url을 감지하고 어떤것을 보여줄지 정합니다.





## 제목을 클릭하면 다른 페이지로 이동하기

**Link**라는 컴포넌트를 사용하면 됩니다.

```react
<Link to="/movie">{title}</Link>
```

`/movie`페이지로 옮겨주세요 하는것입니다. 이러면 페이지 전체가 새로고침 없이 url이 "/movie"로 바뀌고 **Route**가 url이 **변함을 감지**하면 자신이 보여줘야한 **컴포넌트**를 랜더링 합니다.