#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :32-多线程之死锁.py
@Author  :Sunshine
@Date    :10/11/2023 13:19 
'''

import threading
import time

# 鱼 锁
mutex_Yu = threading.Lock()
# 熊掌 锁
mutex_XiongZhang = threading.Lock()  # mutex stands for mutual exclusion (互斥)


class MyThread1(threading.Thread):
    def run(self):
        mutex_Yu.acquire()  # 获取 鱼 锁
        print("线程1 已经得到鱼了")
        time.sleep(1)

        mutex_XiongZhang.acquire()  # 获取 熊掌 锁
        print("线程2 得到熊掌")

        mutex_Yu.release()  # 释放 鱼 锁
        mutex_XiongZhang.release()  # 释放 熊掌 锁


class MyThread2(threading.Thread):
    def run(self):
        mutex_XiongZhang.acquire()  # 获取 熊掌 锁
        print("线程2 获取到熊掌")
        time.sleep(1)

        mutex_Yu.acquire()  # 获取 鱼 锁
        print("线程2 得到鱼")

        mutex_XiongZhang.release()
        mutex_Yu.release()


# 第二种死锁情况
# mutex_TianTang = threading.Lock()  # 去天堂的锁  Lock() 是互斥锁。  可以使用逻辑锁， 这样就不会死锁了
mutex_TianTang = threading.RLock()  # RLock 是逻辑锁 但是针对一个线程才可以使用逻辑锁


class MyThread3(threading.Thread):
    def run(self):
        mutex_TianTang.acquire()  # 获取 去天堂的锁
        print("线程3 进入天堂")
        time.sleep(1)
        self.run()  # 再次进入天堂

        mutex_TianTang.release()


if __name__ == '__main__':
    # t1 = MyThread1()
    # t2 = MyThread2()
    #
    # t1.start()
    # t2.start()

    t3 = MyThread3()
    t3.start()
