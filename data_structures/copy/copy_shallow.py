import copy
import functools

#创建的浅表副本copy()是一个新容器，
# 其中填充了对原始对象内容的引用。在制作list对象的浅表副本时，
# list 会构造一个new 并将原始对象的元素附加到其上。
@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

a = MyClass('a')
my_list = [a]
dup = copy.copy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))

"""
output:
             my_list: [<__main__.MyClass object at 0x00000199E854B8D0>]
                 dup: [<__main__.MyClass object at 0x00000199E854B8D0>]
      dup is my_list: False
      dup == my_list: True
dup[0] is my_list[0]: True
dup[0] == my_list[0]: True
"""