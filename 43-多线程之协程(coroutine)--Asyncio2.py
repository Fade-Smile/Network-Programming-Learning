#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :43-多线程之协程(coroutine)--Asyncio2.py
@Author  :Sunshine
@Date    :14/11/2023 14:40 
'''
import asyncio


async def my_coroutine():
    # 异步操作的内容
    await asyncio.sleep(1)
    return "Done!"


async def main():
    task1 = asyncio.create_task(my_coroutine())
    task2 = asyncio.create_task(my_coroutine())

    result = await asyncio.gather(task1, task2)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
