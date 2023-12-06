#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :01-Create Socket.py
@Author  :Sunshine
@Date    :13/10/2023 14:58 
'''
import socket

'''
在Python中，socket.socket() 函数用于创建一个新的套接字对象，通常用于网络通信。它的常见参数包括:

socket_family（地址族/协议族）：这是一个必需的参数，用于指定套接字的地址族，它可以是以下之一:
    socket.AF_INET:IPv4 地址族，用于基于IPv4的通信。
    socket.AF_INET6:IPv6 地址族，用于基于IPv6的通信。
    socket.AF_UNIX: UNIX 域套接字，用于本地通信。

socket_type（套接字类型）：这也是一个必需的参数，用于指定套接字的类型，它可以是以下之一:
    socket.SOCK_STREAM:TCP 套接字，提供面向连接的、可靠的、基于流的通信。
    socket.SOCK_DGRAM:UDP 套接字，提供面向数据包的、无连接的通信。
    socket.SOCK_RAW: 原始套接字，通常用于特殊目的，例如实现自定义协议。
    
proto(协议编号):
    通常情况下，可以省略这个参数，让系统自动选择适当的协议。
    如果需要明确指定协议，可以使用一个整数，例如 socket.IPPROTO_TCP 或 socket.IPPROTO_UDP。
'''

#  创建套接字(Socket) TCP协议
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  创建套接字(Socket) UDP协议
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(s1)

print(s2)
