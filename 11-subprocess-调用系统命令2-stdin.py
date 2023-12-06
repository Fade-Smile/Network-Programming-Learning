#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :11-subprocess-调用系统命令2-stdin.py
@Author  :Sunshine
@Date    :30/10/2023 13:40 
'''

import subprocess

# 打开文件
with open(r'D:\\Learning-Material\\Python网络开发\\python.txt', 'r') as f:
    # 读取文件内容
    file_content = f.read()

# return_cmd = subprocess.run('python', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
# return_cmd.stdin = 'print("hello world")'

# 使用文件内容作为子进程的输入
# 通过文件句本的方式传参给系统命今，PIPE是不能传参给系统命令。subprocess有接口Popen 可以传参给系统命令
return_cmd = subprocess.run('python', input=file_content, stdout=subprocess.PIPE, text=True, shell=True)
print(return_cmd.stdout)




