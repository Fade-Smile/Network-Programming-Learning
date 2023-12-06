#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :28-多线程之混乱数据结局方法-同步锁-Lock.py
@Author  :Sunshine
@Date    :06/11/2023 14:50 
'''
import threading
import time

g_num = 0


def run():
    # 该方法用于获取锁，也称为互斥锁（互斥的缩写），这是一种同步机制，
    # 用于确保一次只有一个线程可以访问代码的关键部分。获取锁的目的是防止多个线程同时执行代码，
    # 这些代码在访问共享资源时可能导致争用条件或数据损坏。
    lock.acquire()
    print("当前进程%s,开始启动" % threading.current_thread().name)
    global g_num
    for _ in range(500000):
    # for _ in range(5000):  # 无问题, 执行时间太短
        g_num += 1
    print("线程%s,执行之后g_num的值为:%s" % (threading.current_thread().name, g_num))
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建同步锁
    lock = threading.Lock()
    threads_lst = []

    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
        threads_lst.append(t)

    for j in threads_lst:
        j.join()
    print("主线程结束, g_num的值为:%s" % g_num)