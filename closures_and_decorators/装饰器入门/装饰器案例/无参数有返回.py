def my_decorator(fn_name):
    def fn_inner():
        print("努力计算中~")
        return fn_name()
    return fn_inner


@my_decorator
def get_sum():
    a = 1
    b = 2
    c = a + b
    return c

sum = get_sum()
print(f"求和结果{sum}")
