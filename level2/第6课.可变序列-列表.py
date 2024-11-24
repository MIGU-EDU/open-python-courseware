"""

第6课 可变序列-列表

6.1 学习要点
（1）学习Python的可变序列的基本操作。
（2）学习以列表为代表的可变序列的基本操作。

6.2 对标内容
理解列表类型的概念，掌握它的基础用法及操作：访问／更新、获取元素个数、遍历、转换为列表型数据、添加和删除、连接、排序等。

6.3 情景导入
考试结束了，一般要进行成绩统计和查找。为了提高查找的效率，我们一般会采用表格来记录这些数据。
像这种用表格记录数据的情况，在我们生活中有很多，火车站的列车时刻表、飞机场的飞机起落信息表、餐馆里面的价目表等都是例子，
我们在科学课上也借助表格进行过实验数据的统计。那么在Python中该如何表示这些表格中的数据呢？列表是一个非常好的选择。

6.4 列表

6.4.1 什么是列表
列表是Python中内置的有序、可变序列，列表的所有元素放在一对中括号“[]”中，并使用逗号分隔开。
列表的数据项不需要具有相同的类型。

6.4.2 列表的创建
列表的创建有多种方式，最常见的方式有两种：

一种是直接建立，创建时只需要将元素用逗号隔开，并且用中括号括起来就可以了，如［1，＇a＇，（3,5），2］；
另一种则是使用list命令进行创建，list（）用于将元组或字符串转换为列表，如list（＇Python＇）的结果就是['P','y',''y','t',t','h','o','n']

6.4.3 序列的通用操作
所谓序列，指的是一块可存放多个值的连续内存空间，这些值按一定顺序排列，可通过每个值所在位置的编号（称为索引）访问它们。
Python包含6种内建的序列，即列表、元组、字符串、Unicode 字符串、buffer 对象和 xrange对象。
在全国青少年软件编程等级考试Python编程中，buffer 对象和 xrange 对象不作为考核对象，不要求掌握。

下面我们以列表为例，看看序列都有哪些通用操作。

1．通用操作-序列的访问
列表是序列的一种，所以所有的元素都是有序号的，我们称序号为索引。
索引有两种表示方式，一种是从前往后的正方向索引，还有一种为从后往前的反方向索引。
正方向索引的第一个索引号为0，并非1，后面的索引号依次为1、2······反方向的索引，
第一个索引号为-1，接下来依次为-2、-3······如下（正方向索引和反方向索引）所示。

>>> t = ['a','b','c','d','e']
正方向索引  0   1   2   3   4
反方向索引 -5  -4  -3  -2  -1

要访问列表中的值，只需要使用列表变量名加上下标（索引号）即可，如要访问上面第三个元素的值，只需要使用 t[2] 或者t[-3］即可。

2．通用操作--序列的嵌套
序列里面可以再套序列，这叫作序列的嵌套。被嵌套的序列是作为一个整体看待的，所以其下标为一个，如下例所示。

>>> list = ["a","b",[1,2,3],"c"]
>>> list[2]
[1,2,3]

在该案例中，［1,2,3］是作为一个整体看待的，是列表list的第3个元素，所以 list［2］的值为［1,2,3］。
如果需要单独访问嵌套列表中的值，则需要进行列表下标的逐级分解，如下例所示，假设需要访问列表中的2。

>>> list = ["a","b",[1,2,3],"c"]
>>> list[2][1] ＃第一个下标代表嵌套列表在整个列表中的位置，第二个下标代表2的位置
2

3．通用操作-序列的截取
你可以使用索引下标来访问列表中的值，也可以使用中括号［］的形式截取序列，
要将下面示例中的第2个元素到第4个元素截取下来，则需要使用 t[1,4]。

          |开始  结束|
t = ['a','b','c','d','e']
        ['b','c','d']

列表的截取又称作列表的切片，它需要使用两个索引下标来确定切片的起始位置和结束位置。
列表的截取格式为：变量［头下标：尾下标：步长］，其中步长为可选参数，如果没有步长参数，则代表步长为1；
如果切片是从头开始或者是到最后结束，头下标和尾下标也可以没有，示例如下。

t[:3] t[3:] t[-3:]

但是要注意：列表的切片不包含尾部下标对应元素的值，但如果冒号后面没有数字则代表包含最后一个列表元素的值。
例如对于上面示例中，t[1:3] 返回的值是［＇b＇，＇c＇］而不是['b','c','d']，t［3：］返回的值是['d','e']

4．通用操作len（）-取序列的长度
取一个序列的长度的命令为len()，返回值为该序列的元素的个数，如下例len()所示。

>>> T = [1,2,3,4,5]
>>> len(T)
5

如果有序列嵌套的情况，被嵌套的序列是作为一个整体来计算的，如下例所示。

>>> T = [1,2,3,["a","b","c"],4,5,(10,9,8)]
>>>len(T)
7

5．通用操作in--检查元素是否包含在序列中
如果序列比较庞大，或者序列是在不断更新中，如何检查某一个元素是否在该序列中？
需要使用in命令进行判断，其返回值是True或者False，所以往往该命令是结合条件语句使用的，如下例所示。

>>> T = [1,2,3,["a","b","c"],4,5,(10,9,8)]
>>> print(8 in T)
False

上例中，表面看有元素8，怎么返回值是False呢？
这是因为8是在列表的嵌套元素（10,9,8）中，而in不检查序列嵌套元素里面的值，所以结果是False。

6．通用操作max（）--找出序列中的最大元素
max()函数用来找出序列中的最大值，但要注意以下3点。

（1）当序列内的元素均为数字类型时，max（）将返回该序列里最大的数字，如下例所示。

>>> T = [21,2,3,4,5,8,0]
>>> print(max(T))
21

（2）当序列内的元素均为字符串类型时，max() 则是按照Unicode编码的顺序（具体见字符串相关内容）返回编码最大的元素，如下例所示。

>>> T = ["A","a","d","2","Python","我"］
>>> print(max(T))
我

（3）当序列内既有数字类型，又有其他类型的元素时，max（）是无法进行运算的，会报错。

7．通用操作min（）--找出序列中的最小元素
min（）函数和max（）函数的功能刚好相反，是找出序列中的最小元素。
它和nax()函数一样，只能在序列内的元素均为数字类型或者均为字符串类型时才可以使用。

元素均为数字类型时：

>>> T = [21,2,3,4,5,8,0]
>>> print(min(T))
0

元素均为字符串类型时：

>>> T = ["A", "a", "d", "2", "Python", "我"］
>>> print(min(T))
2

8．通用操作sum（）-序列求和运算
sum（）函数可以对全部由数字类型组成的序列进行求和，输出的结果为该序列所有数字的和，如下例所示。

>>> T= [21,2,3,4,5,8,0]
>>> print(sum(T))
43

9．通用操作--序列的加法运算
同一种类型的序列是可以进行加法运算的，但是这里的加法不同于数学中的加法，序列的加法相当于将两个序列结合在一起，如下例所示。

>>> T= [21,2,3,4,5,8,0]
>>> t = ['a','b','c']
>>> print(T+t)
[21,2,3,4,5,8,0,'a','b','c']

10．通用操作--序列的乘法运算
序列也可以进行乘法运算，但是序列只能和正整数相乘，代表的是将该序列重复正整数次，如下例所示。

>>> T = ['a','b','c','d']
>>> print(T*2)
['a','b', 'c', 'd', 'a', 'b', 'c', 'd']

6.4.4 列表的专用操作

1．更新列表中的值
列表值的更新又称作修改列表中的值，可以直接使用列表名加下标进行赋值如下例所示。
>>> List = ['a','b', 'c', 'd','e']
>>> List[2] = 'aa'
>>> List
['a', 'b', 'aa', 'd', 'e']

利用列表切片技术，列表的值也可以同时更新多个，如下例所示。

>>> List = ['a', 'b', 'c','d','e']
>>> List[1:4] = [1,2,3]
>>> List
['a',1,2,3,'e']

2．列表元素的删除
删除列表中的值有多种方法，主要的有以下4种方法。

(1)del()
作用：删除列表中的指定下标的值，如果没有指定下标，则是删除整个变量。
格式：del list＿name（index）
参数：list＿name代表列表名，index代表下标（可省略），如下例所示。

>>> List = ['a','b','c', 'd','e']
>>> del List[1]
>>> List
['aa','c','d','e']

>>> List = ['a','b','c', 'd', 'e']
>>> del List
>>> List
NameError： name ＇List＇ is not defined ＃报错，没有找到＇List＇

(2)pop()
作用：删除指定下标的元素，如果没有指定下标，则默认删除最后一个元素。
格式：list＿name.pop（index）。
参数：list＿name代表列表名，index代表下标，如下例所示。

>>> List = ['a', 'b', 'c', 'd','e']
>>> List.pop(1)
>>> List
[a','c','d', 'e']

>>> List = ['a','b', 'c', 'd','e']
>>> List.pop()
>>> List
['a', 'b', 'c', 'd']

(3)remove()
作用：移除列表里面第一次出现的指定值的元素。我们有时候需要删除某一个元素，但是不知道它在列表的什么位置，这时候使用remove（）最合适。
格式：list＿name.remove（obj）。
参数：list＿name代表列表名，obj代表需要移除的元素的值，但是需要注意的是，一定要确保obj在列表里，否则会报错ValueError，如下例所示。

>>> List = ['a','b', 'c','d','e']
>>> List.remove('c')
>>> List
['a','b','d', 'e']

>>> List = ['a','b', 'c', 'd','e']
>>> List.remove('f')
ValueError： list.remove（x）： x not in list ＃报错

(4)clear()
作用：清除列表所有的元素，但是不删除列表，只是列表为空。
格式：list＿name.clear（）。
参数：list＿name代表列表名。由于是清除列表里面的所有元素，所以该命令没有参数，如下例所示。

>>> List = ['a', 'b', 'c', 'd', 'e']
>>> List.clear()
>>> List
[]＃列表List依然存在，但是为空列表

3．添加列表元素
向列表里添加元素，主要有两种方法。

(1)append()
作用：将元素添加到列表的末尾。
格式：list_name.append(obj)。
参数：list＿name代表列表名称；obj代表要插入的元素，元素可以是单个数据，也可以是列表、元组等，如下例所示。

>>> List = ['a','b','c','d','e']
>>> List.append(1)
>>> List
['a','b', 'c', 'd', 'e', 1]

(2)insert()
作用：将元素插入指定的位置。
格式：list_name.insert(index,obj)。
参数：list_name代表列表名称；index代表列表的下标，该参数只能为整数；obj代表需要插入的元素，如下例所示。

>>> List = ['a', 'b', 'c', 'd','e']
>>> List.insert(2,"Python")
>>> List
['a','b','Python','c', 'd', 'e']

4．查找元素
(1)index()
作用：查找元素在列表中的位置，返回值为该元素在列表中的下标。
格式：list_name.index（obj，start，end）。
参数：list_name代表列表名称，obj代表要查找的元素的值，start代表开始查找的位置，end代表结束查找的位置。
start、end为非必要选项，如果没有，则代表在整个列表里进行查找，如下例所示。

>>> List = ['a', 'b', 'c', 'd', 'e')
>>> List.index("c")
2
注意事项：index（）查找的元素必须已经在列表中，如果该元素不存在，则会导致ValueError 错误。

(2)count()
作用：统计某个元素在列表中出现的次数，返回值为该元素的个数。
格式：list_name.count（obj）。
参数：list_name代表列表名，obj代表需要统计的元素，如下例所示。
注意事项：如果count（）查找的对象不存在，则返回值为0。

5．列表的排序
(1)sort()
作用：对原列表进行排序，不返回新列表。如果指定参数，则使用指定的比较函数进行排序。
格式：list_name.sort(cmp=None,key=None, reverse=False)
参数：list_nanme表示列表名称；cmp、key、reverse均为可选参数，根据等级考试的标准，cmp、key参数不要求掌握，
这里不再赘述；reverse代表是否翻转，默认为不翻转（Falsse），如下例所示。

>>> List = ['e','b','a','d','c','f']
>>> List.sort()
>>> List
['a','b', 'c', 'd', 'e','f']

注意事项：
①sort()函数是在原内存地址上进行排序，所以sort（）函数排序后会直接和原列表名进行绑定，会改变原列表的值；
②sort()函数和求最值函数max（）、min（）函数一样，要求待排列对象必须为同一类型，常见的为数字类型和字符串类型；
③字符串类型在排序时是按照Unicode码顺序进行的，具体请参考字符串相关章节；
④sort（函数默认是按照从小到大的顺序进行排列，字符串是按照Unicode码从小到大的顺序排列，如下例所示；

>>> List = [122,23,1,9,-34,546,,12.3]
>>> List.sort ()
>>> List
[-34, 1, 9, 12.3, 23, 122, 546]

⑤ 如果 sort() 加入了reverse 参数，格式为 list_name.sort(reverse=1) 或者list_name.sort(reverse=True),
其工作原理是首先将列表按照从小到大的顺序进行排序,然后再进行翻转,这样就形成了从大到小的倒序排序,如下例所示。

>>> List = [122,23,1,9,-34,546,12.3]
>>> List.sort (reverse=True)
>>> List
[546, 122, 23, 12.3, 9, 1, -34]

(2) sorted()

作用:对可迭代的对象进行排序操作,会生成新的列表。
格式: sorted(iterable, cmp=None, key=None, reverse=False).
参数: iterable为可迭代对象(在列表中即列表名) ; cmp和key不要求掌握,在此不赘述; reverse代表是否翻转,默认为不翻转(False),
如下例所示。

>>> List = [122,23,1,9,-34,546,12.3]
>>> NewList = sorted (List, reverse=True)
>>> List
[122,23,1,9,-34,546,12.3]
>>> NewList
[546, 122, 23, 12.3, 9, 1, -34]

注意事项：

①sorted()和 sort()一样，对待排序的对象有相同的要求；
②sorted()不是在原内存地址进行排序,是新建一个列表,所以不改变原来的列表值。

(3) reverse()

作用: reverse()函数也是列表中的内置函数,用于反向排列列表中的元素
格式：list_name.reverse()。
参数: list_name代表列表名。
注意事项: reverse()并不进行排序，而是将列表里的元素进行顺序上的前后颠倒;
另外, reverse()和sort()一样:都是在原列表中进行操作,所以没有返回值,但是会改变原列表的值,如下例所示。

>>> List = [122,23,1,9,-34,546,12.3]
>>> List.reverse ()
>>> List
[12.3, 546, -34, 9, 1, 23, 122]

6.4.5 易错点

(1)一个列表中的数据类型可以各不相同,可以同时分别为整数、实数、字符串等基本类型,甚至是列表、元组、字典、集合以及其他自定义类型的对象。
(2)在嵌套的列表中,被嵌套的列表被作为一个整体看待。
(3)求序列的最大值、最小值,要求序列内所有元素必须同时为数字类型或者是字符串类型,不能混合,且不能嵌套,否则会报错。
(4)只有纯数字类型的序列才可以进行求和运算。

(5) clear()和del()的区别:首先, del()中,列表名是在后面的括号中;clear()中，列表名是在clear0的前面，并且用,隔开。
其次，del()可以只删除一个元素,如果不指定下标,只注明列表名,则删除整个变量,所以,列表也就不存在了;
而clear()是清除列表里的所有元素,列表还在,只是为空,此时列表长度为0。

(6) append()一次只能追加一个元素到列表里面,如果追加的是列表或者元组，则是作为一个整体进行追加，如下例所示。

>>> List = ['a','b','c','d', 'e']
>>> List.append ([1,2,3])
>>> List
['a','b','c','d','e',[1,2,3]]

(7) sorted()和sort()的区别: sorted()是Python的内置函数,可用于所有可迭代对象；
而 sort()是列表的内置函数，仅用于列表的排序。列表的 sort()方法是对已经存在的列表进行操作,无返回值;
而内置函数sorted()返回的是一个新的列表,而不是在原来的基础上进行的操作,所以不改变原列表的值。

6.4.6模拟考题
考题1单选题

已知列表a = [1,2,3], b=['4'],执行语句print(a+b)后,输出的结果是(
A. [1,2,3,4]
B. [1,2,3,'4']
C. ['1','2', '3','4']
D. 10

答案：B

解析:这是一个列表加法运算的题目,根据列表加法运算规则,加法运算是把后面的列表补充到前一个列表的后面,
在补充时是不改变原列表中元素的数据类型的,所以,当['4']补充到列表a的后面时依然还是'4',不能变成4,所以选择B。

考题 2 单选题

列表listV = list(range(10)),以下能够输出列表listV中最小元素的语句是）。

A. print(min(listV))
B. print(listV.max())
C. print(min(listV()))
D. print(listV.reveres()[O])

答案：A

解析:这是一道有多个考核点的题目,第一个考核点是新建列表的方式, list()函数就是将其他数据类型转换为列表;
第二个考核点是range(10)生成的可迭代对象是0-9的整数,所以题目中的list(range(10))生成的列表为[0,1,2,3,4,5,6,7,8,9];
第三个考核点是列表求最小值函数,该函数为min(),所以选择A.

其他选项出错原因:
B选项是求最大值并且格式错误;
C选项的格式是错误的, listV是列表名,后面不能有括号;
D选项的拼写和语法都是错误的,正a确的拼写应该为listV.reverse()并且作为列表内置函数,不可以在后面加下标[0],即使可以加,
但是由于reverse()进行了翻转,第一个元素成了9,并非最小的0。

考题 3单选题

运行如下程序，结果是（

l=[1,"laowang",3.14,"laoli"]
l[0]=2
del l[1]
print(l)

A. [1, 3.14, 'laoli']
B. [2, 3.14, 'laoli']
C. ["laowang", 3.14, 'laoli']
D. [2,"laowang", 3.14,]


答案：B

解析:根据题意,我们逐条分析程序运行结果。
程序运行第二行l[0]=2后,l列表变成了[2,"laowang", 3.14,"laoli"];
第三行del l[1]删除第二个元素,运行后， l变为[2,3.14,"laoli"],所以正确答案为B。

考题 4 单选题

关于列表 s 的相关操作，描述不正确的是（
A. s.append():在列表末尾添加新的对象
B. s.reverse():反转列表中的元素
C. s.count():统计某个元素在列表中出现的次数
D. s.clear()：删除列表 s 的最后一个元素

答案: D

解析:clear()的作用是清除列表里面的所有元素,而并非最后一个元素.

考题5单选题

已知列表lis=['1','2',3],则执行print(2 in lis)语句输出的结果是(
A. True
B. true
C. False
D. false

答案：C

解析：首先选项 B 和 D 不符合 Python 的返回值的格式要求，排除在外；
其次,根据题意,貌似2在列表中,但仔细观察,列表里的是字符串格式的'2',
而并非数字格式的2，那当然 2 in lis无法返回True，所以选择 C。

考题6 单选题

运行如下代码，结果是（
l= ["a",1,"b",[1,2]]
print (len (l))

A. 3
B. 4
C. 5
D. 6

答案：B

解析:嵌套列表中,被嵌套的列表是被当作一个整体看待、所以[1.2]在整个大列表中是一个元素,
加上前面的元素,一共有4个元素, len(1)的结果为4

考题 7 单选题

已知有列表a= [1,2,3,4,5],以下语句中,不能输出[5,4,3,2,1]的是
A. print(a[:-6:-1])
B. print(a.sort(reverse=True))
C. print(sorted(a, reverse=True))
D. print([5, 4, 3,2, 1])

答案；B
解析：从题目要求可知，输出的结果是原列表的反向排序。A 选项 a[:-6:-1]是从最后一个元素到倒数第 6 个元素（不含），
以步长为-1 的形式取值，虽素然列表a中只有5个元素，但是由于a[:-6:-1]不含第6个元素，所以不会报错，
因而A选项可以生成列表[5,4,3,2,1]; C选项是将a列表进行反向排序,所以也符合输出要求;
D选项直接输出目标列表, 自然符合要求; B选项看似也是将a列表反向排序,但是使用的是a.sort(reverse=True),
sort()函数是没有返回值的，其作用是将原列表 a 进行排序，
所以 B 选项要想输出目标列表，需要改成a.sort(reverse=True), print(a)才可以。

考题 8 单选题

已知列表 a=[1,2,3,4,5]，执行 a.insert(2,6)后结果是（)。

A. [1,2,3,4,5,2,6]
B. [1,2,3,4,5,6]
C. [1,2,6,3,4,5]
D. [1,2,3,6,4,5]

答案：C
解析: a.insert(2,6)的意思是在下标为2的位置插入一个元素6、所以正确答案是 C。
"""
