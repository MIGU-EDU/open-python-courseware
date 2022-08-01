# 数据处理

"""
13.1 学习要点
一维及二维数据的相关知识：表示、存储、格式化、读入文件、写入文件、提取数据、CSV文件的操作、添加数据。

13.2 对标内容
掌握一维数据表示和读写方法，能够编写程序处理一维数据。
掌握二维数据的表示和读写方法，能够编写程序处理二维数据。
掌握CSV格式文件的读写方法。

13.3 情景导入
一份班级期中考试成绩表，就是一个二维数据。
Python 是最强大的数据处理工具，最基础的数据文件有‘一维数据’、 ‘二维数据’、CSV格式数据文件。

一维数据：由对等关系的有序或无序数据组成，采用线性方式组成。
二维数据：由多个一维数据构成，是一维数据的组合形式；
CSV格式数据文件：国际通用的一二维数据存储格式，扩展名一般为.csv，每行存储一个一维数据，
采用逗号分隔，无空行。Excel 和一般文字编辑软件都可以读入或保存CSV文件。
下面，我们来讲解以上三种数据文件的概念、使用场景、读写操作。

13.4 一维数据

13.4.1 知识点详解

一维数据由对等关系的有序或无序数据构成，采用线性方式组织、对应数学中的数组的概念。
一维数据具有线性特点。

任何表现为序列或集合的对象都可以看作一维数据。
在Python中，一维数据主要采用列表形式表示。

c = ['北京','上海','广州','深圳']
print(c)

一维数据的存储：

- 采用空格分隔元素；
- 采用逗号分隔元素（常用，csv格式）;
- 采用换行分隔元素；
- 采用其它特殊符合（比如；）分隔元素。

CSV 格式就是采用逗号分隔值，它是一种通用的、相对简单的文件格式，
广泛应用，Excel、记事本等大部分编辑器支持直接读入或保存CSV格式文件。CSV文件的扩展名为.csv。

将列表对象输出为CSV格式文件，示例如下。

c = ['北京','上海','广州','深圳']
f = open('city.csv', 'w')
f.write(',',join(c) + '\n')
f.close()

在上述Python 程序的同目录下，如果存在city.csv文件，执行上述程序，
将覆盖city.csv文件(如果想非覆盖，将‘w’改为‘a’即可)；如果不存在city.csv文件，
执行上述程序后，将产生一个city.csv文件。

使用 with 语句打开文件，处理结束后会自动关闭被打开的文件，上述代码用with语句改写如下。

c = ['北京','上海','广州','深圳']
with open('city.csv', 'w') as f:
    f.write(',',join(c) + '\n')

从CSV格式文件中读出数据，表示为列表对象，示例如下：
f = open('city.csv', 'r')
c = f.read().strip().split(',')
f.close()
print(c)

上述代码用with语句改写如下：

with open('city.csv', 'r') as f:
    c = f.read().strip().split(',')
print(c)


13.5 二维数据

13.5.1 知识点详解

二维数据由多个一维数据构成，是一维数据的组合形式，可以用二维列表表示。
列表的每个元素对应二维数据的一行，这个元素本身也是列表。
二维数据一般采用相同的数据类型存储数据。

c = [
    ['张三', '95', '98', '78'],
    ['李四', '95', '98', '78'],
    ['王五', '95', '98', '78'],
]

二维数据用CSV格式存储。CSV文件的每一行是一维数据，整个CSV文件是一个二维数据。

将列表对象输出为CSV格式，示例如下：

c = [
    ['张三', '95', '98', '78'],
    ['李四', '95', '98', '78'],
    ['王五', '95', '98', '78'],
]

f = open('cj.csv', 'w')
for i in c:
    f.write(','.join(i) + '\n')
f.close()

在上述Python程序的同目录下，如果存在cj.csv文件，运行上述程序后，
将覆盖cj.csv文件；如果不存在cj.csv文件，运行上述程序后，将产生一个cj.csv文件。

从csv 格式文件读出数据，表示为列表对象，例如：

f = open('cj.csv', 'r')
c = []
for i in f:
    c.append(i.strip('\n').split(','))
f.close()


13.5.3 模拟考题

要对二维列表所有的数据进行格式化输出，打印成表格形状，程序段如下：

ls = [['金京','89'], ['金京2','29'], ['金京3','99']]

for row in range(len(ls)):
    for column in range(len(ls[row])):
        print(___, end = '\t')

划线处的代码应该为？

ls[row][column]
ls[row]
ls[column]
ls[column][row]

根据二维数据的切片可得答案。


13.6 简单的文件读写

13.61.1 知识点详解

1. 将数据存储于本地CSV文件

方法1：单行写入
with open('xxx.csv', 'w', newlines='') as f:
    writer = csv.writer(f) # 创建初始化写入对象
    writer.writerow(['color', 'red']) # 一行一行写入

在window 里保存的CSV文件是每空一行存储一条数据，使用newlines=‘’ 可以保证存储的数据没有空行

方法2： 多行写入

with open('xxx.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows([('color', 'red'), ('size', 'big')]) # 多行写入


2. read()函数的使用

从文件 ‘c:\test.txt’中读取数据，文件内容例如：

> hello python!
> hello world!

(1)

>>> f = open(r'd:\text.txt', 'r')
>>> s = f.read() # 从文件指针所在的位置，读到文件结尾
>>> s
'hello python! hello world!\n'
>>> f.close()

(2)

>>> f = open(r'd:\text.txt', 'r')
>>> s1 = f.read(15) # 从文件指针所在的位置开始读15个字节
>>> s2 = f.read() # 从文件指针所在的位置读到文件结尾
>>> f.close()
>>> s1
'hello python!\nh'
>>> s2
'ello world!\n'
>>> print(s1,s2)
hello python!
hello world!

(3)

>>> f = open(r'd:\text.txt', 'r')
>>> s1= f.read() # 读取文件中的所有内容，返回一个字符串
>>> s2= f.read() # 读取到了0个字节，因为文件指针已经读到文件尾部
>>> f.close()

3. read()与readline()、readlines() 区别

read()每次读取整个文件，它通常将读取到的文件内容放到一个字符串变量中，也就是说read()
生成的文件内容是一个字符串。

readline() 每次读取文件的一行，通常也是将读取到的一行内容放到一个字符串变量中，返回str类型数据。

readlines() 每次按行读取整个文件内容，将读取的内容放到一个列表中，返回list类型数据。

4. reader() 函数的使用

导入模块csv之后，我们将CSV文件打开，并将结果文件对象存储在f中。
然后，调用csv.reader()，将前面存储的文件对象作为实参传递给他，
从而创建一个与该文件相关联的阅读器（reader）对象，等待进一步处理，如下：

import csv
with open('score.csv') as f:
    rows = list(csv.reader(f))

5. write()函数的使用

wirte()函数的参数是一个字符串，分以下两种情况。

（1） 通过write()函数向文件写入一行数据。

>>> f = open(r'd:\text.txt', 'w')
>>> f.write('hello,world!'\n) # 写入的字符串在末尾包含一个换行符
>>> f.close()

（1） 通过write()函数向文件写入多行数据。

>>> f = open(r'd:\text.txt', 'w')
>>> f.write('hello world!' \n 'hello world!'\n) # 写入的字符串在末尾包含多个换行符
>>> f.close()

6. write() 和 writelines()区别

write()需要传入一个字符串作为参数，否则会报错；writelines()既可以传入字符串，也可以传入一个字符序列，并将该字符序列写入文件。

"""

