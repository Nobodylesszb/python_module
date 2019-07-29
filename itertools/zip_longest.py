import itertools

x =itertools.tee(range(10),2)

for letters in x:
    print(list(letters))

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""