import itertools

# 上文使用过的函数，对迭代器进行切片
x = itertools.islice(range(10), 0, 9, 2)

print(list(x))

"""
[0, 2, 4, 6, 8]
"""

