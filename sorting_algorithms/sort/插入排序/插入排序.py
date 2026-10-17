def insert_sort(my_list):
    n = len(my_list)
    #外循环，控制比较的轮数
    for i in range(1,n):
        #内循环，控制每轮比较的次数
        for j in range(i,0,-1):
            if my_list[j] < my_list[j-1]:
                my_list[j-1],my_list[j] = my_list[j],my_list[j-1]
            else: # 走到这里说明元素找到了自己的位置 break即可
                break






if __name__ == '__main__':
    my_list = [6,7,2,5,4,1]
    insert_sort(my_list)
    print(my_list)
