#! /user/bin/env python
# -*- coding: utf-8 -*-
"""
@author: FLBa
@contact: lz17370837860@163.com
@software: PyCharm
@project: Mutli_Process-main
@file: demo6.py.py
@date: 2022-06-14 10:24
@desc: 
"""
# Pool

from multiprocessing import Pool
import time
import os
import random


def send_message(msg):
    t_start = time.time()
    print("{} 开始执行，进程编号为 {}".format(msg, os.getpid()))
    # time.sleep(0.11)
    time.sleep(random.random()*2)
    t_stop = time.time()
    print('{} 执行完毕， 用时 {} '.format(msg, t_stop - t_start))


if __name__ == '__main__':
    po = Pool(processes=3)
    for i in range(0, 10):
        po.apply_async(send_message, (i,))

    print("----------start------------     {}".format(os.getpid()))
    po.close()  # 关闭进程池，使其不接收新的任务
    po.join()  # 等待进程池里的任务结束，主进程再退出
    print("-----------end-------------")
