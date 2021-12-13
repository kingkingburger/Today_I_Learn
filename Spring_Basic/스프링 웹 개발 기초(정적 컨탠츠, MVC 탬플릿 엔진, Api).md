## 스프링 웹 개발 기초

- 정적 페이지 - 그냥 파일을 웹 브라우저에게 주는 것 
- MVC와 템플릿 엔진 - html을 그냥 주는게 아니라 서버에서 만져서 브라우저에게 주는 것입니다.
- API - JSON이라는 데이터 포멧으로 클라이언트에게 데이터를 전달합니다.







## 정적 컨텐츠 

static폴더에 html 파일을 넣으면 그대로 서버에 나옵니다.



동작하는 것을 `시각화`해서 봅시다.

![image-20211213164926348](https://user-images.githubusercontent.com/65094518/145778877-7ff9646b-93e1-48e0-ae87-79932e6270d1.png)



localhost:8080/hello-static를 스프링이 받으면 **컨트롤러를** 먼저 찾습니다. 

만약 없다면 내부에 있는 resources에 있는 static 폴더를 찾아봅니다.









## MVC와 템플릿 엔진

**view** - 화면을 그리는데 모든 역량을 집중해야 합니다.

**Controller** - 여기는 비지니스 로직을 집중해야 합니다.



**인텔리 J**에서 함수 매개변수에 옵션 보기

```
cmd + p
```



컨트롤러에 새로운 컨트롤러를 만들었습니다.

```
@GetMapping("hello-mvc")
    //@ReqeustParm()은 파라미터를 받는 다는 뜻이다.
    //model을 넘겨줍니다.담으면 view에서 rendering할 때 쓰는 것이죠
    public String helloMvc(@RequestParam(name = "name", required = false) String name, Model model){

        //파라미터로 넘어온 name을 키가 name인 것으로 넘깁니다.
        model.addAttribute("name", name);

        return "hello-mvc-template";
    }
```

RequestParam()에서 옵션은 required가 default로 true가 되어있습니다. 







#### RequestParam의 형식

```
@RequestParam("가져올 데이터 이름")[데이터타입][가져온데이터를 담을 변수]
```



http://localhost:8080/hello-mvc?name=spring 치게되면 hello spring이라고 나옵니다.







#### 동작 방식

파라미터의 name이 spring으로 바뀌고 템플릿도 name이 spring으로 바뀝니다.

![image-20211213170734536](https://user-images.githubusercontent.com/65094518/145778789-195f46a7-f8ee-40c0-8689-84333c535761.png)

컨트롤러에 요청이 들어오면 return값으로 템플릿을 찾으러 가고 model()도 끌고 갑니다.

viewResolver는 view를 찾아주고 템플릿 엔진과 연관짓는 활동을 합니다.









## API 방식

```
@GetMapping("hello-string")
    //응답 body부분에 직접 넣어주겠다.
    @ResponseBody
    public String helloString(@RequestParam("name") String name){

        return "hello " + name; //hello spring
    }
```

@ResponseBody의 뜻은 `응답  body부분에 직접 return 값을 넣어주겠다`는 뜻입니다.

이건 view라는 템플릿을 거치않고 그대로 값을 넣습니다.

hello와 url에 name에 적은 값이 그대로 화면에 출력이 됩니다.





#### 만약 String이 아니라 객체를 넘겨준다면?



```
@GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }

    static class Hello{
        private String name;

        public String getName(){
            return name;
        }

        public void setName(String name){
            this.name = name;
        }
    }
```

Hello 라는 객체에 name을 넣어서 보내면 **JSON형태로 보내집니다**.



객체를 가지고 @ResponseBody를 쓰면 기본으로 JSON으로 넘겨줍니다.
(xml 방식으로 넘길 수 도 있다고 합니다.)





#### getter, setter 편하게 만들기

```
Alt + insert
```



#### Api의 동작방식

![image-20211213172410429](https://user-images.githubusercontent.com/65094518/145778833-e559edc3-7b8b-48c4-a724-1f8a708a37f8.png)



- 요청이 들어오면 내장 톰켓 서버에서 스프링으로 요청을 던집니다!
- 컨트롤러가 @ResponseBody를 보고 한번 생각합니다.(이전에는 view 템플릿을 찾아주는 viewResolver에 주었습니다.)
- ""객체로 들어왔내? 너 Json형태로 나가라!" 하면서 JsonConverter던집니다.

원하는 형태(xml, json ...)를 쓰려면 자동으로 Converter를 정해줍니다.





#### Api에서 model을 필요로 하지 않는 이유는?

Model은 컨트롤러에서 View로 데이터를 전달하기 위한 그릇이라고 생각하시면 됩니다. API에서 모델에 값을 넣지 않는것은, 말씀하신것처럼 View로 데이터를 전달할 필요없이 컨트롤러에서 바로 값을 반환하면 되기 때문입니다.