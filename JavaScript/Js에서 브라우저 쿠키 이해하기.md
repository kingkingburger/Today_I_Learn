## Js에서 브라우저 쿠키 이해하기

로그인 기능을 구현할 때 필수로 알아야할 계념입니다.



## 요청의 한가지 단점

누가 보냈는지 모릅니다.(ip주소와 브라우저 정보정도만)그래서 로그인을 구현하면 됩니다. 그 요청이 누군지 알아내야 합니다.그 때 필요한게 쿠키와 세션입니다.



### 쿠키: 키=값의 쌍입니다.

- 매 요청마다 서버에 쿠키를 동봉해서 보냅니다.
- 서버는 쿠키를 읽어 누구인지 파악합니다.

![Untitled](https://user-images.githubusercontent.com/65094518/217521563-17a0612a-457a-418d-a76e-f0823da4b703.png)

처음에는 서버가 쿠키를 주고 브라우저가 저장하고 있게됩니다. 그 후에 요청을 보낼 때 마다 쿠키를 동봉합니다.



### 쿠키를 서버에서 어떻게 보내줄까?

쿠키를 넣어봅시다.

- writeHead: 요청 헤더에 입력하는 메서드
- Set-Cookie: 브라우저에게 쿠키를 설정하라고 명령

```jsx
const parseCookies = (cookie = "") =>
  cookie
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, [k, v]) => {
      acc[k.trim()] = decodeURIComponent(v);
      return acc;
    }, {});

http
  .createServer(async (req, res) => {
    const cookies = parseCookies(req.headers.cookie); // { mycookie: 'test' }
    // 주소가 /login으로 시작하는 경우
    if (req.url.startsWith("/login")) {
      const url = new URL(req.url, "http://localhost:8084");
      const name = url.searchParams.get("name");
      const expires = new Date();
      // 쿠키 유효 시간을 현재시간 + 5분으로 설정
      expires.setMinutes(expires.getMinutes() + 5);
      res.writeHead(302, {
        Location: "/",
        "Set-Cookie": `name=${encodeURIComponent(
          name
        )}; Expires=${expires.toGMTString()}; HttpOnly; Path=/`,
      });
      res.end();
      // name이라는 쿠키가 있는 경우
    } else if (cookies.name) {
      res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
      res.end(`${cookies.name}님 안녕하세요`);
    } else {
      try {
        const data = await fs.readFile(path.join(__dirname, "cookie2.html"));
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        res.end(data);
      } catch (err) {
        res.writeHead(500, { "Content-Type": "text/plain; charset=utf-8" });
        res.end(err.message);
      }
    }
  })
  .listen(8084, () => {
    console.log("8084번 포트에서 서버 대기 중입니다!");
  });
```

/login 이라는 url 시작이 들어오면  name이라는 params가 있는지 확인합니다. 그리고 writeHead()로 

쿠키넣는 작업을 시작합니다.

- Location: '/' => 요청이 끝나면 `/` 주소로 리다이렉트 시켜라!
- "Set-Cookie" => 브라우저에게 응답쿠키를 넣어준다.
- name=${encodeURIComponent(name)}; => name은 한글이 들어올 수 있으니 encodeURIComponent()를 써서 넣어줍니다. template literald을 벗기면 이상한 문자가 들어있게 됩니다. 왜냐하면 인코딩이 됬기 때문입니다.
- Expires => Expires를 안주면 쿠키는 세션쿠키가 됩니다. 세션쿠기가 되면 브라우저가 끄는 순간 사라집니다. 브라우저가 꺼지기 전에 사용자의 사용시간 스톱워치를 재는것과 비슷하겠네요.

- HttpOnly ⇒ js로 쿠키에 접근하지 못하게!(해킹 대비)
- Path=/ ⇒ / 아래 모든 요청은 쿠키가 모두 유효하다!

![Untitled 1](https://user-images.githubusercontent.com/65094518/217521553-80ea6569-ef0d-4d2a-955f-5bf2e3bd2879.png)

![Untitled 2](https://user-images.githubusercontent.com/65094518/217521558-08a93665-d00f-4e0b-bbf8-90e2b6cbaae0.png)

세션은 브라우저를 끄기 전까지 계속 가지고 있습니다.

![Untitled 3](https://user-images.githubusercontent.com/65094518/217521559-a251bc41-0004-473c-83b3-7c195b0e9666.png)

Request 요청보낼 때 Cookie도 같이 보내줍니다.

8080번 포트에서 서버에서 대기중입니다.
/ undefined
/ mycookie=test
/favicon.ico mycookie=test
/ mycookie=test
/favicon.ico mycookie=test

로그를 보면 favicon이라는게 있는데 브라우저에서 탭에 떠있는 아이콘을 보내주는 것입니다.



### form 에서 get요청을 했을 때

data는 string으로 들어가게 됩니다.

```html
<form action="/login">
  <input id="name" name="name" placeholder="이름을 입력하세요" />
  <button id="login">로그인</button>
</form>
```

name은 **Request URL:**  http://localhost:8084/login?name=%EC%9B%90%EB%AF%BC%ED%98%B8

이런직으로 뒤에 붙게 됩니다.
