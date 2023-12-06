#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :37-多线程之Event.py
@Author  :Sunshine
@Date    :12/11/2023 12:42 
'''

# # 线程1 代表 门， 一开始是开着的状态， 每3三秒需要自动关闭一下， 如果有人通过， 需要重新刷卡打开。
# 线程2 代表 人， 人通过门， 如果门是打开的直接通过， 如果没有打开需要刷卡。 之后门就打开了， 通知人继续进入。

import threading
import time
import random

event = threading.Event()  # 创建一个事件， 默认为False
event.set()  # 设置标志为真， 门一开始就是打开的

door_status = 0  # 代表门的状态， 如果是0~3(不包括3) 代表打开， 如果等于3，代表需要关闭


def door():
    global door_status
    while True:
        print("当前门的door_status为:{}".format(door_status))

        if door_status >= 3:
            print("当前门已经打开3秒, 需要自动关闭!")
            event.clear()

        if event.is_set():
            print("当前门是开着的, 可以通过!")
        else:
            print("门已经关了, 请用户自己刷卡!")
            event.wait()  # 门的线程阻塞等待
            continue   # 当门的线程阻塞后, 结束当前循环
        time.sleep(1)
        door_status += 1  # door_status 代表门开着的秒数


def person():
    global door_status
    n = 0  # 人的计数器， 用于统计进入这个门的人数

    while True:
        if event.is_set():
            n += 1
            print("门开着, 第{}号人通过了这个门".format(n))
        else:
            print("门关着, 第{}号人刷卡之后， 通过这个门".format(n))
            event.set()  # 标志修改为True
            door_status = 0
        time.sleep(random.randint(1, 10))  # 当人通过后， 门随机休眠1-10秒
        print()


if __name__ == '__main__':
    d = threading.Thread(target=door)
    p = threading.Thread(target=person)

    d.start()
    p.start()
