## Thymeleaf로 spring Controller에게 데이터 보내기

#### 1번째 방법 - th:value 와 th:name을 이용하기

\- hidden 값을 이용해 controller 에 값을 전달하고 싶었습니다. 애초에 다른 controller에서 값을 내려줄 때, 저는 model.addAttribute를 통해 키, 벨류를 이용하여 값을 내려주는 과정은 이해하고 있었습니다.

```java
model.addAttribute("userId",1);
<input type="hidden" th:value="${userId}"/>
```

\- 이제 이 값은 th:value에 담기게 됩니다. ${} 문법이 여기에서 중요한데, ${}를 쓰지 않으면 value는 문자 그대로의 userId가 되게 됩니다.

${}를 사용하게 되면 1이 담기게 됩니다.

만약 html에서 변형되는 값을 넘기려면 

```java
model.addAttribute("userId",1);
<input type="hidden" id="result"/>
```

```html
<script >
    function handleOnChange(e) {
        // 선택된 데이터 가져오기
        const value = e.value;
        document.getElementById('result').value = value;
    }
</script>
```

js를 써서 해당 id에다가 직접 value를 넣어줍시다. 



\- 이제 이 1을 controller에 넘겨주기 위해서는 어떻게 해야할까요?

```java
<input type="hidden" th:name="test" th:value="${userId}"/>
```

\- th:name=""을 이용하시면 됩니다. th:value에 담겨있는 값을 th:name을 키값으로 해서 전달이 되는 것이라고 할 수 있습니다.

```java
    @PostMapping("/permit")
    public String permit_policy_page(PolicyDto dto,String userId){    // userId => firstPageId
        Long firstPageId = Long.parseLong(userId);
        ....
	}
```

다만, 이런 방식은 컨트롤러에서 Long 타입이 아닌, String으로밖에 받지 못합니다.

조금 더 세련된 방식으로는 @RequestParam을 이용하는 방법이 있습니다.

```java
    @PostMapping("/permit")
    public String permit_policy_page(PolicyDto dto,@RequestParam("userId") Long firstPageId){    // userId => firstPageId
//        Long firstPageId = Long.parseLong(userId);
	...
    }
```

th:name값을 받아서 바로 Long 타입으로 변환할 수 있습니다.



#### 2 번째 방법 - form 테그 이용하기

우선 호출하는 컨트롤러에서부터 값을 담을 객체를 @ModelAttribute 어노테이션을 붙여줍니다. 

```java
@RequestMapping("/moveLogin.do")
    private ModelAndView moveLogin(@ModelAttribute LoginVO loginVO,
            HttpServletRequest request) throws Exception {
        return new ModelAndView("login/login");
    }
```

여기서는 LoginVo타입의 값을 넣어줬습니다.

```html
<form th:action="@{/login.do}" 
      th:object="${loginVO}"  action="#" id="loginForm" method="post">
    <div class="form-group">
        <input type="email" th:field="*{email}" name="email" 
               id="email" placeholder="Email" />
    </div>
    <div class="form-group">
        <input type="password" th:field="*{password}" name="password" 
               id="password" placeholder="Password" />
    </div>
    <button type="submit"">Login</button>
</form>
```

그리고 form테그의 

th:action에 속성에 전달한 url,

th:object에 값을 담을 객체를 잡아줍니다.

그 다음으로  값을 입력받을 input 태그의 th:field에 form태그에서 선언한 객체에 담길 항목들을 잡아주면 됩니다.



마지막으로 submit으로 값을 넘겨받을 컨트롤러를 아래와 같이 코딩하면 loginVO객체 안에 email과 password 값이 각각 들어갑니다.

```java
@RequestMapping("/login.do")
private ModelAndView doLogin(@Valid LoginVO loginVO, BindingResult result,
                             RedirectAttributes redirect, HttpServletRequest request, HttpServletResponse response) throws Exception {
    System.out.println("---------------------> login!!!!!!!!!!!");
    System.out.println("---------------------> " + loginVO.getEmail());
    System.out.println("---------------------> " + loginVO.getPassword());
    System.out.println("---------------------> login!!!!!!!!!!!");

    return new ModelAndView("main");
}
```

