#该accumulate()函数处理输入iterable，
# 将第n和第n + 1项传递给函数并生成返回值而不是任何一个输入。
# 用于组合这两个值的默认函数会将它们相加，
# 因此accumulate()可用于生成一系列数字输入的累积和

from itertools import *

print(list(accumulate(range(5))))
print(list(accumulate('abcde')))

"""
output:
[0, 1, 3, 6, 10]
['a', 'ab', 'abc', 'abcd', 'abcde']
"""