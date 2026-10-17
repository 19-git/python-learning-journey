"""
案例：演示单任务，前面不执行完毕，后面绝对无法执行
"""

def fun_a():
    for i in range(1000):
        print("HELLO WORLD")

def fun_b():
    for i in range(1):
        print("HELLO python")

fun_a()
print("*"*20)
fun_b()