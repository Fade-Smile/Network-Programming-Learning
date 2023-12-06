#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :02-UDP-echo服务端.py
@Author  :Sunshine
@Date    :13/10/2023 22:50 
'''

from socket import *

# 1. 创建一个服务端的socket
socket_server = socket(AF_INET, SOCK_DGRAM)

#  2. 定义服务器端的IP地址和端口号
host_port = ('', 8090)  # 如果服务器是真实的物理小型服务器， IP地址有很多。任何本机的IP地址都绑定 用 ‘’。

#  3. 服务器端的socket来绑定地址和端口，只有绑定了地址和端口，才能称之为服务器的Socket
socket_server.bind(host_port)

while True:
    #  4. 接收客户端的数据, 每次接收1kb的数据, 收到的每一个数据包，里面是一个元组，第一个值是数据内容，第二个值是源地址
    data = socket_server.recvfrom(1024)

    #  服务器收到数据之后原封不动返回， 而且是收到哪个客户端的信息就返回给那个客户端
    socket_server.sendto(data[0], data[1])
    print(data[0].decode('utf-8'))
    print(data)
    print()

# 5. 关闭套接字，释放资源；
socket_server.close()


