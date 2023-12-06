#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :24-多线程之线程之间数据共享.py
@Author  :Sunshine
@Date    :06/11/2023 13:37 
'''

# 所有子线程传入一个共同的参数，作为所有子线程的共享数据
from threading import Thread
import time

# 定义一个全局变量
global_num = 0


def run1():
    global global_num
    # time.sleep(1)
    for i in range(10):
        global_num += 1
    print("线程1， 执行之后的结果为: %d" % global_num)


def run2():
    global global_num
    # for i in range(10):
    #     global_num -= 1
    print("线程2， 执行之后的结果为: %d" % global_num)


if __name__ == '__main__':
    '''入口'''
    # 创建2个线程
    t1 = Thread(target=run1)
    t2 = Thread(target=run2)

    t1.start()
    time.sleep(1)  # 延迟1秒， 保证线程1所有的工作已经做完。
    t2.start()

    print('主线程结束, 全局变量global_num的值为:%d' % global_num)
