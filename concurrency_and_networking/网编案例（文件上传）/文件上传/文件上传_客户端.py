"""
1.创建客户端socket对象
2.链接服务器端的IP 和 端口号
3.关联数据源文件，读取内容，写给服务器端
4.释放资源
"""
#导包
import socket
# 1.创建客户端socket对象
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.链接服务器端的IP 和 端口号(以元组形式封装)
client_socket.connect(("127.0.0.1",6667))
# 3.关联数据源文件，读取内容，写给服务器端
with open('d:/测试/测试1.txt','rb') as scr_file:
    #循环读取内容
    while True:
        #具体读取操作
        data = scr_file.read(8192)
        #将读取的数据发送给服务器端
        client_socket.send(data)
        #如果读取到的数据为空，说明文件读取完毕
        if len(data) == 0:
            break

# 4.释放资源
client_socket.close()
































