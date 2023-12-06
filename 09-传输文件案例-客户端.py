#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :09-传输文件案例-客户端.py
@Author  :Sunshine
@Date    :29/10/2023 23:44 
'''
from socket import *
import struct
import os

client = socket(AF_INET, SOCK_STREAM)
client.connect(('192.168.1.92', 8088))

# 客户端给传输一个文件到服务器
file_path = 'new.mp4'
f = open(file_path, 'rb')

# 再发送真正的文件数据之前, 先准备一个报头
size = os.path.getsize(file_path)  # 获取文件的字节长度
# 创建一个报头, i为 4 个字节的 int 。
header = struct.pack('!i', size)  # 接收方 会适用 struct解包， 得到一个int类型数字
client.send(header)

# 发送文件内容
while True:
    data = f.read(1024)  # 每次读取1024字节
    if not data:
        break
    client.send(data)

print('客户端上传文件完成')

f.close()
client.close()
