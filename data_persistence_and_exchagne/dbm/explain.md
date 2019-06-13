### dbm

#### explain
- dbm是DBM样式数据库的前端，它使用简单的字符串值作为访问包含字符串的记录的键。它用于 whichdb()标识数据库，然后使用适当的模块打开它们。它用作后端shelve，用于将对象存储在DBM数据库中pickle。

#### 数据库类型

- Python附带了几个用于访问DBM样式数据库的模块。选择的默认实现取决于当前系统上可用的库以及编译Python时使用的选项。与特定实现的独立接口允许Python程序与其他语言中的程序交换数据，这些程序不会在可用格式之间自动切换，或者编写可在多个平台上工作的可移植数据文件。

**dbm.gnu** 
- dbm.gnu是dbm GNU项目中库版本的接口。它的工作方式与此处描述的其他DBM实现相同，只需对flags 支持的更改进行一些更改open()。

除了标准的'r'，'w'，'c'，和'n'标志， dbm.gnu.open()支持：

'f'以快速模式打开数据库。在快速模式下，对数据库的写入不同步。
's'以同步模式打开数据库。对数据库的更改将在创建时写入文件，而不是在数据库关闭或显式同步之前被延迟。
'u' 打开数据库解锁。
**dbm.ndbm** 
该dbm.ndbm模块提供了dbm格式的Unix ndbm实现的接口，具体取决于编译期间模块的配置方式。module属性library 标识库configure在编译扩展模块时能够找到的名称。

**dbm.dumb** 
dbm.dumb当没有其他实现可用时，该模块是DBM API的可移植回退实现。不需要使用外部依赖项dbm.dumb，但它比大多数其他实现慢。