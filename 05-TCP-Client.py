#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :05-TCP-Client.py
@Author  :Sunshine
@Date    :27/10/2023 15:02 
'''

from socket import *

# Step 1: 创建客户端的TCP套接字
TCP_client_socket = socket(AF_INET, SOCK_STREAM)

# Step 2: 目标服务器和端口号
server_IP_Port = ('192.168.1.92', 8088)

# Step 3: 客户端发送连接请求 【不是传输数据】
TCP_client_socket.connect(server_IP_Port)
# connect('server_ip_address', port_number)函数， 指定了要连接的服务器的地址和端口。

send_data = input('请输入: ')
TCP_client_socket.send(send_data.encode('utf-8'))

# Step 4: 接受服务器返回的数据
recv_data = TCP_client_socket.recv(1024)
print("客户端接受到服务器的数据为:", recv_data.decode('utf-8'))

TCP_client_socket.close()
