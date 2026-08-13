# ***学习纲要：***

##### **1，debug,注释，输出函数**

##### **2，变量，标识符，**

##### **3，数值类型，字符串，格式化输出**

##### **4，算数，赋值运算符，输入函数，转义字符**

##### **5，比较运算符，逻辑运算符，三目运算**

##### **6，判断类：if-else/elif，try-except**

##### **7，while/for循环**

##### **8，break/contine关键字**

##### **9，列表，元组，字典，集合**

##### **10，类型转换：int,float,str,eva,tuple,list,chr()**

##### **11，深浅拷贝，可变与不可变对象**





## 注释（Comments）：

**注释就是代码里“给人看”的文字，电脑执行时会忽略它们。**



**单行注释（你已经知道）：**



**python**

**# 这是一个单行注释**

**print("你好")**

**多行注释（“假的”）：**

**Python 本身没有真正的多行注释，你看到的三引号 """...""" 其实是一个没有被赋值给变量的字符串，它只是被解释器无视了，所以被当成注释来用。**



**python**

**"""**

**这是三引号包起来的多行文字**

**它会被 Python 忽略**

**因为没赋值给任何变量**

**"""**

**print("你好")**

**但请注意区别（很多教程搞错）：**

**如果你把 """...""" 写在函数或类的开头第一行，它就不再是注释，而变成“文档字符串（Docstring）”。它会被 Python 保存下来，当你用 help(函数名) 时会显示这个内容。**



**python**

**def greet():**

&#x20;   **"""这个函数用来打印欢迎语"""**

&#x20;   **print("你好")**

**help(greet)  # 会显示 "这个函数用来打印欢迎语"**





## 有关print：

print() 的完整参数签名是：



```python

print(\*objects, sep=' ', end='\\n', file=None, flush=False)
```

你提到的 str 其实应该是 \*objects（可以传多个值，不限个数），sep、end、file 都在，但你还漏了一个 flush。



📌 参数顺序（按定义顺序）

| 顺序 | 参数名 | 含义 | 是否必须 |
| :--- | :--- | :--- | :--- |
| 1 | \*objects | 你要打印的内容，可以写多个，用逗号隔开 | 否（不传就打印空行） |
| 2 | sep | 多个内容之间的分隔符，默认是空格 | 否 |
| 3 | end | 打印结束时的结尾字符，默认是换行 `\n` | 否 |
| 4 | file | 输出到哪里，默认是屏幕（sys.stdout） | 否 |
| 5 | flush | 是否强制立即刷新输出缓冲区，默认 False | 否 |

🔍 你漏掉的 flush 是干什么的？

默认情况下，print 会把内容先存进输出缓冲区，等缓冲区满了或程序结束了再一次性显示到屏幕上。这在正常打印中你感觉不到。

但如果你在写进度条或长时间循环，希望每打印一次就立刻显示在屏幕上，而不是等循环结束才一起出现，就需要 flush=True。



```python

import time

for i in range(5):

&#x20;   print(f"进度：{i}", end="", flush=True)

&#x20;   time.sleep(1)
```

不写 flush=True，这 5 个进度可能会攒到循环结束后才一起蹦出来；加上后，每 1 秒立刻显示一个。



🧠 关于顺序的一个关键细节

sep、end、file、flush 都是关键字参数，你在调用时不需要按定义顺序写，只要写清楚参数名就行：



```python

print("A", "B", end=">>>", sep="--")
```

\# 输出：A--B>>>

这里 sep 写在 end 前面，完全没问题。

但如果你不写参数名，只写位置，那么第 2 个值会被当成 sep，第 3 个被当成 end，第 4 个被当成 file，第 5 个被当成 flush。所以一般建议都写明参数名，避免搞混。





## 标识符：

🏷️第一层：标识符的硬性语法（你基本知道，快速过）

组成：字母（a-z, A-Z）、数字（0-9）、下划线（\_）。

首字符不能是数字：1a 不行，a1 行。

大小写敏感：Name 和 name 是两个不同的变量。

关键字不能当标识符：if、while、for、def、class、import、return、try、except、raise、with、yield、lambda、global、nonlocal、True、False、None（一共 35 个，你不需要背，VSCode 会帮你标颜色）。

如果你想知道全部关键字，在 Python 终端输入：



```python

import keyword

print(keyword.kwlist)
```

🔍 第二层：下划线（\_）的四种“暗号”（这是细节）

你以为下划线只是用来分割单词（比如 user\_name），但在 Python 里，它的位置有特殊含义：

| 写法 | 含义 | 你在哪里见过？ |
| :--- | :--- | :--- |
| `_`（单独的下划线） | 用作占位符，表示“这个值我不要” | 你写过 `_, ext = os.path.splitext(filename)`，这里的 `_` 就是占位，只取后缀，忽略文件名。 |
| `name_`（单下划线结尾） | 用来避开 Python 关键字 | 如果你想给变量取名 `class`，会报错，所以写成 `class_` 就可以。你之前在类里用过。 |
| `_name`（单下划线开头） | “受保护的”，仅是一种约定，告诉其他程序员：“这是内部用的，别在外面随便改它”。Python 本身不会阻止你，但 PEP 8 规范建议这样做。 | 你暂时不需要主动写，但在看别人代码时会碰到。 |
| `__name`（双下划线开头） | “名称修饰”，Python 会悄悄把它改成 `_类名__name`，防止子类意外覆盖父类的属性。 | 你目前不需要自己写，但以后读框架源码时会遇到。 |
| `__name__`（双下划线开头和结尾） | “魔术方法/属性”，Python 系统内置的特殊方法。你自己的变量名绝对不能用这种格式，否则会覆盖 Python 的底层功能。 | 你天天见：`__init__`、`__name__`（在 `if __name__ == "__main__"` 里）。 |





## 变量：

⚠️ 第一层：变量不是“盒子”，是“标签”（这是必须扭转的概念）

很多教程告诉你“变量像一个盒子，往里放东西”，但在 Python 里，变量是贴在对象上的便利贴。

代码实证（你在终端里跑一下，亲眼看看）：



```python

a = 1

b = a

print(id(a), id(b))   # id() 是查看对象在内存里的唯一编号


# 你会发现 a 和 b 的编号完全一样！说明它们指向的是同一个东西。



a = 2

print(a, b)           # 输出：2 1

# 为什么 b 还是 1？因为你把 a 的贴纸撕下来，贴到了 2 上，但 b 还贴在原来的 1 上。
```

如果你换成可变对象（列表），效果就不同了：



```python

list_a = [1, 2, 3]

list_b = list_a        # list_b 也贴到了同一个列表上

list_a.append(4)       # 修改了这个列表

print(list_b)          # 输出：[1, 2, 3, 4]  （因为 list_b 贴的还是同一个列表）
```

