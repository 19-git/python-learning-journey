def my_decorator(fn_name):
    def fn_inner(a,b):
        print("努力计算中~")
        fn_name(a,b)
    return fn_inner

@my_decorator
def get_sum(a,b):
    sum = a + b
    print(f"所求和sum:{sum}")

get_sum(1,2)
