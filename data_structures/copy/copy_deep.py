import copy
import functools

#创建的深层副本deepcopy()是一个新容器，
# 其中填充了原始对象内容的副本。要构建a的深层副本，
# 构造listnew list，将复制原始列表的元素，然后将这些副本附加到新列表中。
#将调用替换为copy()with deepcopy()会使输出明显不同。
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
dup = copy.deepcopy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))

"""
output:
             my_list: [<__main__.MyClass object at 0x00000185804AB8D0>]
                 dup: [<__main__.MyClass object at 0x0000018580654D68>]
      dup is my_list: False
      dup == my_list: True
dup[0] is my_list[0]: False
dup[0] == my_list[0]: True
"""