#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :10-subprocess-调用系统命令1.py
@Author  :Sunshine
@Date    :30/10/2023 13:07 
'''
import subprocess


# 1、 简单的写法
# 开启一个子进程， 执行系统命令， arg, encoding, shell
# runcmd = subprocess.run('dir d:\\Learning-Material', encoding='UTF-8', shell=True)
# print(runcmd)

# 2、 定义一个函数 调用系统的所有命令
def run_cmd(command):
    # 初始化一个子进程来执行系统命令
    # subprocess.PIPE 是 subprocess 模块中的一个特殊常量，用于定义子进程的标准输入、标准输出和标准错误的处理方式。
    # 具体来说，subprocess.PIPE 表示将相关的标准流（输入、输出或错误）与管道连接，以便在父进程和子进程之间进行数据交换。
    return_cmd = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='GBK', shell=True)
    if return_cmd.returncode == 0:
        print('Success:')
        print(return_cmd.stdout)
    else:
        print('命令执行错误')
        print(return_cmd)


run_cmd('ipconfig')
run_cmd('dir d:\\')
run_cmd('exit 1')
