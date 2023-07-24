## nextjs13 에서 server component, client component에 대해서

next.js 컴포넌트는 종류가 2개입니다.

1. server component
2. client component

기본적으로 react를 생각한다면 모든 컴포넌트는 client 컴포넌트가 되었습니다. 하지만 nextjs의 컴포넌트는 server component입니다.

아무데나 대충 만든건 server component가 됩니다.

‘use client’를 적으면 client component가 됩니다.

### 차이점은?

server component에서는 html에 자바스크립트 기능 넣기 불가능 합니다.

![image](https://github.com/kingkingburger/Today_I_Learn/assets/65094518/d140aed2-5aaf-4c45-a733-d3e2312bfc49)

이게 안됩니다. 그동안 에러났던게 이해가 되네요.

useState, useEffect등 사용불가합니다.



html을 동적으로 만드는 것들이 아예 안됩니다. client로 바꿔야하죠

client가 더 좋네요? ⇒ server component는 로딩속도가 빠릅니다.

client가 더 느립니다. hydration때문인데요. html을 유저에게 보낸 후에 자바스크립트로 html을 다시읽고 분석하는 일입니다.



### (추천)

큰 페이지는 server component

js기능 필요한 곳만 client component