结论：

- 对于不可变类型（整数、字符串、元组），修改旧变量，新变量不会变（因为是“撕贴纸”操作）。
- 对于可变类型（列表、字典、集合），修改一个变量，另一个也会变（因为是“修改盒子里的内容”操作）。

这个区别是你以后遇到“为什么改了 A，B 也跟着变了”类 bug 的根源。



🔄 第二层：同时给多个变量赋值（拆包与星号）

你已经在 for category, exts in CATEGORIES.items(): 里用过了，这是拆包（Unpacking）。

基础拆包：



```python

x, y = 1, 2

print(x, y)   # 输出：1 2
```

星号拆包（取剩余所有）：



```python

first, *middle, last = [1, 2, 3, 4, 5]

print(first)   # 输出：1

print(middle)  # 输出：\[2, 3, 4]

print(last)    # 输出：5
```

这在处理不确定长度的数据时非常有用。



🧠 第三层：变量名的“生命周期”

- 你在函数内部定义的变量（比如 `def main():` 里面的 `i`），只在这个函数里生效，函数结束就消失了（局部变量）。
- 你在函数外部定义的变量（比如文件顶部的 `TARGET_FOLDER0`），在整个文件里都能用（全局变量）。
- 如果你在函数里想修改全局变量，需要用 `global` 关键字声明（但你现在基本不需要）。





## 可变与不可变对象：

对于不可变类型（整数、字符串、元组），修改旧变量，新变量不会变（因为是“撕贴纸”操作）。

对于可变类型（列表、字典、集合），修改一个变量，另一个也会变（因为是“修改盒子里的内容”操作）。

这个区别是你以后遇到“为什么改了 A，B 也跟着变了”类 bug 的根源。



```python

a = 1

b = a

print(id(a), id(b))   # id() 是查看对象在内存里的唯一编号


# 你会发现 a 和 b 的编号完全一样！说明它们指向的是同一个东西。



a = 2

print(a, b)           # 输出：2 1

# 为什么 b 还是 1？因为你把 a 的贴纸撕下来，贴到了 2 上，但 b 还贴在原来的 1 上。
```

如果你换成可变对象（列表），效果就不同了：



```python

list_a = [1, 2, 3]

list_b = list_a        # list_b 也贴到了同一个列表上

list_a.append(4)       # 修改了这个列表

print(list_b)          # 输出：[1, 2, 3, 4]  （因为 list\_b 贴的还是同一个列表）
```


```python

s = "hello"

# s[0] = "H"   # 如果你取消注释这一行，会报错！因为字符串不可变，不允许改里面的字符。



# 正确的做法是造一个新的字符串

s = "H" + s[1:]  # 这时候 s 撕掉了旧标签，贴到了新字符串 "Hello" 上
```


```python

a=[1,2,3]

b=a

a=[3]

print(b)#输出\[1,2,3]，b不变
```

因为 a = \[3] 是“重新贴标签”，不是“修改盒子里的内容”。

我来分两步还原电脑当时的操作，你就彻底明白了：

🧠 第一步：a = \[1, 2, 3] 和 b = a

电脑在内存里造了一个盒子（列表 \[1, 2, 3]），然后把 两张便利贴 a 和 b 都贴在了这个盒子上。

此时：

- a → 指向 \[1, 2, 3] 这个盒子
- b → 指向 同一个 \[1, 2, 3] 这个盒子

🔄 第二步：a = \[3]

这是最关键的一步！电脑做了一件事：

- 重新造了一个全新的盒子，里面装着 \[3]（新盒子）。
- 把贴纸 a 撕下来，从旧盒子上撕掉，贴到了这个新盒子上。

此时：

- a → 指向新的盒子 \[3]（彻底换了对象）
- b → 依然贴在旧的盒子 \[1, 2, 3] 上（纹丝不动）

所以当你 print(b) 时，b 依然贴在旧盒子上，打印出 \[1, 2, 3]。

⚔️ 对比：如果我是“修改”盒子，而不是“替换”盒子

如果你写的是 a\[0] = 3（修改盒子里的第一个元素），而不是 a = \[3]（换一个新盒子），那么：



```python

a = [1, 2, 3]

b = a

a[0] = 3   # 打开同一个盒子，把第一个数字 1 改成 3

print(b)   # 输出：[3, 2, 3]
```

因为 a 和 b 贴的还是同一个盒子，你修改了盒子里的内容，b 当然能看见。

📌 一句话帮你焊死这个区别

- `a = [3]`（等号赋值）：是 “撕标签，换盒子”（不影响 b）。
- `a[0] = 3`（索引赋值/方法调用）：是 “修改盒子里的东西”（影响 b）。

只要不涉及等号 = 重新赋值，而是在原有对象上调用方法（`.append()`、`.remove()`、`[索引]=`），那就是“改内容”；只要用了 =，那就是“换标签”。



```python

a=2

b=a

a+=4

print(b)#输出2，b没变
```

因为a += 4 对于整数（不可变对象）来说，本质上就是一次‘=’（重新赋值），而不是“修改盒子里的内容”

如果 a 是列表（可变对象），情况就不同了



```python

a = [1, 2, 3]

b = a

a += [4]      # 这里会原地修改列表，不会造新列表

print(b)      # 输出：\[1, 2, 3, 4]（b 跟着变了）
```

为什么？ 因为列表是可变对象，+= 在列表身上会触发“原地扩展”操作，不会造新列表，所有贴着的标签（a 和 b）都能看到变化。







## ***模块***



### 1. 语言核心 & 内置支持

| 模块 | 用途 |
| :--- | :--- |
| `__future__` | 启用未来版本的语言特性（如 `print_function`） |
| `builtins` | 提供内置函数、异常和常量 |
| `keyword` | 检测一个字符串是否为 Python 关键字 |
| `operator` | 将运算符（`+`, `*`）作为函数使用 |
| `_operator` | `operator` 模块的 C 实现 |
| `_collections_abc` | 集合抽象基类的底层实现 |
| `_py_abc` | `abc` 模块的辅助实现 |
| `_compat_pickle` | 跨 Python 版本 pickle 兼容的内部支持 |
| `codecs` | 编解码器注册与基类 |
| `_codecs` | C 语言编解码器支持 |
| `_multibytecodec` | 多字节编解码器内部模块 |
| `_codecs_cn` / `_codecs_hk` / `_codecs_iso2022` / `_codecs_jp` / `_codecs_kr` / `_codecs_tw` | 针对特定语言/区域的编解码器实现 |
| `encodings` | 标准编码集合 |
| `locale` | 本地化服务（数字、货币格式等） |
| `_locale` | `locale` 的 C 实现 |
| `stringprep` | RFC 3454 字符串预处理（用于国际化域名） |
| `unicodedata` | Unicode 字符数据库 |
| `_suggestions` | 当导入模块名拼写错误时，提供建议的候选模块 |
| `_colorize` | 为回溯信息添加 ANSI 颜色的内部支持 |
| `_pyrepl` | Python 3.13+ 新的交互式解释器（REPL）后端 |
| `_interpchannels`, `_interpqueues`, `_interpreters` | 子解释器通信支持（Python 3.12+） |



