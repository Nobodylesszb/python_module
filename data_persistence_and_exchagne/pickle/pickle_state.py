#并非所有物体都可以腌制。具有依赖于操作系统或其他进程的运行时状态的套接字，文件句柄，\
# 数据库连接和其他对象可能无法以有意义的方式保存。具有不可选属性的对象可以定义 __getstate__()和__setstate__()返回要被pickle的实例的状态的子集。

# 该__getstate__()方法必须返回包含对象内部状态的对象。
# 表示该状态的一种便捷方式是使用字典，但该值可以是任何可选对象。
# 存储状态，并__setstate__()在从pickle加载对象时传递状态。

import pickle


class State:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'State({!r})'.format(self.__dict__)


class MyClass:

    def __init__(self, name):
        print('MyClass.__init__({})'.format(name))
        self._set_name(name)

    def _set_name(self, name):
        self.name = name
        self.computed = name[::-1]

    def __repr__(self):
        return 'MyClass({!r}) (computed={!r})'.format(
            self.name, self.computed)

    def __getstate__(self):
        state = State(self.name)
        print('__getstate__ -> {!r}'.format(state))
        return state

    def __setstate__(self, state):
        print('__setstate__({!r})'.format(state))
        self._set_name(state.name)


inst = MyClass('name here')
print('Before:', inst)

dumped = pickle.dumps(inst)

reloaded = pickle.loads(dumped)
print('After:', reloaded)


"""
MyClass.__init__(name here)
Before: MyClass('name here') (computed='ereh eman')
__getstate__ -> State({'name': 'name here'})
__setstate__(State({'name': 'name here'}))
After: MyClass('name here') (computed='ereh eman')
"""