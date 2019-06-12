# 构建路径
# 除了将现有路径分开之外，
# 经常需要从其他字符串构建路径。要将多个路径组件组合为单个值，请使用join()：

import os.path

PATHS = [
    ('one', 'two', 'three'),
    ('/', 'one', 'two', 'three'),
    ('/one', '/two', '/three'),
]

for parts in PATHS:
    print('{} : {!r}'.format(parts, os.path.join(*parts)))

"""
output:
('one', 'two', 'three') : 'one\\two\\three'
('/', 'one', 'two', 'three') : '/one\\two\\three'
('/one', '/two', '/three') : '/three'

"""