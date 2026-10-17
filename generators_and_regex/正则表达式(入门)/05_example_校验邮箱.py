"""
案例：演示正则表达式之校验邮箱。

正则规则：
    |       代表 或者的意思
    ()      代表分组，从左往右数，第几个左小括号(，就表示第几组
    \num    代表引用第几组的内容。

    扩展:
        (?P<分组名>)   设置分组
        (?P=分组名)    使用分组
"""

import re

email = "abc@163.com"

result = re.match(r'^[a-zA-Z0-9_]{3,20}@(163|126|qq)\.com$',email)

print(result.group() if result else '未匹配 ')