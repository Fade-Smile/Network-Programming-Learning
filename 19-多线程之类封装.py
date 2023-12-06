#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :19-多线程之类封装.py
@Author  :Sunshine
@Date    :05/11/2023 12:43 
'''
import threading
import time, os


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print('线程名称: %s, 输出:%d' % (self.name, i))  # 自定义的线程类， 可以从父类中继承name属性
            time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    print('主线程开始时间: %s' % start)

    thread_lst = []
    # 创建多个线程
    s = 'abcde'
    for i in range(5):
        t = MyThread(name=s[i])  # 创建线程，里面参数代表线程的名字，如果不传，系统会默认有一个名字
        t.start()  # 线程启动
        thread_lst.append(t)

    end = time.time()

    print('主线程结束, 中间执行的时间为%.2f' % (end - start))


