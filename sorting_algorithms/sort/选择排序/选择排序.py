def select_sort(my_list):
    n = len(my_list)
    for i in range(n-1):
        min_index = i  # 每轮都假设最前面的数为最小值 再在之后的数中找出真正的最小值 做替换
        for j in range(i+1,n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[min_index], my_list[i] = my_list[i], my_list[min_index]





if __name__ == '__main__':
    my_list = [9,8,5,2,4,7]
    select_sort(my_list)
    print(my_list)