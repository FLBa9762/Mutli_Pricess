import multiprocessing
import time


def test_code(number):
    multi = 1
    for i in range(1, number):
        multi *= i
    return multi


def process1():
    multi1 = test_code(100000)
    # print("this is process1, {}".format(multi1))


def process2():
    multi2 = test_code(100000)
    # print("this is process2, {}".format(multi2))


def run():

    task1 = multiprocessing .Process(target=process1)
    task2 = multiprocessing .Process(target=process2)
    task1.start()
    task2.start()
    # 等待子进程 task1 和 task2 执行结束后再执行后边代码
    task1.join()
    task2.join()


def run_1():
    start = time.time()
    process1()
    process2()
    end = time.time()
    time_used = end - start
    print("Normal Time Used: {}".format(time_used))


if __name__ == '__main__':
    start = time.time()
    run()
    end = time.time()
    time_used = end - start
    print("MultiProcess Time Used: {}".format(time_used))
    run_1()
