"""
正则替换步骤：
    1.导包
        import re
    2.正则匹配
        result = re.match('正则表达式','要校验的字符串')                         依次匹配
        resurt = re.search('正则表达式','要校验的字符串')                        分段查找
        result = re.sub(’正则规则‘，’新字符串‘，’要被替换的字符串‘)                替换
    3.获取结果
        result.group()
"""

import re

s = '胜利，失败，失败，失败，胜利'

result = re.sub('失败','胜利',s)

print(result)


































