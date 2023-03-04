"""
第4课 turtle 库

4.1 学习要点

turtle库的综合应用，利用turtle绘制各种不同的图形。

4.2 对标内容

（1）会用turtle库完成简单的顺序执行的Python程序，能够解决较为简单的问题。
（2）会编写含有变量及库文件的基本程序。
（3）具备用计算思维的方式解决简单的问题能力。
（4）知道第三方库turtle的功能，会导入该库文件，掌握它的一些简单使用方法。

4.3 情景导入

如果你认为Python只能做那些冷冰冰的数据处理，那你就错了，Python也可以做很多有趣的事情，
比如同学们最喜欢的画画，Python也非常“擅长”，它甚至可以绘制出一幅与众不同的画作。
那Python笔下的画作是什么样的呢？让我们拭目以待吧！


4.4 turtle 的坐标系

turtle的坐标系有两个：一个是画布在整个屏幕中的坐标系，另一个是画笔在整个画布中的坐标系。

4.4.1 知识点详解

1．画布在屏幕中的坐标系

画布在屏幕中的坐标系如图4-1所示。
图4-1 画布在屏幕中的坐标系

画布的（0,0）坐标位于屏幕的左上方。
最小单位为像素。

setup()设置画布大小及位置，格式为：turtle.setup（width，height，startx，starty)。
setup()的参数：第一个为画布长度，第二个为画布高度，第三个为画布起始的x坐标，第四个为画布起始的y坐标。

setup()不是必需的，只有当需要改变画布大小或者坐标位置的时候使用；如果没有设置setup()
直接使用 turtle进行绘图，画布默认的大小尺寸为800像素x600像素，并且位于屏幕的正中央。

setup()的4个参数，可以没有坐标信息，甚至可以连4个参数都没有。如果4个参数都没有，则按照默认尺寸和位置进行设置；
setup()前两个参数可以使用小于等于1.0的小数表示，代表的是画布的大小占整个屏幕尺寸的比例。
比如 setup（1.0,1.0）代表的是按屏幕尺寸（宽和高）100％的比例进行设置，setup（0.5,0.5）代表的是按屏幕尺寸的50％比例缩小画布。

2．画笔在画布中的坐标系
画笔在画布中的坐标系和画布在屏幕中的坐标系是不一样的，最大的不同是画布的正中心是坐标系的原点（0,0）

图4-2 画笔在画布中的坐标系

由图4-2我们可以看出来，这就是标准的xOy坐标系，横坐标为x，纵坐标为y，原点O的坐标为（0,0）。
对应的命令：turtle.goto（x，y），作用为让小海龟走到指定的坐标。
turtle.goto（x，y）的单位为像素。


4.4.2 易错点

（1）两个坐标系的原点位置不同，要注意是在设置哪个坐标系。
（2）setup（）不是必需的，默认的画布尺寸为800像素x600像素，而并非400像素x300像素。

4.4.3 模拟考题

考题1 单选题

以下哪个turtle库中的指令不会使小海龟发生位置移动变化的？（ ）
A.在turtle库中的指令forward（）
B.在turtle库中的指令goto（）
C.在turtle库中的指令 setup（）
D.在turtle库中的指令 home（）

答案：C

解析：A为让小海龟前进，B为让小海龟到达指定的坐标，
C为设定画布的大小，D为让小海龟回到原点，所以只有C不会使小海龟发生移动。

考题2 单选题

在turtle库中，用于将画笔移动到坐标(x,y)）的命令是（）。
A.turtle.go(y,x)
B.turtle.go(x,y)
C.turtle.goto(x,y)
D.turtle.goup(x,y)

答案：C
解析：这道题很具有迷惑性，go和goto很像，但是，在turtle库中，只有goto函数，所以答案是C。


4.5 turtle 的画笔体系

4.5.1 知识点详解

1．画笔的命名

在turtle中可以有多支画笔，但是每一支画笔都必须要有自己独有的名字，如果只有一支画笔，则不需要命名。
画笔命名函数：turtle.Pen（）；格式为pen1=turtle.pen()，前面的 pen1 为画笔的名称。
命名画笔后，该画笔的所有函数均需要在前面加上画笔名称，不能再使用默认的turtle前缀。

2．画笔设置函数

(1)turtle.pensize(a)
作用：设置画笔的粗细。
参数：a代表画笔的像素数。
特别说明：画笔设置粗细只改变设置后的绘图，设置前已经绘制的图形不改变。

(2) turtle.penup()
作用：抬笔。
参数：无。
特别说明：抬笔后，画笔的所有操作及移动都不会在画布上留下痕迹。

(3) turtle.pendown()
作用：让画笔落下。
参数：无。
特别说明：画笔落下后，才能够绘制相应的图形。

(4) turtle.hideturtle()
作用：隐藏小海龟，表示不显示小海龟。
参数：无。
特别说明：隐藏并不影响小海龟的绘图，即隐藏后小海龟还是可以绘图的。

(5) turtle.showturtle()
作用：显示小海龟。
参数：无。

(6) turtle．shape（）和 turtle.Turtle（）
作用：设置小海龟的形状。
参数：括号里面只能填海龟形状，在turtle中，小海龟的形状只有6种，
分别为"arrow" "turtle" "circle" "square" "triangle"＂和"classic"。
特别说明：默认小海龟形状为＂classic"；参数为字符串，所以须要加引号，例如 turtle.shape('arrow')

(7) turtle.write(arg,move=false,align='left', font=('arial',8,'normal'))
作用：在小海龟当前位置书写文字。
参数：arg为需要书写的文字信息；move为可选参数，如果move为True，则笔将移动到右下角；
align为可选参数，只能是字符串"left"t”（左）、r＂（中）或＂right＂（右）之一，表示字符的对齐方式；
font为可选参数，表示所要使用的字体。特别说明：turtle.write（）是将文字显示在绘制的画布上，不是显示在IDLE的交互环境里。

3．与颜色相关的设置

(1)turtle.pencolor(color)
作用：设置画笔的颜色。
参数：color代表的是画笔颜色。
特别说明：参数color有两种表示方式：第一种为字符串形式，内容为颜色的英文，字母用小写的，
如“green""red"；第二种为RGB三元组值形式，RGB是工业界的一种颜色标准，是指红、绿、蓝3种颜色的数值，数字越大，该颜色越深，
如 turtle．pencolor（255,255,255）代表的是黑色。但是在使用RGB三原色时，
需要在前面加上turtle．colormode（255）将颜色设定为RGB模式。

(2)turtle.color(color1,color2)
作用：同时设置画笔及填充的颜色。
参数：第一个参数color1代表的是画笔颜色，第二个参数color2代表的是填充颜色。
特别说明：如果只有一个参数，则代表该颜色既是画笔颜色也是填充颜色。参数color1和color2均可以使用RGB模式表示。

(3) turtle.fillcolor(color)
作用：设置填充颜色。
参数：color代表是填充颜色。
特别说明：填充颜色需要在开始填充前进行声明才有效。参数可以使用RGB模式表示。

(4) turtle.begin_fill()
作用：设置填充的起始点，表示开始填充。
参数：无。
特别说明：开始填充必须和结束填充成对配合使用。

(5) turtle.end_fill()
作用：设置填充的终点，表示结束填充。
参数：无。
特别说明：结束填充必须和开始填充成对配合使用。

(6) turtle.bgcolor(color)
作用：设置画布的背景颜色。
参数：color为背景颜色的文本名或RGB数值。

4.5.2 易错点
（1）命名多支画笔时必须使用turtle．Pen（），命名的格式为a（画笔名）＝turtle.Pen（）。这里要特别注意P要大写。
（2）所有的颜色设置，均可以采用字符串和RGB两种模式，但是在字符串模式下，颜色名称一定要加引号。
（3）所有的颜色设置也可以采用RGB值来表示，虽然这不在等级考试的要求中，但是不能因此就认为使用RGB值表示就是错误的。
（4）turtle．begin＿fill（函数必须在开始绘制需要填充的图形前就声明。
（5）turtle．Turtle（）命令除了可以设置小海龟的形状外，也可以进行多支画笔的设置。


4.5.3 模拟考题

考题1单选题
下面的图形最有可能是哪段代码执行后的效果？（）

A.
import turtle
turtle.pensize(5)
turtle.begin fill()
turtle.color('red')
turtle.fillcolor('yellow')
turtle.circle(50,steps=6)
turtle.end fill()
turtle.hideturtle()

B.
import turtle
turtle.pensize(5)
turtle.color('red')
turtle.begin fill()
turtle.fillcolor('yellow')
turtle.circle(50,steps=6)
turtle.end fill()
turtle.hideturtle()

C.
import turtle
turtle.pensize(5)
turtle.fillcolor('red')
turtle.begin fil1()
turtle.color('yellow')
turtle.circle(50,steps=6)
turtle.end fill()
turtle.hideturtle()

D.
import turtle
turtle.pensize(5)
turtle.begin fill()
turtle.color('red', 'yellow')
turtle.circle(50,steps=6)
turtle.end fill()
turtle.hideturtle()


答案：C

解析：我们可以看出这是绘制一个正六边形，并且画笔颜色和填充颜色都是黄色。
A、B选项都是先设定了画笔颜色和填充颜色为红色(turtle.color('red'))），
随后在填充时又声明了填充颜色为黄色（turtle.fillcolor（＇yellow＇））；
语句都放到了 turtle.begin＿fill（）里面，所以画笔颜色为红色；fillcolor('yellow')
D选项直接设定画笔颜色为红色，填充颜色为黄色，所以也不符合题目要求；
只有C选项虽然开始设定的填充颜色为红色，但是随后又设定填充颜色和画笔颜色均为黄色，所以C选项符合题目要求。


考题2 单选题

运行下面的程序后，画布上会出现几只小海龟？()

import turtle
tl=turtle.Turtle ('turtle')
t2=turtle.Turtle('turtle')
t3=turtle.Turtle('turtle')
t4=turtle.Turtle('turtle')
t1.forward(50)
t2.forward(100)
t3.forward(150)
t4.forward(200)

A.0
B.1
C.4
D.5


答案：C
解析：程序中的t1=turtle.Turtle.Turtle（＇turtle＇）就是在设置turtle不同画笔的名称，
本题中有t1、t2、t3、t4这4支画笔，所以选择C。

"""