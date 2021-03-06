# 字典 基本概念和操作

"""
字典，首先想到的是日常生活中用的字典。查字典是怎么进行的？我们只知道读音，不知道字如何写，
可以通过音序查字法找到对应的值；如果我们只知道字的写法，但是不知道读音，可以通过部首查字查找相对应的读音
大家有没有发现，不管使用哪种查字法，都要有一个已知的关键信息，通过这个关键信息可以找到对应的其他信息。
这其实也是Python中的基本原理：通过键找到值，它们是对应的关系。

1：什么是字典？

python中的字典指的是一种可变的容器类型，而且它可以装任意类型对象。所谓容器类型，就是可以存储数据的地方。
Python中的字典是用大括号{}括起来的，并且每一个元素由键和值两部分组成，并且键和值之间必须使用英文冒号(:)隔开。
由于它们必须一一对应，所以又称作键值对，每组键值对之间必须使用英文逗号(,)隔开。如下所示：

>>> dirs = {'西瓜': 9.6, '桃子':2, '苹果': 4}

2：字典有什么特征

键是字典中进行读取值及赋值很重要的标记，所以要求有唯一性，并且是不可变序列；值可以是其他任意数据类型，不要求具有唯一性。
字典并不是序列，所以没有序列，因而也就没有索引。

3：字典的创建

字典直接使用{}来建立，格式符合字典的要求即可。如下所示：

>>> dirs = {}

4: 访问字典的值

由于字典没有索引，所以我们不能使用索引的方法来访问字典。要访问字典的值，有两种常用方法。
第一种：使用字典名加键进行访问，这种方法有点像是把键当做字典的 ‘索引’ 来访问，格式为 ‘字典名[键名]’，如下：

>>> dirs = {'西瓜': 9.6, '桃子':2, '苹果': 4}
>>> print(dirs['西瓜'])
9.6

第二种：使用字典中的get()函数进行访问，格式为‘字典名.get(键名)’，如下所示：

>>> dirs = {'西瓜': 9.6, '桃子':2, '苹果': 4}
>>> print(dirs.get('桃子'))
2

5: 修改已有的键的值

直接使用字典名加键的方式进行赋值即可，如下：

>>> dirs = {"西瓜": 3, "桃子": 2, "苹果": 4}
>>> dirs['西瓜'] = 10
>>> print(dirs)
{'西瓜': 10, '桃子': 2, '苹果': 4}

6: 给字典增添新的键值对

同样也采用字典加键的方式直接赋值即可，也就是说：采用该方法赋值，如果字典中也有键，
则将该键的值修改为最新的值；如果字典中没有该键，则新增该键值对到字典中。

>>> dirs = {"西瓜": 3, "桃子": 2, "苹果": 4}
>>> dirs['梨'] = 8
>>> print(dirs)
{'西瓜': 3, '桃子': 2, '苹果': 4, '梨': 8}


7: 删除字典里面已有的值

使用del可以删除一个键值对，如下例所示：
>>> dirs = {"西瓜": 3, "桃子": 2, "苹果": 4}
>>> del dirs['西瓜']
>>> print(dirs)
{'桃子': 2, '苹果': 4}

8: 清空字典的值

clear() 可以清空字典里面的所有值，使字典成为一个空字典，其格式为 “字典名.clear()”

9: 求字典的长度

>>> dirs = {"西瓜": 3, "桃子": 2, "苹果": 4}
>>> print(len(dirs))
3

10: 检查键是否在字典中

使用 in 可以检测是否在字典中，如果在则返回 True, 否则返回 False;
但是这里要注意：in 只检查键，并不检查值。如下列中 "python" 是值，
并不是键，所以返回值依然是 False

>>> dirs = {"西瓜": 3, "桃子": 2, "苹果": 4}
>>> print('python' in dirs)
False

# 易错点

(1) 字典的键具有唯一性，如果创建时同一键被赋值两次，则后一个值会取代前一个值成为键的值，如下：
>>> dirs = {"西瓜": 3, "桃子": 2, "苹果": 4}
>>> print("dirs['西瓜']:", dirs['西瓜'])
dirs['西瓜']: 3

键必须不可变，所以可以用数字、字符串、或元组充当，而用列表就不行，会报 TypeError 错误。
>>> # dirs = {["西瓜"]: 3, "桃子": 2, "苹果": 4}
>>> # print(dirs['西瓜'])
TypeError: unhashable type: 'list'

(2) 字典的值必须使用字典里已有的键来访问，如果用字典里没有的键访问，会报KeyError错误。
(3) 把键当做 “索引” 访问字典和使用 get() 函数访问字典的区别：最大的区别是 get() 函数
可以自定义没有该键时的返回值，如果没有自定义，则返回None; 而把键当做 “索引” 来访问字典时，
如果没有该键，则会报错。
"""

