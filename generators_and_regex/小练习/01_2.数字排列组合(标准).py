"""
1.
思路：将数字转换成字符串，然后调用字符串的功能做判断
"""
# count=0
# for s in [str(i) for i in range(1234,4321+1)]:
#     if ('1' in s and '2' in s and '3' in s and '4' in s)and(('13'not in s)and('31'not in s))and(s[0]!='4'):
#         count+=1
#         print(s,end=' ' if count % 5 !=0 else '\n')

# print([int(s) for s in  [str(i) for i in range(1234,4321+1)] if ('1' in s and '2' in s and '3' in s and '4' in s)and(('13'not in s)and('31'not in s))and(s[0]!='4')])

"""
2.

"""
my_list =['aa','bb','cc','bb','bb','bb','dd']

# new_list = [s for s in my_list if s != 'bb']
# print(new_list)

for s in my_list[:]:#浅拷贝一份副本 通过遍历副本的方式 移原源列表里的字符串 (副本的列表无变化)  [:]切片的本质是浅拷贝
    if s == 'bb':
        my_list.remove('bb')
print(my_list)








