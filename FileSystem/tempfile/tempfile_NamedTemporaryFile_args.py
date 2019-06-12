# 预测名称
# 虽然不如严格的匿名临时文件安全，包括名称中的可预测部分，
# 但可以找到该文件并检查它以进行调试。
# 到目前为止所描述的所有函数都有三个参数来控制文件名到某种程度。
# 名称使用以下公式生成：
# dir + prefix + random + suffix
# 除了random可以将所有值作为参数传递给用于创建临时文件或目录的函数

import tempfile

with tempfile.NamedTemporaryFile(suffix='_suffix',
                                 prefix='prefix_',
                                 dir='/FileSystem/tempfile/') as temp:
    print('temp:')
    print('  ', temp)
    print('temp.name:')
    print('  ', temp.name)

"""
output:
temp:
   <tempfile._TemporaryFileWrapper object at 0x1018b2d68>
temp.name:
   /tmp/prefix_q6wd5czl_suffix
"""