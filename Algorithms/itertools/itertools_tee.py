# 该tee()函数根据单个原始输入返回几个独立的迭代器（默认为2）

from itertools import *

r = islice(count(), 5)
print('r:',r)
print('r:',list(r))
i1, i2 = tee(r)

print('i1:', list(i1))
print('i2:', list(i2))
# 迭代器只能使用一次，使用后元素消耗完
"""
output:
r: <itertools.islice object at 0x0000019DE1E95818>
r: [0, 1, 2, 3, 4]
i1: []
i2: []
"""

# r = islice(count(), 5)
# i1, i2 = tee(r)

# print('i1:', list(i1))
# print('i2:', list(i2))

"""
output:
i1: [0, 1, 2, 3, 4]
i2: [0, 1, 2, 3, 4]

"""