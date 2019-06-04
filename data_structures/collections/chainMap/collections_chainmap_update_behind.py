#ChainMap不会缓存子映射中的值。
# 因此，如果修改了它们的内容，则在ChainMap访问时反映结果 

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After : {}'.format(m['c']))

"""
output:
Before: C
After : E
"""