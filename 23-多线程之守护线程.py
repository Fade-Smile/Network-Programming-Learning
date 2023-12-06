#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :23-多线程之守护线程.py
@Author  :Sunshine
@Date    :05/11/2023 13:46 
'''

import threading
import time, os


class MyThread(threading.Thread):

    def run(self):
        for i in range(3):
            print('线程名称: %s, 输出:%d' % (self.name, i))
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print('主线程开始时间: %s' % start)

    # 创建1个线程
    t = MyThread(name='my_thread-1')  # 创建线程，里面参数代表线程的名字，如果不传，系统会默认有一个名字
    # t.setDaemon(True) # 设置守护线程，里面参数代表线程的名字，如果不传，系统会默认有一个名字
    t.daemon=True
    t.start()  # 启动线程

    # 等待所有的于线程都停止之后，主线程才中止
    time.sleep(1)

    end = time.time()
    print('主线程结束, 中间执行的时间为%.2f' % (end - start))