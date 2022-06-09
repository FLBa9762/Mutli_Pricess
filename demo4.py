# 主进程和子进程的结束顺序

import multiprocessing
import time


def work():
    for i in range(10):
        print("working!")
        time.sleep(0.2)


if __name__ == '__main__':
    process = multiprocessing.Process(target=work)
    # process.daemon = True     # 守护主进程
    process.start()
    time.sleep(1)
    process.terminate()     # 手动结束子进程
    print("主进程完毕！")

