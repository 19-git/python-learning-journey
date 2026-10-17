def bubble_sort(my_list):   # 形参接受可变类型,则形参的改变直接影响实参
    n = len(my_list)

    for i in range(n-1):
        #确保每次使用前count清零 放置于for内
        count = 0  # 细节 定义变量记录具体交换次数

        for j in range(n-i-1):
            if my_list[j] > my_list[j+1]:
                count +=1 #细节 走到这里说明交换次数加一
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        #细节 打印每轮交换的次数
        print(f'第{i+1}轮交换了{count}次~')
        #细节 本轮如果没有发生交换 说明本就有序 则跳出循环
        if count == 0:
            break




if __name__ == '__main__':
    my_list = [5,3,6,7,2]
    #my_list = [1,2,3,4,5]
    bubble_sort(my_list)
    print(my_list)





