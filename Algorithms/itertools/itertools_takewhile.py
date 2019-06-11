#相反的dropwhile()是takewhile()。它返回一个迭代器，
# 只要测试函数返回true，它就会从输入迭代器返回项

from itertools import *


def should_take(x):
    print('Testing:', x)
    return x < 2


for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

#一旦should_take()返回False，就takewhile() 停止处理输入
"""
output:
Testing: -1
Yielding: -1
Testing: 0
Yielding: 0
Testing: 1
Yielding: 1
Testing: 2
"""