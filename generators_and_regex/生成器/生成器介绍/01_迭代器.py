"""
案例：演示自定义迭代器

迭代器介绍：
    概述：
        自定义的类，只要重写了__iter__() 和 __next__()方法，就可被称作 迭代器
    目的：
        隐藏的底层逻辑，让用户使用更方便
        惰性加载，用的时候才会获取
"""

#自定义迭代器
#1.自定义迭代器类
class MyIterator:
    #2.通过__init__魔法方法，初始化属性，指定：范围
    def __init__(self,start,end):
        self.current_value = start
        self.end = end

    #3.重写iterator魔法方法，返回当前对象(迭代器对象)
    def __iter__(self):
        return self

    #4.重写__next__魔法方法，返回当前值，并更新当前值
    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration
        self.current_value = self.current_value + 1
        return self.current_value - 1


for i in MyIterator(1,5):
    print(i)

























