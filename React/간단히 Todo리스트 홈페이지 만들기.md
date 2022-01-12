React에서 <form>안에 <button>이 1개만 있다면 그건 자동으로 submit 이벤트를 가지고 있습니다.

```react
setTodos((currentArray) => [todo, ...currentArray]);
```

js에서 array안에 또 array를 넣을 때 요소들이 그대로 들어가길 원한다면 Array앞에`...`을 붙혀주자



html부분에서 js를 사용하고 싶다면 `{}`를 쓰면 됩니다.





## js의 map()

리스트의 모든것들을 `map(함수)` 매개변수에 들어있는 함수에 넣습니다. 파이썬의  map과 비슷하네요





## 같은 component의 list를 render할 때 key라는 prop을 넣어야 한다.

원래 map()에 첫 번째 매개변수는 array의 값이였습니다. 두 번째 매개변수는 index입니다.

```react
{todos.map((item, index) => (
        <li key={index}>{item}</li>
))}
```

todos라는 array의 item과 index를 가져옵니다. list의 key는 고유해야하기 때문에 2번재 index를 넣어줍니다.







전체코드

```
import Button from "./Button";
import styles from "./App.module.css";
import { useState, useEffect } from "react";

function App() {
  const [todo, setTodo] = useState("");
  const [todos, setTodos] = useState([]);
  const onChange = (event) => setTodo(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    if (todo === "") {
      return;
    }
    setTodos((currentArray) => [todo, ...currentArray]);
    setTodo("");
  };
  return (
    <div>
      <h1>My To Dos ({todos.length})</h1>
      <form onSubmit={onSubmit}>
        <input
          onChange={onChange}
          value={todo}
          type="text"
          placeholder="Write your to do..."
        ></input>
        <button>Add To Do</button>
      </form>
      <hr />
      {todos.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </div>
  );
}

export default App;

```

