def double_decorator(choice):
        def my_decorator(fn_name):
            def fn_inner(a,b):
                if choice == "+":
                    print("努力[相加]中~")
                elif choice == "-":
                    print("努力[相减]中~")
                return fn_name(a,b)
            return fn_inner
        return my_decorator

@double_decorator("+")
def get_sum(a,b):
    return a+b

@double_decorator("-")
def get_sub(a,b):
    return a-b


sum = get_sum(1,2)
print(sum)

sub = get_sub(1,2)
print(sub)