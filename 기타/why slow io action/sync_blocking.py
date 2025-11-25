import time

def sync_blocking():
    print("1. 다운로드 요청(제어권 넘겨줌, 결과 기다림)")

    # [Blocking] 3초 동안 여기서 코드 실행이 멈춥니다.
    # 이 줄이 끝나야 다음 줄로 넘어갑니다.
    data = network.download_file()

    print(f"2. 데이터 수신 완료: {data}")
    print("3. 다음 작업 진행")


sync_blocking()