#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :31-多线程之局部变量不会造成数据混乱-1.py
@Author  :Sunshine
@Date    :10/11/2023 12:52 
'''

import threading
import time


class MyThread(threading.Thread):
    # 重写 构造方法
    def  __init__(self, num, sleepTime):
        threading.Thread.__init__(self)
        self.num = num
        self.sleepTime = sleepTime

    def run(self):
        self.num += 1
        time.sleep(self.sleepTime)
        print('线程(%s), num = %d'% (self.name, self.num))


if __name__ == '__main__':
    lock = threading.Lock()
    t1 = MyThread(100, 5)
    t1.start()
    t2 = MyThread(200, 1)
    t2.start()