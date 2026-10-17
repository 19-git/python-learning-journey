def my_decorator(fn_name):
    def fn_inner(a, b):
        if fn_name.__name__ == "get_sum":
            print("努力[相加]中~")
        elif fn_name.__name__ == "get_sub":
            print("努力[相减]中~")
        return fn_name(a, b)
    return fn_inner


@my_decorator
def get_sum(a, b):
    return a + b


@my_decorator
def get_sub(a, b):
    return a - b


sum = get_sum(1, 2)
print(sum)

sub = get_sub(1, 2)
print(sub)