### 2. 系统 & 平台交互

#### `sys` 模块：与 Python 解释器交互

| 属性/函数 | 描述 | 关键点 |
| :--- | :--- | :--- |
| `sys.argv` | 命令行参数列表 | `argv[0]` 是脚本名，之后的元素是传入的参数 |
| `sys.path` | 模块搜索路径列表 | 你可以修改它来添加自定义的模块搜索目录 |
| `sys.exit([arg])` | 退出程序 | 正常退出用 `sys.exit(0)`，异常退出用非零值 |
| `sys.version` | Python 解释器的版本信息 | |
| `sys.platform` | 操作系统平台标识，如 `'win32'`、`'linux'` | |
| `sys.executable` | Python 解释器可执行文件的路径 | |
| `sys.modules` | 返回已导入模块的字典 | |
| `sys.builtin_module_names` | Python 解释器内建模块的元组 | |
| `sys.getdefaultencoding()` | 获取当前系统默认编码 | |


#### `os` 模块：与操作系统交互

**常用属性（系统信息）**

| 属性 | 描述 |
| :--- | :--- |
| `os.name` | 操作系统的名称，如 `'nt'` (Windows) 或 `'posix'` (Linux/macOS) |
| `os.sep` | 路径分隔符，Windows 上是 `'\\'`，Linux/macOS 上是 `'/'` |
| `os.linesep` | 当前系统的换行符 |
| `os.pathsep` | 环境变量中用于分隔不同路径的符号 |
| `os.getcwd()` | 获取当前工作目录的绝对路径 |


**常用函数（目录操作）**

| 函数 | 描述 | 关键点 |
| :--- | :--- | :--- |
| `os.listdir(path)` | 返回指定目录下所有文件和子目录名称的列表 | 不包含完整路径信息 |
| `os.mkdir(path)` | 创建一个目录 | 父目录必须存在，否则报错 `FileNotFoundError` |
| `os.makedirs(path)` | 递归创建目录，自动创建所有不存在的父目录 | 推荐使用，可避免父目录不存在的错误 |
| `os.rmdir(path)` | 删除一个空目录 | 目录非空会报错，要删非空目录需用 `shutil.rmtree()` |
| `os.chdir(path)` | 改变当前工作目录 | 类似在命令行中执行 `cd` 命令 |


**常用函数（文件操作）**

| 函数 | 描述 | 关键点 |
| :--- | :--- | :--- |
| `os.remove(path)` | 删除一个文件 | 文件不存在会报错 `FileNotFoundError` |
| `os.rename(src, dst)` | 重命名文件或目录 | 跨平台行为可能不同 |
| `os.replace(src, dst)` | 重命名，如果目标文件存在则无条件覆盖 | 比 `rename` 更安全 |


**运行系统命令**

| 函数 | 描述 |
| :--- | :--- |
| `os.system(command)` | 在子shell中执行操作系统命令（更推荐用 `subprocess` 模块执行复杂命令） |


**`os.path` 子模块：智能处理路径**

| 函数 | 描述 | 示例 |
| :--- | :--- | :--- |
| `os.path.join(a, *p)` | 智能拼接路径 | `os.path.join("folder", "file.txt")` |
| `os.path.exists(path)` | 判断路径是否存在 | `if os.path.exists("data.txt"):` |
| `os.path.isfile(path)` | 判断是否为文件 | |
| `os.path.isdir(path)` | 判断是否为目录 | |
| `os.path.abspath(path)` | 返回路径的绝对路径版本 | |
| `os.path.basename(path)` | 提取路径中的文件名 | `os.path.basename("/a/b/c.txt") -> "c.txt"` |
| `os.path.dirname(path)` | 提取路径中的目录名 | `os.path.dirname("/a/b/c.txt") -> "/a/b"` |
| `os.path.split(path)` | 将路径分割成 (目录, 文件名) 的元组 | |
| `os.path.splitext(path)` | 将路径分割成 (主文件名, 扩展名) | `splitext("c.txt") -> ("c", ".txt")` |


#### 其他系统/平台相关模块

| 模块 | 用途 |
| :--- | :--- |
| `_osx_support` | 为 macOS 构建时提供支持 |
| `posixpath` | Unix 风格的路径操作（`os.path` 在 Unix 下的实现） |
| `ntpath` | Windows 风格的路径操作（`os.path` 在 Windows 下的实现） |
| `genericpath` | 所有平台通用的路径操作 |
| `nturl2path` | Windows 下 URL 与文件路径的转换 |
| `platform` | 获取平台标识信息 |
| `sysconfig` | 访问 Python 配置信息（如安装路径、编译参数） |
| `_sysconfig` | `sysconfig` 的内部辅助 |
| `site` | 初始化第三方库路径（site-packages） |
| `_sitebuiltins` | `site` 模块使用的内置函数 |
| `atexit` | 注册程序退出时的清理函数 |
| `signal` | 异步系统信号处理 |
| `_signal` | `signal` 的 C 实现 |
| `errno` | 标准系统错误码 |
| `ctypes` | C 语言外部函数库接口 |
| `_ctypes` | `ctypes` 的 C 扩展核心 |
| `win32ctypes` | pywin32 库的轻量级 `ctypes` 替代 |
| `msvcrt` | Windows 下 Microsoft Visual C 运行时库的访问 |
| `_winapi` | 直接调用 Windows API 的内部辅助 |
| `_overlapped` | Windows 重叠 I/O 的内部支持 |
| `winreg` | Windows 注册表操作 |
| `winsound` | Windows 声音播放接口 |
| `_wmi` | 访问 Windows Management Instrumentation (WMI) 的内部模块（可能来自特定包） |
| `_android_support` | 在 Android 平台上的特定支持（常由 PyInstaller 引导） |
| `_apple_support` | 在 Apple/macOS 平台上的特定支持 |
| `_ios_support` | 在 iOS 平台上的特定支持 |



### 3. 工具与数据结构

