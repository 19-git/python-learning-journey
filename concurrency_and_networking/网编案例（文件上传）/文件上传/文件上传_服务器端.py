"""
1.创建服务器端socket对象
2.绑定IP 和 端口号
3.设置最大监听数
4.等待客户端申请建立链接
5.读取客户端上传的文件数据
6.将读取的数据写到本地文件中，并写入
7.释放资源
"""
#导包
import socket

# 1.创建服务器端socket对象
sever_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.绑定IP 和 端口号(以元组形式封装)
sever_socket.bind(("127.0.0.1",6667))
# 3.设置最大监听数
sever_socket.listen(5)
# 4.等待客户端申请建立链接
accept_socket,client_address = sever_socket.accept()
# 5.读取客户端上传的文件数据,并写入
with open('./data/my_txt','wb') as dest_file:
    #循环读取数据
    while True:
        #接受客户端发送的文件数据
        bys = accept_socket.recv(8192)
        #
        if not bys:
            break
        #将读取到的数据写入到目的地文件中
        dest_file.write(bys)

# 6.释放资源
accept_socket.close()






























