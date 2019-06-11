# 通用函数
# 在像Python这样的动态类型语言中 
# 通常需要根据参数的类型执行稍微不同的操作，
# 尤其是在处理项目列表和单个项目之间的差异时。这是很简单的直接检查的参数的类型，
# 但在将行为差异可被分离成单独的功能的情况下functools提供了 
# singledispatch()装饰注册一组通用函数基于所述第一参数的一个函数的类型进行自动切换。

import functools


@functools.singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))


@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))


@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list()')
    for item in arg:
        print('  {}'.format(item))


myfunc('string argument')
myfunc(1)
myfunc(2.3)
myfunc(['a', 'b', 'c'])

"""
output:
default myfunc('string argument')
myfunc_int(1)
default myfunc(2.3)
myfunc_list()
  a
  b
  c
"""

# register()新函数的属性用作注册替代实现的另一个装饰器。
# singledispatch()如果没有找到其他特定于类型的函数，
# 则包装的第一个函数是默认实现，如本float例中的情况