#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :20-多线程之函数封装-join.py
@Author  :Sunshine
@Date    :05/11/2023 13:36 
'''
from threading import Thread
from time import sleep, time


def run(name):
    '''执行任务'''
    print("Threading:{} start".format(name))
    sleep(3)
    print("Threading:{} end".format(name))


if __name__ == '__main__':
    '''入口'''
    # 开始时间
    start = time()
    # 创建线程列表
    t_list = []
    # 循环创建线程
    for i in range(10):
        t = Thread(target=run, args=('t{}'.format(i),))
        t.start()
        t_list.append(t)
    # 等待线程结束
    for t in t_list:
        t.join()
    # 计算使用时间
    end = time() - start
    print(end)