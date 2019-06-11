from itertools import *


def check_item(x):
    print('Testing:', x)
    return x < 1


for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

"""
output:
Testing: -1
Testing: 0
Testing: 1
Yielding: 1
Testing: 2
Yielding: 2
Testing: -2
"""