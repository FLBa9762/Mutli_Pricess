#! /user/bin/env python
# -*- coding: utf-8 -*-
"""
@author: FLBa
@contact: lz17370837860@163.com
@software: PyCharm
@project: Mutli_Process-main
@file: demo5.py
@date: 2022-06-14 09:30
@desc: 
"""
# Queue


from multiprocessing import Queue
import multiprocessing
import numpy as np
import time


def episode(q):
    data = np.arange(1, 11)
    for i in data:
        q.put(i)


def send_message(q):
    for epi in range(10):
        print("episode: {}".format(epi))
        episode(q)
        time.sleep(0.5)
    print("send_done! ")


def receive_message(q):
    receiver = []
    i = 0
    while True:
        rec = q.get()
        receiver.append(rec)
        print("receive: {}".format(i))
        i += 1


def run():
    q = Queue(20)
    print(q.qsize())
    process1 = multiprocessing.Process(target=send_message, args=(q,))
    process2 = multiprocessing.Process(target=receive_message, args=(q,))
    process1.start()
    # process1.join()
    process2.start()


if __name__ == '__main__':
    run()
