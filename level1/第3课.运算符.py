"""
第三课、运算符

3.1 学习要点

（1) Python 的4种运算符：算术运算符、赋值运算符、比较运算符、逻辑运算符
（2）运算符的优先级。

3.2 对标内容

（1）掌握并熟练编写带有数值类型变量的程序，具备解决数学运算基本问题的能力。
（2）理解比较表达式、运算符、逻辑运算的基本概念，掌握 Python 编程基础的逻辑表达式。
（3）学会使用算术运算符（+、-、*、/)、赋值运算符（=）、比较运算符（==、<、>、<=、>=、!=）、逻辑运算符（and、or、not），知道运算符的优先顺序。

3.3 情境导入

计算机编程最早是为了解决数学问题而发明的。宽泛地说，我国古代的算盘也是一种计算器，只不过这种计算器不是用电的，所以不能称为电子计算机。
计算机编程始终是和数学紧密结合的，特别是人工智能时代的编程，大部分是对数据的处理和挖掘，这些都离不开数学。
所以，学好数学对学习编程有着非常重要的帮助；反过来，学习编程也有利于学习数学。

3.4 算术运算符

3.4.1 如识点详解

Python中的算术运算符一部分和我们数学中的算术运算符一致,但是也有一部分很不相同,具体如下所示。


名称   |   数学中的运算符   |   Python的运算符   |   在Python中的作用
---------------------------------------------------------------------------------------
加              +                 +              把两个对象相加
---------------------------------------------------------------------------------------
减              -                 -              把两个对象相减
---------------------------------------------------------------------------------------
乘              ×                 *              把两个数相乘或是返回一个被重复若干次的字符串
---------------------------------------------------------------------------------------
除              ÷                 /              把两个对象相除,商是小数(哪怕能整除,也保留一位小数)
---------------------------------------------------------------------------------------
取整除                             //             取两个数相除的商(整数)
---------------------------------------------------------------------------------------
取模                              ％              取两个数相除的余数
---------------------------------------------------------------------------------------
幕                                **             取x的n次方的结果
---------------------------------------------------------------------------------------

Python中的加和乘可以用于字符串类型运算,但是其他运算符不能用于字符串类型。
在Python中有两个运算符在小学数学中是没有的,一个是取整除,一个是取模,这两个运算其实都是数学除法运算在Python中的补充。
算术运算符的运算规则和顺序是和数学中的四则混合运算的规则和顺序一致的。

3.4.2 易错点

(1)取整除(//)是向下取整,不是四舍五入,也可以理解为去掉余数。比如:24//5的结果4,并不是5。
(2)取模(%)是取两个数相除的余数,如果能整除,则取模结果为0。


3.4.3 模拟考题

考题1 单选题

a=2, b=3,那么c=a**b运算的结果是?

A. 6 B.8 C.9 D. 23

答案: B
解析:**在Python中代表的是幕运算,相当于数学中的2^3,也就是3个2相乘,所以结果是8,选B。


考题2 单选题

执行(2*3)/(9-3*2),输出的结果是什么?

A. 1 B. 2.0 C.2 D. 1.0

答案: B
解析:根据数学运算的规则,题目中的算式可以写成6÷3。虽然6÷3确实等于2,
但是在Python中,如果能除尽,系统会自动保留一位小数,所以正确的应该是2.0而不是2,所以B正确。

考题3 单选题

print(46//8)的结果是?
A. 5  B. 6  C. 5.0  D. 5.75

答案: A
解析: //在Python中是取整除运算符,其作用是取两个数相除的商(整数),舍弃余数。
本题中,46除以8的商是5,所以选择A。这里特别要提醒大家,取整除运算的结果是没有小数点的,所以C也是错误的。

考题4 单选题

要抽出一个三位数(如479)的个位上的数字,输入以下哪段代码可以获得其中的个位数上的9?

A. print(479%10//10)
B. print(479//10//10)
C. print(479%10%10)
D. print(479//10%10)


答案: C
解析:要取三位数的个位上的数字,其实最简单的方法就是求这个数除以10的余数,但是题目中并没有479%10的选项。
我们经过观察就可以看出, A和C比较符合,那么我们来看A选项,它可以转化为9//10(9整除10),结果为0;
C选项可以转化为9%10(9取模10),结果为9,所以选择C。当然,我们也可以计算一下其他两个选项,B的结果为4;D的结果为7。
其实通过这道题,我们也可以学会怎么拆分一个三位数。


3.5 赋值运算符

3.5.1知识点详解

在数学运算中,赋值运算只有一种,就是等于(=);但是在Python中,却有很多种赋值运算,如表3-2所示。


    运算符   |          描述           |      举例      |      作用
----------------------------------------------------------------------
      =          最常见的数学赋值运算          a = 5        把5赋值给a
----------------------------------------------------------------------
     +=            加法赋值运算符             a += b       相当于a = a+b
----------------------------------------------------------------------
     -=            减法赋值运算符             a -= b       相当于a = a-b
----------------------------------------------------------------------
     *=            乘法赋值运算符             a *= b       相当于a = a*b
----------------------------------------------------------------------
     /=            除法赋值运算符             a /= b       相当于a = a/b
----------------------------------------------------------------------
     %=            取模赋值运算符             a %= b       相当于a = a%b
----------------------------------------------------------------------
     **=            幂赋值运算符             a **= b       相当于a = a**b
----------------------------------------------------------------------
     //=            取整除赋值运算符          a //= 5       相当于a = a//b
----------------------------------------------------------------------

除了等号(=)运算符,剩余的运算符都是相应算术运算符的简写。

3.5.2 易错点
除了用等号赋值之外,其余的赋值方式在数学中是没有的,所以除了等号外都是易错点。

3.5.3 模拟考题

考题1 单选题

已知变量a=2, b=3,执行语句a%=a+b后,变量a的值为()

A. 0  B. 2  C. 3  D. 12

答案: B
解析:该题主要的考核点就是取模赋值,根据取模赋值的公式,a%=b相当于a=a%b,
可以将考题中的语句a% = a+b中的a+b作为一个整体参与取模赋值,
所以原算式可以等价于a= a%(a+b),根据题目给的变量值,可以代人数值a= 2%(2+3),结果为2,所以答案为B。

考题2 单选题

已知变量a=5, b=6,执行语句a*=a+b后,变量a的值为( )。

A. 11 B. 30 C. 31 D. 55


答案: D
解析: 根据 *= 运算符的运算规则, a *= a + b 可以转换为 a = a * (a + b),将a、b的值代入算式,
可得到 a = 5 *(5 + 6),结果为55,所以正确答案是D。


3.6 比较运算符

3.6.1 知识点详解

比较运算符又称为关系运算符,其最大的特点就是返回值只有两种:True或者False
比较运算用于对常量、变量或表达式的结果进行大小比较,如果这种比较是成立的,则返回True (真),反之则返回False (假)。

Python中常用的比较运算符如下所示。


    比较运算符      |     名称      |               说明
--------------------------------------------------------------------------------------------------------------
       >                大于          如果>前面的值大于后面的值,则返回True,否则返回False
--------------------------------------------------------------------------------------------------------------
       <                小于          如果<前面的值小于后面的值,则返回True,否则返回False
--------------------------------------------------------------------------------------------------------------
       ==               等于          如果== 两边的值相等,则返回True,否则返回False
--------------------------------------------------------------------------------------------------------------
       >=               大于等于       等价于数学中的≥,如果>=前面的值大于或者等于后面的值,则返回True,否则返回False
--------------------------------------------------------------------------------------------------------------
       <=               小于等于       等价于数学中的≤,如果<=前面的值小于或者等于后面的值,则返回True,否则返回False
--------------------------------------------------------------------------------------------------------------
       !=               不等于         等价于数学中的≠,如果!=两边的值不相等，则返回True,否则返回False
--------------------------------------------------------------------------------------------------------------
       is                是           判断两个变量所引用的对象是否相同,如果相同则返回True,否则返回False
--------------------------------------------------------------------------------------------------------------
       is not           不是          判断两个变量所引用的对象是否不相同,如果不相同则返回True,否则返回False
--------------------------------------------------------------------------------------------------------------


3.6.2易错点

1. == 和 =

在编程中,经常会出现将 == 误写成 = 的情况，因为我们习惯将口头上的“等于”写成 =，但是我们口头上的“等于”可能有两种意思:
一种是将一个值赋值给另外一个变量、这时候,使用 = ; 而有时候我们所说的“等于”表示的是比较两个对象是否相等、这时候,要使用 == ,

如下所示。

>>> a = 5 #把5值给a，返回值是5
>>> a == 5 #看 a是否和5 相等，返回值只有True 或者 False

2. == 和 is 的区别

初学Python,大家可能对is比较陌生,很多人会误将它和 == 的功能混为一谈,但其实is与 == 有本质上的区别,完全不是一码事儿:
== 用来比较两个变量的值是否相等，而is则用来比对两个变量引用的是否是同一个对象，如下所示。

>>> a = [5,2]
>>> b = [5,2]
>>> print (a == b)
True
>>> print (a is b)
False

通过上面的案例我们可以看出，a和b的值虽然是相等的，但是，a并不是b。


3.6.3模拟考题

考题1单选题

执行语句 print(10==10.0),结果为()。

A. 10
B. 10.0
C. True
D. False


答案: C

解析：本题的考核点主要在于=和==的区别，=是赋值运算符，而==是比较运算符,10和10.0是相等的,所以返回值是True。

考题2单选题

下列代码的运行结果是

a=0
b=False
print (a==b)

A. 0
B. False
C. True
D. error

答案:C

解析:本题有两个考点,一个是对比较运算符==的理解和应用、还有一个就是对False和0的关系的考核。
在Python中,0和空都是False,所以,False是和0相等的,本题的答案是C。



3.7 逻辑运算符

3.7.1 知识点详解

Python中的逻辑运算符只有3个: and、or和not,如下所示。

    逻辑运算符   |          名称           |            描述
----------------------------------------------------------------------
     and                   与                逻辑与运算，等价于数学中的“且”
----------------------------------------------------------------------
     or                    或                逻辑或运算，等价于数学中的“或”
----------------------------------------------------------------------
    not                    非                逻辑非运算，等价于数学中的“非”
----------------------------------------------------------------------

Python中的逻辑操作符 and 和 or,也叫惰性求值,就是从左至右解析。由于它们是惰性的,只要确定了值,就不往后解析代码。

逻辑or运算，是True惰性求值：只要第一个值是True或非0,整条指令为True或非0,后面就不再做运算;
反之,如果第一个是False,后面不管是True还是False,都是返回后面的值。

逻辑and运算，是False惰性求值：只要第一个值是False,结果就是False,后面的就不需要运算了,无论后面是True还是False;
反之,如果第一个值是True,直接返回后面的值。

逻辑not运算,是将之前的值进行翻转,之前的值是True,运算后变成False;
之前的值是False,运算后变为True。

3.7.2 易错点

and运算是False惰性求值,所以只要前面的值是False,则不需要看后面的值。
or运算是True惰性求值,所以只要前面的值是True或者非0,则不需要看后面的值。
在Python中, True不仅仅是1,只要是非0及非空的对象都被认为是True,所以and,or的返回值不一定只有True和False,

如下所示。
>>> print (123 or 22 )
123
>>> print (23 and "abc")
abc

3.7.3模拟考题

考题1单选题

假设 a=20, b=3,那么 a or b 的结果是

A. 20
B. False
C. True
D. 3

答案: A

解析:根据Python的or运算的规则，如果or前面的值为True,则整个运算的值为前面的值，否则为后面的值;
20是非0的，所以为True,返回值自然是20。这里最容易搞错的是以为返回值是True, Python的逻辑运算or和and返回的值,
只有前或者后运算中的结果确实是True时才返回True。

考题2单选题

已知x=5, y=6,则表达式not(x!=y)的值为

A. True
B. False
C. 5
D. 6

答案:B

解析：根据题目信息，我们可以将not(x!=y)修改为not(5!=6),5 确实不等于6,所以 5!=6 返回的值为True,
但是由于前面加了not进行翻转,所以not(5!=6) 的结果为False,应选择B。



3.8 运算符的优先级

3.8.1 知识点详解

所谓优先级，就是当多个运算符同时出现在一个表达式中时，先执行哪个运算符。
我们已经学过的Python运算符的优先级如下所示。


    运算符说明   |            Python运算符            |         优先级     |        优先级顺序
-------------------------------------------------------------------------------------------------
     小括号                    （）                              8                   高
-------------------------------------------------------------------------------------------------
     乘方                      **                               7                   |
-------------------------------------------------------------------------------------------------
     乘除                   *、/、//、%                          6                   |
-------------------------------------------------------------------------------------------------
     加减                      +、-                             5                   |
-------------------------------------------------------------------------------------------------
    比较运算符            ==、!=、>、>=、<、<=                     4                   |
-------------------------------------------------------------------------------------------------
    逻辑非                     not                              3                    |
-------------------------------------------------------------------------------------------------
    逻辑与                     and                              2                    |
-------------------------------------------------------------------------------------------------
    逻辑或                     or                               1                    低
-------------------------------------------------------------------------------------------------



3.8.2易错点


运算符除了要考虑优先级之外，还需要考虑运算符的结合性，所谓结合性,就是当一个表达式中出现多个优先级相同的运算符时,先执行哪个运算符:
先执行左边的叫左结合性,先执行右边的叫右结合性。比如1000/ 25 * 16,由于乘除是同一级别运算符,那是先算哪一个呢？

根据四则混合运算的原则,我们学习过的运算符多数属于左结合性(即先算左边的),只有幂(**)、逻辑非(not)是右结合性。

Python逻辑运算返回为True时，值不一定是True或者1,而可以是表达式的值,这一点与其他编程语言有很大的区别,我们一定要注意。

3.8.3 模拟考题考题

1单选题

在下面的运算符中，按照运算优先级，哪一个是最高级？

A. **
B. *
C. +
D. //


答案: A

解析:本题主要考核运算符的优先级,题目中比较幂(**)、乘(*)、加(+)、整除(//)这4个运算符的优先级，
显然，优先级最高的是幂运算，其次是乘和整除，最低的是加,因而答案是A。


考题2单选题

假设a=2, b=1, c= a and b-1,那么c的值是

A. 3
B. 1
C. 2
D. 0

答案: D


解析:首先、由于本题涉及多个运算符的运算，所以先要看这些运算符的优先级，题目中涉及=、and、-这3种运算符，
由于=是赋值运算符，并非是比较运算符==、所以只剩下and和-两种运算符，根据规则，-运算符的优先级要高于and,
所以先算-、原算式可以改为c = 2 and (1-1), 即c = 2 and 0;根据and的运算规则,我们可以得出c=0,所以选择D。


考题3单选题


print(2*3 > 4*2 or 121>12 and 7 % 3 == 4 %3) 的结果是

A. False
B. True
C. 3
D. 4


答案: B


解析:这是一个典型的运算符优先级的考题,由于整个计算里涉及的运算符比较多,我们根据优先级进行分步计算。
根据规则,题目中的*(乘)和%(取模)属于该式中的最高级运算符,优先进行计算,这样我们可以将原式改为6>8 。
r121>12 and 1==1;接下来，比较运算符是最高级的，需要先进行计算，则原式可以改为(6 > 8) or (121 > 12) and (1 == 1),
经过计算，算式又进一步演变为False or True and True;

接下来， or和 and运算， and 的优先级高，先进行计算,原式可以改为False or (True and True),
即 False or True;根据 or 的运算规则，前面的为False,则结果是or后面的值，所以答案是True,选择B。
"""
