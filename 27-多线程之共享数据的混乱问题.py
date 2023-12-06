#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :27-多线程之共享数据的混乱问题.py
@Author  :Sunshine
@Date    :06/11/2023 14:19 
'''

import threading
import time

g_num = 0


def run():
    print("当前进程%s,开始启动" % threading.current_thread().name)
    global g_num
    for _ in range(500000):
    # for _ in range(5000):  # 无问题, 执行时间太短
        g_num += 1
    print("线程%s,执行之后g_num的值为:%s" % (threading.current_thread().name, g_num))


if __name__ == '__main__':
    threads_lst = []
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()
        threads_lst.append(t)

    for j in threads_lst:
        j.join()
    print("主线程结束, g_num的值为:%s" % g_num)
