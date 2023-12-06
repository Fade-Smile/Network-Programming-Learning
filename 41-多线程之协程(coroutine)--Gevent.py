#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :41-多线程之协程(coroutine)--Gevent.py
@Author  :Sunshine
@Date    :14/11/2023 13:50 
'''
import gevent


# 开发协程的案例
#  一个任务是回答
#   一个任务是问


def ask(name):
    print('%s: 我要买个手提包!' % name)  # 1
    gevent.sleep(0)  # 人为模拟IO阻塞
    # gevent.sleep()是一个用于暂停当前 Greenlet 协程执行的函数，类似于 Python 中的time.sleep()函数。
    # 但与time.sleep()不同的是，gevent.sleep()是协程友好的，它会让出执行权给其他可以运行的协程，而不是阻塞
    print('%s: 我想学Python!' % name)  # 3


def answer(name):
    print('%s: 买买买!' % name)  # 2
    gevent.sleep(0)
    print('%s: OK!' % name)  # 4


if __name__ == '__main__':
    # gevent.spawn()函数的作用是创建一个新的Greenlet协程对象，并将指定的函数以及它的参数传递给该协程。
    # 然后立即启动这个协程，使其开始执行。
    # 这个函数返回一个表示新协程的Greenlet对象，您可以使用这个对象来控制和管理这个协程的行为。
    a = gevent.spawn(ask, '小乔')
    b = gevent.spawn(answer, '周瑜')

    #  使用 joinall() 等待所有的 Greenlet 对象执行完毕，这里的Greenlet对象是指 a 和 b
    gevent.joinall([a, b])  # 自动切换并行执行
