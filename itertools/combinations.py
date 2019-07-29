import itertools

x = itertools.combinations(range(4),3)
print(list(x))

y = itertools.combinations_with_replacement('abc',2)
print(list(y))

"""
output:
[(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
[('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
"""