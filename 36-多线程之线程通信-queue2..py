#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :36-多线程之线程通信-queue2.py
@Author  :Sunshine
@Date    :10/11/2023 14:14 
'''

import threading, queue
import time

# 创建队列
q = queue.Queue(1)  # 先进先出的队列 【FIFO】
# q = queue.LifoQueue  # 后进先出的队列
# q = queue.PriorityQueue  # 优先级的队列


# 定义生产者线程
class Producer(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            time.sleep(1)
            print("生产线程开始生成数据")
            count += 1
            msg = "生成产品{}".format(count)
            q.put(msg)   # 默认阻塞
            print(msg)


# 定义消费者线程
class Comsumer(threading.Thread):
    def run(self):
        global q
        while True:
            print('开启消费线程')
            msg = q.get()  # 默认阻塞
            print("消费者线程得到了数据:{}".format(msg))
            time.sleep(5)


if __name__ == '__main__':
    p = Producer()
    c = Comsumer()

    p.start()
    c.start()
