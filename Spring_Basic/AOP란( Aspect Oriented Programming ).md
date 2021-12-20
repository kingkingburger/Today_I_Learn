## AOP란?( Aspect Oriented Programming )

 **관점 지향 프로그래밍**이라고 불린다. 관점 지향은 쉽게 말해 **어떤 로직을 기준으로 핵심적인 관점, 부가적인 관점으로 나누어서 보고 그 관점을 기준으로 각각 모듈화하겠다는 것이다**. 여기서 모듈화란 어떤 공통된 로직이나 기능을 하나의 단위로 묶는 것을 말한다. 





## AOP 적용

공통 관심 사항(cross-cutting concern) vs 핵심 관심 사항(core concern) 분리

![image](https://user-images.githubusercontent.com/65094518/146698856-586888b1-b1da-47cd-aa67-535f3441a95d.png)

시간 측정 로직을 한곳에 모으고 각각의 컨트롤러에 적용시킵니다.



```java
@Aspect
@Component
public class TimeTraceAop {

    //어느 컴포넌트에 적용할 거냐 타겟을 정해줘야 합니다.
    //           폴더.패키지명.class명.(매개변수명) 등을 다 넣으라는 소리 입니다.
    @Around("execution(* hello.hellospring..*(..))")
    public Object execute(ProceedingJoinPoint joinPoint) throws Throwable{
        //호출이 될 때 joinPoin 에다가 타겟을 넣어준다, 이것은 호출 될 때마다 인터럽트가 걸리는 것 입니다.
        long start = System.currentTimeMillis();

        System.out.println("START: " + joinPoint.toString());

        try{
            Object result = joinPoint.proceed();
            return result;
        } finally{
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;

            System.out.println("END : " + joinPoint.toString() + " " + timeMs + "ms");
        }
    }
}
```

시간을 측정해주는 로직을 AOP로 만들려고 합니다. `@Aspect`를 붙히면  **'넌 공통 관심 사항 매서드야!'** 라고 선언합니다. 이것도 스프링 Bean에 넣어줍니다.

`@Around`는 AOP의 범위를 설정할 수 있습니다. 

예를 들어 hello.hellospring이라는 패키지 밑에있는 모든 파일들에 적용할거면 `"execution(* hello.hellospring..*(..))"`을 합니다.

 '나는 밑에있는 service 폴더에만 적용할래!' 하면  `"execution(* hello.hellospring.service..*(..))"` service밑에 있는 폴더에 모두 적용합니다 라고 선언하는 것과 같습니다.







## AOP 적용 전 의존관계

![image](https://user-images.githubusercontent.com/65094518/146700921-25d94e05-ca6f-4799-bb40-238f34d0e165.png)

`memeberController`는 `memberService`를 `@Autowired`로 의존주입을 받고 있습니다. 이 때 memberservice에 AOP를 적용하면

![image](https://user-images.githubusercontent.com/65094518/146700982-b31bbf55-bf12-43ff-bac6-4a706737e627.png)

memberService의 가짜 객체가 일단 나타나서 `공통 관심 사항` 로직을 수행합니다 그리고 `joinPoint.proceed()`를 해서 실제 memberService가 동작하게 합니다.



#### 전체적인 그림을 보면

![image](https://user-images.githubusercontent.com/65094518/146701052-d9f1d351-4dca-493d-88ef-8c70c5c000ea.png)

모든 객체들이 일단 가짜로 만들어지고 `joinPoint.preceed()`로 진짜가 수행되게 됩니다.