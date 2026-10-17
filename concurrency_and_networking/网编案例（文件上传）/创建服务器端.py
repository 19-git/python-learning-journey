"""
案例：网编入门案例，服务器给客户端发送信息客户端给出回执信息

服务器端开发流程：
    1.创建服务器端socket对象
    2.绑定ip地址和端口号
    3.设置最大监听数
    4.等待客户端申请建立链接
    5.给客户端发送信息
    6.接收客户端的信息并打印
    7.释放资源

细节：
    客户端和服务器是通过字节流（bytes）的形式实现的
"""
#导包
import socket
# 1.创建服务器端socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定ip地址和端口号
server_socket.bind(('127.0.0.1', 10086))
# 3.设置最大监听数
server_socket.listen(5)
while True:
    try:
        # 4.等待客户端申请建立链接
        # print(1)
        accept_socket,client_info = server_socket.accept()#一旦客户端连上，会生成独立 accept_socket，专门和当前客户端收发数据
        # print(2)
        # 5.给客户端发送信息
        accept_socket.send(b'welcome to socket!')
            # 6.接收客户端的信息并打印
        date = accept_socket.recv(1024).decode('utf-8')
        print(f'服务器端收到 来自{client_info}的信息:{date}')
        # 7.释放资源
        accept_socket.close()
    except:
        pass











































