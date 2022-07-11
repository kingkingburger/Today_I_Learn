## 입출력 스트림 (InputStream, OutputStream)란?

### Stream이란?

> 프로그램은 외부에서 데이터를 읽거나 외부로 데이터를 출력하는 작업이 빈번하게 일어납니다.
> 이때 데이터는 어떠한 통로를 통해서 데이터가 이동되는데, 이 통로를 Stream 이라고 합니다.
>
> 자바에는 이러한 기능을 수행하기 위해 InputStream와 OutputStream이 존재하며 **단일 방향으로 연속적으로 흘러갑니다.
> **InputStream과 OutputStream은 추상 클래스이며 추상 메소드를 오버라이딩해서 다양한 역할을 수행할 수 있습니다. 
> (예 : 파일, 네트워크, 메모리 입출력)
>
> 자바에서 기본적으로 제공하는 I/O 기능은 java.io 패키지에서 제공됩니다. 
> **InputStream은 외부에서 데이터를 읽는 역할**을 수행하고
>  **OutputStream은 외부로 데이터를 출력하는 역할**을 수행합니다.    



#### **InputStream**이란?

> - 바이트 기반 입력 스트림의 최상위 추상클래스입니다. (모든 바이트 기반 입력 스트림은 이 클래스를 상속받습니다.)
> - 파일 데이터를 읽거나 네트워크 소켓을 통해 데이터를 읽거나 키보드에서 입력한 데이터를 읽을 때 사용합니다. 
> - InputStream은 읽기에 대한 **다양한 추상 메소드**를 정의해 두었습니다.
> - 그리고 InputStream의 **추상메소드를 오버라이딩하여 목적에 따라 데이터를 입력** 받을 수 있습니다.

### InputStream은 데이터를 읽어야 한다

파일에서 오건, 메모리에서 오건, 네트워크에서 오건 통로로 데이터를 빨아들이는 기능이 필요하다!
데이터를 읽는 기능과 관련된 메소드는 3개가 있다.

```
/**
 * 1byte를 읽어 그 값을 int로 바꿔 반환하거나 (1byte = -128 ~ 127 또는 0 ~ 255이다)
 * 더 이상 읽을 수 없는 경우는 -1을 반환한다
 */
public abstract int read() throws IOException;

// Main method
byte[] data = new byte[]{1, 2};
ByteArrayInputStream inputStream = new ByteArrayInputStream(data);

System.out.println(inputStream.read()); // 바이트 하나를 읽었으니, 1을 읽었고 1이 출력된다
System.out.println(inputStream.read()); // 바이트 하나를 추가로 읽었으니, 2를 읽었고 2가 출력된다
System.out.println(inputStream.read()); // 더 이상 읽을 바이트가 없으니 -1이 출력된다
/**
 * 1byte씩 읽는게 아니라 파라미터로 주어진 byte 배열 크기만큼 데이터를 읽고 총 몇 byte를 읽었는지 반환한다.
 * 데이터를 읽다가 모두 읽으면, 그 만큼의 크기를 반환하고
 * 시작부터 읽을게 없으면 -1을 반환한다
 */
public int read(byte b[]) throws IOException { }

// Main method
byte[] data = new byte[]{10, 20, 30, 40, 50};
ByteArrayInputStream inputStream = new ByteArrayInputStream(data);

byte[] buffer = new byte[3];
System.out.println(inputStream.read(buffer)); // 바이트 3개(10, 20, 30)을 읽어 buffer에 넘겨주고 3을 출력한다
System.out.println(inputStream.read(buffer)); // 바이트 2개(40, 50)을 읽어 buffer에 넘겨주고 2를 출력한다
System.out.println(inputStream.read(buffer)); // 시작부터 읽을게 없으니 -1을 출력한다
/**
 * len개의 byte를 읽어서 주어진 byte[] b의 b[off]부터 저장한다
 * 저장한 개수를 반환하고, 읽을게 더 이상 없다면 -1을 반환한다
 *
 * 만약 bytep[] 크기가 부족하다면 IndexOutOfBoundsException을 낸다
 */
public int read(byte[] b, int off, int len) throws IOException { }
```

여기까지 읽었다면 InputStream에 대해 한 가지 알아낼 수 있다.

- InputStream은 말 그대로 통로이기 때문에, (read만 사용해서는) 한 번 읽었던 것을 다시 되돌아가 읽을 수 없다.

### InputStream은 데이터를 스킵할 수 있다

