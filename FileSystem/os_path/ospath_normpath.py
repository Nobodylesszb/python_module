#使用join()嵌入变量或使用嵌入变量从单独的字符串组装的路径
# 可能最终会带有额外的分隔符或相对路径组件。
# 用它normpath()来清理它们：

import os.path

PATHS = [
    'one//two//three',
    'one/./two/./three',
    'one/../alt/two/three',
]

for path in PATHS:
    print('{!r:>22} : {!r}'.format(path, os.path.normpath(path)))

"""
output:
     'one//two//three' : 'one\\two\\three'
   'one/./two/./three' : 'one\\two\\three'
'one/../alt/two/three' : 'alt\\two\\three'
"""