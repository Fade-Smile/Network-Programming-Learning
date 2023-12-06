#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :22-多线程之获取线程数量.py
@Author  :Sunshine
@Date    :05/11/2023 13:02 
'''
import threading
import time, os


def run(name):
    for i in range(3):
        print('线程名称: %s, 输出:%d' % (name, i)) #自定义的线程类，可以从文类中继承name属性
        time.sleep(1)


if __name__ == '__main__':
    print('主线程开始时间: %s' % time.time())

    # 创建多个线程
    s = 'abcde'
    for i in range(5):
        t = threading.Thread(target=run, name=s[i], args=(s[i],))  # 创建线程, 里面参数代表线程的名字，如果不传，系统会默认有一个名字
        t.start()  # 线程启动
    while True:
        count = len(threading.enumerate())  # 获得当前正在运行的线程数量
        print('当前正在执行的线程数量为: %s' % count)
        if count <= 1:
            break

    print('主线程结束')
