# finditer()函数返回一个迭代器，
# 它生成Match 实例而不是返回的字符串findall()
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(
        text[s:e], s, e))

"""
Found 'ab' at 0:2
Found 'ab' at 5:7
"""