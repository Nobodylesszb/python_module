# 默认情况下，货架不跟踪对易失性对象的修改。
# 这意味着如果更改了存储在工具架中的项目的内容，
# 则必须通过再次存储整个项目来显式更新工具架

import shelve

with shelve.open('test_shelf.db') as s:
    print(s['key'])
    s['key']['new_value'] = 'this was not here before'

with shelve.open('test_shelf.db', writeback=True) as s:
    print(s['key'])

"""
output:
{'int': 10, 'float': 9.5, 'string': 'Sample data'}
{'int': 10, 'float': 9.5, 'string': 'Sample data'}
"""