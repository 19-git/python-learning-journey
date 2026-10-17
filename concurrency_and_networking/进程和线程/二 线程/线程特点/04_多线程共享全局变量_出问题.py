"""
演示:多线程共享全局变量，可能出现的问题。
问题:
    累加次数不够。

产生原因:
    线程1还没有来得及执行完(一个完整的动作)前，被线程2抢走了资源，就产生了问题

解决方法:
    使用互斥锁

细节:要在合适的时机释放(死锁)，使用多个锁(锁不住)
"""
import threading

g_sum = 0
#创建线程锁
mutex1 = threading.Lock()
mutex2 = threading.Lock()

def sum_num1():
    mutex1.acquire()
    global g_sum
    for i in range(1000000):
        g_sum += 1
    print(f"sum_num1的累加结果是{g_sum}")
    mutex1.release()

def sum_num2():
    mutex2.acquire()
    global g_sum
    for i in range(1000000):
        g_sum += 1
    print(f"sum_num2的累加结果是{g_sum}")
    mutex2.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=sum_num1)
    t2 = threading.Thread(target=sum_num2)
    t1.start()
    t2.start()