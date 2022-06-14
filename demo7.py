#! /user/bin/env python
# -*- coding: utf-8 -*-
"""
@author: FLBa
@contact: lz17370837860@163.com
@software: PyCharm
@project: Mutli_Process-main
@file: demo7.py
@date: 2022-06-14 15:02
@desc: 
"""
# Pipe

import multiprocessing


def send_message(conn_1):
    conn_1.send("send_message!!!")
    print("conn1 send message: {}".format("send_message!!!"))
    data = conn_1.recv()
    print("ok, finish ! {}".format(data))


def receive_message(conn2):
    data = conn2.recv()
    print("conn2 receive data: {}".format(data))
    conn2.send("conn2 received message")
    print("conn2 send message:{}".format("conn2 received message"))


if __name__ == '__main__':
    conn_1, conn_2 = multiprocessing.Pipe(duplex=True)
    p1 = multiprocessing.Process(target=send_message, args=(conn_1,))
    p2 = multiprocessing.Process(target=receive_message, args=(conn_2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()