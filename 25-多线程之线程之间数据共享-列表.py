#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :25-多线程之线程之间数据共享-列表.py
@Author  :Sunshine
@Date    :06/11/2023 13:52
'''

# 所有子线程传入一个共同的参数，作为所有子线程的共享数据
from threading import Thread
import time


def run1(num):
    for i in range(10):
        num[0] += 1
    print("线程1， 执行之后的结果为: %d" % num[0])


def run2(num):
    print("线程2， 执行之后的结果为: %d" % num[0])


if __name__ == '__main__':
    '''入口'''
    i = [0]  # i 变量为了多个线程可以共享，我们必须使用可变类型
    # 创建2个线程
    t1 = Thread(target=run1, args=(i,))
    t2 = Thread(target=run2, args=(i,))

    t1.start()
    time.sleep(1)  # 延迟1秒， 保证线程1所有的工作已经做完。
    t2.start()

    print('主线程结束, 全局变量global_num的值为:%d' % i[0])
