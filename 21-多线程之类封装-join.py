#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :21-多线程之类封装-join.py
@Author  :Sunshine
@Date    :05/11/2023 13:39 
'''
from threading import Thread
from time import sleep, time


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("Threading:{} start".format(self.name))
        sleep(3)
        print("Threading:{} end".format(self.name))


if __name__ == '__main__':
    '''入口'''
    # 开始时间
    start = time()
    # 创建线程列表
    t_list = []
    # 循环创建线程
    for i in range(10):
        t = MyThread(f"t{i}")
        t.start()
        t_list.append(t)

    # 等待线程结束
    for t in t_list:
        t.join()
    # 计算时间
    end = time() - start
    print(end)
