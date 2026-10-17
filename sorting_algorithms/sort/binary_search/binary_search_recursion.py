def binary_search(my_list, target):
    n = len(my_list)
    if n == 0:
        return False
    mid = n//2
    if my_list[mid] == target:
        return True
    elif my_list[mid] < target:
        return binary_search(my_list[mid+1 : n], target)
    else:
        return binary_search(my_list[0 : mid], target)




if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 9, 10]
    print(binary_search(my_list, 2))
