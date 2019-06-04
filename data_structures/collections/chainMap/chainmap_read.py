# 本ChainMap类管理字典的序列，
# 并通过他们在给他们找到与键关联的值的顺序搜索。
# A ChainMap构成一个良好的“上下文”容器，
# 因为它可以被视为一个堆栈，当堆栈增长时会发生更改，
# 随着堆栈的缩小，这些更改会再次被丢弃

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print(m)
# print(m.values())
print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print()

print('Keys = {}'.format(list(m.keys())))
print('Values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))

"""
ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
ValuesView(ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}))
Individual Values
a = A
b = B
c = C

Keys = ['b', 'c', 'a']
Values = ['B', 'C', 'A']

Items:
b = B
c = C
a = A

"d" in m: False
"""