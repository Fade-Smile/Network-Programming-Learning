#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :35-多线程之线程通信-queue.py
@Author  :Sunshine
@Date    :10/11/2023 14:14 
'''

import threading, queue
import time

# 创建队列
q = queue.Queue(1000)  # 先进先出的队列 【FIFO】


# q = queue.LifoQueue  # 后进先出的队列
# q = queue.PriorityQueue  # 优先级的队列


# 定义生产者线程
class Producer(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 1000:
                # 直接生成100条
                for i in range(100):
                    count += 1
                    msg = "生产产品{}".format(count)
                    q.put(msg)
                    print(msg)
            time.sleep(0.5)


# 定义消费者线程
class Comsumer(threading.Thread):
    def run(self):
        global q
        while True:
            for i in range(100):
                msg = q.get()
                print("消费者线程得到了数据:{}".format(msg))
            time.sleep(1)


if __name__ == '__main__':
    p = Producer()
    c = Comsumer()

    p.start()
    c.start()
