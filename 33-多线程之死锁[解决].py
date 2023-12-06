#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :33-多线程之死锁[解决].py
@Author  :Sunshine
@Date    :10/11/2023 13:19 
'''
# 让多个线程交叉有序的竞争多个资源
import threading
import time

# 鱼 锁
mutex_Yu = threading.Lock()
# 熊掌 锁
mutex_XiongZhang = threading.Lock()  # mutex stands for mutual exclusion (互斥)


class MyThread1(threading.Thread):
    def run(self):
        while True:
            mutex_Yu.acquire()  # 获取 鱼 锁
            print("线程1 已经得到鱼了")
            time.sleep(1)
            mutex_Yu.release()  # 释放 鱼 锁

            mutex_XiongZhang.acquire()  # 获取 熊掌 锁
            print("线程2 得到熊掌")
            time.sleep(1)
            mutex_XiongZhang.release()  # 释放 熊掌 锁


class MyThread2(threading.Thread):
    def run(self):
        while True:
            mutex_XiongZhang.acquire()  # 获取 熊掌 锁
            print("线程2 获取到熊掌")
            time.sleep(1)
            mutex_XiongZhang.release()  # 获取 熊掌 锁

            mutex_Yu.acquire()  # 获取 鱼 锁
            print("线程2 得到鱼")
            time.sleep(1)
            mutex_Yu.release()  # 释放 熊掌 锁


if __name__ == '__main__':
    t1 = MyThread1()
    t2 = MyThread2()

    t1.start()
    t2.start()
