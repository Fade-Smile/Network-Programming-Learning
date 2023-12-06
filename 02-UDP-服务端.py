#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :02-UDP-服务端.py
@Author  :Sunshine
@Date    :13/10/2023 22:50 
'''

from socket import *

# 1. 创建一个服务端的socket
socket_server = socket(AF_INET, SOCK_DGRAM)

#  2. 定义服务器端的IP地址和端口号
host_port = ('192.168.1.92', 8090)

#  3. 服务器端的socket来绑定地址和端口，只有绑定了地址和端口，才能称之为服务器的Socket
socket_server.bind(host_port)

#  4. 接收客户端的数据, 每次接收1kb的数据, 收到的每一个数据包，里面是一个元组，第一个值是数据内容，第二个值是源地址
data = socket_server.recvfrom(1024)
print(data[0].decode('utf-8'))
print(data)

# 5. 关闭套接字，释放资源；
socket_server.close()


