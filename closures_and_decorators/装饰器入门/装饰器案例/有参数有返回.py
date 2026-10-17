def my_decorator(fn_name):
    def fn_inner(a,b):
        print("努力计算中~")
        return fn_name(a,b)
    return fn_inner

@my_decorator
def get_sum(a,b):
    a = 1
    b = 1
    return a+b

sum = get_sum(1,2)
print(sum)