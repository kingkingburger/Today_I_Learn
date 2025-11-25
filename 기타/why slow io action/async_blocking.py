import concurrent.futures

def async_blocking():

    #  [Async] 별도 일꾼(Thread)에게 작업을 시킴
    future = thread_pool.submit(network.download_file)

    print('여기서 다른일을 할 수 있는데')

    # [Blocking] 시켜놓고 결과가 나올 때 까지 멈춰서 기다림
    #  비동기의 장점을 스스로 없에버림
    result = future.result()

    print(f"2. 데이터 수신 완료: {result}")
    print("3. 다음 작업 진행")

async_blocking()