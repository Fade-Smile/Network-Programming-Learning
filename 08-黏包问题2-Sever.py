#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :08-黏包问题2-Sever.py
@Author  :Sunshine
@Date    :29/10/2023 14:11 
'''
from socket import *
import time

sever_socket = socket(AF_INET, SOCK_STREAM)

sever_socket.bind(('', 9999))
sever_socket.listen(5)
client_socket, client_addr = sever_socket.accept()
print('连接成功', client_addr)

# 第一次没有接收完整
data1 = client_socket.recv(3)
print('第一个数据包: ', data1)
time.sleep(6)
# 第二次会接收第一次未接收完的数据， 若还有空间， 再接收新的数据
data2 = client_socket.recv(10)
print('第二个数据包: ', data2)
# 最后一次， 接收剩余的数据
data3 = client_socket.recv(20)
print('第三个数据包: ', data3)

client_socket.close()
sever_socket.close()