| 模块 | 用途 |
| :--- | :--- |
| `collections` | 容器数据类型（namedtuple, deque, Counter 等） |
| `_collections` | `collections` 的 C 实现 |
| `heapq` | 堆队列算法（优先队列） |
| `_heapq` | `heapq` 的 C 实现 |
| `bisect` | 有序列表的二分查找和插入 |
| `_bisect` | `bisect` 的 C 实现 |
| `array` | 紧凑的数值类型数组 |
| `queue` | 线程安全的队列类 |
| `_queue` | `queue` 的 C 实现 |
| `struct` | 解析打包的二进制数据 |
| `_struct` | `struct` 的 C 实现 |
| `weakref` | 弱引用支持 |
| `_weakref` | `weakref` 的 C 实现 |
| `_weakrefset` | 弱引用集合的内部实现 |
| `enum` | 枚举类型 |
| `typing` | 类型提示支持 |
| `_typing` | `typing` 的内部辅助 |
| `dataclasses` | 数据类装饰器（自动生成 `__init__` 等方法） |
| `abc` | 抽象基类 |
| `_abc` | `abc` 的 C 实现 |
| `functools` | 高阶函数工具（lru_cache, partial） |
| `_functools` | `functools` 的 C 实现 |
| `itertools` | 高效循环和迭代器 |
| `contextlib` | 上下文管理器工具 |
| `contextvars` | 上下文变量（用于异步编程） |
| `_contextvars` | `contextvars` 的 C 实现 |
| `copy` | 浅拷贝和深拷贝操作 |
| `copyreg` | 注册 pickle 支持的拷贝函数 |
| `reprlib` | 生成有限长度的 repr() |
| `pprint` | 美化打印数据结构 |
| `types` | 动态类型创建与内部类型对象 |
| `numbers` | 数值抽象基类 |



### 4. 数学 & 数字

| 模块 | 用途 |
| :--- | :--- |
| `math` | 数学函数（浮点运算） |
| `cmath` | 复数数学函数 |
| `decimal` | 十进制定点和浮点运算 |
| `_decimal` | `decimal` 的 C 实现 |
| `_pydecimal` | `decimal` 的纯 Python 后备实现 |
| `fractions` | 有理数 |
| `random` | 生成伪随机数 |
| `_random` | `random` 的 C 实现核心 |
| `statistics` | 数学统计函数 |
| `_statistics` | `statistics` 的内部支持 |
| `hashlib` | 安全哈希与消息摘要算法 |
| `_hashlib` | `hashlib` 的 C 接口 |
| `_md5`, `_sha1`, `_sha2`, `_sha3`, `_blake2` | 各类哈希算法的 C 实现 |
| `hmac` | 密钥哈希消息认证码 |
| `_pylong` | 长整数内部实现辅助 |
| `opcode` | Python 字节码指令的助记符 |
| `_opcode` | `opcode` 的内部 C 核心 |
| `_opcode_metadata` | 字节码指令的元数据 |



### 5. 文本 & 字符串处理

| 模块 | 用途 |
| :--- | :--- |
| `string` | 字符串常量和模板 |
| `_string` | `string` 模块的内部 C 辅助 |
| `re` | 正则表达式 |
| `_sre` | `re` 的 C 实现核心 |
| `sre_compile`, `sre_constants`, `sre_parse` | `re` 模块的内部子模块 |
| `textwrap` | 文本段落自动换行与填充 |
| `difflib` | 差异计算和比较工具 |
| `fnmatch` | Unix 文件名模式匹配 |
| `glob` | Unix 风格的路径名模式展开 |
| `linecache` | 缓存文本行以高效重复读取 |
| `gettext` | 国际化和本地化消息翻译 |
| `rlcompleter` | Readline 的自动补全支持 |



### 6. 日期 & 时间

| 模块 | 用途 |
| :--- | :--- |
| `datetime` | 日期和时间操作 |
| `_datetime` | `datetime` 的 C 实现 |
| `_pydatetime` | `datetime` 的纯 Python 后备实现 |
| `time` | 时间访问和转换 |
| `calendar` | 日历相关函数 |
| `zoneinfo` | IANA 时区数据库支持 |
| `_zoneinfo` | `zoneinfo` 的 C 实现 |
| `_strptime` | 解析时间字符串的内部辅助 |



### 7. 文件、数据持久化 & 压缩

| 模块 | 用途 |
| :--- | :--- |
| `pathlib` | 面向对象的文件系统路径操作 |
| `io` | 流处理工具核心模块 |
| `_io` | `io` 模块的 C 实现 |
| `_pyio` | `io` 的纯 Python 后备实现 |
| `tempfile` | 生成临时文件和目录 |
| `shutil` | 高级文件操作（复制、移动、归档） |
| `fileinput` | 遍历多个输入文件流 |
| `filecmp` | 文件与目录比较 |
| `stat` | 解析 `os.stat()` 的结果 |
| `_stat` | `stat` 的 C 实现 |
| `mmap` | 内存映射文件支持 |
| `pickle` | Python 对象序列化 |
| `_pickle` | `pickle` 的 C 实现 |
| `pickletools` | pickle 流的分析和工具 |
| `shelve` | 使用字典接口的持久化对象存储 |
| `marshal` | 内部 Python 对象序列化（用于 .pyc） |
| `dbm` | Unix (n)dbm 数据库接口 |
| `sqlite3` | SQLite 数据库接口 |
| `_sqlite3` | `sqlite3` 的 C 实现 |
| `csv` | CSV 文件读写 |
| `_csv` | `csv` 的 C 实现 |
| `configparser` | 配置文件解析器 |
| `tomllib` | Python 3.11+ 内置的 TOML 文件解析器 |
| `tomli` | 第三方 TOML 解析器（tomllib 的后向移植） |
| `netrc` | 解析 .netrc 文件 |
| `plistlib` | 苹果属性列表（.plist）的读写 |
| `gzip` | Gzip 压缩解压 |
| `bz2` | Bzip2 压缩解压 |
| `_bz2` | `bz2` 的 C 实现 |
| `lzma` | LZMA 算法压缩解压 |
| `_lzma` | `lzma` 的 C 实现 |
| `_compression` | 压缩算法的基础内部辅助 |
| `zipfile` | ZIP 文件操作 |
| `tarfile` | Tar 归档文件操作 |
| `zlib` | zlib 压缩库的接口 |
| `zipimport` | 从 ZIP 文件中导入模块 |
| `zipp` | 第三方库，提供 `zipfile.Path` 的兼容性增强 |
| `_markupbase` | html 和 xhtml 解析器的内部基类 |



### 8. 网络 & 通信

