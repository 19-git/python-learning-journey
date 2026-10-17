import re

result = re.match('.*abc','123abc')

result = re.search('q+abc','qqabc')

result = re.search('y{2}ab','yyab')

result = re.search('y{3,}ab','yyyyab')

result = re.search('y{1,4}ab','yyab')

print(result.group() if result else '未匹配')