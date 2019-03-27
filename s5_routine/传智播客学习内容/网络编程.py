# -*-coding:utf-8-*-
from socket import *

#创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)
#准备接收方的地址
sendAddr = ('192.168.1.103',8080)
#发送从键盘获取数据
sendData=input('请输入将要发送的数据')

#发送数据到指定的电脑上
udpSocket.sendto(sendData,sendAddr)
#等待接收对方发送的数据
recvData=udpSocket.recvfrom(1024)#1024代表本次接收的最大字节数
#显示对方发送的数据
print(recvfrom)
#关闭套接字
udpSocket.close()
#每次运行端口号都可能发生变化
#我们可以进行绑定


#绑定示例
udpSocket = socket(AF_INET,SOCK_DGRAM)
#绑定套接字
bindAddr=('',7788)
udpSocket.bind(bindAddr)
#ip一般不用写
#等待接收对方发送的数据
recvData=udpSocket.recvfrom(1024)
#显示接收到的数据
print(recvData)
#关闭套接字
udpSocket.close()

udp应用：echo服务器
