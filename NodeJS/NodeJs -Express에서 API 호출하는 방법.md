## NodeJs -Express에서 API 호출하는 방법



Express앱은 API RL을 호출해야 합니다.

이 작업을 하기 위해 `request` 모듈을 사용 합니다.





## request 모듈 설치하기

```
npm install request
```

루트 폴더 커맨드 라인에 설치합니다.





## request 모듈 사용하기

```
var request = request('request');
```

모든 컨트롤러가 있는 파일에 위 문법같이 `request`를 사용했습니다.





## request 기본 구조

```
request(options, callback)
```

- options - JavaScript object defining the request, api를 호출하는 것 이니 api요청 옵션을 지정합니다.
- callback - Function to run when a response is received, 비동기식으로 api 호출이 진행 됩니다.



options에 들어갈 목록들 입니다.

| **url**    | full 형태로 url을 지정해줘야 합니다.<br />ex("http://yourapi.com/api.path") |
| ---------- | ------------------------------------------------------------ |
| **method** | GET, POST, PUT, DELETE 형태중 하나를 고릅니다. defulat로 GET입니다. |
| **json**   | 요청 본문을 JS 형태로 보냅니다, body data가 필요하지 않은 경우 빈 개체를 보내야 합니다<br />(POST 방식에서 JS 객체를 채워 보냅니다.) |
| **qs**     | api에 파라미터를 요청할 때 JS를 쿼리스트링을 실어다가 보낼 수 있습니다. |





## 예시코드

```javascript
const getLocationInfo =(req,res,callback) =>{
    const path = `/api/locations/${req.params.locationid}`;
    const requestOptions ={
        url:`${apiOptions.server}${path}`,
        method:'GET',
        json:{},
    };
    request(requestOptions,(err, {statusCode}, body) => {
        const data = body;
        if(statusCode === 200){
            data.coords={
                lng: body.coords[0],
                lat: body.coords[1]
            };
            callback(req,res,data);
        } else{
            showError(req,res,statusCode);
        }  
    });
};
```

getLocationInfo()메서드는 매개변수로 `callback함수`를 받습니다. 호출하는 부분에서 `callback함수`를 넣어서 호출을 해야합니다.

request()메서드를 쓸 때 requestOptions 라는` JS 객체 옵션`과 `callback함수`를 사용합니다.

```javascript
const locationInfo = (req, res) => {
    getLocationInfo(req,res,
        (req,res,responseData) => renderDetailPage(req,res,responseData)    
    );
};
```

어떻게 호출하고 동작하는지 보겠습니다.
`locationInfo()`가 `getLocationInfo`를 호출할 때 세 번째 매개변수로 `callback()함수`를 주었습니다.

 `getLocationInfo()`가 성공적으로 body를 가져오면 `callback함수`인 `renderDetailPage()`을 호출합니다.
이 때 body는 responseData에 들어갈 것입니다.