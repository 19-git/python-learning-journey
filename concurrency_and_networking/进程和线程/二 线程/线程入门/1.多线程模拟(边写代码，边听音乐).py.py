import threading
import time

def coding():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在敲第{i}遍代码~")

def music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在听第{i}遍音乐！！！！")


#重点的细节：通过main进程(主程序)来创建子进程  易忘
if __name__ == "__main__":
    # 创建两个进程对象，分别关联上述的两个目标函数
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)

    t1.start()
    t2.start()