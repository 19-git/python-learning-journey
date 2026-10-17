"""
校验手机号
    规则：1.长度11位  2.纯数字  3.第一位是1  4.第二位[3-9]
"""

import re

result = re.match(r'^1[3-9]\d{9}$','13909696222')

print(result.group()if result else '未匹配')