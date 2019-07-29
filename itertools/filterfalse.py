import itertools
x = itertools.filterfalse(lambda e: e < 5, (1, 5, 3, 6, 9, 4))
print(list(x))

"""
[5, 6, 9]
"""
