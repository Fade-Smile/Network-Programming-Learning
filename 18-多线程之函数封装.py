#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :18-多线程之函数封装.py
@Author  :Sunshine
@Date    :05/11/2023 12:32 
'''
import threading
import time, os


def run(name):
    for i in range(3):
        print('线程名称: %s, 输出:%d' % (name,i))
        time.sleep(1)


if __name__ == '__main__':
    print('主线程开始时间: %s' % time.time())

    # 创建多个线程
    s = 'abcde'
    for i in range(5):
        t = threading.Thread(target=run, name=s[i], args=(s[i],))   # 创建线程
        t.start()  # 线程启动

    print('主线程结束')
