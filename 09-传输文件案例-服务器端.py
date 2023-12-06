#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :09-传输文件案例-服务器端.py
@Author  :Sunshine
@Date    :29/10/2023 23:55 
'''
from socket import *
import struct

sever = socket(AF_INET, SOCK_STREAM)
sever.bind(('', 8088))

sever.listen(5)
client_socket, client_addr = sever.accept()

f = open(r'D:\Learning-Material\Python网络开发\服务器.mp4', 'wb')

header_data = client_socket.recv(4)
# 注: unpack返回的是一个元组， 元组的第一个值就是长度
print(struct.unpack('!i', header_data))
size = struct.unpack('!i', header_data)[0]

recv_size = 0 # 用于累计 接收到的数据长度
while recv_size < size:
    data = client_socket.recv(1024)
    f.write(data)
    recv_size += len(data)  # 累加接收到的数据的字节长度

print('服务器端接收完成')
f.close()
client_socket.close()
