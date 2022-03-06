## Docker란?

어플리케이션을 패키징 할 수 있는 툴

컨테이너 안에 어플리케이션, 시스템툴, 외부 라이브러리 들은 담아서 다른 서버나 시스템에 넘겨줄 수 있습니다.

내 pc의 nodejs와 서버의 nodejs가 있다고 해서 내pc에 있는 것을 서버로 보내면 안될 수 있습니다. 버저니 달라서 나타나는 문제일 수 있죠

**어플리케이션을 구동하는데 필요한 모든것들**은 컨테이너안에 담을 수 있습니다.

VM보다 가벼움 계념이 **컨테이너 엔진** 이라고 생각합시다. 이 컨테이너 엔진중에 가장 유명한게 **Docker** 입니다.



## Docker는 어떻게 동작하는가?

컨테이너를 만들고 -> 구성하고 -> 배포합니다.



컨테이너를 만들기 위해서는 **Dockerfile을 만들고 -> image를 만들고 -> Container**를 만듭니다.

- **Dockerfile** -> 요리로 치면 레시피, 어떤 프레임워크 라이브러리, 어떻게 구동해야하는지 등...
- **image 파일** -> 우리 어플리케이션을 스냅샷 해서 파일로 만든다고 보면 됩니다. 이는 불변합니다.
- **Container** -> 샌드박스 처럼 image를 Container 안에서 실행시킵니다. 

image를 class라고 생각하고 container는 인스턴스라고 생각합니다.



## 컨테이너를 배포(이미지를 공유하는법)

내 local에서 **image**를 만들어서 **Constainer Registry**에 push 합니다. 그 다음 서버에서 pull을 하면 됩니다. github와 비슷하네요. 물론 서버에는 Docker 엔진이 있어야 하죠

github와 비슷한 dockerhub를 사용합니다.







## 이미지를 만드는법

```
FROM node:17-alpine

WORKDIR /app

COPY pakage.json package-lock.json ./

RUN npm ci

COPY index.js .

ENTRYPOINT ["node", "index.js"]
```

FROM으로 base image를 가져옵니다. 기본적인 용품을 맨 위에서 챙깁니다.

WORKDIR은 '이 디렉토리에 저장합니다.' 라는 뜻입니다.

COPY로 pakage.json에 있는것을 가져옵니다. 그 다음에 RUN으로 pakage.json 안에 써져있는 모든것을 실행합니다.

내가만든 파일은 맨 아래쪽에 쓰는게 좋습니다. 정확히는 자주 바뀌는 파일은 아래쪽에 둡니다.

ENTRYPOINT로 Dokcer를 실행합니다.



## docker를 실행하기

```
docker run -d -p 8080:8080 fun-docker
```

-d 옵션은 백그라운드에서 동작하도록 하는 것입니다. 터미널아 너는 계속 일을 해라고 합니다.

-p 옵션은 local의 8080과 container의 8080을 묶어줍니다. 각각의 container 개별적인 고립된 환경에서 동작하므로 local과 연결해줘야 합니다.



```
 docker ps
```

현재 실행중인 container를 볼 수 있습니다.



```
docker logs 6d312da326d3
```

Container ID로 모든 log를 볼 수 있습니다.



## dockerhub에 올리기

dockerhub의 repository의 이름과 내 local의 image이름이 같아야 합니다. 내 local image의 이름을 바꿔봅시다.

```
 docker tag fun-docker:latest bisu0303/docker-example:tagname
```

docker tag로 이름을 바꿨습니다. bisu0303/... 은 제 dockerhub repository의 주소입니다.



```
docker push bisu0303/docker-example:tagname
```

내 repository에 올립니다.

![image](https://user-images.githubusercontent.com/65094518/156916427-f3531341-bcc0-4d97-b537-fe815b94b533.png)

이렇게 dockerhub에 올렸습니다.
