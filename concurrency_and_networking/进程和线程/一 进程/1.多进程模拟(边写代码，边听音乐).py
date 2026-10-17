"""
实现方式
1.导包
2.创建进程对象，关联目标函数
3.启动进程
"""

import multiprocessing
import time

def coding():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在敲第{i}遍代码~")

def music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在听第{i}遍音乐！！！！")

#创建两个进程对象，分别关联上述的两个目标函数
p1 = multiprocessing.Process(target=coding)
p2 = multiprocessing.Process(target=music)

#重点的细节：通过main进程(主程序)来创建子进程  易忘
if __name__ == "__main__":
    p1.start()
    p2.start()
















