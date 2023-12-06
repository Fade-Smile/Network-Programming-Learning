#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :14-multiprocess-创建子进程【类】.py
@Author  :Sunshine
@Date    :31/10/2023 14:59 
'''

# 分装一个进程类
from multiprocessing import Process
import os
import time

a = 100  # 全局变量


# 自定义一个进程类
class MyProcess(Process):

    def __init__(self, xname):
        Process.__init__(self)  # 加载父类给我们提供的功能
        self.name = xname

    def run(self):  # 子进程在运行过程中运行的函数
        print('当前进程的ID', os.getpid())  # getpid() 获取当前调用函数的进程 id
        print('父进程的ID', os.getppid())  # getppid() 获取当前进程的父进程 id
        print('当前进程的名字', self.name)
        a = 200
        print('子进程里面打印a', a)
        time.sleep(3)


if __name__ == '__main__':

    # 当前开始的时间戳
    start = time.time()
    # 创建10个子进程放入一个列表中
    process_list = []
    for i in range(10):
        p = MyProcess('process-%d' % (i + 1))  # 创建我们自定义的进程类
        p.start()
        process_list.append(p)
        # p.join()  # 若join 放在这里就变成了, 这样父进程会等待每个子进程一个接一个地执行完毕。

    for i in process_list:
        # 我们一般都会需要父进程等待所有子进程结束， 才执行后面的代码
        # join 等待当前的子进程p结束
        p.join()  # 10 个子进程可以并行执行

    # 所有子进程结束
    r = time.time() - start
    print('10个子进程一共执行的时间是', r)
    print('父进程后打印', a)
