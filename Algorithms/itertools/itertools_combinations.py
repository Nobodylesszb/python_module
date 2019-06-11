#要将值限制为唯一组合而不是排列，请使用combinations()。
# 只要输入的成员是唯一的，输出就不会包含任何重复的值

from itertools import *


def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()


print('Unique pairs:\n')
show(combinations('abcd', r=2))

"""
Unique pairs:

ab ac ad 
bc bd 
cd 
"""