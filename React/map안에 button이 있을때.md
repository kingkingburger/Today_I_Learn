## map안에 button이 있을때

제가 공부한 코드중 일부분 입니다.

```react
const [filter, setFilter] = useState(0);
  const list = ["전체", "BTS", "LISA", "아이폰"];

  const isMatched = (data) => {
    let word = list[filter];
    if (word === "전체") {
      word = "";
    }
    return data.channelTitle.includes(word) || data.description.includes(word);
  };

  return (
    <Layout activeMenu="explore">
      <div className={styles.tagcontainer}>
        {list.map((str, index) => (
          <button
            onClick={() => setFilter(index)}
            key={index}
            className={filter === index ? styles.clickedtag : styles.tag}
          >
            {str}
          </button>
        ))}
      </div>
```

button이 눌리면 filter의 값을 바꾸는 코드입니다.

궁금점이 든게 map은 array전부를 돌고 button입력을 기다릴까? 아니면 button입력이 먼저될까 궁금해졌서 디버그를 찍어봤습니다.

button이 입력되면 **list에 있는 것을 쭉 돈다음** setFilter()를 호출해서 State값을 수정합니다. 버튼은 onClick에서 비동기식으로 설정되어 있으니 입력을 받으면 list의 배열을 모를거라고 생각했습니다. 

생각과는 다르게 **list배열**을 한번 돌고 **filter**를 정한다음 **isMatch**를 실행했습니다.