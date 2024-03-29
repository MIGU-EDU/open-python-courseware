"""
15.6冒泡排序

15.6.1知识点译解

1.冒泡排序的概念
冒泡排序是在一列数据中把较大(或较小)的数据逐次向右推移的一种排序技术。
冒泡排序是最简单的排序方法,分为内外两层循环。

外层循序代表的是总共要跑的遍数,2个数据比较一遍。3个数据比较两遍,以此类推,n个数据就跑n-1遍。
内层循环真正比较数据大小,每次比较都会将大的数据放到后面(以升序为例)。

冒泡排序过程容易理解,每一遍加工都是将本遍最大(或最小)的数据移动至本遍的右端位置。
每个数如同水中的气泡一样,小的气泡上升,被排到最上面;而大的气泡被依次排在下面,这样的过程我们比喻成“冒泡”。
冒泡排序有多种变式。

2.冒泡排序的基本思想(以升序为例)

依次比较相邻的两个数,将小数放在前面,大数放在后面。
第一遍从第1个元素开始,让它和第2个元素进行比较,若出现反序(大数在前,小数在后)则交换;
然后让第2个元素和第3个元素进行比较,若出现反序则交换;依次类推,直到比较完最后一对元素为止。
第一遍排序结束时,最后一个元素为所有元素中的最大值。

接下来进行第二遍排序。从第1个元素开始,让它和第2个元素进行比较,若出现反序则交换;
然后让第2个元素和第3个元素进行比较,若出现反序则交换;依次类推,直到比较完最后一对元素(即倒数第二对数)为止。
这样,倒数第二个数为第二大的数。

…………

n个数排序共需进行n-1遍。

Python编程门门与法进阶

实例模拟:
5 8 4 3 7
(5,8) 4 3 7 将5和8比较,不交换位置。
5 (4,8) 3 7 将8和4比较,交换位置。
5 4 (3,8) 7 将8和3比较,交换位置。
5 4 3 (7,8) 将8和7比较,交换位置,8被调到了末尾。

3.冒泡程序框架(伪代码)

for i (0 ~ n-1) #共进行n-1遍排序
    for j (0 ~ n-1-i) #第i遍排序
        if数据对反序,则:
            交换数据对

4.冒泡程序的实现(升序)

a=[1, 3, 2, 5, 8, 7, 6]
count = len (a)
for i in range (0, count-1):
    for j in range (0, count-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print (a)
运行结果:
[1,2,3,5,6,7,8]

若要将列表中的元素降序排序,该如何修改程序?
只需将代码:
if a[j] > a[j+1]:
修改为:
if a[j] < a[j+1]:

思考题

(1)某书店在5所学校的流动售书量(单位为本)分别是80、125、64、68、46。
采用冒泡排序对其进行升序排序,完成第二遍时的结果是().

(2)有一组原始数据: 23、25、18、63、84、77、65、9、33、17。
利用冒泡排序算法进行从小到大排序,最多需要进行()次加工,才可以完成整个数据的排序.

A. 5 B. 6 C. 8 D.9

15.6.2易错点
(1)理解冒泡排序的算法原理。
(2)交换元素的本质就是变换索引号。

15.6.3 模拟考题

考题1 选择题

主持人大赛的成绩排名,可以采用的算法是()。
A.解析算法 B.枚举算法 C.排序算法 D.查找算法
答案: C
解析:成绩排名问题符合用排序算法解决的问题特征。

考题2 编程题
在一列表中产生n(n>=10)个50以内的数据,删除其重复数据并按照升序排序输出,同时输出删除数据个数。
例如输入: n=10
随机产生a=[1,2,3,7,4,7,3,8,5,7]
输出: a=[1,2,3,4,5,7,8]
输出:共删除数据为3个
请编写程序实现上述功能。

import random
max = int (input ("请输入要产生的数据个数: "))
①
for i in range(max):
    a.append(random.randrange(1, 50, 1))

print("原始数据: ")
print(a)

key, n = 0, max
while key < n:
    i = n - 1
    while ②
        i = i - 1

    if i == key:
        key = key + 1
    else:
        a.remove(③)
        n = n - 1

for i in range (n):
    for j in range (len(a) -1, i, -1):
        if a[j] < a[j-1]:
            a[j],a[j-1] = ④

print("去重后排序数据: ")
print(a)
print("共删除数据: ", ⑤,"个")

评分标准:
① a = [](3分)
② a[i] != a[key] (4分)
③ a[i] (3分)
④ a[j-1],a[j] (3分)
⑤ max - n (3分)
"""
