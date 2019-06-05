import collections

c = collections.Counter('extremely')
c['z'] = 0
print(c)
#该elements()方法返回一个迭代器，
# 它生成所有已知的项目Counter。
print(list(c.elements()))
"""
output:
Counter({'e': 3, 'x': 1, 't': 1, 'r': 1, 'm': 1, 'l': 1, 'y': 1,
'z': 0})
['e', 'e', 'e', 'x', 't', 'r', 'm', 'l', 'y']
"""