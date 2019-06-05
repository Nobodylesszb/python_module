#namedtuple提供了几个有用的属性和方法来处理子类和实例。
# 所有这些内置属性都有一个前缀为下划线（_）的名称，
# 在大多数Python程序中按照惯例表示私有属性。对于 namedtuple，
# 然而，前缀是为了保护名称从用户提供的属性名称冲突

import collections
Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
print('Fields:', bob._fields)

"""
output:
Representation: Person(name='Bob', age=30)
Fields: ('name', 'age')
"""