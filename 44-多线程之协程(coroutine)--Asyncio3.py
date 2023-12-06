#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :44-多线程之协程(coroutine)--Asyncio3.py
@Author  :Sunshine
@Date    :14/11/2023 15:13 
'''
import asyncio


async def print_sum(x, y):
    result = await compute(x, y)  # 等待下一个协程帮忙计算
    print('%s + %s = %s' % (x, y, result))


async def compute(x, y):
    print('开始计算x: %s 和y: %s' % (x, y))
    await asyncio.sleep(0)
    return y + x


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(10, 20))
loop.close()

"""
1. async def print_sum(x, y): 和 async def compute(x, y):：这两个是异步函数（协程），分别用于打印两个数的和以及计算这个和。
                            这些异步函数内部包含了 await 关键字，用于暂停函数的执行，等待异步操作的完成。

2. result = await compute(x, y): 在 print_sum 函数中调用了 compute 函数，并使用 await 关键字等待其返回结果。
                            这里的 await 表示暂停 print_sum 函数的执行，等待 compute 函数的结果返回后再继续执行。

3. loop = asyncio.get_event_loop(): 获取当前线程的事件循环。

4. loop.run_until_complete(print_sum(10, 20)): 这行代码运行事件循环，直到 print_sum(10, 20) 协程执行完成。
                                                在这个过程中，print_sum 协程会等待 compute 协程的结果。

5. loop.close(): 关闭事件循环。
"""

"""
这段代码的作用是展示了两个异步函数之间的调用关系。print_sum 函数等待 compute 函数计算两个数的和，但在等待期间允许事件循环执行其他的异步任务。
compute 函数模拟了一个异步操作(使用 await asyncio.sleep(0))，在实际场景中可能是一个 I/O 操作或者其他异步任务。
当 compute 函数完成计算后，它的结果将返回给 print_sum 函数，print_sum 函数继续执行并打印计算结果。
"""
