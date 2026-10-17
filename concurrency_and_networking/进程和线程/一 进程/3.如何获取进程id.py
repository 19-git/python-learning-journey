import multiprocessing
import os
import time


def coding():
    for i in range(2):
        print(f"正在敲第{i}遍代码~")
    print(f'coding子进程的pid:{multiprocessing.current_process().pid},{os.getpid()},父进程的id:{os.getppid()}')

def music():
    for i in range(2):
        print(f"正在听第{i}遍音乐！！！！")
    print(f'music子进程的pid:{multiprocessing.current_process().pid},{os.getpid()},父进程的pid:{os.getppid()}')


#创建两个进程对象，分别关联上述的两个目标函数
p1 = multiprocessing.Process(target=coding)
p2 = multiprocessing.Process(target=music)

#重点的细节：通过main进程(主程序)来创建子进程  易忘
if __name__ == "__main__":
    p1.start()
    p2.start()
    time.sleep(1)
    print(f'main主进程的pid:{multiprocessing.current_process().pid},{os.getpid()},父进程的id:{os.getppid()}')
