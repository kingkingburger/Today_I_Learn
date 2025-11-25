def on_complete(data):
    print(f"3. [알림] 데이터 수신 완료: {data}")

def async_non_blocking():
    print('1. 다운로드 요청(콜백 함수 등록)')

    # [Non-blocking + async]
    # "다운로드 해줘. 끝나면 on_complete 함수 실행해줘." 라고 말하고 즉시 리턴
    network.download_file(on_complete)

    print("2. 기다리지 않고 내 할 일 계속한다 (Ui 업데이트, 계산 등)")

async_non_blocking()