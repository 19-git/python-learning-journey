#需求：通过yield方式，获取到生成器 1~10之间的整数
#回顾：推导式写法
my_g = (i for i in range(10))

#yield方式如下
#1.定义函数，储存到生成器中，并返回
def my_fun():
    # my_list = []            #创建
    # for i in range(1,11):
    #     my_list.append(i)   #添加
    # return my_list          #返回

    #效果和上述代码类似
    # yield在这里做了三件事儿：1.创建生成器对象，2.把值存储到生成器中，3.返回生成器，
    for i in range(1,11):
        yield i

my_generator = my_fun()
print(type(my_generator))
print(next(my_generator))

print()

for item in my_generator:
    print(item)
