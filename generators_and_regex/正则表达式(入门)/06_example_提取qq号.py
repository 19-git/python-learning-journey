import re

s = 'qq:123456'

result = re.match(r'^qq:(\d{6,12})$',s)

if result:
        print(f'提取qq号:{result.group(1)}')
else:
    print('未匹配  ')