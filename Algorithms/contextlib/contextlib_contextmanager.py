# 通过使用 _ enter _ () 和 _ exit _ () 方法编写类, 以传统方式创建上下文管理器并不困难。
# 但是, 有时把所有的东西都写出来, 对于一个微不足道的上下文来说是额外的开销。
# 在这种情况下, 使用上下文管理器 () 装饰器将生成器函数转换为上下文管理器。

import contextlib

@contextlib.contextmanager
def make_context():
    print('  entering')
    try:
        yield 'abcd'
    except RuntimeError as err:
        print('  ERROR:', err)
    finally:
        print('  exiting')

print('Normal:')
with make_context() as value:
    print('  inside with statement:', value)

print('\nHandled error:')
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print('\nUnhandled error:')
with make_context() as value:
    raise ValueError('this exception is not handled')

#生成器应该初始化上下文, 只产生一次, 然后清理上下文。生成的值 (如果有) 
# 绑定到与语句的 as 子句中的变量。
# 带有块内的异常在生成器内重新引发, 因此可以在那里处理。
#Exceptions from within the with block are re-raised inside the generator, 
# so they can be handled there.

"""
output:
Normal:
  entering
  inside with statement: abcd
  exiting

Handled error:
  entering
  ERROR: showing example of handling an error
  exiting

Unhandled error:
  entering
  exiting
Traceback (most recent call last):
  File "d:\myownproject\python_module\Algorithms\contextlib\contextlib_contextmanager.py", line 27, in <module>
    raise ValueError('this exception is not handled')
ValueError: this exception is not handled
"""