### tempfile

#### explain
- 安全地创建具有唯一名称的临时文件，因此想要破坏应用程序或窃取数据的人无法猜到这些文件具有挑战性。该tempfile模块提供了几个安全地创建临时文件系统资源的功能。 TemporaryFile()打开并返回一个未命名的文件， NamedTemporaryFile()打开并返回一个命名文件， SpooledTemporaryFile在写入磁盘之前将其内容保存在内存中，并且TemporaryDirectory是一个上下文管理器，在关闭上下文时删除该目录