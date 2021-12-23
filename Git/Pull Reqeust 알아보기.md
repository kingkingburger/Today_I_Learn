## Pull Reqeust 알아보기

`pull reqeuest`  = 내가 작업한 코드가 있으니 내 브랜치를 당겨 검토 후 병합해주세요.

협업을 하려면 일단 원격 저장소가 있어야 합니다. 우리가 함께할 저장소를 만들어야하죠

그 다음

1. Fork
2. clone, remote설정
3. branch 생성
4. 수정 작업 후 add, commit, push
5. Pull Request 생성
6. 코드리뷰, Merge Pull Reqest
7. Merge 이후 branch 삭제 및 동기화

를 순서대로 합니다.





## 1. Fork

![image](https://user-images.githubusercontent.com/65094518/147234705-771e5d5e-5317-4bac-ab0f-1039af69d384.png)

fork를 눌러서 다른 사람의 repository를 나의 repository로 가져옵니다.(다른사람의 원격 저장소를 나의 원격 저장소로 가져옵니다.)

![image](https://user-images.githubusercontent.com/65094518/147235411-b1b9d9f2-80be-4084-b24e-7f3b6d744a7e.png)

(흰색은 폴더입니다!)









## 2. clone

![image](https://user-images.githubusercontent.com/65094518/147235557-44f4aaba-e69d-41ce-9b02-1d5c0056b9cb.png)

```
git clone https://github.com/kingkingburger/test
```

나의 `원격 저장소`에 있는 것들을 내 `로컬 저장소`에 옮겨야하니 clone을 해줍니다. clone을 하면 자동으로 remote가 나의 `원격 저장소`로 되어있습니다.





##  3. remote 설정

![image](https://user-images.githubusercontent.com/65094518/147236192-67a076d5-161d-4127-8d71-076066113f35.png)

```
# 원본 프로젝트 저장소를 원격 저장소로 추가
$ git remote test2(별명) https://github.com/원본계정/(다른사람 원격저장소)

# 원격 저장소 설정 현황 확인방법
$ git remote -v
```





## 4. branch 생성

![image-20211223204924862](C:\Users\원민호\AppData\Roaming\Typora\typora-user-images\image-20211223204924862.png)

노랑색 `branch`가 생겼습니다! 자신의 로컬 컴퓨터에서 코드를 추가, 수정, 삭제 작업은 branch를 만들어서 진행해야 합니다.

> 개발을 하다 보면 코드를 여러 개로 복사해야 하는 일이 자주 생긴다. 코드를 통째로 복사하고 나서 원래 코드와는 상관없이 독립적으로 개발을 진행할 수 있는데, 이렇게 독립적으로 개발하는 것이 브랜치다. - pro git book

```
# develop 이라는 이름의 branch를 생성한다.
$ git checkout -b develop
Switched to a new branch 'develop'

# 이제 2개의 브랜치가 존재한다.
$ git branch
* develop
  master
```







## 5. 작업 후 add, commit, push

![image](https://user-images.githubusercontent.com/65094518/147236833-7f153f8c-b7a7-4d05-a3b5-db3d75af63d5.png)

```
# develop 브랜치에서 수정한 파일 모두를 add합니다.
$ git add .

# develop 브랜치에서 수정한 파일을 commit 합니다.
$ git commit -m "test입니다."

# develop 브랜치의 수정 내역을 origin 으로 푸시한다.
$ git push origin develop
```





## 6. Pull Reqeust 생성

push 완료 후 본인 계정의 github 저장소에 들어오면 **Compare & pull reqeust** 버튼이 활성화 되어 있습니다. 해당 버튼을 선택하여 메시지를 작성하고 PR을 생성합니다.

![image](https://user-images.githubusercontent.com/65094518/147237098-7ef93210-8e1e-4562-966e-f7644d9efd91.png)

(다른분의 사진을 가져왔습니다[. 출처](https://wayhome25.github.io/git/2017/07/08/git-first-pull-request-story/))





## 7. 코드리뷰, Merge Pull Request

PR을 받은 원본 저장소 관리자는 코드 변경내역을 확인하고 Merge 여부를 결정합니다.

[코드리뷰로 [프로젝트에 기여하기]](https://devlog-wjdrbs96.tistory.com/231?category=882255)





## 8. Merge 이후 동기화 및 branch 삭제

원본 저장소에 Merge가 완료되면 로컬 코드와 원본 저장소의 코드를 동기화 합니다. 작업하던 로컬의 branch를 삭제합니다.

```
# 코드 동기화
$ git pull real-blog(remote 별명)
# 브랜치 삭제
$ git branch -d develop(브랜치 별명)
```

나중에 추가로 작업할 일이 있으면 `git pull test1(remote 별명)` 명령을 통해 원본 저장소와 동기화를 진행하고 4~7을 반복합니다.





#### 왜 branch를 만들어서 작업을 할까요?

> 만약 프로그래밍을 하신다면, 실제 배포 되어 사용중인 코드가 있을거고, 기능 개발중인 코드가 있을거예요. 아직 한창 개발중인 프로그램인데 갑자기 고객사로부터 이슈가 도착해서 급하게 수정을 들어가야 하는 경우, 내가 지금 개발하고있는 신기능이 포함된 코드에서 수정을 하게 되면 실제 배포할 때 미완성 된 신기능도 같이 섞여서 들어가게 될 겁니다.
> 그렇기 때문에 현재 배포 되어있는 버전에서 브랜치를 파생해서 개발 브랜치를 만들어 신기술을 해당 브랜치 내에서 작업하면, 급하게 버그 요청이 들어왔을 때 마스터 브랜치에서 다시 이슈 픽스 브랜치를 파생해서 해당 브랜치에서만 버그를 고쳐서 병합을 진행하면 현재 내가 개발하고있는 신기술은 개발 브랜치에 온전히 있는 상태에서 배포 된 프로그램의 이슈만 고치는 작업을 진행할 수 있습니다.
> 물론 개발 브랜치도 나중에 마스터로 병합하게 되면 이슈 픽스 브랜치의 내용을 계승할 수 있고요.





#### 내 원격 저장소는 다른사람 repository의 상태와 같아야 합니다.

```
$ git pull (원격저장소 이름) 내원격저장소
```

