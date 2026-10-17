def quick_sort(my_list,start,end):

    #核心细节 递归要有结束条件 不然死循环
    #如果start>=end 递归结束 说明排好序了
    if start >= end:
        return

    #left right 分别表示 分界值左右的索引
    left = start
    right = end
    #定义变量mid 表示起始的值为分界值
    mid = my_list[start]
    #只要left比right小就一直找
    while left < right:
        #只要分界值右边的数据比分界值大,right就-1,直至循环结束
        while my_list[right] >= mid and left < right:
            right -= 1
        #走到这 说明my_list[right] 比分界值小,放左侧
        my_list[left] = my_list[right]

        #只要分界值左边的数据比分界值小,left就+1,直至循环结束
        while my_list[left] < mid and left < right:
            left += 1
        #走到这 说明my_list[left] 比分界值大,放右边侧
        my_list[right] = my_list[left]

    #走到这 循环结束 分界值的位置已经找到 赋值即可
    my_list[right] = mid

    #递归方式 处理 第一次操作后 分界值左侧的数据
    quick_sort(my_list,start,right-1)

    #递归方式 处理 第一次操作后 分界值右侧的数据
    quick_sort(my_list,left+1,end)




if __name__ == '__main__':
    my_list = [5,2,6,9,8,7,4,1]
    quick_sort(my_list,0,len(my_list)-1)
    print(my_list)

























