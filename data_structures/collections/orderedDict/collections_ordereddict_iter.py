import collections
print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k,v in d.items():
    print(k,v)

print('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k, v in d.items():
    print(k, v)

"""
output:
Regular dictionary:
a A
b B
c C

OrderedDict:
a A
b B
c C
"""

#在Python 3.6之前，常规dict不跟踪插入顺序，
# 并且迭代它会根据密钥在哈希表中的存储方式按顺序生成值，
# 而哈希表又受随机值的影响以减少冲突。在一个OrderedDict与此相反，
# 在其中被插入的项目的顺序被记住并创建一个迭代时使用。


