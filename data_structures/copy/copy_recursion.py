import copy


class Graph:

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return 'Graph(name={}, id={})'.format(
            self.name, id(self))

    def __deepcopy__(self, memo):
        print('\nCalling __deepcopy__ for {!r}'.format(self))
        if self in memo:
            existing = memo.get(self)
            print('  Already copied to {!r}'.format(existing))
            return existing
        print('  Memo dictionary:')
        if memo:
            for k, v in memo.items():
                print('    {}: {}'.format(k, v))
        else:
            print('    (empty)')
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print('  Copying to new object {}'.format(dup))
        memo[self] = dup
        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup


root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])
root.add_connection(a)
root.add_connection(b)

dup = copy.deepcopy(root)


#所述Graph类包括几个基本的有向图的方法。可以使用名称和与其连接的现有节点列表初始化实例。该add_connection() 方法用于设置双向连接。它也被深拷贝运算符使用。

#该__deepcopy__()方法打印消息以显示其调用方式，并根据需要管理备忘录字典内容。
# 它不是复制整个连接列表，而是创建一个新列表，并将各个连接的副本附加到它。
# 这确保了备忘录字典在每个新节点被复制时更新，并且它避免了递归问题或节点的额外副本。和以前一样，
# 该方法在完成时返回复制的对象。


"""
output:
Calling __deepcopy__ for Graph(name=root, id=2038461780824)
  Memo dictionary:
    (empty)
  Copying to new object Graph(name=root, id=2038461783512)

Calling __deepcopy__ for Graph(name=a, id=2038461782336)
  Memo dictionary:
    Graph(name=root, id=2038461780824): Graph(name=root, id=2038461783512)
  Copying to new object Graph(name=a, id=2038461789240)

Calling __deepcopy__ for Graph(name=root, id=2038461780824)
  Already copied to Graph(name=root, id=2038461783512)

Calling __deepcopy__ for Graph(name=b, id=2038461782952)
  Memo dictionary:
    Graph(name=root, id=2038461780824): Graph(name=root, id=2038461783512)
    Graph(name=a, id=2038461782336): Graph(name=a, id=2038461789240)
    2038461780824: Graph(name=root, id=2038461783512)
    2038461737288: [Graph(name=root, id=2038461780824), Graph(name=a, id=2038461782336)]
    2038461782336: Graph(name=a, id=2038461789240)
  Copying to new object Graph(name=b, id=2038461789464)
"""
