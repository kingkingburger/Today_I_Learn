#### ✅ Invalid type "number[]" of template literal expression에러가 났을 때 

```ts
${params.ccIdCompanies ? `where c.cc_id_company in (${params.ccIdCompanies})` : ''}
```

위 문장에서 에러가 났습니다. params에서 들어온 ccIdCompanies라는 변수가 number[] 타입인데 이걸 template literal에서 표현할 수가 없어~ 이런뜻인거 같습니다.

**params.ccIdCompanies**에는 `[265,278]`이라는 값만 들어갈 것입니다. 그러면 배열만 쫙 풀면 되지 않을까요??

```tsx
${params.ccIdCompanies ? `where c.cc_id_company in (${params.ccIdCompanies.toString()})` : ''}
```

이렇게 toString으로 감싸면 string으로 인식이 됩니다. 배열을 풀때 `265,278` 이런식으로만 풀어줍니다.



처음에는 `...`문법을 생각했습니다. 그런데 template literal에서는 안되는거 같아요.

[`restrict-template-expressions`에 대한 자세한 설명글 입니다.](https://github.com/typescript-eslint/typescript-eslint/blob/v4.12.0/packages/eslint-plugin/docs/rules/restrict-template-expressions.md)



**틀린** 코드

```
const arg1 = [1, 2];
const msg1 = `arg1 = ${arg1}`;

const arg2 = { name: 'Foo' };
const msg2 = `arg2 = ${arg2 || null}`;
```

**맞는** 코드

```
const arg = 'foo';
const msg1 = `arg = ${arg}`;
const msg2 = `arg = ${arg || 'default'}`;

const stringWithKindProp: string & { _kind?: 'MyString' } = 'foo';
const msg3 = `stringWithKindProp = ${stringWithKindProp}`;
```








