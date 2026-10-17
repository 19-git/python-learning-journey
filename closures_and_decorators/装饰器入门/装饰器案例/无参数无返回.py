def my_decorator(fn_name):
    def fn_inner():
        print("努力计算中~")
        fn_name()
    return fn_inner

@my_decorator
def get_sum():
    a = 1
    b = 2
    sum = a + b
    print(f"求和结果sum = {sum}")

if __name__ == '__main__':
    get_sum()
