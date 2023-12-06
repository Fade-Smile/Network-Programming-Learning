#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :34-多线程之线程通信-信号量.py
@Author  :Sunshine
@Date    :10/11/2023 14:02 
'''

# 信号量: 设置在多线程中，并行运行的线程个数
# 这种信号量机制对于控制并发访问共享资源是很有用的，可以确保在同一时刻最多有指定数量的线程能够访问敏感资源。
import threading
import time

semapshore = threading.BoundedSemaphore(3)  # 一次只运行同时三个人过安检
#  semapshore 的 BoundedSemaphore 对象。BoundedSemaphore 是 Python 中的信号量（Semaphore）实现之一，
#  它是一种控制多个线程访问共享资源的方法。

# 表示创建了一个有界信号量，其初始值为 3。
# 有界信号量允许一定数量的线程同时访问共享资源，而超过这个数量的线程需要等待其他线程释放信号量后才能继续执行。


def run(num):
    semapshore.acquire()
    print('第{}个人正在过安检'.format(num))
    time.sleep(2)
    semapshore.release()


if __name__ == '__main__':
    for i in range(100):
        thread = threading.Thread(target=run, args=(i,))
        thread.start()
