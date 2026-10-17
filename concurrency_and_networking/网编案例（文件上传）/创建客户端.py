"""
案例：网编入门案例，服务器给客户端发送信息客户端给出回执信息

客户端开发流程：
    1.创建客户端socket对象
    2.链接服务器端，指定:服务器端IP,端口号,
    3.接受服务器端的信息并打印
    4.给服务器端发送信息
    5.释放资源

细节：
    客户端和服务器是通过字节流（bytes）的形式实现的
"""

#导包
import socket

# 1.创建客户端socket对象
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.链接服务器端，指定:服务器端IP,端口号
client_socket.connect(("127.0.0.1",10086))
# 3.接受服务器端的信息并打印
data = client_socket.recv(1024).decode('utf-8')
print(f"客户端收到信息:{data}")
# 4.给服务器端发送信息
client_socket.send('socket好玩有趣'.encode('utf-8'))
# 5.释放资源
client_socket.close()































