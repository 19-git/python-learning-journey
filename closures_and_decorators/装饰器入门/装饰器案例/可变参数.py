def my_decorator(fn_name):
    def fn_inner(*args, **kwargs):
        print("努力计算中~")
        return fn_name(*args,**kwargs)
    return fn_inner

@my_decorator
def get_sum(*args,**kwargs):
    return sum(args) + sum(kwargs.values())

sum = get_sum(1,2,a=3,b=4)
print(sum)