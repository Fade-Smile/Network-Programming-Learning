#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :42-多线程之协程(coroutine)--Asyncio.py
@Author  :Sunshine
@Date    :14/11/2023 14:40 
'''
import asyncio


# 定义一个异步函数，允许在函数内部使用 await 关键字来等待其他异步操作的完成，使得函数可以暂停和恢复执行，
# 以便在等待 I/O 操作或其他异步任务时不会阻塞整个程序。
async def fun1():  # 定义一个协程
    for i in range(5):
        print('协程1!!!')
        await asyncio.sleep(0)  # 人为的模拟IO阻塞
        # await 用于暂停函数的执行，等待其他异步任务的完成。


async def fun2():
    for i in range(5):
        print('协程2!!!')
        await asyncio.sleep(0)

# 获取循环事件
loop = asyncio.get_event_loop()
# asyncio.get_event_loop() 函数 用于获取当前线程的事件循环（Event Loop）对象。
# 在异步编程中，事件循环是协程的基础设施，负责调度和执行异步任务，以及管理协程的执行顺序。
# 事件循环负责监控协程的状态并在合适的时候进行切换，使得异步任务能够按照预期的顺序执行。

# 启动多个协程并行执行
loop.run_until_complete(asyncio.gather(fun1(), fun2()))
# asyncio.gather() 方法接收多个协程作为参数，并行地运行这些协程，并等待它们全部完成。
# run_until_complete() 用于运行异步任务直到其完成
# 注意: run_until_complete() 是一个阻塞方法，它会一直运行，直到传入的 Future 对象完成为止。

loop.close()
