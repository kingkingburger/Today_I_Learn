## React에서는 css를 module처럼 쓴다!

파일을 xxx.module.css로 바꾸고 안에 `.title`이라는  설정을 줘보자
 그 다음 **컴포넌트**에다가 `import styles from "./xxx.module.css"`를 하면 styles라는 변수 안에 `.title`의 속성이 들어있다. 그러면`<button className={styles.btn}>{text}</button>` className에 들어가서 적용이 되게 한다!

브라우저에서 보면 랜덤한 class이름으로 나온다.





