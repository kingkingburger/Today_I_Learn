## React bootstrap 사용해보기

1. `npm install react-bootstrap bootstrap`으로 패키지를 설치합니다.
2. 최상위 루트 파일에 `import 'bootstrap/dist/css/bootstrap.min.css';`을 넣어줍니다. 추가하지 않는다면 부트스트랩의 스타일은 적용되지 않습니다.

[react-bootstrap](https://react-bootstrap.netlify.app/components/navbar/)사이트에서 원하는 기능을 검색합니다. 만약 Button을 가져오고 싶다 하면

```react
import Button from 'react-bootstrap/Button';
// or 
import { Button } from 'source/_posts/style/react-bootstrap';
```

을 코드 위에 넣어주고

```react
import { Button, ButtonToolbar } from 'react-bootstrap';

<ButtonToolbar>
    <Button variant="primary">Primary</Button>
    <Button variant="secondary">Secondary</Button>
    <Button variant="success">Success</Button>
    <Button variant="warning">Warning</Button>
    <Button variant="danger">Danger</Button>
    <Button variant="info">Info</Button>
    <Button variant="light">Light</Button>
    <Button variant="dark">Dark</Button>
    <Button variant="link">Link</Button>
</ButtonToolbar>
```

홈페이지를 보면서 어떤 속성이 파악하고 버튼을 사용하면 됩니다.



