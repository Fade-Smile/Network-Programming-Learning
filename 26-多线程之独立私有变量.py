#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :26-多线程之独立私有变量.py
@Author  :Sunshine
@Date    :06/11/2023 14:05 
'''
import threading
import random, time
# 让每个线程拥有一个独立的私有变量


def run():
    # 创建一个独立的, 私有变量
    local_var = threading.local()
    local_var.numbers = [1]  # 每个线程先给一个初始值1
    # 为了模拟线程执行的时间不同
    time.sleep(random.random())  # 随机休眠时间
    for h in range(8):
        # 在私有变量中, 放入随机的数字
        local_var.numbers.append(random.choice(range(10)))
    # 打印当前线程的私有变量值
    print(threading.current_thread(), local_var.numbers)


if __name__ == '__main__':

    threads_lst = []  # 线程列表, 方便调用join

    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
        threads_lst.append(t)

    for j in threads_lst:
        t.join()
