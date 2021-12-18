## index.html은 왜 호출이 안되나요?

스프링은 컨트롤러가 정적 파일보다 우선순위가 높습니다.





## html에서 온 데이터를 db에 저장하기

```java
//mebers/new에서 post로 요청을 보낸다.
@PostMapping("/members/new")
public String create(MemberForm form){

    //html에서 문자를 받아옴
    Member member = new Member(); //Member 객체에 
    member.setName(form.getName());  // form에서 온 Name을 붙혀줍니다.

    //db에 저장해야 함
    memberService.join(member);

    return "redirect:/";
}
```

처음에 `MemberForm`형태에서 바로 db에 넣는 줄 알았지만 memberService를 쓰기위해서는 member객체를 써야했습니다.





## Get방식으로 받아왔을 때 

```java
@GetMapping("/members/new")
public String createForm(){
    return "/members/createMemberForm";
}
```

url에 `/members/new`가 들어오면 아무것도 하지 않고 `/members/createMemberForm`을 리턴합니다. 리턴을 하게되면 `template`에서 파일을 찾아보게 됩니다. `createMemberForm`을 찾게되면 thyleaf 탬플릿이 랜더링을 합니다.





## Post방식으로 보내기

```html
<div class="container">
    <form action="/members/new" method="post">
        <div class="form-group">
            <label for="name">이름</label>
            <input type="text" id="name" name="name" placeholder="이름을 입력하세요">
        </div>
        <button type="submit">등록</button>
    </form>
</div> <!-- /container -->
```

name은 server로 넘어올 때 key 값입니다. 버튼을 누르면 `/members/new`에 post방식으로 name을 보내게 됩니다.





## 회원 컨트롤러에서 조회 기능

```java
@GetMapping("/members")
public String list(Model model){
    List<Member> members = memberService.findMembers();
    model.addAttribute("members", members);
    return "members/memberlist";
}
```

`memberService`의 `findMembers()`를 이용해서 모든 member들을 가져옵니다. 그리고 `mode.addAttribute()`를 통해서 members객체를 "members"이름으로 Model에 추가합니다.





## Memberlist를 보여주는 html

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>
<div class="container">
    <div>
        <table>
            <thead>
            <tr>
                <th>#</th>
                <th>이름</th>
            </tr>
            </thead>
            <tbody>
            <tr th:each="member : ${members}">
                <td th:text="${member.id}"></td>
                <td th:text="${member.name}"></td>
            </tr>
            </tbody>
        </table>
    </div>
</div> <!-- /container -->
</body>
</html>
```

$ 사인은 model안에 있는 값들을 가져오는 것 입니다.

th:each는 thyleaf 문법입니다. 모든 내용을 도는 foreach문법가 비슷합니다.