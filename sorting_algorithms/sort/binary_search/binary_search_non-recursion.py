def binary_search_non_recursion(my_list, target):
    start = 0
    end = len(my_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if my_list[mid] == target:
            return True
        elif target < my_list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(binary_search_non_recursion(my_list, 15))












