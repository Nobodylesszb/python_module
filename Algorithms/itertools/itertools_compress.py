#compress()提供了另一种过滤迭代内容的方法。它不是调用函数，
# 而是使用另一个iterable中的值来指示何时接受值以及何时忽略它

from itertools import *

every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=' ')
print()

"""
output:
3 6 9 
"""