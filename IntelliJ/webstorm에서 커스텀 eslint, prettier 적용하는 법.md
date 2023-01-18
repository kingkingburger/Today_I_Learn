# webstorm에서 커스텀 eslint, prettier 적용하는 법

각 프로젝트마다 eslint, prettier를 다르게 적용하고 싶을 때가 있습니다.

eslint는 .eslintrc.js 파일로 prettier는 prettierec 파일로 저장을 해서 각 프로젝트마다 적용시킬 수 있습니다.



![img](https://blog.kakaocdn.net/dn/bH5Iem/btrWv8Cdbdi/JKFxPSfClgNOCYnwTfsVxk/img.png)



현재 파일구조 입니다. 프로젝트 최상단에 .eslint.js와 .prettierrc가 있는것을 확인할 수 있습니다.

 

 

## 🟩 .eslintrc.js 설정하기



![img](https://blog.kakaocdn.net/dn/RSS0R/btrWv8vqS52/eXTDQB2qIgxIM4eMhNDg2K/img.png)



Ctrl + Alt + S를 눌러서 설정 파일에 간다음 → eslint → Manual ESLint configuration을 클릭해줍니다.



![img](https://blog.kakaocdn.net/dn/IJ5tX/btrWBhw6nCe/Ptr0moO3cL4x9dRTEIkbtK/img.png)



ESLint package는 .eslintrc.js 파일이 어디있는지 보여주는 것 입니다.



![img](https://blog.kakaocdn.net/dn/dGqrn8/btrWx8HGubS/lZCy450ol7XHWRMSkjVQI1/img.png)



ESLint package에다가 현재 eslintrc.js 파일이 어디있는지 넣어줘야 합니다. 저는 npm i eslint로 다운 받아온 eslint를 사용하겠습니다.



![img](https://blog.kakaocdn.net/dn/buS8Fu/btrWx5RNV6E/A8pQdgeVMPxU0PJzHGhQSk/img.png)



Working directories에 eslint를 적용할 파일을 선택해줍니다.



![img](https://blog.kakaocdn.net/dn/bH3RVn/btrWzWfHva0/pKDMvPcVBC0nDlmuYHxX0k/img.png)



프로젝트 전체에 적용할 것이니 프로젝트 파일 자체를 선택해주면 됩니다.

 

## 🟩 .prettierrc 설정하기



![img](https://blog.kakaocdn.net/dn/SksVm/btrWBiQkdvm/JQuhSinIvhgYAOubiKwWl0/img.png)



prettier도 비슷합니다.

 

Ctrl + Alt + s -> prettier 검색 -> prettier 들어갑니다.

 

**Prettier Package는** 내가 만든 **.prettierrc파일** 찾아줍니다. 없다면 npm 모듈로 지정된 prettier를 사용할 것 입니다.

 

**On save**를 체크하면 저장할 때마다 prettier가 동작합니다.



![img](https://blog.kakaocdn.net/dn/bGkDTN/btrWx8VefPS/qHXheEMyjyMrT4ilKeFMi1/img.png)![img](https://blog.kakaocdn.net/dn/bp6FXE/btrWwsmYWL2/KzaiBddTFenfBt8Hiq56VK/img.png)



.prettierrc파일은 프로젝트 최상단에 있으니 프로젝트 파일 자체를 넣어줍시다.