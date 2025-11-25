import time

def sync_non_blocking():
    print("1. 다운로드 요청")

    # 소켓을 '논블로킹 모드'로 설정
    network.socket.setblocking(False)

    # [Polling] 반복해서 확인
    data = None
    while not data:
        try:
            # [Non-blocking] 데이터 없으면 즉시 에러(EwouldBlock) 발생 후 리턴
            data = network.socket.recv()
        except BlockingIOError:
            print(" 데이터 아직 안옴(딴짓 가능하지만, 확인하느라 바쁜)")
            # 여기서 잠깐 딴짓을 할 수 있지만, 다시 금방 확인하러 와야함
            time.sleep(0.1)
    
    print(f"2. 데이터 수신 완료: {data}")
    print("3. 다음 작업 진행")

sync_non_blocking()