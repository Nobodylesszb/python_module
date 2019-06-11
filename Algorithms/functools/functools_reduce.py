# 减少数据集
# 该reduce()函数将可调用数据和数据序列作为输入，
# 并根据使用序列中的值调用callable并累积结果输出，生成单个值作为输出。

import functools


def do_reduce(a, b):
    print('do_reduce({}, {})'.format(a, b))
    return a + b


data = range(1, 5)
print(data)
result = functools.reduce(do_reduce, data)
print('result: {}'.format(result))

"""
range(1, 5)
do_reduce(1, 2)
do_reduce(3, 3)
do_reduce(6, 4)
result: 10
"""