| 模块 | 用途 |
| :--- | :--- |
| `socket` | 底层网络接口 |
| `_socket` | `socket` 的 C 实现 |
| `ssl` | TLS/SSL 套接字封装 |
| `_ssl` | `ssl` 的 C 实现 |
| `socketserver` | 通用网络服务器框架 |
| `select` | 同步 I/O 多路复用 |
| `selectors` | 高级 I/O 多路复用 |
| `asyncio` | 异步 I/O 框架 |
| `_asyncio` | `asyncio` 的 C 加速模块 |
| `ipaddress` | 创建、检查和操作 IP 地址 |
| `http` | HTTP 协议模块集合 |
| `urllib` | URL 处理合集 |
| `ftplib` | FTP 协议客户端 |
| `poplib` | POP3 协议客户端 |
| `imaplib` | IMAP4 协议客户端 |
| `smtplib` | SMTP 协议客户端 |
| `xmlrpc` | XML-RPC 客户端和服务器 |
| `uuid` | UUID 对象生成 |
| `_uuid` | `uuid` 的 C 实现 |
| `json` | JSON 编码和解码 |
| `_json` | `json` 的 C 实现 |
| `email` | 电子邮件与 MIME 处理包 |
| `mailbox` | 解析各种格式的邮箱文件 |
| `mimetypes` | 文件名到 MIME 类型的映射 |
| `quopri` | Quoted-printable 编码解码 |
| `base64` | Base64/32/16 编码解码 |
| `binascii` | 二进制与 ASCII 互转 |
| `xml` | XML 处理包 |
| `pyexpat` | Expat XML 解析器的接口 |
| `_elementtree` | `xml.etree.ElementTree` 的 C 实现 |
| `html` | HTML 实用函数（转义、解析） |
| `webbrowser` | 控制 Web 浏览器 |



### 9. 并发 & 多进程

| 模块 | 用途 |
| :--- | :--- |
| `threading` | 线程基础模块 |
| `_thread` | 低级线程接口（C 实现） |
| `_threading_local` | 线程本地数据的内部实现 |
| `multiprocessing` | 基于进程的并行 |
| `_multiprocessing` | `multiprocessing` 的 C 实现辅助 |
| `subprocess` | 启动并管理子进程 |
| `sched` | 通用事件调度器 |



### 10. 开发工具：调试、测试与分析

| 模块 | 用途 |
| :--- | :--- |
| `traceback` | 提取、格式化和打印堆栈回溯 |
| `_tracemalloc` | 内存分配追踪的底层 C 支持 |
| `tracemalloc` | 内存分配追踪的高级接口 |
| `pdb` | Python 调试器 |
| `bdb` | 基础调试器框架 |
| `faulthandler` | 处理致命错误的转储回溯信息 |
| `warnings` | 警告控制与过滤 |
| `_warnings` | `warnings` 的 C 实现 |
| `unittest` | 单元测试框架 |
| `doctest` | 通过文档示例进行测试 |
| `cProfile`, `profile` | 性能分析器（cProfile 为 C 版） |
| `_lsprof` | `cProfile` 使用的底层 C 剖析器 |
| `pstats` | 剖析统计数据操作 |
| `timeit` | 测量小段代码执行时间 |
| `inspect` | 检查活动对象（源代码、参数等） |
| `ast` | 抽象语法树 |
| `_ast` | `ast` 的 C 加速模块 |
| `symtable` | 访问编译器的符号表 |
| `_symtable` | `symtable` 的 C 实现 |
| `token` | 定义解析器使用的 token 常量 |
| `_tokenize` | `tokenize` 模块的 C 加速 |
| `tokenize` | Python 源代码的记号化器 |
| `dis` | 反汇编 Python 字节码 |
| `py_compile` | 将 Python 源文件编译为字节码 |
| `compileall` | 递归编译整个目录树的 .py 文件 |
| `pyclbr` | 类浏览器，提取源代码中的类/函数信息 |
| `modulefinder` | 找出脚本导入的所有模块（用于打包） |
| `tabnanny` | 检测源码中混淆的缩进 |
| `code` | 提供可交互的解释器模拟功能 |
| `codeop` | 判断一段代码能否被编译 |



### 11. 导入 & 模块系统

| 模块 | 用途 |
| :--- | :--- |
| `importlib` | `import` 语句的完整实现和自定义 |
| `importlib_metadata` | 第三方库，读取已安装包的元数据（`importlib.metadata` 的后向移植） |
| `imp`, `_imp` | 导入的内部实现（`_imp` 是 C 核心，`imp` 已废弃） |
| `pkgutil` | 包相关的工具（如遍历包中模块） |
| `runpy` | 执行 Python 模块/脚本（如 `-m` 实现） |
| `_distutils_hack` | 确保在特定环境中正确加载 setuptools 的补丁 |
| `ordlookup` | 辅助查找 Windows DLL 中的导出序号（常用于 PyInstaller） |



### 12. 其他标准库 & 应用框架

| 模块 | 用途 |
| :--- | :--- |
| `cmd` | 构建基于命令行的解释器框架 |
| `shlex` | 按照 shell 语法解析字符串 |
| `argparse` | 命令行参数解析 |
| `optparse` | 已废弃的命令行参数解析器（argparse 取代） |
| `getopt` | C 风格 `getopt()` 参数解析 |
| `logging` | 日志记录框架 |
| `getpass` | 安全地获取密码输入 |
| `curses` | 终端字符界面处理 |
| `tkinter` | Tk GUI 工具包接口 |
| `_tkinter` | `tkinter` 的 C 接口 |
| `turtle` | 海龟绘图库 |
| `turtledemo` | 海龟绘图的演示代码 |
| `idlelib` | Python 自带的 IDE（IDLE）的实现库 |
| `pydoc` | 自动生成文档 |
| `pydoc_data` | `pydoc` 使用的数据文件 |
| `ensurepip` | 安装 pip 的引导工具 |
| `venv` | 创建虚拟环境 |
| `secrets` | 生成加密强安全的随机数 |
| `wave` | WAV 音频文件读写 |
| `colorsys` | 颜色系统转换 |
| `antigravity` | 彩蛋，打开 xkcd 漫画 #353 |
| `this` | 彩蛋，打印《Python 之禅》 |
| `__hello__` | 彩蛋，打印 “Hello world!” |
| `__phello__` | 与 `__hello__` 类似的变体 |
| `xxsubtype` | 一个用 C 展示如何创建内置类型子类的示例模块 |



### 13. 第三方包 & PyInstaller 环境模块

这些通常在你的环境中为打包服务。

