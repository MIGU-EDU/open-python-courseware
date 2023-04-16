"""

第22课 第三方库（模块）的获取、安装与调用

22.1 学习要点

（1）理解模块化架构和包的管理，了解pip命令、集成安装方法和文件安装方法。
（2）掌握import和from方式。

22.2 对标内容
掌握第三方库（模块）的功能、获取、安装、调用等。

22.3 第三方库的获取、安装与调用

22.3.1 第三方库的获取、安装方法

安装Python第三方库的3种方法为：
（1）使用pip命令；
（2）集成安装方法；
（3）文件安装方法。

1．使用pip命令（需要联网）

使用python自带的pip安装工具安装第三方库时，需要打开操作系统提供的命令行，适合windows、macOS 和 Linux 等操作系统。

pip -h:查看pip的帮助信息。

常用的pip指令如下。
pip install＜第三方库名＞：安装指定的第三方库。
pip install-U＜第三方库名＞：将已经安装的第三方库更新到最新版本中。
pip uninstall ＜ 第三方库＞：卸载指定的第三方库。
pip download ＜ 第三方库＞：下载但不安装指定的第三方库，作为后续的安装基础。
pip show＜ 第三方库＞：列出指定第三方库的详细信息。
píp search ＜ 第三方库＞：根据关键词在名称和介绍中搜索第三方库。
pip list：列出当前系统已经安装的第三方库。
python -m pip install --upgrade pip：升级 pip（Python 3.4之后的版本都自带了 pip）。
了解常用模块pytesseract、pyquery、requests、urllib3、wheel．wordcloud（词云图）、xlrd（读Excel文件）、xlwt（写Excel文件）。
setuptools、pymouse（模拟鼠标操作）、PyAotuGUI（模拟鼠标、键盘操作）、selenium（自动化测试环境搭建）、scrapy、cx＿Oracle的安装方法。

下面以安装 wheel模块为例介绍具体的安装方法。
方法1：按“Win＋R”组合键进入cmd窗口，直接运行如下代码。
>>> pip install wheel
方法2：在本地安装whl文件。
（1）将whl文件下载到计算机上（任意位置即可）
（2）按"Win + R" 组合键进入cmd窗口，切换到存放whl文件的目录。
（3）通过以下命令安装whl文件（*****.whl 是我们下载的whl文件的名称）。
>>> pip install *****.whl

2:集成安装方法

暂不涉及

3:文件安装方法

3. 文件安装方法

下载对应版本的.exe安装文件，如 numpy-1.9.2-win32-superpack-python2.7.exe、 mlpy-3.5.0.win32-py2.7.exe,运行该文件即可。


22.3.2 第三方库的导入方法

使用Python 进行编程时,有些功能没必要自己实现,可以借助Python现有的标准库或者其他人提供的第三方库，如下例所示。
>>> import math
>>> math.pi
>>> math.sin(0.5)
>>> math.sqrt (144)

1. import模块名1 [as别名1],模块名2 [as别名2], …

使用这种语法格式的 import 语句，会导入指定模块中的所有成员(包括变量、函数、类等)。
当需要使用模块中的成员时,只需将该模块名(或别名)作为前缀,如下例所示。

注意，用[]括起来的部分，可以使用，也可以省略。
>>> import math as m
>>> m.pi

2. from 模块名 import 成员名1 [as别名1],成员名2 [as别名2],

使用这种语法格式的import语句,只会导入模块中指定的成员,而不是全部成员。
同时、当程序中使用该成员时,无须附加任何前缀,直接使用成员名(或别名）即可。

>>> from math import * #导入模块中的所有成员

22.3.3 易错点

（1）注重实操体验。
(2)记忆相关的操作语句的语法。

22.3.4 模拟号题
考题1单选题

用于安装Python第三方库的工具是
A. install
B. pip
C. wheel
D. setup

答案: B

解析:可以用"pip install第三方库名”安装Python第三方库。
使用"pip install-upgrade numpy”命令能够升级 numpy科学计算扩展库。


考题2判断题

答案：正确

解析：使用“pip install-upgrade 包名”命令能够更新已安装的第三方库。
"""