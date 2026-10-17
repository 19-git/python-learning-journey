"""
方式1：args方式，接受所有的位置参数
方式2：kwargs方式，接受所有的关键字参数
"""
#导包
import threading,time

def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}遍代码~")

def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}遍音乐！！！！")


#重要:创建主进程(主线程)main
if __name__ == '__main__':
    #创建两个子进程，分别关联上述的目标函数
    p1 = threading.Thread(target=coding,args=('mxy',10))
    p2 = threading.Thread(target=music,args=('yzy',10))
    #p2 = multiprocessing.Process(target=music,kwargs={'count':10,'name':'yzy'})
    p1.start()
    p2.start()