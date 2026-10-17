"""
案例：演示正则表达式之 校验单个字符.

正则表达式介绍：
    概述：
        正确的，符合特定规定的 字符串。
        Regular Expression,正则表达式，简称：re
    细节：
        1.学习正则表达式的规则
        2.要求能看懂 其表达式 并且 会简单修改
        3.正则不独属于py
    步骤：
        1.导包
            import re
        2.正则匹配
            resurt = re.match('正则表达式'，‘要校验的字符串’)    从(要校验的字符串)前往后依次匹配(正则表达式)   能匹配即可
            resurt = re.search('正则表达式','要校验的字符串')    (要校验的字符串)中分段查找(正则表达式)
        3.获取匹配结果
            result.group()
"""

#1.导包
import re

#2.正则校验   参1：正则规则  参2：要被校验的字符串
result = re.match('.it','ait')     #匹配成功
result = re.match('.it','你it')    #匹配成功
result = re.match('.it','你好it')   #匹配失败
result = re.match('[^abg]it','qit')#匹配成功
result = re.match('[^abc]de','qde123')#匹配成功  qde   因为从前往后依次查找，匹配到就返回
result = re.search('abc','123abc456')   #abc
result = re.match('[3-7]abd','4abd')   #[3-7]等价[34567]

#3.获取匹配结果
if result:
    print(result.group())
else:
    print('匹配失败')




























