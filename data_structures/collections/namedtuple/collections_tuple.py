import collections
Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nRepresentation:', bob)

jane = Person(name='Jane', age=29)
print('\nField by name:', jane.name)

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is {} years old'.format(*p))

"""
Representation: Person(name='Bob', age=30)

Field by name: Jane

Fields by index:
Bob is 30 years old
Jane is 29 years old
"""
#像一个普通的tuple，一个namedtuple是不可改变的。
# 此限制允许tuple实例具有一致的哈希值，
# 这使得可以将它们用作词典中的键并包含在集合中
