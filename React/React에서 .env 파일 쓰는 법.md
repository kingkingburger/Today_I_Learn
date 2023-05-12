## React에서 .env 파일 쓰는법



react에서 env 파일 쓰려면 REACT_APP_를 붙여줘야 한답니다. 안그러면 리액트 앱에서 변수를 불러우지 않는다네요.

![img](https://mblogthumb-phinf.pstatic.net/MjAyMDA3MTdfODgg/MDAxNTk0OTQ1MjQ4OTY0.qJ6Op6OsH-Hyyr1bPveOUycsxs662pem7r57b4FwH1Eg.6pJ0Hgm0NgguTZmcbaEKqzL63bsfZajxl0Z-LuWSx04g.PNG.legend25/image.png?type=w800)

#### .env 파일

```
REACT_APP_SERVICE_VERSION='0.0.1'
REACT_APP_SERVICE_TYPE='local'
REACT_APP_API_URL='localhost:8080'
```



### 사용법

<div>
  {process.env.REACT_APP_SERVICE_VERSION}
  {process.env.REACT_APP_SERVICE_TYPE}
</div>

별도의 import를 하지않고 전역, 어디서든 process.env.으로 가져와서 사용할 수 있습니다.

하지만 동작하지 않습니다. undefine가 뜨네요. ⇒ 리액트 서버를 한번 껏다 키겠습니다.

잘 동작합니다.