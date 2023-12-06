#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :12-subprocess-调用系统命令3-popen.py
@Author  :Sunshine
@Date    :30/10/2023 14:24 
'''
import subprocess

# popen = subprocess.Popen('dir D://', encoding='utf-8', shell=True)
# print(popen)
# print(popen.stdout)

# 创建一个子进程， 用于执行python命令
popen = subprocess.Popen('python', stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

# python命令中传入三条命令
popen.stdin.write('print("Hello World!")\n'.encode('utf-8'))
popen.stdin.write('import os\n'.encode('utf-8'))
popen.stdin.write('print(os.environ)\n'.encode('utf-8'))

popen.stdin.close()

# out = popen.stdout.read().decode('gbk')
# popen.stdout.close()
# print(out)

# 第二种输出
out, err = popen.communicate()
print(out.decode('GBK'))







