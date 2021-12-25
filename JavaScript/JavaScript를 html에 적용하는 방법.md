## JavaScript를 html에 적용하는 방법


    <body>
    <script type="text/javascript" src="test.js"></script>
    </body>

외부 파일로 연결하는 방법 입니다.





## html의 id 형태 태그를 js로 가져오기, [getElementById]

```javascript
document.getElementById("console")
```

태그가 `id=console`인 경우에 태그 전체를 가져 옵니다. 만약 `input`태그에 쓴 값을 가져오고 싶다면 뒤에 .value를 써줍니다.

```
document.getElementById("console").value
```





## html의 class 형태 태그를 js로 가져오기,[getElementsByClassName]

이 함수는 태그의 class="" 속성을 사용하여 접근한다. 

동일한 class명이 존재할수 있기때문에 ( id속성은 html 문서에 동일한 id속성이 존재하면 안된다..)

 id 속성을 사용하여 접근하는 **getElementById**() 와 달리 **getElementsByClassName**() 은 컬렉션 객체를 반환한다. 따라서 for문을 사용하거나 특정 index에 위치한 element를 반환받아 사용할수있다.

객체 하나를 가져올려면 뒤에 .item(i)을 붙히면 됩니다.

```java
document.getElementsByClassName("classname").item(1);
```

classname에 있는 첫 번째 객체를 반환합니다.





## innerHTML

(html은 대문자로 써주자!..)

<> 태그 밖에 있는 값을 해석하고 가지고 옵니다!

innerText라는 것도 있습니다. html 문자열 그대로 보여지게 됩니다.

참고자료https://hianna.tistory.com/480





