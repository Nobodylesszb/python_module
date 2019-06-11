import copy
import functools
#自定义复制行为
# 它是可以控制的副本如何使用做出 __copy__()和__deepcopy__()特殊方法。

# __copy__() 在没有任何参数的情况下调用，并且应该返回该对象的浅表副本。
# __deepcopy__()使用备注字典调用，并返回该对象的深层副本。需要深度复制的任何成员属性都应copy.deepcopy()与memo字典一起传递，以控制递归。（备忘录词典稍后会有更详细的解释。）

@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

    def __copy__(self):
        print('__copy__()')
        return MyClass(self.name)

    def __deepcopy__(self, memo):
        print('__deepcopy__({})'.format(memo))
        return MyClass(copy.deepcopy(self.name, memo))


a = MyClass('a')

sc = copy.copy(a)
print(sc ==a)
dc = copy.deepcopy(a)
print(dc ==a)

"""
output:
__copy__()
True
__deepcopy__({})
True
"""