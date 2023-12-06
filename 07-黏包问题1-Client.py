#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :07-黏包问题1-Client.py
@Author  :Sunshine
@Date    :29/10/2023 13:53 
'''
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('192.168.1.92', 8080))

client_socket.send('Hello'.encode('utf-8'))
client_socket.send('World'.encode('utf-8'))

client_socket.close()
