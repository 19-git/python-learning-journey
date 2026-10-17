"""
案例：演示生成器 的 推导式写法

生成器:
    概述：
        生成器 是 基于数据规则，用一部分再生成一部分，而不是一下子生成所有
    目的：
        可以节省大量的内存
    实现方式：
        1.推导式写法
        2.yield关键字
"""
import sys #system 系统模块

#场景1：生成器 推导式写法
#需求1:生成1~10之间的整数
my_generator = (i for i in range(1,11))
print(my_generator)
print(type(my_generator))

print()

#需求2：生成1~10之间的偶数
my_generator1 = (i for i in range(1,11) if i%2==0)
print(my_generator1)

print()

#需求3：如何从生成器中获取数据
#思路1：next
print(next(my_generator1))
print(next(my_generator1))
print(next(my_generator1))

print()

for i in my_generator1:
    print(i)

print()

#验证生成器的目的 可以减少内存占用
my_list = [i for i in range(10000000)]
my_generator2 = (i for i in range(10000000))
print(type(my_generator2),type(my_list))

print(f'my_list 占用的内存: {sys.getsizeof(my_list)}')
print(f'my_generator2 占用的内存: {sys.getsizeof(my_generator2)}')





































