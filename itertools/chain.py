from itertools import *
x = chain(range(3), range(4), [3,2,1])
print(x)
print(list(x))
print(list(x)) #只能迭代一次

"""
<itertools.chain object at 0x000001EED930C278>
[0, 1, 2, 0, 1, 2, 3, 3, 2, 1]
[]
"""
