#该starmap()函数类似于map()，
# 但不是从多个迭代器构造元组，
# 而是使用*语法将单个迭代器中的项拆分为映射函数的参数

from itertools import *

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]

for i in starmap(lambda x, y: (x, y, x * y), values):
    print('{} * {} = {}'.format(*i))


"""
0 * 5 = 0
1 * 6 = 6
2 * 7 = 14
3 * 8 = 24
4 * 9 = 36
"""