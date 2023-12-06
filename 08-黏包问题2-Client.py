#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :08-黏包问题2-Client.py
@Author  :Sunshine
@Date    :29/10/2023 14:11 
'''
#  接收方可能出现的黏包问题
#  导入Time模块 用于拉长客户端发送多个数据包的时间间隔
from socket import *
import time

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('192.168.1.92', 9999))

client_socket.send('Hello'.encode('utf-8'))
time.sleep(5)  # 让当前的线程休眠5秒
client_socket.send('World! Welcome to XXX World'.encode('utf-8'))

client_socket.close()
