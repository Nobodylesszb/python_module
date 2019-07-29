import itertools
# x = itertools.compress(range(5),(True, False, True, True, False))
# print(list(x))

"""
output:
[0, 2, 3]
"""


x = itertools.count(start=20, step=-1)
print(list(x))
print(list(itertools.islice(x, 0, 10, 1)))


 