```
/**
 * n byte의 데이터를 스킵하고 실제로 스킵한 byte 개수가 출력된다
 * 지원하지 않을 경우 IOException이 나오게 된다
 */
public long skip(long n) throws IOException { }

// Main method
byte[] data = new byte[]{10, 20, 30, 40, 50};
ByteArrayInputStream inputStream = new ByteArrayInputStream(data);

System.out.println(inputStream.skip(3)); // 3개 skip 성공, 3을 출력
System.out.println(inputStream.read()); // 위에서 10, 20, 30을 skip했으므로 40을 출력
```



### InputStream은 데이터가 얼마나 남았는지 알려준다

```
public int available() throws IOException;
```



### InputStream은 닫을 수 있다

통로를 부실 수 있는 것이다

```
public void close() throws IOException;
```



### InputStream은 읽었던 데이터를 특정 시점부터 다시 읽을 수 있다

```
/**
 * 특정 시점을 기록하는 메소드 : mark
 * readlimit은 마킹할 위치를 기록하는 것이 아니라,
 * 현재 위치를 마킹하고나서 최대 몇개의 byte를 더 읽을 수 있는지를 의미한다
 *
 * 예를 들어, readlimit을 100으로 설정했다면,
 * 지금 mark를 호출하고 read()를 101번 호출 할 수 없는 것이다.
 */
public synchronized void mark(int readlimit) { }
/**
 * mark되어 있는 지점으로 돌아간다
 * 이 이후에 read를 하면 아까 mark 해두었던 시점부터 데이터를 읽어들이는 것이다.
 */
public syncrhonized void reset() throws IOException { }
/**
 * 이 InputStream 구현체가 mark / reset을 지원하는지, 지원하지 않는지를 표기한다.
 */
public boolean markSupported()
```



## 정리하면

InputStream은 데이터를 byte 단위로 읽어들이는 통로이며 (읽어들인 데이터를 byte로 돌려줌)

InputStream이 갖춰야 할 덕목으로는

- 데이터 읽기
- 특정 시점으로 되돌아가기
- 얼마나 데이터가 남았는지 보여주기
- 통로 끊기





## OutputStream의 정의

OutputStream 추상 클래스는 **데이터가 나가는 통로의 역할에 관해 규정**하고 있는 추상 클래스이다.

InputStream을 한 번 봤기 때문에 쉽게 이해할 수 있다.. 반대되는 개념이겠거니...



## OutputStream 주요 메소드

그럼 이제 데이터가 나가는 통로는 어떤 역할을 수행해야 하는지 주요 메소드를 알아보자!



### OuputStream은 쓸 수 있어야 한다

파일로 보내건, 메모리로 보내건, 네트워크로 보내건 통로로 데이터를 내부내는 기능이 필요하다!
데이터를 쓰는 기능과 관련된 메소드는 3개가 있다.

```
/**
 * b를 OutputStream으로 내보낸다
 */
public abstract void write(int b) throws IOException;

// Main method : ByteArrayOutputStream은 Byte Array'로' 내보내는 통로이다
ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
outputStream.write(1); // outpustream에는 [1]이 들어있다
outputStream.write(2000); // outputStream에는 [1, -48]이 들어있다
/**
 * byte 배열 b를 OutputStream으로 내보낸다
 */
public void write(byte b[]) throws IOException;

// Main method
ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
outputStream.write(new byte[]{1, 2}); // outpustream에는 [1, 2]이 들어있다
/**
 * byte 배열 b를 off부터 len만큼 OutputStream으로 내보낸다
 */
public void write(byte b[], int off, int len) throws IOException;
```



### OutputStream은 버퍼를 비울 수 있다

```
/**
 * 버퍼가 존재하는 경우, 해당 버퍼에서 데이터를 모두 목적지로 보내는 역할을 수행한다
 * ByteArrayOutputStream의 경우 버퍼가 없어 아무런 영향이 없다
 */
public void flush() throws IOException { }
```



### OutputStream은 닫을 수 있다

통로를 부실 수 있는 것이다

```
public void close() throws IOException;
```



## 정리하면

OutputStream이 InputStream보다 훨씬 간단하네요 ㅎㅎㅎ

OutputStream이 갖춰야 할 덕목으로는

- 데이터 쓰기
- 버퍼 비우기
- 통로 끊기





#### 참고

https://lannstark.tistory.com/50?category=840464

https://bamdule.tistory.com/179