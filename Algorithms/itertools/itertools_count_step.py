#start和step参数count()可以是可以一起添加的任何数值
import fractions
from itertools import *

start = fractions.Fraction(1, 4)
step = fractions.Fraction(1, 4)
print('start:',start)
print('end:',step)
for i in zip(count(start, step), ['a', 'b', 'c','d']):
    print('{}: {}'.format(*i))

"""
start: 1/4
end: 1/4
1/4: a
1/2: b
3/4: c
1: d
"""