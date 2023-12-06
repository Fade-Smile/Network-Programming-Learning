#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :15-multiprocess-queue-多个进程之间实现通信.py
@Author  :Sunshine
@Date    :03/11/2023 13:38 
'''

import os
import time
from multiprocessing import Process, Queue


# 创建两个进程，一个进程负责读, 一个进程负责写

# 负责写的进程(发送数据包的进程)
class WriteProcess(Process):

    def __init__(self, xname, mq):
        Process.__init__(self)
        self.name = xname
        self.mq = mq

    def run(self):
        # 把多条数据写入到队列中
        print('进程名字: %s, ID: %s; 已经启动' % (self.name, os.getpid()))
        for i in range(1, 6):
            self.mq.put(i)  # write 进程负责把数据写入Queue
            time.sleep(1)  # 休眠1秒
        print("进程名字:%s, 进程ID: %s; 已经结束" % (self.name, os.getpid()))


# 负责读取队列中的数据
class ReadProcess(Process):

    def __init__(self, xname, mq):
        Process.__init__(self)
        self.name = xname
        self.mq = mq

    def run(self):
        print('进程名字: %s, ID: %s; 已经启动' % (self.name, os.getpid()))
        while True:
            # get 是一个阻塞函数
            value = self.mq.get(True)  # 从队列中获取一个数据项。如果队列为空，那么调用get方法会阻塞当前进程直到队列中有数据。
            print(value)
        # 这行代码不会执行
        print('进程名字: %s, ID: %s; 已经结束' % (self.name, os.getpid()))


if __name__ == '__main__':
    q = Queue()  # 创建一个多进程共享的队列，可以安全地在多个进程之间传递数据。

    pw = WriteProcess('Writer', q)
    pr = ReadProcess('Read', q)

    # 启动两个进程
    pw.start()
    pr.start()

    # 让父进程等待子进程结束
    pw.join()
    # pr进程是一个死循环
    pr.terminate()  # 强制结束pr进程
    print('父进程结束')
