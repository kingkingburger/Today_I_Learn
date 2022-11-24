## Seqeulize에서 연관관계 Json 가져오기

연관관계에서의 이점이 최악입니다. 묶는건 편하지만 따로 관리하기 때문에 객채를 typescript형태로 가져오지 못하겠습니다..

typescript에서 json을 어떻게 다루는가에 대해서 알필요가 있습니다.

`as Record<string, any>` 로 가져오는건 너무나 위험합니다. any에 어떤값이 들어있을 줄 알고, 그리고 key가 무조건 string이냐?.. 그건 맞는듯합니다.

any로 가지고 오는순간 typescript는 긴장하게 됩니다. 어떤값이 들어올지 모르기 때문에 하나라도 들어온다고 가정하고 코드를 짜면 typescript는 빨간줄을 토해내는 발악을 합니다.

아.. 진짜 any에 xx들어온다고.. 라고 생각하면 예외처리를 할 수 있습니다. 

```ts
if (A?.xx) {
  A.xx = JSON.parse(A.xx as string);
}
```

A가 들어올지 안올지 모르지만 들어온다면 .... 하는 예외처리를 또 해줘야 합니다.

그러면 any말고 json형태로 들어오는 모든것을 interface로 만들면 되지 않냐??? -> 맞습니다. 하지만 언제 include된 객체들을 전부 interface로 만들어둡니까.  벼룩잡으려고 초가집 태워버립니다..



#### ✅Sequelize가 이렇게 되어있을 때 

![image](https://user-images.githubusercontent.com/112359150/203746822-ce1336ec-9a20-4f8d-8eeb-11dcb40af976.png)

저렇게 되어 있으면 

![image](https://user-images.githubusercontent.com/112359150/203747178-1d6a32b0-b514-40fa-8dfa-3f8315bf3f8f.png)

요로콤 Json이 나옵니다.

그러면 result에 반환타입이 NotiAttribute로만되어있어서 NotiAttribute속성밖에 쓰지 못합니다. 

그러면 data안에 있는 `CalMeter`, `MachineRoom`, `Customer`는? 실제로 반환도 되고 값도 들어가있습니다. 그런데 typescript에서 쓰질못합니다. ㅡㅡ 



💢왜 why? -> 속성이 NotiAttribute로만 되어있어서 

NotiAttribute 참고 ㅎㅎ

![image](https://user-images.githubusercontent.com/112359150/203747892-487166c8-ac85-409d-b7e7-270948821672.png)

🤦‍♂️ 오케이 그러면 NotiAttribute에 `CalMeter`, `MachineRoom`, `Customer` 속성 넣으면 되잖아!

😂 그러면 NotiAttribute의 무결성이 깨지게 되는거같습니다. NotiAttribute는 NotiAttribute의 속성만 가지고 있어야 Sequelize가 재대로 동작하는거 같습니다.

🤦‍♂️ 그럼 다른 interface 파가지고 만들면 되지 않을까? 

😂 맞습니다. extend로 기존 attribute를 가져와서 만들면 됩니다! 하지만 Sequelize가 허락하지 않는가 보네요... Dao의 반환값을 NotiAttribute가 아닌것을 가진 interface를 넣으면 에러가 발생하게 됩니다.



그래서 interface를 만들지 않고 해결하는 방법을 찾아본 결과

```ts
const { NotiListHistories, ...other } = result as Record<string, any>;
```

이렇게 생각이 났습니다. `...`(전개연산자) 를 써서 다른 요소들을 모두 빼네고 내가 원하는 Json의 칼럼만 가져오는 것입니다!

하지만 위에서 본 

![image](https://user-images.githubusercontent.com/112359150/203747178-1d6a32b0-b514-40fa-8dfa-3f8315bf3f8f.png)

여기서 Customer를 꺼내고 싶다면 

```ts
const { CalMeter, ...other } = result as Record<string, any>;
const MechineRoom = CalMeter?.MachineRoom;
const Customer = MechineRoom?.Customer;
```

이렇게 객체 꺼내듯이 하면 됩니다.

