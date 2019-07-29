import itertools

x  = itertools.dropwhile(lambda e: e < 5, range(10))

print(list(x))

"""
[5, 6, 7, 8, 9]
"""

#与dropwhile相反，保留元素直至真值函数值为假
y = itertools.takewhile(lambda e: e < 5, range(10))

print(list(y))

"""
[0, 1, 2, 3, 4]
"""