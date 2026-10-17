"""
1
需求:
    问1，2，3，4能组合成的四位数有几种情况，按照5个一行输出。
要求:
    1.要求同时包含1，2，3，4这四个数字。
        1234，1324均可 1122，1123不行
    2.要求数字1和3不能挨着。
        1324，3124不行 1234，3412可以
    3，数字4不能开头。
    4．5行以内搞定（包5行）
"""
# count =0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             for l in range(1,5):
#                 if (i!=j and i!=k and i!=l and j!=k and j!=l and k!=l)and((i+j!=4)and(j+k!=4)and(k+l!=4))and(i!=4):
#                     num = i*1000+j*100+k*10+l
#                     count+=1
#                     if count%5!=0:
#                         print(num,end=' ')
#                     else:
#                         print(num)

"""
2
已知列表:my_list =['aa','bb','cc','bb','bb','bb','dd'], 删除所有的bb元素，尽可能多的用不同的解决方案做。
"""

my_list =['aa','bb','cc','bb','bb','bb','dd']
new_list = []

# my_list.remove('bb')
# print(my_list)

# for i in range(0,len(my_list)):
#     if my_list[i] != 'bb':
#         new_list.append(my_list[i])
# print(new_list)

for s in my_list:
    if s == 'bb':
        my_list.remove('bb')
print(my_list)

# import copy
#
# new_list = copy.copy(my_list)
# print(new_list)

















































