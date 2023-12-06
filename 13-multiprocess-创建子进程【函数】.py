#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :13-multiprocess-创建子进程【函数】.py
@Author  :Sunshine
@Date    :31/10/2023 14:35 
'''

# 创建一个子进程来调用某个函数
from multiprocessing import Process
import os
import time


def func1(name):
    print('当前进程的ID', os.getpid())  # getpid() 获取当前调用函数的进程 id
    print('父进程的ID', os.getppid())  # getppid() 获取当前进程的父进程 id
    print('当前进程的名字', name)

    time.sleep(3)


# 入口
if __name__ == '__main__':
    start = time.time()
    # 常见多个子进程， 来调用func1函数
    for i in range(10):
        p = Process(target=func1, args=('进程%d' % i,))  # 创建一个子进程
        p.start()  # 开始子进程

    print('父进程的代码执行完成')

    # 父进程的代码中默认没有任何阻塞，同时父进程必须等待所有子进程结束之后才停止
