## docker 와 docker-compose의 차이점

[Difference between Docker Compose Vs Dockerfile](https://dockerlabs.collabnix.com/beginners/difference-compose-dockerfile.html)번역본 입니다.

> Dockerfile은 사용자가 이미지를 어셈블하기 위해 호출할 수 있는 명령이 포함된 간단한 텍스트 파일인 반면 Docker Compose는 다중 컨테이너 Docker 애플리케이션을 정의하고 실행하기 위한 도구입니다.
>
> Docker Compose는 앱을 구성하는 서비스를 docker-compose.yml에 정의하여 격리된 환경에서 함께 실행할 수 있습니다. docker-compose up을 실행하여 하나의 명령으로 앱을 실행합니다. 프로젝트의 docker-compose.yml에 빌드 명령을 추가하면 Docker compose는 Dockerfile을 사용합니다. Docker 워크플로는 생성하려는 각 이미지에 적합한 Dockerfile을 빌드한 다음 compose를 사용하여 build 명령을 사용하여 이미지를 조합하는 것이어야 합니다.





#### 🔷Docker

- **Single Container**를 관리합니다.

- 이미지를 빌드 해줍니다.

- 커맨드 라인에서 명령어를 실행할 수 있습니다.

  

####  🔷Docker-compose

- yaml file 기반으로 **Multi container** 관리할 수 있습니다.
- yaml파일에 명령어를 적어서 컨테이너를 정의하고 관리한다. 
- 앱이 실행되는 동안 컨테이너를 관리해줍니다.





