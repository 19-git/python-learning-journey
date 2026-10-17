def fun_out(num1):
    def fun_inn(num2):
        sum = num1 + num2
        return sum
    return fun_inn

print(fun_out(3)(5))
fun_inn=fun_out(3)
print(fun_inn(5))