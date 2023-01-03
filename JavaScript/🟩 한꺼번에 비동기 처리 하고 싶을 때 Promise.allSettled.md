## 🟩 한꺼번에 비동기 처리 하고 싶을 때 Promise.allSettled

기존의 Promise.all()의 진화된 버전 입니다.

Promise.all()은 주어진 프로미스 중 하나가 reject(거부,실패) 되는 경우 모든 Promise가 reject 됩니다.

```js
const success90percentPromise = () => {
  return new Promise((resolve, reject) => {
    const value = Math.random();
    if (value >= 0.1) {
      return resolve(value);
    }
    return reject(value);
  });
}

async function fulfilledPromises() {
  const promises = Array(10)
    .fill(0)
    .map(() => success90percentPromise());
  const result = [];
  try {
    const promiseResult = await Promise.all(promises);
    result.push(...promiseResult);
  } catch (e) {
    console.error(`error on ${e}`);
  }

  console.log(result);
}

fulfilledPromises();
//error on 0.005512747899925952
//[]
```

위 코드는  90% 확률로 promise를 반환하는 함수를 10번 반복합니다. 

반환된 promise중에 10%확률로 reject가 되기 때문에 1번이라고 reject되면 error로 처리가 됩니다.



```js
const success90percentPromise = () => {
  return new Promise((resolve, reject) => {
    const value = Math.random();
    if (value >= 0.1) {
      return resolve(value);
    }
    return reject(value);
  });
}

async function fulfilledPromises() {
  const promises = Array(10)
    .fill(0)
    .map(() => success90percentPromise());
  const result = [];
  try {
    const promiseResult = await Promise.allSettled(promises);
    result.push(...promiseResult);
  } catch (e) {
    console.error(`error on ${e}`);
  }

  console.log(result);
}

fulfilledPromises();
// [
//   { status: "fulfilled", value: 0.57138451422671 },
//   { status: "fulfilled", value: 0.9751896985323971 },
//   { status: "fulfilled", value: 0.36620249895906176 },
//   { status: "fulfilled", value: 0.4280705198456176 },
//   { status: "fulfilled", value: 0.16056729536579262 },
//   { status: "rejected", reason: 0.07729737054085639 },
//   { status: "fulfilled", value: 0.5978070068427903 },
//   { status: "fulfilled", value: 0.8525224109153984 },
//   { status: "fulfilled", value: 0.8540939807768344 },
//   { status: "rejected", reason: 0.011490346125412332 },
// ];
```

만약 allSettled를 사용했다면 어떤 promise가 resolve되었고 reject되었는지 알 수 있습니다.



프로미스를 동시에 사용하고 싶을 때 1개라도 reject되면 팅기는 Promise.all()과는 다르게 reject되는 promise가 있더라고 결과값을 받아와서 사용할 수 있어 더 편리할거 같습니다.

![image](https://user-images.githubusercontent.com/112359150/210196525-3e9b3464-250d-4b66-84a5-d0de45fead3c.png)

```json
{
  "compilerOptions": {
    "target": "ES2020" 
  }
}

```

만약 typescript에서 쓸 려면 tsconfig.json을 es2020이상으로 맞춰주셔야 합니다.





