from itertools import *


def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c']

b = make_iterables_to_chain()
print('b,{}'.format(b))


for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')
print()

"""
output:
b,<generator object make_iterables_to_chain at 0x00000226BED76830>
1 2 3 a b c 
"""