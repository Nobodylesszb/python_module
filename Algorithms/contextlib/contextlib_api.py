class Context:
    def __init__(self):
        print('__init__()')
    
    def __enter__(self):
        print('__enter__()')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')

with Context():
    print('Doing work in the context')

#组合上下文管理器和with语句是一种更紧凑的编写try:finally块的__exit__()方法，
# 因为即使引发了异常，也总是调用上下文管理器的方法

"""
output:
__init__()
__enter__()
Doing work in the context
__exit__()
"""

