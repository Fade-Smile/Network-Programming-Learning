#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :30-多线程之局部变量不会造成数据混乱.py
@Author  :Sunshine
@Date    :10/11/2023 12:52 
'''

import threading
import time


def run():
    print("当前进程%s,开始启动" % threading.current_thread().name)
    g_num = 0
    for _ in range(500000):
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
    print("主线程结束")