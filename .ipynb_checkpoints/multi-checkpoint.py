#multithreading을 사용함. 물리적으로 cpu코어를 활용하여 병렬처리

import multiprocessing
import time as t


def long_task(): # 일거리를 길게 만들기
    for w in range(5):
        print(f"일하는 중...{w+1}")
        t.sleep(1)

if __name__ == "__main__":
    start = t.time()
    print("=====start=====")

    processes = []
    for n in range(5):
        p = multiprocessing.Process(target=long_task)
        processes.append(p)

    for pr in processes:
        pr.start()  # 프로세스 시작
    for pr in processes:
        pr.join()   # 프로세스가 끝날 때까지 기다림 waiting

    print("=====end======= ")

    print(f"총 작업 시간: {t.time() - start:.2f}초")
