# 进程间不共享全局变量

import multiprocessing
import time


global_list = []


def send_function():
    for i in range(3):
        global_list.append(i)
    print("send_data:{}".format(global_list))


def receive_function():
    print("receive_data:{}".format(global_list))


if __name__ == '__main__':
    send = multiprocessing.Process(target=send_function)
    receive = multiprocessing.Process(target=receive_function)
    send.start()
    time.sleep(1)   # 等待 send_function() 修改完全局变量后再读取
    receive.start()
