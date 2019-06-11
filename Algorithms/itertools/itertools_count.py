#该count()函数返回一个无限期生成连续整数的迭代器。
# 第一个数字可以作为参数传递（默认值为零）。
# 没有上限参数（range()有关结果集的更多控制，请参阅内置参数）

from itertools import *

for i in zip(count(1), ['a', 'b', 'c']):
    print(i)


"""
output:
(1, 'a')
(2, 'b')
(3, 'c')
"""