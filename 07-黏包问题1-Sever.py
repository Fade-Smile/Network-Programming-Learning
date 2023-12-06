#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :07-黏包问题1-Sever.py
@Author  :Sunshine
@Date    :29/10/2023 13:39 
'''
from socket import *

sever_socket = socket(AF_INET, SOCK_STREAM)

sever_socket.bind(('', 8080))
sever_socket.listen(5)
client_socket, client_addr = sever_socket.accept()

data1 = client_socket.recv(1024)
data2 = client_socket.recv(1024)

print('第一条数据: ', data1)
print('第二条数据: ', data2)

client_socket.close()
sever_socket.close()