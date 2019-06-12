class WithinContext:

    def __init__(self, context):
        print('WithinContext.__init__({})'.format(context))

    def do_something(self):
        print('WithinContext.do_something()')

    def __del__(self):
        print('WithinContext.__del__')


class Context:

    def __init__(self):
        print('Context.__init__()')

    def __enter__(self):
        print('Context.__enter__()')
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit__()')


with Context() as c:
    c.do_something()

#与变量关联的值c是返回的对象__enter__()，该对象不一定是Context在with语句中创建的 实例

"""
output:
Context.__init__()
Context.__enter__()
WithinContext.__init__(<__main__.Context object at 0x101f046d8>)
WithinContext.do_something()
Context.__exit__()
WithinContext.__del__
"""