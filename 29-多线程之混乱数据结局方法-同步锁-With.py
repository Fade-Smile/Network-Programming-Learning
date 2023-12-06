#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :29- 多线程之混乱数据结局方法-同步锁-with.py
@Author  :Sunshine
@Date    :06/11/2023 14:50 
'''
import threading
import time

g_num = 0


def run():
    print("当前进程%s,开始启动" % threading.current_thread().name)
    global g_num
    # 获得这把锁的钥匙，同时会自动释放这把锁
    with lock:
        for _ in range(500000):
        # for _ in range(5000):  # 无问题, 执行时间太短
            g_num += 1
    print("线程%s,执行之后g_num的值为:%s" % (threading.current_thread().name, g_num))


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