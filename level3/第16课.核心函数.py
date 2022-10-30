"""
第16课: 核心函数

16.1 学习要点

至少掌握69个常用函数中的大多数最常用函数,
包含数学运算函数(7个)：
abs、div_mod、 max、 min、 pow、round, sum;

类型转换函数(15) :
bool,int、 float、 str、 ord、 chr,bin、 hex, tuple, list、 dict, set, enumerate、range、object;

序列操作函数(6):
ali,any, niter,map、next,sorted;

对象操作函数(6个):
help,dir、type、ascii、 format、vars;

交互操作函数(2个):
print、input;

文件操作函数(1个):
open。

16.2 对标内容

记住常用核心内置函数的功能及用法。

16.3 数学运算函数
16.3.1 知识点详解

1. abs(x)
该函数返回数字的绝对值。参数x为数值表达式。
函数返回x (数字)的绝对值。

例如:
>>> abs(3.9)
3.9
>>> abs(-3.9)
3.9

2. divmod(a,b)

该函数把除数和余数运算结果结合起来,返回一个包含商和余数的元组(a//b, a%b)。
参数a为数字,b为数字。

例如
>>> divmod(7, 2)
(3, 1)

16.3.2易错点

(1) divmod()函数返回的是商和余数组成的元组,不是列表。
(2)余数的符号由第二个参数的符号决定,如下所示。

>>> divmod (-7,2)
(-4, 1)
>>> divmod (7,-2)
(-4, -2)
>>> divmod (-7,-2)
(3, -1)

16.3.3 模拟考题

考题1 单选题


关于abs(函数,描述不正确的是()

A. abs()函数的功能是取整数的绝对值
B. abs()函数的功能是取实数的绝对值
C. abs()函数的功能是取一个数的绝对值
D. 负数的绝对值是正数正确

答案: A
解析:本题考核对abs()函数的理解。

考题2 判断题

divmod()函数的返回值是一个包含商和余数的列表。()

答案:错误
解析: divmod()函数的返回值是一个包含商和余数的元组。

16.4 类型转换函数

16.4.1 知识点详解

1. bool()
用于将给定参数转换为布尔类型,如果没有参数,则返回False。
以下展示了使用bool()函数的实例。
>>> bool()
False
>>> bool(0)
False
>>> bool(1)
True
>>> bool(2)
True

2. ord("字符串")

该函数的返回值类型为int,返回参数所对应的ASCII码值,

如下例所示。ASCII 码表如表16-1所示。

>>> ord ("0")
48

3. chr(数值表达式)
该函数的返回值类型为字符串,其数值表达式取值范围为0~255,
返回参数所对应的ASCII码字符串,如下例所示。

>>> print (chr(78))
N

4. set()

该函数创建一个无序不重复元素集,可进行关系测试,删除重复数据,
还可以计算交集、差集、并集等。

以下实例展示了set()函数的使用方法。

>>> x = set('runoob')
>>> y = set ('google')
>>> x, y
({'r', 'b', 'n', 'o', 'u'), ('l', 'g', 'o', 'e'}) #重复的元素被删除

>>> x & y  #交集
{'o')

>>> x | y #并集
{'r', 'b', 'l', 'n', 'g', 'o', "u', 'e'}

>>> x - y #差集
('n', 'r', b', 'u')


5. enumerate()

该函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列,
同时列出数据和数据下标,一般用在for循环中。

普通的for循环如下所示。

>>> l = [78, 98, 69, 85]
>>> for i in l:
>>>     print(i)
78
98
69
85

使用enumerate()函数的for循环如下所示。
>>> l = [78, 98,69,85]
>>> for a, i in enumerate(l):
>>>     print(a, i)
0 78
1 98
2 69
3 85

6. object()
object类是Python中所有类的基类,如果定又一个天时没有指定继承哪个类,
则默认继承object类。object()函数无参数,返同一个新的无特征对象。

>>> object ()

<object object at Ox00000174C47F5D00>

16.4.2 易错点
(1) bool()函数的参数与返回值的记忆问题。
(2) set()函数的简单运算。

16.4.3 模拟考题

考题1 判断题
bool()、bool(None)、bool(")、bool(["])这5个表达式输出的结果都是False。

答案:错误
解析: bool(["])列表参数中有一个字符串元素。


考题2判断题
在Python中,执行print(ord('a')+12)语句,能够得到一个数字结果。

答案:正确
解析: ord('a')的结果是数字,再加12仍旧是数字。


16.5 序列操作函数

16.5.1知识点详解

1. all()
该函数用于判断给定的可迭代参数中的所有元素是否都为True,如果是则返回True,否则返回False。
元素除了值是0、空、None、False外都算True。

以下展示了使用all()函数的实例。

>>> all(['a', 'b', 'c', 'd']) #列表中的元素都不为空或0
True
>>> all(['a', 'b', , 'd') #列表中存在一个空元素
False
>>> all([0, 1, 2, 3]) #列表中存在一个值为0的元素
False
>>> all(('a', 'b', 'c', 'd')) #元组中的元素都不为空或0
True
>>> all(('a', 'b', , 'd')) #元组中存在一个空元素
False
>>> all((0, 1, 2, 3)) #元组中存在一个值为0的元素
False
>>> all([]) #空列表
True
>>> all(()) #空元组
True

2. any()
该函数用于判断给定的可迭代参数iterable是否全部为False,是则返回False,否则返回True。
元素除了值是0、空、False外都算True。

>>> any(['a', 'b', 'c', 'd']) #列表中的元素都不为空或0
True
>>> any(['a', 'b', , 'd']) # 列表中存在一个为空的元素
True
>>> any([0, '', False]) #列表中的元素全为0、空、False
False
>>> any('a', 'b', 'c', 'd')) #元组中的元素都不为空或0
True
>>> any(('a', 'b', '', 'd')) #元组中存在一个空元素
True
>>> any ((0, '', False)) #元组中的元素全为0、空、False
False
>>> any ([]) #空列表
False
>>> any(()) #空元组
False


3. filter()
该函数用于过滤序列,过滤掉不符合条件的元素,返回一个选代器对象。
如果要将结果转换为列表,可以使用list()函数来转换。

该函数接收两个参数,第一个为函数,第二个为序列,序列的每个元素作为参数传递给函数进行判断,
然后返回True或False,最后将返回True的元素放到新列表中。

filter()函数的实例:过滤出列表中的所有奇数。

>>> def jishu(o):
>>>    return o % 2 == 1
>>> newlist = filter(jishu, [1, 2, 3, 4, 5, 6, 1, 8, 9, 10])
>>> n = list(newlist)
>>> print(n)
[1, 3, 5, 7, 9)

4. map(function,iterable, ...)
map()是Python的内置函数,会根据提供的函数对指定的序列做映射。
第一个参数接受一个函数名,后面的参数接受一个或多个可选代的序列。
把函数依次作用在列表中的每一个元素上,得到一个新的列表并返回。
注意,map()函数不改变原列表,而是返回一个新列表,如下例所示。

>>> def square(x):
>>>     return x ** 2
>>> l = list (map(square, [1, 2, 3, 4, 5]))
>>> print (l)
[1, 4, 9, 16, 25]

通过使用lambda匿名函数的方法使用map()函数,如下例所示。

>>> l = list(map(lambda x, y: x+y, [1,3,5,7,9], [2, 4, 6,8, 10]))
>>> print(l)
[3,7,11, 15, 19]

通过lambda函数使返回值是一个元组,如下例所示。
>>> l = list(map(lambda x, y : (x**y, x+y), [2,4, 6], [3, 2,1]))
>>> print (1)
[(8, 5), (16, 6), (6, 7)

map()函数还可以实现类型转换。

例 1 将元组转换为列表
>>> l = list(map(int, (1,2, 3)))
>>> print (1)
[1,2,3]

例 2 将字符串转换为列表
>>> l = list(map(int, '1234'))
>>> print (1)
[1,2,3,4]


例 3 提取字典中的键,并将结果放在一个列表中
>>> l = list(map(int,{1:2, 2:3, 3:4}))
>>> print (1)
[1,2,3,]

16.5.2 易错点

(1) all()与any()这两个函数的用法容易混清。
(2)熟记 map()函数的简单用法。

16.5.3 模拟考题

考题 1单选题

以下表达式的值为 Fasle的是()。
A. all(())
B. any((0, 1))
C. all((0,))
D. any(['a', 'b', '', 'd'])

答案: C
解析:本题考核all()与any()这两个函数的用法。

考题2 判断题

在Python中,函数all([])将返回False。

答案:错误
解析:空列表返回True。


16.6 对象操作函数

16.6.1 知识点详解

1. help()

该函数用于查看函数或模块用途的详细说明,返回对象为帮助信息。
以下实例展示了help()函数的使用方法。

>>> help('sys') #查看sys模块的帮助信息
>>> help ('str') #查看str数据类型的帮助信息
>>> a = [1,2,3]
>>> help(a) #查看列表的帮助信息
>>> help(a.append) #显示列表的append方法的帮助信息

2. dir([object])
参数object为对象、变量、类型。该函数不带参数时,返回当前范围内的变量、方法和定义的类型列表;
带参数时,返回参数的属性、方法列表。如果参数包含方法_dir_(),该方法将被调用。

如果参数不包含_dir_(),该方法将最大限度地收集参数信息。

>>> dir() #获得当前模块的属性列表
>>> dir([]) #查看列表的方法

对dir()函数了解即可。


3. ascii()
该函数返回一个表示对象的字符串,如下例所示。
>>> ascii((1,2))
'(1, 2)'
>>> ascii ([1,2])
[1, 2]
>>> ascii({1:2, 'name':5})
"(1: 2, 'name': 5)"
>>> ascii('?')
"'?'"
>>> ascii(([1,1,2,3]))
'(1, 2, 3)"

4. vars([object])

该函数返回对象object的属性和属性值的字典对象;
如果没有参数,就打印当前调用位置的属性和属性值,如下例所示
>>> a = 2
>>> b = vars()
>>> b["a"]
2

对vars()函数了解即可。

16.6.2 易错点
(1)本节大多数内容了解即可。
(2)注意不要混滑ascii()函数与ord()函数的用法。

16.6.3模拟考题

考题1单选题

ascii(chr(65))的值是
Α. 'Α'
B. 65
C. "A"
D. '65'

答案: C
解析:本题考核ascii()函数与chr()函数的用法。

考题2单选题

下列选项中具有查看函数或模块说明功能的函数是
A. help()函数
B. ascii()函数
C. dir()函数
D. vars()函数

答案: A
解析:本题考核对上述函数用法的了解。

"""