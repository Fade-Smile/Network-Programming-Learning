#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :17-进程池Pool.py
@Author  :Sunshine
@Date    :03/11/2023 14:44 
'''

from multiprocessing.pool import Pool
import os, time
import random


# 打印进程的信息, 并且记录该进程执行的时长
def run(name):
    start = time.time()
    print('进程名字: %s, ID: %s; 已经启动' % (name, os.getpid()), end='\n')

    time.sleep(random.choice([1, 2, 3, 4, 5]))  # 进程随机休眠秒速
    end = time.time()
    print('进程名字: %s, ID: %s; 已经结束了， 耗时%.2f' % (name, os.getpid(), end - start), end='\n')


if __name__ == '__main__':
    p = Pool(5)  # CPU的核心数
    for i in range(10):
        # 请求得到一个进程， 然后异步（非阻塞式调用）调用run函数
        p.apply_async(run, ('process' + str(i),))
    p.close()
    p.join()
    print('父进程结束')
