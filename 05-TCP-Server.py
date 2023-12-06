#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :05-TCP-Server.py
@Author  :Sunshine
@Date    :27/10/2023 14:36 
'''
from socket import *

# Step 1: Create  Server Socket with TCP protocol
TCP_sever_socket = socket(AF_INET, SOCK_STREAM)

# Step 2: bind IP address and port number
host_port = ('', 8088)
TCP_sever_socket.bind(host_port)

# Step 3: 服务器的Socket监听
TCP_sever_socket.listen(5)
# listen(n) 用于设置套接字为监听状态，以便等待客户端的连接请求。
# n 指数字 表示监听队列的最大长度，也就是服务器能够同时等待的客户端连接请求的最大数量。

'''
TCP_server_socket.listen(1)
服务器允许有1个连接是挂起的，如果是5，服务器默认可以有5个连接是挂起的

listen（1）只允许一个客户端在排队
这个数字1不决定服务器能处理多少服务器（大多情况下，5个就可以）

挂起：服务端在处理某客户端时，其他客户端在等待，排队
服务器处理能力和多线程有关，用多个线程处理多个客户端，这里listen（5），如果服务端可以多线程处理5个人客户端，那么还可以挂起5个客户端

listen（）太多会影响用户体验，要不就直接拒绝
'''

# Step 4: 等待客户端的连接请求
client_socket, client_address = TCP_sever_socket.accept()
# accept() 用于接受客户端的连接请求。
# 当 accept() 被调用时，它会阻塞程序的执行，等待客户端连接请求。
# 一旦有客户端连接请求到达，accept() 会接受连接，创建一个新的套接字 client_socket 用于与该客户端通信。
# client_address 是一个包含客户端地址信息的元组，通常包括客户端的IP地址和端口号。

#  Step 5: 服务器接收客户端发送过来的数据
data = client_socket.recv(1024) # data 是字节数据
print('服务器端接收的数据是: ', data.decode('utf-8'))

#  Step 6: 服务器端发送数据给客户
senData = "已收到 !"
client_socket.send(senData.encode('utf8'))

# Step 7: 关闭套接字
client_socket.close()
# 意味着当前客户端的服务已经完成.

TCP_sever_socket.close()
# 整个服务器全部关闭

