# 合并和拆分迭代器
# 该chain()函数将多个迭代器作为参数，
# 并返回一个迭代器，该迭代器生成所有输入的内容，
# 就好像它们来自单个迭代器一样

from itertools import *

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()
"""
output:
1 2 3 a b c 
"""