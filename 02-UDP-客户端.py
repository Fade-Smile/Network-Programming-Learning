#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :02-UDP-客户端.py
@Author  :Sunshine
@Date    :13/10/2023 22:50 
'''

from socket import *

# 创建一个UDP协议的套接字，然后发送一条数据到网络上的另外一个进程

# 1. 创建套接字
client_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 定义一个接收信息的目标, 8080是一个目标服务器的端口，127.0.0.1是目标服务器地址
# server_host_port = ('127.0.0.1', 8080)
# server_host_port = ('www.baidu.com', 8080)
server_host_port = ('192.168.1.92', 8090)

# 3. 准备即将发送的数据， encode表示按照一种编码格式 把数据变成 字节数组 bytes
#  数据一定是字节数据才能发送
data_s = input('请输入: ').encode('utf-8')

# 4. 发送数据, 标识一个进程是通过 IP + 端口 + 协议
client_socket.sendto(data_s, server_host_port)

print('发送完成')

# 5. 关闭套接字， 释放系统资源
client_socket.close()


