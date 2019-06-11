#该cycle()函数返回一个迭代器，它重复无限期给出的参数的内容。
# 由于它必须记住输入迭代器的全部内容，
# 如果迭代器很长，它可能会消耗相当多的内存
from itertools import *

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)

"""
output:
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'a')
(4, 'b')
(5, 'c')
(6, 'a')
"""