#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project :Python网络开发 
@File    :04-TFTP-Client.py
@Author  :Sunshine
@Date    :14/10/2023 14:49 
'''

from socket import *
import struct  # 负责Python数据结构和c语言数据结构转换
import os

# 客户端的Socket
s = socket(AF_INET, SOCK_DGRAM)

# 定义目标服务器的地址和端口号
host_port = ('192.168.1.92', 69)


def download(file_name, s, host_port):
    """
    使用Python中的struct模块来创建一个二进制数据包。

    '!H%dsb5sb' 代表格式:
        !: 表示使用网络字节序，即大端字节序，确保数据在网络上传输时按照规定的字节顺序。
        H: 一个无符号短整数（2字节），用于存储整数值1。
        %ds: 这是一个动态字段，%d会被len(fileName)替换，表示一个字符串，长度由len(fileName)确定。
        b: 一个有符号字节（1字节），用于存储整数值0。把Python里的int类型改为Char
        5s: 一个长度为5的字符串，用于存储字符串"octet"。
        b: 又是一个有符号字节（1字节），用于存储整数值0。

    参数列表：1, fileName.encode('utf-8'), 0, 'octet'.decode('utf-8'), 0。
        1被放入无符号短整数字段（H）。
        fileName.encode('utf-8')被放入动态字符串字段（%ds），并且是根据fileName的UTF-8编码。
        0被放入两个有符号字节字段（b）。
        'octet'.decode('utf-8')被放入长度为5的字符串字段（'5s'），并且是根据"octet"的UTF-8解码。
        最后的0又被放入一个有符号字节字段（b）。

    组装一个客户端请求的数据包，包含5个部分的数据
    第一部分:操作码(int)
    第二部分: 文件名 (str)
    第三部分:分隔符
    第四部分: 模式(字节数据的存储和解析) octet
    第五部分:分隔符
    一个数据包，本质是字节数值，是由不同的python类型，生成的。encode可以把字符串转换成字节数组。int呢? tuple呢?
    """
    # "!H%dsb5sb" 代表格式：！开头，请求的数据包
    data_package = struct.pack('!H%dsb5sb' % len(file_name), 1, file_name.encode('utf-8'), 0, 'octet'.encode('utf-8'), 0)

    # 把数据包发到目标服务器
    s.sendto(data_package, host_port)

    # 客户端首先创建一个空白文件
    f = open('client_' + file_name, 'ab')

    while True:

        # 客户端接收服务器发过来的数据，数据只有两种：1、下载文件内容数据报，2、error信息报
        recv_data, (server_ip, server_port) = s.recvfrom(1024)

        operator_code, num = struct.unpack('!HH', recv_data[:4])  # 把前4个字节的数据解包出来

        if int(operator_code) == 5:  # 判断数据包是否是error信息报
            print("服务器返回：你要下载的文件不存在!")
            break

        # 如果是文件内容的数据，需要保存文件内容
        f.write(recv_data[4:])

        if len(recv_data) < 516:  # 意味着服务器传输过来的文件已经接收完成了
            print("客户端下载成功")
            break

        # 客户端收到数据包之后，还需要发送一个确认ACK给服务器
        ack_package = struct.pack('!HH', 4, num)
        s.sendto(ack_package, (server_ip, server_port))

    # 释放资源
    f.close()
    s.close()


def upload(file_name, s, host_port):
    if not os.path.exists(file_name):
        print("该文件不存在.")
        return

    num = 1
    f = open(file_name, 'rb')

    # Send the upload request
    data_package = struct.pack('!H%dsb5sb' % len(file_name), 2, file_name.encode('utf-8'), 0, 'octet'.encode('utf-8'), 0)
    s.sendto(data_package, host_port)

    while True:
        # Read file data
        read_data = f.read(512)
        data_package = struct.pack('!HH', 3, num) + read_data
        s.sendto(data_package, host_port)

        if len(read_data) < 512:
            print("客户端:%s,文件上传完成" % host_port[0])
            break

        # Receive server ACK
        recv_ack, _ = s.recvfrom(1024)
        operator_code, ack_num = struct.unpack('!HH', recv_ack)
        print("服务器：%s,的确认信息是" % host_port[0], ack_num)
        num += 1

        if int(operator_code) != 4 or int(ack_num) < 1:
            break

    f.close()


def main():
    # Input the file name and operation choice (1 for download, 2 for upload)
    operation_choice = input("选择操作（1为下载，2为上传）: ")
    file_name = input("请输入文件名: ")

    s = socket(AF_INET, SOCK_DGRAM)
    host_port = ('192.168.1.92', 69)

    if operation_choice == '1':
        download(file_name, s, host_port)
    elif operation_choice == '2':
        upload(file_name, s, host_port)
    else:
        print("操作选择无效。 使用 1 进行下载或使用 2 进行上传。")

    s.close()


if __name__ == '__main__':
    main()

