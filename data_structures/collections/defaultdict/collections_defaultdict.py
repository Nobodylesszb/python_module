import collections

#标准字典包括setdefault()用于检索值并在值不存在时建立默认值的方法。
# 相反，defaultdict让初始化容器时，调用者可以预先指定默认值。
def default_factory():
    return 'default value'


d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])

"""
output:
d: defaultdict(<function default_factory at 0x000001DA74E17BF8>, {'foo': 'bar'})
foo => bar
bar => default value
"""