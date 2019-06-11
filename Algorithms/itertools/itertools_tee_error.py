#通过tee()共享它们的输入创建的新迭代器，因此在创建新迭代器之后不应使用原始迭代器
#如果从原始输入中消耗了值，则新迭代器将不会生成这些值
from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)

print('r:', end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()

print('i1:', list(i1))
print('i2:', list(i2))


"""
output:
r: 0 1 2 
i1: [3, 4]
i2: [3, 4]
"""