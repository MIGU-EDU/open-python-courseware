"""

15.4 解析算法

15.4.1 问题引入
用基姆拉尔森公式计算某天是星期几。

W= (D+2*M+3* (M+1 ) /5+Y+Y/4-Y/100+Y/400) mod 7

Y表示年,是4位数,如2022; M表示月,D表示日。

注意: (1)该公式中要把1月和2月分别当成上一年的13月和14月处理,
例如:2022年1月4日要换成2021年13月4日代人公式。

(2)该式的运算中结果与星期几的对应关系为,0代表星期日,
1代表星期一 6代表星期六。

15.4.2 知识点详解

1.解析算法的概念
(1)解析:用数学公式描述客观事物间的数量关系。
(2)解析算法:用解析的方法找出表示问题的前提条件与结果之间关系的数学表达式,
并通过表达式的计算来实现问题的求解。

例如:计算以速度v作匀速直线运动的一个物体,在t秒内经过的距离s,
则可通过公式s=vt得到。

2.解析算法的程序实现

(1)建立正确的数学模型(得出正确的数学计算式)。

(2)将数学表达式转换为Python表达式。
用Python编制解析算法程序时,必须保证计算过程描述的正确性。
特别是把数学表达式转换成Python表达式时,必须注意这种转换的正确性,
否则容易发生运算结果错误或运行过程出错的情况。

思考题

(1)计算长方体体积的算法描述如下。

①输入长方体的长(z)、宽(w)、高(h)。
②计算长方形体积v= zwh。
③输出结果。
④结束。

上述算法属于( )。
A.枚举算法
B.排序算法
C.解析算法
D 递归算法

(2)下列问题适合用解析算法求解的是()。

A.将13张纸牌按从小到大进行排列
B.统计100以内各位数字之和恰好为10的偶数的个数
C.计算一辆车行驶100千米的油耗
D.寻找本年级身高最高的同学

(3)有如下问题:

①已知圆锥体的半径r和高度h,使用公式V= mrh求出此圆锥体的体积。
②已知班级中每位同学的期中考试成绩总分为s,
按照s的值从大到小的顺序进行成绩排名。
③已知圆的周长s,利用公式r= s/(2m)求半径r。

属于解析算法的选项是()。
A. ①2 B. ①3 C. 3④ D 2④

(4)出租车计价规则:3千米以内,收费10元;超出3千米,每千米多收2元。
假定千米数为x,收费金额为y。解决此问题的公式和流程图如下图所示。

流程图加框处部分的算法属于()。

A.解析算法 B.排序算法 C.枚举算法 D.递归算法

例题

某书店出租图书的费用标准如下:借书一天内,收费2元;借书超过一天的,
超过部分按每天0.8元收取。最后费用按四舍五入折算成整数。程序算法如下图所示。

n = eval (input ('输入借书天数:'))
if not n < 1:
    if n = 1:
        S = 2
    else:
        S = 2+ (n-1) * 0.8
    print ('费用(元): ',s)
else:
    print ('输入有误! ')

15.4.3 易错点

(1)将数学表达式转为Python表达式时,可能会把运算符、运算顺序写错。
(2)要留意分支结构的解析算法。


"""