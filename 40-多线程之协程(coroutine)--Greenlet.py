#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :40-多线程之协程(coroutine)--Greenlet.py
@Author  :Sunshine
@Date    :14/11/2023 12:36 
'''
from greenlet import greenlet


# 开发协程的案例
#  一个任务是回答
#   一个任务是问


def ask(name):
    print('%s: 我要买个手提包!' % name)  # 1
    b.switch('吕布')  # answer函数第一次切换，需要传参
    print('%s: 我想学Python!' % name)  # 3
    b.switch()


def answer(name):
    print('%s: 买买买!'% name)  # 2
    a.switch()
    print('%s: OK!' % name)  # 4


if __name__ == '__main__':
    a = greenlet(ask)  # 创建一个协程
    b = greenlet(answer)  # 创建第二个参数

    a.switch('貂蝉')  # 每个函数只有在第一次切换的时候才需要传参，后面不需要
    # switch() 函数用于在不同的协程之间进行切换
