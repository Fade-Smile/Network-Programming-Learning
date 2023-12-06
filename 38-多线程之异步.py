#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :38-多线程之异步.py
@Author  :Sunshine
@Date    :12/11/2023 13:25 
'''

from multiprocessing import Pool
import os
import time


def father():
    print("当前进程ID:{0}, 它的父进程是:{1}".format(os.getpid(), os.getppid()))
    print("女儿叫你起床, 你开始慢慢起床")
    time.sleep(3)
    print("3秒之后。。。")
    print("你起床了")
    return 'Father wake up'


def daughter():
    print("女儿开始早读, 当前进程是:%s" % os.getpid())
    time.sleep(5)
    print("5秒之后。。。")
    print("女儿早读完成")


# test3任务 是前面异步任务test1完成了, 才调用test3
def together(args):
    # time.sleep(5)
    print(f"最后一起吃早餐, 当前进程的id:{os.getpid()}")
    print("参数是:%s" % args)


if __name__ == '__main__':
    # 女儿使用 主进程代表
    # 父亲使用 进程池中的某个子进程代表

    # 创建进程池
    pool = Pool(4)
    pool.apply_async(func=father, callback=together)   # callback 表示回调函数. 主进程自动调用的
    # 回调函数是一种在特定事件发生或异步操作完成时执行的函数。
    # 这个函数通常作为参数传递给另一个函数，以便在适当的时候调用。
    # 回调函数用于实现异步编程、事件处理和处理异步任务完成后的操作。

    # 主进程代表女儿， 叫父亲起床后， 继续自己的早读
    daughter()

    print("主进程结束, 主进程ID:%s" % os.getpid())


"""
1. father 函数：模拟父亲起床的过程。它在标准输出中打印一些消息，然后返回字符串 'Father wake up'。

2. daughter 函数：模拟女儿早读的过程。同样，在标准输出中打印一些消息。

3. together 函数：回调函数，用于在 father 函数异步执行完成后被调用。它打印一些消息，其中包括异步任务的结果。

4. 进程池创建：Pool(4) 创建了一个包含4个进程的进程池。

5. 异步执行 father 任务：pool.apply_async(func=father, callback=together) 将 father 任务异步提交给进程池中的某个子进程执行。
这个异步任务执行完成后，会调用 together 函数作为回调函数。

6. 主进程执行 daughter 任务：在主进程中，调用 daughter 函数，模拟女儿早读的过程。

7. 输出信息：在标准输出中打印了一系列的消息，包括父亲起床、女儿早读、最后一起吃早餐等。


同步: 在同步执行中，任务按照顺序依次执行，一个任务的执行会阻塞后续任务的执行，直到前一个任务完成。
在这里，daughter 函数是在主进程中同步执行的，它会等待 father 函数异步执行完成后才继续执行。

异步: 在异步执行中，任务的执行不会阻塞后续任务。
在这里，father 函数是异步执行的，即主进程不会等待其完成就继续执行后续任务。
异步执行通常用于提高程序的并发性和性能。
"""