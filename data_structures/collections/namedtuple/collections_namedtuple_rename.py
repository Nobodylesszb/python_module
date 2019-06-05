import collections

with_class = collections.namedtuple(
    'Person', 'name class age',
    rename=True)
print(with_class._fields)

two_ages = collections.namedtuple(
    'Person', 'name age age',
    rename=True)
print(two_ages._fields)

#重命名字段的新名称取决于它们在元组中的索引，
# 因此名称的字段class将变为_1，并且重复 age字段将更改为_2。
"""
output:
('name', '_1', 'age')
('name', 'age', '_2')
"""