# 过滤
# 该dropwhile()函数返回一个迭代器，它在条件第一次变为false后生成输入迭代器的元素

from itertools import *


def should_drop(x):
    print('Testing:', x)
    return x < 1


for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
    
#dropwhile()不过滤输入的每个项目; 在第一次条件为假之后，返回输入中的所有剩余项目
"""
output:
Testing: -1
Testing: 0
Testing: 1
Yielding: 1
Yielding: 2
Yielding: -2
"""