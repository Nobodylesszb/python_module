import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nBefore:', bob)
bob2 = bob._replace(name='Robert')
print('After:', bob2)
print('Same?:', bob is bob2)

"""
ons_namedtuple_asdict.py
Representation: Person(name='Bob', age=30)
As Dictionary: OrderedDict([('name', 'Bob'), ('age', 30)])
"""

"""
output:
Before: Person(name='Bob', age=30)
After: Person(name='Robert', age=30)
Same?: False
"""