from itertools import accumulate

x = accumulate(range(10))
print(x)
print(list(x))

"""
<itertools.accumulate object at 0x000002CF62696CC8>
[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
"""

