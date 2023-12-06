#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :06-TCP-qq聊天-Server.py
@Author  :Sunshine
@Date    :28/10/2023 13:59 
'''
from socket import *

TCP_sever_socket = socket(AF_INET, SOCK_STREAM)

TCP_sever_socket.bind(('', 8008))
TCP_sever_socket.listen(1)

while True:
    client_socket, client_address = TCP_sever_socket.accept()

    while True:
        recv_data = client_socket.recv(1024)
        if len(recv_data) > 0:  # 客户端没有退出， 而且发送数据到服务器
            print('客户端:', recv_data.decode('utf-8'))
        if recv_data.decode('utf-8') == 'exit':
            print('客户端已经退出!')
            break

        # 发送数据给客户端
        send_data = input("Send:")
        if len(send_data) > 0:
            client_socket.send(send_data.encode('utf-8'))
    client_socket.close()

TCP_sever_socket.close()
