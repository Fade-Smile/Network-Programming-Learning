#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :16-multiprocess-pipe-一对一进程通信.py
@Author  :Sunshine
@Date    :03/11/2023 14:04 
'''


import os, time
from multiprocessing import Process, Pipe


# 创建两个进程，一个进程负责读, 一个进程负责写

# 负责写的进程(发送数据包的进程)
class WriteProcess(Process):

    def __init__(self, xname, pipe):
        Process.__init__(self)
        self.name = xname
        self.pipe = pipe

    def run(self):
        # 把多条数据写入到队列中
        print('进程名字: %s, ID: %s; 已经启动' % (self.name, os.getpid()))
        for i in range(1, 6):
            self.pipe.send(i)  # write 进程负责把数据通过管道发送给另一个进程
            time.sleep(1)  # 休眠1秒
        print("进程名字:%s, 进程ID: %s; 已经结束" % (self.name, os.getpid()))


# 负责读取队列中的数据
class ReadProcess(Process):

    def __init__(self, xname, pipe):
        Process.__init__(self)
        self.name = xname
        self.pipe = pipe

    def run(self):
        print('进程名字: %s, ID: %s; 已经启动' % (self.name, os.getpid()))
        while True:
            # get 是一个阻塞函数
            value = self.pipe.recv()  # 从管道中获取一个数据项。如果管道为空，那么调用recv方法会阻塞当前进程直到管道中有数据。
            print(value)
        # 这行代码不会执行
        print('进程名字: %s, ID: %s; 已经结束' % (self.name, os.getpid()))


if __name__ == '__main__':
    p1, p2 = Pipe()  # 创建一个多进程管道， 会得到管道的两端
    pw = WriteProcess('Writer', p2)
    pr = ReadProcess('Read', p1)

    # 启动两个进程
    pw.start()
    pr.start()

    # 让父进程等待子进程结束
    pw.join()
    # pr进程是一个死循环
    pr.terminate()  # 强制结束pr进程
    print('父进程结束')