| 模块 | 用途 |
| :--- | :--- |
| `pip` | Python 包安装器 |
| `setuptools` | 构建和分发 Python 包的核心工具 |
| `wheel` | `setuptools` 的一个扩展，用于构建 Wheel 格式包 |
| `packaging` | 解析、比较和操作 Python 包版本号的库 |
| `platformdirs` | 确定平台特定的应用程序目录（如缓存、配置） |
| `more_itertools` | `itertools` 的增强库，提供更多迭代器工具 |
| `backports` | 一个命名空间包，用于向后移植新版本标准库的功能 |
| `autocommand` | 一个库，能将普通函数自动转换为命令行程序 |
| `altgraph` | 有向图算法库，PyInstaller 的核心依赖，用于分析模块依赖关系 |
| `pyinstaller` | 你很可能在用它的相关支持文件 |
| `_pyinstaller_hooks_contrib` | PyInstaller 贡献的“钩子”合集，帮助打包各种第三方库 |
| `pefile` | 解析 Windows PE (Portable Executable) 文件格式的库 |
| `peutils` | `pefile` 的辅助工具库 |
| `file_organizer` | 可能是一个自定义或第三方文件整理工具 |





## ***文件格式***

这是一个非常宏大的问题，计算机世界里的文件格式成千上万，没有人能真正穷举“所有”。但我可以为你系统地梳理**常见的、有代表性的文件格式**，按用途分类，帮你建立一个全局认知地图。



📌 分类逻辑

- 文本与数据交换：人类可读或结构化数据
- 文档与排版：办公、出版、电子书
- 图像：位图与矢量
- 音频：未压缩、无损、有损
- 视频与动画：容器与编码结合
- 压缩与归档：打包与压缩
- 可执行与库：程序与代码
- 数据库与数据存储：结构化存储
- 网页与网络：前端与互联网相关
- 磁盘与系统：操作系统、虚拟机、磁盘映像
- 字体：文字渲染
- 其他专业领域：CAD、GIS、科学数据等





---

### 1. 纯文本与结构化数据

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| 纯文本 | `.txt` | 无格式文本 |
| 富文本 | `.rtf` | 富文本格式 |
| 标记语言 | `.md`, `.markdown` | Markdown |
| 数据交换 | `.json` | JavaScript对象表示法 |
| 数据交换 | `.xml` | 可扩展标记语言 |
| 数据交换 | `.yaml`, `.yml` | 人类友好的数据序列化格式 |
| 数据交换 | `.csv` | 逗号分隔值 |
| 数据交换 | `.tsv` | 制表符分隔值 |
| 数据交换 | `.toml` | Tom's Obvious, Minimal Language |
| 数据交换 | `.properties` | Java属性文件 |
| 配置文件 | `.ini`, `.cfg` | 配置文件 |
| 日志 | `.log` | 通用日志文件 |



### 2. 办公文档与排版

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| Microsoft Word | `.doc`, `.docx` | Word文档 |
| Microsoft Excel | `.xls`, `.xlsx` | 电子表格 |
| Microsoft PowerPoint | `.ppt`, `.pptx` | 演示文稿 |
| OpenDocument | `.odt`, `.ods`, `.odp` | 开放文档格式 |
| PDF | `.pdf` | 便携式文档格式 |
| PostScript | `.ps` | 页面描述语言 |
| EPUB | `.epub` | 电子书标准格式 |
| MOBI | `.mobi` | Kindle电子书格式 |
| AZW | `.azw`, `.azw3` | Amazon Kindle格式 |
| DjVu | `.djvu` | 扫描文档压缩格式 |
| LaTeX | `.tex` | 排版系统源文件 |
| 中国文档标准 | `.uof`, `.ofd` | 国产文档格式 |



### 3. 图像

#### 位图 (Raster)

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| JPEG | `.jpg`, `.jpeg` | 有损压缩，照片最常用 |
| PNG | `.png` | 无损压缩，支持透明 |
| GIF | `.gif` | 支持动画，256色 |
| BMP | `.bmp` | Windows位图，无压缩/简单 |
| TIFF | `.tif`, `.tiff` | 专业印刷、扫描 |
| WebP | `.webp` | Google推出，有损/无损/动画 |
| HEIF/HEIC | `.heic`, `.heif` | 高效图像格式（苹果设备） |
| AVIF | `.avif` | 基于AV1的图像格式 |
| RAW | `.raw`, `.cr2`, `.nef`, `.arw` | 相机原始数据（各品牌不同） |
| ICO | `.ico` | 图标文件 |
| PSD | `.psd` | Adobe Photoshop源文件 |

#### 矢量 (Vector)

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| SVG | `.svg` | 可缩放矢量图形 |
| EPS | `.eps` | 封装PostScript |
| AI | `.ai` | Adobe Illustrator |
| CDR | `.cdr` | CorelDRAW |
| WMF/EMF | `.wmf`, `.emf` | Windows图元文件 |



### 4. 音频

#### 未压缩

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| WAV | `.wav` | 波形音频，无损 |
| AIFF | `.aiff`, `.aif` | 苹果无损音频 |
| PCM | `.pcm` | 原始脉冲编码调制 |

#### 无损压缩

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| FLAC | `.flac` | 自由无损音频 |
| ALAC | `.m4a`, `.alac` | 苹果无损 |
| APE | `.ape` | Monkey's Audio |
| WavPack | `.wv` | 混合有损/无损模式 |

#### 有损压缩

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| MP3 | `.mp3` | MPEG音频层III |
| AAC | `.aac`, `.m4a` | 高级音频编码 |
| OGG Vorbis | `.ogg` | 开放有损格式 |
| Opus | `.opus` | 低延迟、高质量 |
| WMA | `.wma` | Windows Media Audio |

#### MIDI

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| MIDI | `.mid`, `.midi` | 乐器数字接口 |



### 5. 视频与动画

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| MP4 | `.mp4` | 最通用的视频容器 |
| AVI | `.avi` | 微软音视频交错 |
| MOV | `.mov` | QuickTime容器 |
| MKV | `.mkv` | Matroska多媒体容器 |
| WMV | `.wmv` | Windows Media Video |
| FLV | `.flv` | Flash视频 |
| WebM | `.webm` | 开放网络视频 |
| AVCHD | `.mts`, `.m2ts` | 高清视频（摄像机常用） |
| 3GP | `.3gp` | 移动设备视频 |
| GIF（动画） | `.gif` | 简单动画 |
| APNG | `.apng` | 动画PNG |
| SWF | `.swf` | Shockwave Flash |



### 6. 压缩与归档

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| ZIP | `.zip` | 最通用的压缩包 |
| RAR | `.rar` | WinRAR压缩格式 |
| 7-Zip | `.7z` | 高压缩比 |
| Gzip | `.gz` | GNU压缩（常配合tar） |
| Tar | `.tar` | 归档（不压缩） |
| Tar.gz/tgz | `.tar.gz`, `.tgz` | 归档+gzip压缩 |
| Bzip2 | `.bz2` | 高压缩比（常配合tar） |
| XZ/LZMA | `.xz` | 高压缩率（LZMA2） |
| CAB | `.cab` | Windows Cabinet |
| ISO | `.iso` | 光盘映像（也可归为磁盘） |
| DMG | `.dmg` | macOS磁盘映像 |



