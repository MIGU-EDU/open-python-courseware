'''


第17课 函数的相关概念

17.1 学习要点
理解函数及过程、函数的参数、匿名函数等概念。

17.2 对标内容
理解函数及过程、函数的参数等概念。

17.3 函数的相天概念

17.3.1 知识点详解

1.函数的意义

在写一段程序的时候,需要多次用到同样的功能,如果每次都要重复写相同的代码,不仅会增加代码量,而且阅读与修改极不方便。
如果把实现相同功能的代码作为一个代码块封装在一起,形成一个函数,每次需要时调用这个函数,就很方便了!

定义函数的代码如下所示。

>>> def user(): #def关键字后面加函数名定义函数,定义以英文冒号结尾
>>>     print ("Hello World") #函数体,用来写该函数需要完成的功能的代码
>>> user() #使用函数名（）的方式调用函数

运行结果：Hello World

向函数传递参数信息的代码如下所示。

>>> def user(name):
>>>     print("Hello World" + name)
>>> user('zhangsan')

运行结果：Hello World zhangsan

2.形参和实参

从名字就可以看出、实参(实际参数)是一个实实在在存在的参数,是实际占用内存地址的;
而形参(形式参数)只是意义上的一种参数,在定义时是不用内存地址的。

如在上面的例子中， name就是一个形参,'zhangsan'是在调用函数时传入的一个实参,它的值被存储在形参name中。

（1）位置实参

在调用函数时，必须将每个实参都关联到函数定义中的每一个形参，最简单的关联方式就是基于实参的位置(顺序)。

>>> def f(a,b,c): #首先在定义函数时传入3个形参a、b、c
>>>     print (a, b, c) #在调用该函数时,通过位置实参的方式,将实参映射到形参,一一对应, 即a=3, b=2, c=1
>>> f(3,2,1)

运行结果：321

需要注意,如果使用位置实参的方式传值,传入的实参个数必须与形参相同.否则运行程序会报错。

（2）关键字实参
关键字实参是通过“关键字=值”的方式传值,就不需要考虑函数调用过程中形参的顺序。
同一个参数不能传两个值。

>>> def f(a,b,c):
>>>     print (a,b,c)
>>> f(a=1,b=2,c=3) #通过“关键字=值”的方式,将实参与形参关联映射,不需要考虑形参的顺序,顺序也可以改变,即a=2, b=3, c=1,运行的结果不会发生改变

运行结果：123

（3）既有位置实参，又有关键字实参

>>> def f(a,b,c):
>>>     print (a,b,c)
>>> f(1,b=2,c=3) #混用两种方式时,位置实参必须放在关键字实参之前,否则运行程序会报错，如 1，b=2，3 或者b=2，1，3 都不可行

运行结果：123

（4）默认值

定义函数时,也可以指定形参的默认值,如果在调用函数时给函数提供了实参, Python将使用指定的实参值;
否则将自动调用形参的默认值。因此,如果给形参指定了默认值,调用时可以不给它传值。使用默认值可以简化函数的调用。

>>> def f(a,b=2): #定义函数时在这里给形参设置了默认值y=2
>>>     print (a,b)
>>> f(1) #在调用此函数时，只传入了一个实参，y的值就会使用默认值

运行结果：12

还可以在调用时更改默认值,如下例所示。

>>> def f(a,b=2):
>>>     print (a,b)
>>> f(1,3) #在调用该函数时,给设置了默认值的形参y再次赋值,运行结果会使用新传入的实参值

运行结果：13

在使用形参默认值时需要注意:在形参列表中必须先列出没有默认值的形参,再列出有默认值的形参。
这使得 Python 依然能够正确地解读位置实参。

在函数调用过程中,可以混合使用位置实参、关键字实参和默认值,但是一定要遵循其中相关的规则,否则会导致程序运行出错。
当提供的实参多于或少于函数定义时所提供的形参时,程序会报错,

如下例所示。

>>> def f(a=2, b):
>>>     print (a,b)
>>> f(1) #这种情况，程序是不允许运行的

（5）列表和字典
当不确定需要传入的值是多少时,在定义形参时,可以使用*args (列表)、**kwargs (字典)来表示。

例 1

>>> def f(*args,**kwargs): #使用*args代表列表，使用**kwargs代表字典，这种形式可以在调用函数时传入多个实参
>>>     print (args)
>>>     print (kwargs)
>>> f(*[1,2,3,4,5], **{"y" : 1}) #如果想让传入的值以列表或字典的形式显示出来,就需要在元素前加上*或**

运行结果：(1, 2, 3, 4, 5){'y': 1}

例 2

>>> def f(*args,**kwargs):
>>>     print (args)
>>>     print (kwargs)
>>> f(11,2,3,4,5],{"y":1}) #[1,2,3,4,5],("y":1)被传给args

运行结果：([1, 2, 3, 4, 5], {'y': 1}){}

例3

>>> def f(*args,**kwargs):
>>>     print (args)
>>>     print (kwargs)
>>> f(1,2,3,4,5,y=1) #y=1作为键值对被传给kwargs

运行结果：(1, 2, 3, 4, 5){'y': 1}

思考
函数的定义必须在主程序调用语句之前出现。对于不带参数的函数,输入并运行以下代码。

>>> def pr():
>>>     print (pr ()
>>>     print ('welcome! ')
>>> pr()

对于带参数的函数,输入并运行以下代码。

>>> def rt (a):
>>>     for n in range (a):
>>>         for m in range(n+1):
>>>            print ('*', end='')
>>>         print ()
>>> while True:
>>>     b= input ('input Line:')
>>>     if b=='0':
            break
>>>     c=int(b)
>>>     rt (c)


3. 匿名函数

匿名函数使用关键字lambda,冒号之前的部分表示匿名函数的参数列表,冒号之后的部分表示匿名函数的返回值,
但是请注意,这部分只能为表达式,不能为赋值语句,否则会出现“can't assign to lambda”错误。

匿名函数不需要用return来返回值,表达式本身的结果就是返回值。在定义匿名函数时,需要将它直接赋值给一个变量,
然后再像一般函数一样调用。


17.3.2 易错点

(1)函数的参数传递是本节重点,知识点容易混淆,要重点学习。
(2)函数的定义必须在主程序调用语句之前出现,这是由Pyhton是解释性语言的特性决定的。


17.3.3 模拟考题

考题1单选题

以下选项中,哪一个不属于函数的作用? (

A. 提高代码的执行速度
B. 提高代码的重复利用率
C. 增强代码的可读性
D. 降低编程的复杂度

答案：A

解析:函数能够提高代码的重复利用率,增强代码的可读性,降低编程的复杂度,但提高代码的执行速度不是它的特点。

考题2单选题

关于计算圆面积的匿名函数的定义,以下哪一个语法格式是正确的?
A. lambda r:3.1415926*r*r
B. result=lambda r:3.1415926*r*r
C. lambda r,3.1415926*r*r
D. result=lambda r,3.1415926*r*r

答案:B

解析:关键字lambda表示匿名函数,冒号之前表示的是这个函数的参数,冒号之后表示的是返回值。
定义匿名函数时,要将它赋值给一个变量。

考题 3 判断题

代码：

myFun=lambda a,b=2:a*b
print (myFun (4))
print (myFun (5,3))

运行结果为：
8
15

答案：正确

解析:本题考核匿名函数的定义、使用方法以及默认参数。
本题中采用了两种方式来调用匿名函数myFun,第一个myFun(4)只传入一个实参,a被赋值为4,b就使用默认值2,
所以myFun(4)的结果是4×2=8; 第二个myFun(5,3)传入两个实参, a被赋值为5, b的默认值2被替换为3,
所以myFun(5,3)的结果是5×3=15

'''