class Context:
    def __init__(self,handle_error):
        print('__init__({})'.format(handle_error))
        self.handle_error = handle_error
    
    def __enter__(self):
        print('__enter()')
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('__exit__()')
        print('  exc_type =', exc_type)
        print('  exc_val  =', exc_val)
        print('  exc_tb   =', exc_tb)
        return self.handle_error

    

with Context(True):
    raise RuntimeError('error message handled')

print()

with Context(False):
    raise RuntimeError('error message propagated')


#如果上下文管理器可以处理异常，__exit__() 则应返回true值以指示不需要传播该异常。
# 返回false会导致在__exit__()返回后重新引发异常


"""
output:
Context.__init__()
Context.__enter__()
WithinContext.__init__(<__main__.Context object at 0x00000292180F4400>)
WithinContext.do_something()
Context.__exit__()
WithinContext.__del__

[Done] exited with code=0 in 0.101 seconds

[Running] set PYTHONIOENCODING=utf8 && python "d:\myownproject\python_module\Algorithms\contextlib\contextlib_api_error.py"
__init__(True)
__enter()
__exit__()
  exc_type = <class 'RuntimeError'>
  exc_val  = error message handled
  exc_tb   = <traceback object at 0x0000027824BBF808>

__init__(False)
__enter()
__exit__()
  exc_type = <class 'RuntimeError'>
  exc_val  = error message propagated
  exc_tb   = <traceback object at 0x0000027824BBF808>
Traceback (most recent call last):
  File "d:\myownproject\python_module\Algorithms\contextlib\contextlib_api_error.py", line 25, in <module>
    raise RuntimeError('error message propagated')
RuntimeError: error message propagated
"""