### 7. 可执行文件、库与脚本

#### Windows

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| 可执行程序 | `.exe` | 应用程序 |
| 动态链接库 | `.dll` | 库文件 |
| 批处理 | `.bat`, `.cmd` | 命令行脚本 |
| PowerShell脚本 | `.ps1` | PowerShell脚本 |
| 屏幕保护 | `.scr` | 本质是exe |
| 安装包 | `.msi` | Windows安装包 |

#### Linux / Unix

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| 可执行二进制 | 无固定扩展名 | ELF格式 |
| 共享库 | `.so` | 动态库 |
| Shell脚本 | `.sh` | Bash等脚本 |

#### macOS

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| 应用程序包 | `.app` | 目录结构 |
| 动态库 | `.dylib` | macOS动态库 |

#### 跨平台

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| Java字节码 | `.class` | Java类文件 |
| Java归档 | `.jar` | Java打包 |
| Python脚本 | `.py` | Python源代码 |
| Python字节码 | `.pyc` | 编译后字节码 |



### 8. 数据库与数据存储

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| SQLite | `.db`, `.sqlite` | 嵌入式数据库 |
| Microsoft Access | `.mdb`, `.accdb` | Access数据库 |
| MySQL dump | `.sql` | SQL导出文件 |
| Berkeley DB | 无固定 | 嵌入式键值存储 |
| 序列化数据 | `.dat`, `.pkl` | 程序私有数据 |



### 9. 网页与网络

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| HTML | `.html`, `.htm` | 网页结构 |
| CSS | `.css` | 层叠样式表 |
| JavaScript | `.js` | 脚本语言 |
| TypeScript | `.ts` | JS的超集 |
| PHP | `.php` | 服务器脚本 |
| ASP.NET | `.aspx` | 微软动态页 |
| WebAssembly | `.wasm` | 浏览器字节码 |
| 字体 | `.woff`, `.woff2` | Web开放字体 |
| 证书 | `.crt`, `.pem`, `.key` | SSL/TLS证书与密钥 |



### 10. 磁盘、虚拟化与系统映像

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| ISO 9660 | `.iso` | 光盘映像 |
| VHD/VHDX | `.vhd`, `.vhdx` | 虚拟硬盘（Hyper-V） |
| VMDK | `.vmdk` | 虚拟机磁盘（VMware） |
| QCOW2 | `.qcow2` | QEMU副本写入 |
| VDI | `.vdi` | VirtualBox磁盘映像 |
| IMG | `.img` | 原始磁盘映像 |
| DMG | `.dmg` | macOS磁盘映像 |
| WIM | `.wim` | Windows映像格式 |



### 11. 字体

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| TrueType | `.ttf` | 通用字体 |
| OpenType | `.otf` | 增强字体格式 |
| Web Open Font | `.woff`, `.woff2` | 网页字体 |
| Embedded OpenType | `.eot` | 微软网页字体（旧） |
| PostScript Type1 | `.pfb`, `.pfm` | 旧式打印机字体 |



### 12. 专业/工程/科学

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| AutoCAD | `.dwg`, `.dxf` | CAD设计 |
| 3D模型 | `.obj`, `.stl`, `.fbx`, `.blend` | 三维模型与打印 |
| MATLAB | `.mat` | 科学数据 |
| HDF5 | `.h5`, `.hdf5` | 层次数据格式 |
| NetCDF | `.nc` | 科学数组数据 |
| FITS | `.fits` | 天文数据 |
| GeoTIFF | `.tif` + 地理头 | 地理空间图像 |
| KML/KMZ | `.kml`, `.kmz` | Google Earth |
| GPX | `.gpx` | GPS数据交换 |
| Gerber | `.gbr`, `.gerber` | PCB电路板制造 |
| 医学影像 | `.dcm` (DICOM) | 医学数字成像 |



### 13. 其他常见杂项

| 格式 | 扩展名 | 说明 |
| :--- | :--- | :--- |
| 电子书 | `.fb2` | FictionBook |
| 漫画 | `.cbr`, `.cbz` | 压缩包封装的漫画 |
| 字幕 | `.srt`, `.ass`, `.sub` | 视频字幕 |
| 光盘映像 | `.bin`, `.cue` | 二进制映像+描述文件 |
| 密码数据库 | `.kdbx` | KeePass密码管理器 |
| 邮件存储 | `.pst` (Outlook), `.mbox` | 电子邮件归档 |
| 注册表 | `.reg` | Windows注册表导出 |
| 脚本/宏 | `.vbs`, `.ahk` | VBScript, AutoHotkey |


---

### 🧠 结尾思考

你看到的只是“主流格式”的冰山一角。**文件格式本质上是数据的组织规则**——定义好了如何存储、如何解析。只要愿意，任何人和组织都可以设计自己的格式（用特定扩展名或魔数来识别）。

如果你对**某一种格式的内部结构**或者**如何用代码读写它**感兴趣，可以继续提问，我们可以深入解剖。





# *数值类型*

Python 的数值类型体系比较丰富，下面是各种类型的对比表格，方便你快速查阅。

| 类型 | 定义方式 | 特点 | 注意事项 |
| :--- | :--- | :--- | :--- |
| **整数（int）** | 直接写数字，如 `a = 10` | 无大小限制，支持任意大整数 | 除法 `/` 总是返回 float，整除用 `//` |
| **浮点数（float）** | 带小数点或科学计数法，如 `3.14`、`2.99e8` | 双精度 64 位，符合 IEEE 754 标准 | `0.1 + 0.2 != 0.3`，比较时用 `math.isclose()` |
| **复数（complex）** | `2 + 3j`，虚部用 `j` | 支持 `real` 和 `imag` 属性 | 数学函数用 `cmath` 模块，不是 `math` |
| **Decimal** | `Decimal('0.1')` | 精确十进制运算，适合财务计算 | 必须从字符串创建，速度比 float 慢 |
| **Fraction** | `Fraction(1, 3)` | 精确分数表示，自动约分 | 适合数论、概率计算等需要精确比例的场景 |
| **布尔值（bool）** | `True` / `False` | `bool` 是 `int` 的子类，`True == 1` | 可参与算术运算，但逻辑上应独立使用 |


### 进制表示与转换

| 进制 | 前缀 | 示例 | 转换函数 |
| :--- | :--- | :--- | :--- |
| 二进制 | `0b` | `0b1101` → 13 | `bin()` |
| 八进制 | `0o` | `0o77` → 63 | `oct()` |
| 十六进制 | `0x` | `0xFF` → 255 | `hex()` |


