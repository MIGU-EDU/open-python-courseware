# 编码与数制

"""
12.1 学习要点
（1） 二进制数、八进制数、十六进制数的概念及它们与十进制数相互转换的方法。
（2）如何使用 Python 中的数制转换函数。

12.2 对标内容
能够进行二进制、八进制、十六进制与十进制之间的转换；理解 Python 中的数制转换函数。

12.3 情景导入
二进制起源于中国。二进制的运用，在我国古代就已经显现得淋漓尽致。
中国古代的二进制运用与现代电子计算机中二进制的运用是一致的。首先从易经上可以看到二进制的起源。
易经阐述的是世间万象变化，通过卦爻来说明天地人间、日月系统以内、人生与事物变化的法则。
易经中的卦爻是用阳爻（-）、阴爻（--）表示的，可看作用二进制手段实现的。中国古代将二进制运用于天地、
人事、哲学研究，而现代的信息系统领域将二进制运用于电子数字化研究。

12.4 十进制与二进制

12.4.1 知识点详解

人们通常把用来表示信息的符合组合称为信息代码，而编制代码的过程称为信息编码。
在计算机中，所有的信息都是采用二进制数存储的，计算机存储的最小单位是位，
每一个二进制位可以表示0和1 两种信息。

二进制数的特点是：有0 和 1 两个基本数码，采用逢二进一的进位规则。
将十进制数转化为二进制数的方法：除以2取余，逆序输出。
例如：（143）₁₀ =（10001111）₂
所以2取余数，直到商为0，将所得余数倒排序。
——————————————————————————————————

将二进制数转化为十进制数的方法：按权展开，逐项相加。
例如：（1011）₂ = 1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2º = (11)₁₀
n 个二进制位最多能表示的不同信息个数是2ⁿ；n 位的二进制数能表示的最大十进制数是2ⁿ - 1。

Python 中的转换函数：bin() 函数将十进制整数转换二进制数字符串，要求参数必须为整数；
int() 函数将二进制数字符串转换为十进制数。
例如：

>>> bin(11)
'0b1011' # 以0b开头的数字代码串，表示一个二进制数
>>> int('0b1011', 2)
11
>>> int('1011', 2) # 也可以省略0b, 与上一行代码等价
11

12.4.2 易错点

（1）bin() 函数将十进制整数转换为二进制数，返回的结果是字符串
（2）二进制数的前缀 ‘0b’ 可以省略，同时‘0b’ 与 ‘0B’ 等价，不区分大小写，八进制数、十六进制数的表示同理。

12.4.3 模拟考题

将十进制数120转换为二进制数时，该二进制数的数位是（）？
A.5 B.6 C.7 D.8
答案：C
解析：将120除2取余，逆向输出，得到的答案是1111000.

二进制数10101010对应的十进制数位169.

答案：错误
解析：按权展开，得到的答案是170.


12.5 十进制与八进制

12.5.1 知识点详解

八进制数的特点是：有0、1、2、3、4、5、6、7共8个基本数码，采用逢八进一的进位规则。
将十进制数转换为八进制数的方法：除以8取余，逆序输出。
例如：（143）₁₀ =（217）₈
除以8取余数，直到商为0，将所得余数倒排序。

——————————————————————————————————————

将八进制数转换为十进制数的方法：按权展开，逐项相加
例如：（218）₈ = 2 × 8² + 1 × 8¹ + 7 × 8º = （143）₁₀

Python 中的转换函数：oct（）函数将十进制整数转换为八进制数字符串，要求参数必须为整数；
int() 函数将八进制数字符串转换为十进制数。

例如：

>>> oct(143)
'0o217'
>>> int('0o217', 8)
143
>>> int('217', 8)
143

12.5.2 易错点

（1）oct()函数将十进制整数转换为八进制数字，返回的结果是字符串。
（2）八进制数的前缀 ‘0o’ 可以省略，‘0o’ 与 ‘0O’ 等价。

12.5.3 模拟

表达式oct('11', 8)的值是（）？

A.10 B.11 C.12 D.13
答案： D
解析：将11除以8取余，逆向输出，得到的答案是13。

八进制数68对应的十进制数位56（）？

答案：错误
解析：八进制数没有‘8’这个基数，所以答案是错误。


12.6 十进制与十六进制

12.6.1 知识点详解

十六进制的特点是：有0、1、2、3、4、5、6、7、8、9、A、B、C、D、E、F共16个基本数码，
采用逢十六进一的进位规则。

将十进制数转为十六进制的方法：除以16取余，逆序输出。
例如：（143）₁₀ = （8F）₁₆
除以16取余数，直到商为0，将所得余数倒排序。
将十六进制数转为十进制数的办法：安全展开，逐项相加。
例如：（8F）₁₆ = 8 × 16¹ + 15 × 16º = （143）₁₀

Python 中的转换函数：hex() 函数将十进制数转换为十六进制数字符串，
要去参数必须为整数；int()函数将十六进制数字符串转换为十进制数。

例如：
>>> hex(143)
'0x8f'
>>> int('0x8f', 16)
143
>>> int('8F', 16)
143

12.6.2 易错点

（1）hex()函数将十进制整数转换为十六进制数字，返回的结果是字符串。
（2）八进制数的前缀 ‘0x’ 可以省略，‘0x’ 与 ‘0X’ 等价。

12.6.3 模拟

将十进制数30 转换为十六进制数，最低位上的数是（）？
A.c B.d C.e D.f
答案：C
解析：将30除以16取余，余数为十进制14，转为十六进制数是e或E，所以答案是C.

将十进制数转换为十六进制数后，它的位数一定会变短（）
答案：错误
解析：10以内的十进制数转换为十六进制数，位数不变，所以答案是错误

12.7 二进制与十六进制

12.7.1 知识点详解

将二进制数转为十六进制的方法：从低位开始4位1组，
逐组转换（如果位数不够，左边补0凑足）
例如：（101110111110111）₂ = （5DF7）₁₆

    二进制数    0101 1101  1111 0111
    十六进制数   5    D     F    7

将十六进制数转换为二进制数的方法：逐位肢解，1位数转换为4位二进制数
（如果位数最左边有0，省略不写）
例如：（5DF7）₁₆ = （101110111110111）₂

    十六进制数  5    D     F    7
    二进制数   0101 1101  1111 0111

合并4组4位二进制数，把最左边的0省略不写，得到的101110111110111.
Python 中的转换函数：hex()函数将二进制的整数转换为十六进制数的字符串，
要求参数必须为整数，bin()函数将十六进制数转换为二进制数。

例如：
>>> hex(0b101110111110111)
'0x5df7'
>>> bin(0x5df7)
'0b101110111110111'

12.7.2 易错点

（1）hex() 函数将二进制整数转换为十六进制数，二进制数不必加引号；
（2）bin() 函数将十六进制数转换为二进制数，十六进制数不必加引号；

12.7.3 模拟

下列关于表达式的计算结果，不正确的是（）
A.hex(int('11',2))得到的结果是‘0x3’
B.hex(0b11110111)的结果是‘0xf7’
C.hex(int('11', 16))结果是‘0x17’
D.bin(0xf7)结果是‘0b11110111’


答案：c
解析：C选项正确的结果应该是'0x11'

二进制数11110011转换为十六进制数位F3()
答案: 正确
解析：二进制整数转化为十六进制数，从低位开始4位1组，逐组转化。
"""

