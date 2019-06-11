# 比较
# 在Python 2下，类可以定义一个__cmp__()方法，该方法返回-1，0或1基于对象是否小于，
# 等于或大于被比较的项。Python 2.1中引入的富比较方法API（ ，__lt__()， __le__()，__eq__()，__ne__()，__gt__()和 __ge__()），
# 其执行单一比较操作，并返回一个布尔值。Python 3不赞成使用__cmp__()这些新方法，并functools提供了一些工具，
# 可以更轻松地编写符合Python 3中新的比较要求的类。

# 丰富的比较
# 丰富的比较API旨在允许具有复杂比较的类以尽可能最有效的方式实现每个测试。但是，
# 对于比较相对简单的类，手动创建每个丰富的比较方法都没有意义。本total_ordering()类装饰需要一个类，它提供一些方法，并增加了他们的休息。
import functools
import inspect
from pprint import pprint


@functools.total_ordering
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print('  testing __eq__({}, {})'.format(
            self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print('  testing __gt__({}, {})'.format(
            self.val, other.val))
        return self.val > other.val


print('Methods:\n')
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print('\nComparisons:')
for expr in ['a < b', 'a <= b', 'a == b', 'a >= b', 'a > b']:
    print('\n{:<6}:'.format(expr))
    result = eval(expr)
    print('  result of {}: {}'.format(expr, result))

"""
output:

Methods:

[('__eq__', <function MyObject.__eq__ at 0x10139a488>),
 ('__ge__', <function _ge_from_gt at 0x1012e2510>),
 ('__gt__', <function MyObject.__gt__ at 0x10139a510>),
 ('__init__', <function MyObject.__init__ at 0x10139a400>),
 ('__le__', <function _le_from_gt at 0x1012e2598>),
 ('__lt__', <function _lt_from_gt at 0x1012e2488>)]

Comparisons:

a < b :
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a < b: True

a <= b:
  testing __gt__(1, 2)
  result of a <= b: True

a == b:
  testing __eq__(1, 2)
  result of a == b: False

a >= b:
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a >= b: False

a > b :
  testing __gt__(1, 2)
  result of a > b: False
"""