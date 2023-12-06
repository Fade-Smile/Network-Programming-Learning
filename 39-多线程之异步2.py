#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :39-多线程之异步2.py
@Author  :Sunshine
@Date    :12/11/2023 13:25 
'''
"""
同步 + 异步例子 - 家庭日常场景：

同步情景：

1. 爸爸看电视： 家里的爸爸正在看电视，这是一个同步操作。
2. 爸爸看到女儿回家： 突然，爸爸看到女儿回家了，这时爸爸需要同步操作关掉电视。
3. 爸爸准备烹饪大餐： 爸爸决定准备一个烹饪大餐，这个过程包括同步操作如查看食谱、洗切蔬菜、点火烧水，以及异步操作如使用烤箱烤鸡和电饭锅煮干饭
                    （它会在设定好的时间自己完成）。
4. 妈妈做家务： 在同步操作的同时，妈妈在做家务，将浴室脏衣篓里的衣服放入洗衣机，设定好时间后开始打扫卫生。

异步情景：
1. 女儿放学回家： 在妈妈做家务的过程中，女儿放学回家了。女儿异步地去自己的房间做作业。
2. 妈妈晾晒衣服： 妈妈在做家务的同时，异步操作将洗完的衣服晾在阳台。

最后的同步操作：
家庭共进晚餐： 当女儿完成作业，妈妈完成家务时，一家三口同步操作，围坐在餐桌前一起享受爸爸准备的烹饪大餐。
"""
import os
import time
from multiprocessing import Pool


class Father:
    def __init__(self):
        self.process_id = os.getpid()

    def watch_tv(self):
        print(f"父亲 {self.process_id}: 在看电视")

    def close_tv(self):
        print(f"父亲 {self.process_id}: 关掉电视")

    def daughter_arrives_home(self, daughter):
        print(f"父亲 {self.process_id}: 看到女儿回家了")
        self.close_tv()  # 看到女儿回家后关掉电视
        self.prepare_dinner()

    def prepare_dinner(self):
        print(f"父亲 {self.process_id}: 开始准备一个烹饪大餐")
        self.sync_operations()
        async_result_oven = pool.apply_async(self.use_oven_bake_chicken)
        async_result_rice = pool.apply_async(self.cook_rice)

        # Wait for the async results to complete
        async_result_oven.get()
        async_result_rice.get()

        self.dinner_preparation_callback()

    def dinner_preparation_callback(self):
        print(f"父亲 {self.process_id}: 烹饪大餐完成")

    def sync_operations(self):
        time.sleep(1)  # 模拟同步操作

    def use_oven_bake_chicken(self):
        print(f"父亲 {self.process_id}: 使用烤箱烤鸡")
        time.sleep(5)
        print(f"父亲 {self.process_id}: 使用烤箱烤鸡完成")

    def cook_rice(self):
        print(f"父亲 {self.process_id}: 使用电饭锅煮饭")
        time.sleep(4)
        print(f"父亲 {self.process_id}: 使用电饭锅煮饭完成")


class Mother:
    def __init__(self):
        self.process_id = os.getpid()

    def do_housework(self):
        print(f"母亲 {self.process_id}: 在做家务")
        self.laundry()
        time.sleep(1)
        self.clean_house()

    def laundry(self):
        print(f"母亲 {self.process_id}: 将衣服放入洗衣机")
        time.sleep(4)
        print(f"母亲 {self.process_id}: 衣服洗完了")

    def clean_house(self):
        print(f"母亲 {self.process_id}: 开始打扫卫生")
        time.sleep(8)
        print(f"母亲 {self.process_id}: 打扫卫生完成")

    def dry_clothes(self, callback=None):
        print(f"母亲 {self.process_id}: 在阳台晾晒衣服")
        time.sleep(3)
        print(f"母亲 {self.process_id}: 衣服晾晒完成")
        if callback:
            callback()

    def sync_operations(self):
        time.sleep(1)  # 模拟同步操作


class Daughter:
    def __init__(self):
        self.process_id = os.getpid()

    def do_homework(self, callback=None):
        print(f"女儿 {self.process_id}: 开始做作业")
        time.sleep(6)
        print(f"女儿 {self.process_id}: 做作业完成")
        if callback:
            callback()

    def return_home(self, father):
        print(f"女儿 {self.process_id}: 放学回家了")
        father.daughter_arrives_home(self)
        self.do_homework()

    def sync_operations(self):
        time.sleep(1)  # 模拟同步操作


def dinner_preparation_callback(result):
    print("一家三口共进晚餐.")


def daughter_homework_callback(result):
    print("女儿做作业完成.")


if __name__ == '__main__':
    with Pool(4) as pool:
        father = Father()
        mother = Mother()
        daughter = Daughter()

        father.watch_tv()
        daughter.return_home(father)

        # 异步操作
        # async_result_daughter_homework = pool.apply_async(daughter.do_homework, callback=daughter_homework_callback)
        async_result_mother_dry_clothes = pool.apply_async(mother.dry_clothes, callback=dinner_preparation_callback)

        # 等待异步操作完成
        # async_result_daughter_homework.get()
        async_result_mother_dry_clothes.get()

        # 同步操作
        father.sync_operations()
        mother.sync_operations()
        daughter.sync_operations()
