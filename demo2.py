# 带有参数的进程

# import multiprocessing
# import time
# import os
#
#
# def test_code(number):
#     multi = 1
#     for i in range(1, number):
#         multi *= i
#     return multi
#
#
# def process1(num):
#     multi1 = test_code(num)
#     print("process1:{}".format(os.getppid()))
#     # print("this is process1, {}".format(multi1))
#
#
# def process2(num):
#     multi2 = test_code(num)
#     print("process2:{}".format(os.getppid()))
#     # print("this is process2, {}".format(multi2))
#
#
# def run():
#     task1 = multiprocessing .Process(target=process1, args=(100000,))
#     task2 = multiprocessing .Process(target=process2, args=(100000,))
#     print("run:{}".format(os.getpid()))
#     task1.start()
#     task2.start()
#     task1.join()
#     task2.join()
#
#
# if __name__ == '__main__':
#     start = time.time()
#     print("main:{}".format(os.getpid()))
#     run()
#     end = time.time()
#     time_used = end - start
#     print("MultiProcess Time Used: {}".format(time_used))


import multiprocessing
import time
import os

#子进程
def process1(num):
    print("process1:{}".format(os.getppid()))

#子进程
def process2(num):
    print("process2:{}".format(os.getppid()))

#父进程
def run():
    print("run:{}".format(os.getpid()))
    task1 = multiprocessing .Process(target=process1, args=(100000,))
    task2 = multiprocessing .Process(target=process2, args=(100000,))
    task1.start()
    task2.start()

#父进程
if __name__ == '__main__':
    print("main:{}".format(os.getpid()))
    run()
