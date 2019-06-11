# zip()第一个输入迭代器耗尽时停止。
# 要处理所有输入，即使迭代器产生不同数量的值，也要使用zip_longest()

from itertools import *

r1 = range(3)
r2 = range(2)

print('zip stops early:')
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print('\nzip_longest processes all of the values:')
print(list(zip_longest(r1, r2)))

"""
output:
zip stops early:
[(0, 0), (1, 1)]

zip_longest processes all of the values:
[(0, 0), (1, 1), (2, None)]
"""