### 类型转换速查

| 目标类型 | 函数 | 示例 |
| :--- | :--- | :--- |
| 整数 | `int()` | `int(3.9)` → 3（截断，不是四舍五入） |
| 浮点数 | `float()` | `float(42)` → 42.0 |
| 复数 | `complex()` | `complex(2, 3)` → (2+3j) |


### 浮点数安全比较

```python

import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

### 精确计算示例

当需要绝对精确的十进制计算（如金额）时，用 `Decimal`；当需要精确分数时，用 `Fraction`：

```python

from decimal import Decimal
Decimal('0.1') + Decimal('0.2')  # Decimal('0.3')

from fractions import Fraction
Fraction(6, 8)  # 3/4
```




## 字符串

### 1. 字符串的定义

Python 中字符串是 **不可变的 Unicode 序列**。用单引号、双引号或三引号定义。

```python

s1 = 'hello'
s2 = "world"
s3 = '''多行
字符串'''
s4 = """也支持
多行"""
```

单引号和双引号完全等价，内部包含引号时交替使用可避免转义。

三引号常用于文档字符串（docstring）或多行注释。


### 2. 转义字符

| 转义序列 | 含义 | 示例 |
| :--- | :--- | :--- |
| `\n` | 换行 | `print("A\nB")` → A 换行 B |
| `\t` | 制表符（Tab） | `print("A\tB")` → A     B |
| `\\` | 输出一个反斜杠 | `print("C:\\Users")` → `C:\Users` |
| `\'` | 在单引号字符串中输出单引号 | `print('It\'s ok')` → It's ok |
| `\"` | 在双引号字符串中输出双引号 | `print("He said \"Hi\"")` → He said "Hi" |
| `\xhh` | 十六进制字符 | `print('\x41')` → A |
| `\uhhhh` | 16位 Unicode 字符 | `print('\u4f60')` → 你 |
| `\Uhhhhhhhh` | 32位 Unicode 字符 | `print('\U0001F600')` → 😀 |

```python

path = r"C:\Users\name"
pattern = r"\d+\.\d+" #正则表达式
```


### 3. 基本操作

| 操作 | 示例 | 结果 |
| :--- | :--- | :--- |
| 拼接 | `"Py" + "thon"` | `'Python'` |
| 重复 | `"Ha" * 3` | `'HaHaHa'` |
| 索引（正） | `s[0]` | 第一个字符 |
| 索引（负） | `s[-1]` | 最后一个字符 |
| 切片 | `s[7:9]` | 取索引 7 到 8（左闭右开） |
| 切片步长 | `s[::2]` | 隔一个取一个 |
| 成员检查 | `'ell' in s` | `True` |
| 长度 | `len(s)` | 字符数（Unicode 计数） |

---

### 4. 常用字符串方法

| 方法 | 说明 | 示例 |
| :--- | :--- | :--- |
| `lower()` / `upper()` | 大小写转换 | `"Python".upper()` → `'PYTHON'` |
| `capitalize()` / `title()` | 首字母大写 / 单词首字母大写 | `"hello world".title()` → `'Hello World'` |
| `strip()` | 移除两端空白（包括空格、换行、制表符） | `"  hi\n".strip()` → `'hi'` |
| `split(sep)` | 按分隔符切分成列表 | `"a,b,c".split(",")` → `['a','b','c']` |
| `join(iterable)` | 用字符串连接可迭代对象 | `",".join(['a','b'])` → `'a,b'` |
| `replace(old, new)` | 替换子串 | `"ok ok".replace("ok","yes")` → `'yes yes'` |
| `find(sub)` | 查找子串，返回索引，未找到返回 `-1` | `"hello".find("ll")` → `2` |
| `startswith(prefix)` | 判断是否以某前缀开头 | `"img.png".startswith("img")` → `True` |
| `endswith(suffix)` | 判断是否以某后缀结尾 | `"img.png".endswith(".png")` → `True` |
| `isdigit()` | 是否全是数字 | `"123".isdigit()` → `True` |
| `isalpha()` | 是否全是字母 | `"abc".isalpha()` → `True` |
| `encode(encoding)` | 编码为字节串 | `"你好".encode("utf-8")` → `b'\xe4\xbd\xa0...'` |

---

### 5. 格式化字符串（重点）

现代 Python 最推荐 **f-string**（Python 3.6+）：

```python

name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")
print(f"Pi is roughly {22/7:.2f}")           # 保留两位小数
print(f"{42:06d}")                           # 输出：000042（6位，补零）
```

格式说明符格式：{变量名: 填充 对齐 宽度 .精度 类型}

| 对齐符号 | 含义 |
| :--- | :--- |
| `<` | 左对齐 |
| `>` | 右对齐 |
| `^` | 居中对齐 |

类型符号：b 二进制、x 十六进制、o 八进制、% 百分比。


### 6. 编码与字节串

Python 3 区分 **字符串（`str`）** 和 **字节串（`bytes`）**。

- `str` 是 Unicode 码点序列，用于处理文本。
- `bytes` 是 0-255 整数序列，用于处理二进制数据（如图像、网络传输）。

两者通过 `encode()` 和 `decode()` 互相转换：

```python

text = "Python ♥ 中文"
data = text.encode("utf-8")   # b'Python \xe2\x99\xa5...'
text2 = data.decode("utf-8")   # 还原为原字符串
```

重要提醒：处理文件读写时，务必指定 encoding="utf-8"，否则 Windows 下可能默认用 GBK 编码导致中文乱码。


### 7. 遍历字符串

```python

for char in "abc":
    print(char)

# 需要索引时用 enumerate
for i, ch in enumerate("世界"):
    print(i, ch)   # 0 '世', 1 '界'
```


### 8. 字符串的不可变性

每次操作字符串都是生成新对象，原字符串不会改变：

```python

s = "Hello"
s.upper()      # 返回 "HELLO"，但 s 还是 "Hello"
print(s)       # "Hello"
```

性能提示：若需频繁拼接大量字符串（如循环中），请使用 list 收集后用 ''.join()，避免产生大量临时对象导致效率低下。


### 9. 字符串与文件处理
```python

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()       # 整个文件读成字符串
    lines = f.readlines()    # 按行读成字符串列表

with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Hello, 世界!")
```


### 10. 相关标准库模块

| 模块 | 用途 |
| :--- | :--- |
| `string` | 提供字符串常量（`ascii_letters`, `digits`, `punctuation` 等）和模板 `Template` |
| `re` | 正则表达式：搜索、替换、匹配模式 |
| `textwrap` | 段落自动换行、缩进、截断等 |
| `difflib` | 计算两个字符串序列差异 |
| `unicodedata` | 查询 Unicode 字符属性 |