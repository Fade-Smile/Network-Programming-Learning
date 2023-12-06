#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :03-UDP-echo客户端1.py
@Author  :Sunshine
@Date    :13/10/2023 22:50 
'''

from socket import *

'''
1. 客户端可以发送多条数据。
2. 客户端如果发送一个’exit‘ 则客户端退出。
3. 服务器端收到什么就返回什么。
'''
# 创建一个UDP协议的套接字，然后发送一条数据到网络上的另外一个进程

#  定义变量， 是否退出客户端的标记
flag = True
# 1. 创建套接字
client_socket = socket(AF_INET, SOCK_DGRAM)

while flag:
    # 2. 定义一个接收信息的目标
    server_host_port = ('192.168.1.92', 8090)

    # 3. 准备即将发送的数据， encode表示按照一种编码格式 把数据变成 字节数组 bytes
    #  数据一定是字节数据才能发送
    data_s = input('请输入: ').encode('utf-8')

    # 4. 发送数据, 标识一个进程是通过 IP + 端口 + 协议
    client_socket.sendto(data_s, server_host_port)

    # 从服务器接收返回过来的数据， 打印出返回的数据
    print('返回的数据是: ', client_socket.recvfrom(1024)[0].decode('utf-8'))

    if data_s.decode('utf-8') == 'exit' or data_s.decode('utf-8') == 'EXIT':
        flag = False

# 5. 关闭套接字， 释放系统资源
client_socket.close()
