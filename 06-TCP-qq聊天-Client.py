#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :06-TCP-qq聊天-Client.py
@Author  :Sunshine
@Date    :28/10/2023 14:09 
'''
from socket import *

TCP_client_socket = socket(AF_INET, SOCK_STREAM)

TCP_client_socket.connect(('192.168.1.92', 8008))

while True:
    send_data = input('send:')
    if len(send_data) > 0:
        TCP_client_socket.send(send_data.encode('utf-8'))
    if send_data == 'exit':
        TCP_client_socket.close()
        break

    # 客户端结束服务器返回的内容
    recv_data = TCP_client_socket.recv(1024)
    print("服务器:", recv_data.decode('utf-8'))

TCP_client_socket.close()