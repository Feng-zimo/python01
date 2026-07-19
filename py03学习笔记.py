# 数据类型学习

# int 整数类型
a = 1
a = -1

# float 浮点类型
b = 1.1

# str 字符串类型
c = "1"

# bool 布尔类型
d = True
e = False

# None 空类型
f = None

# 检测数据类型
print(type(a))  # 输出：<class 'int'>
print(type(b))  # 输出：<class 'float'>
print(type(c))  # 输出：<class 'str'>
print(type(d))  # 输出：<class 'bool'>
print(type(e))  # 输出：<class 'bool'>
print(type(f))  # 输出：<class 'NoneType'>

# 变量命名规则
# 变量名由字母、数字、下划线组成
# 变量名不能以数字开头
# 变量名区分大小写
# 变量名不能是关键字

# 关键字有
"""
    and, as, assert, break, class, continue, def, del, elif,
    else, except, False, finally, for, from, global, if, import,
    in, is, lambda, None, nonlocal, not, or, pass, raise, return,
    True, try, while, with, yield
"""

# 布尔值可以当做整数类型对待，True相当于1，False相当于0
print(True + 1)  # 输出：2
print(False + 1)  # 输出：1
print(True + False)  # 输出：1

# True要严格区分大小写，t一定要大写
# true会被当做变量名，而不是布尔值

# complex，复数类型
# 固定写法 z = a + bj
z = 1 + 2j
print(type(z))  # 输出：<class 'complex'>
ma = 1 + 2j
ma1 = 2 + 3j
print(ma + ma1)  # 输出：(3+5j),复数相加，实部和虚部分别相加
print(ma - ma1)  # 输出：(-1-1j),复数相减，实部和虚部分别相减
# 只能是j，否则报错，必须是小写j


# =====================================================================
# 详细讲字符串类型
# 字符串str，需要加上引号，"'都可以，包含多行内容可以使用三引号
# name= sixstar,应该是" sixstar "
name = ' sixstar '
name = " sixstar "
name = """ sixstar """
# 都可以

# 3引号可以包含多行内容
name = """很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
    很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长

"""

# 也可以用3引号做多行注释
"""
多行注释，不需要变量名


"""

# =====================================================================
# 占位符的作用:格式化字符串
# 占位符的三种方式：%，format，格式化f

# 最常用的是%s，%s是字符串占位符
"""
    %s,代表字符串占位符（最常用）
    %d,代表整数占位符
    %f,代表浮点数占位符
    %x,代表十六进制占位符（小写字母）
    %X,代表十六进制占位符（大写字母）
    %o,代表八进制占位符
    %e,代表科学计数法占位符（小写e）
    %E,代表科学计数法占位符（大写E）
    %c,代表字符占位符（单个字符）
    %r,代表repr()占位符
    %%,代表输出一个%号本身（转义）
    注意：Python中没有%b、%B、%O这些占位符
"""

# 占位符只是占据位置，并不会被输出
age = 18
name = "bingbing"
print("我的名字:%s,我的年龄:%d" % (name, age))

# %4d,代表整数占位符，占4个位置
a = 123
print("%4d" % a)  # 输出：  123
print("%2d" % a)  # 输出：123     注意若%ad中a小于后面的变量的位数时，则会输出原数
print("%6d" % a)  # 输出：    123
print("%06d" % a)  # 输出：000123      表示输出的整数显示位数，不足的话用0补足
print("%-6d" % a)  # 输出：123    表示输出的整数显示位数，不足的话用空格补足

# %f,代表浮点数占位符
a = 1.2
print("%f" % a)  # 输出：1.200000      默认输出6位小数
print("%6f" % a)  # 输出：  1.200000      表示输出的浮点数显示位数，不足的话用空格补足
print("%06f" % a)  # 输出：001.200000      表示输出的浮点数显示位数，不足的话用0补足
print("%-6f" % a)  # 输出：1.200000    表示输出的浮点数显示位数，不足的话用空格补足
print("%6.2f" % a)  # 输出：  1.20      表示输出的浮点数显示位数，不足的话用空格补足，且只显示2位小数
b = 2.34567
print("%.3f" % b)  # 输出：2.346 四舍五入，显示3位小数

# %%转义：输出%号本身
print("我是%%的1%%")  # 输出：我是%的1%
# 字符串中有%%时，会被转义为一个%


# =====================================================================
# format()格式化
# 格式："{}".format(变量)
print("我的名字:{},我的年龄:{}".format(name, age))

# 可以通过索引指定位置
print("{0}的年龄是{1},{0}很开心".format(name, age))

# 可以通过关键字指定
print("我的名字:{name},我的年龄:{age}".format(name="小明", age=20))

# format()格式化数字
print("{:.2f}".format(3.14159))  # 输出：3.14，保留2位小数
print("{:>10}".format("hello"))  # 输出：     hello，右对齐，宽度10
print("{:<10}".format("hello"))  # 输出：hello     ，左对齐，宽度10
print("{:^10}".format("hello"))  # 输出：  hello   ，居中对齐，宽度10
print("{:0>5d}".format(42))  # 输出：00042，用0填充，宽度5

# f格式化（f-string，Python3.6+推荐使用）
# 格式：f"{表达式}"
print(f"{name}的年龄是{age}")

# f-string中可以使用表达式
print(f"3年后{name}的年龄是{age + 3}")

# f-string格式化数字
pi = 3.14159
print(f"圆周率：{pi:.2f}")  # 输出：圆周率：3.14
print(f"数字：{42:05d}")  # 输出：数字：00042
print(f"右对齐：{'hello':>10}")  # 输出：     hello


# =====================================================================
# if判断学习
"""
if (条件 A) {
    if (条件 B) {
        动作 1     # A 和 B 同时满足
    } else {
        动作 2     # 仅 A 满足
    }
} else {
    动作 3       # A 不满足
}
"""

age = input("请输入你的年龄：")
if int(age) < 18:
    print("你未成年,不能上网，请离开")
else:
    print("你已成年")
# 一定要加int！否则会报错！

score = input("请输入你的分数：")
if int(score) == 100:
    print("你真棒")
elif int(score) >= 90:
    print("优秀")
elif int(score) >= 80:
    print("良好")
elif int(score) >= 70:
    print("中等")
elif int(score) == 60:
    print("继续努力哈！")
elif int(score) >= 60:
    print("及格")
else:
    print("不及格")
# 注意：条件判断是从上往下执行的，一旦满足某个条件就不会再往下判断
# 所以==60和==100这种精确匹配要放在范围匹配的前面，否则永远不会被执行到


# =====================================================================
# 运算符
"""
    比较运算符：==（等于）, !=（不等于）, >（大于）, <（小于）, >=（大于等于）, <=（小于等于）
    逻辑运算符：and(和), or(或), not(非)
    三目运算符（三元表达式）：条件为真时执行的操作 if 条件 else 条件为假时执行的操作
"""
# ==比较的是两个变量是否相等，相等返回为真，不相等返回为假
# !=比较的是两个变量是否不相等，不相等返回为真，相等返回为假
# >比较的是两个变量是否大于，大于返回为真，小于返回为假
# <比较的是两个变量是否小于，小于返回为真，大于返回为假
# >=比较的是两个变量是否大于等于，大于等于返回为真，小于返回为假
# <=比较的是两个变量是否小于等于，小于等于返回为真，大于返回为假
# and(和)：两个条件都为真时，才返回为真，否则返回为假
# or(或)：两个条件中只要有一个为真时，就返回为真，只有两个条件都为假时，才返回为假
# not(非)：对一个条件取反，如果条件为真，取反后为假，如果条件为假，取反后为真

a = 666
b = 999
print(a == b)  # 输出：False
print(a != b)  # 输出：True
print(a > b)  # 输出：False
print(a >= b)  # 输出：False
print(a <= b)  # 输出：True
print(a < b)  # 输出：True

if a < b:
    print("a<b")

a = 666
if a == 999:
    print("a=999")
else:
    print("a!=999")


# =====================================================================
# 循环
# while 循环, for循环，break，和continue
# if 只有一次判断，while可以一直执行判断
# while 条件：
#     循环体
#     改变变量

# while循环的执行流程：先判断条件是否满足，如果满足就执行循环体，
# 然后改变变量，再次判断条件是否满足，以此类推，直到条件不满足为止

# 输出一百遍 好好学习，天天向上
i = 1
while i <= 100:
    print("好好学习，天天向上")
    i += 1

# 死循环基本格式
"""
while True:
    循环体

"""
"""
while True:
    print("这是一个死循环")
    a = input("请输入q退出:")
    if a == "q":
        break
while False:
    print("不会执行的死循环")
    break

while 2:
    print("这是一个死循环")
    a = input("请输入q退出:")
    if a == "q":
        break
"""

# 计算1~100的和
i = 1

while i <= 100:
    print(i)  # 但我们应该把这一百个数加起来，而不是一个个输出，所以我们需要一个变量来存储和
    i += 1

i = 1
s = 0
while i <= 100:
    print(i)
    s += i
    i += 1
print("1~100的和为：", s)

# while 循环嵌套
# while 循环嵌套就是在一个while循环中再嵌套一个while循环
"""
    基本格式
    while 条件1:
        while 条件2:
            执行语句1
        执行语句2
    执行语句3
"""
i = 1
while i <= 3:
    print(f"外层循环第{i}次")
    j = 1  # 进入内循环
    while j <= 5:
        print(f"内层循环第{j}次")
        j += 1
    i += 1


# =====================================================================
# 字符串编码
""" 编码     年份      描述                                              所占字节数
    ASCII   1976年   只包含英文字符，使用7位二进制表示一个字符            8bit/1bytes
    GB2312  1980年   包含简体中文字符，使用2个字节表示一个汉字            16bit/2bytes
    Unicode 1991年   包含所有常用字符，使用4个字节表示一个字符            32bit/4bytes
    UTF-8   1992年   包含所有常用字符，使用1~4个字节表示一个字符，兼容ASCII  8bit/1bytes
"""
# Unicode编码：所有字符都是2个字节
# 好处：字符与数字的转化效率高，兼容ASCII码
# 坏处：占用空间大
# UTF-8编码：所有字符都是1~4个字节，精准，对不同的字符占用空间不同
# 好处：节省空间
# 坏处：字符与数字的转化效率低，每次都需要计算字符需要几个字符表示

# encode编码
# decode解码

# 字符串编码转化：
a = "Hello"
print(a, type(a))  # 输出：Hello <class 'str'>
a1 = a.encode()  # 编码
print("编码后：", a1)
print(a1, type(a1))  # 输出：b'Hello' <class 'bytes'>   bytes，以字节为单位处理
a2 = a1.decode()
print(a2, type(a2))  # 输出：Hello <class 'str'>
# 注意：对于bytes，只需要知道它跟字符串之间的类型转换

st = "你好"
st1 = st.encode("utf-8")  # 编码
print(st1, type(st1))  # 输出：b'\xe4\xbd\xa0\xe5\xa5\xbd' <class 'bytes'>
st2 = st1.decode("utf-8")
print(st2, type(st2))  # 输出：你好 <class 'str'>


# =====================================================================
# 字符串运算符
"""
    操作符     描述          示例
    +          字符串连接    a="Hello" b="World" c=a+b  #c="HelloWorld"
    *          字符串重复    a="Hello" b=a*3  #b="HelloHelloHello"
    []         字符串索引    a="Hello" b=a[0]
    [:]        字符串切片    a="Hello" b=a[0:2]  #b="He"
    in         字符串包含    a="Hello" b="H" c=b in a  #c=True
    not in     字符串不包含  a="Hello" b="H" c=b not in a  #c=False
    r/R        原始字符串    a=r"Hello\\nWorld"  #a="Hello\\nWorld"
"""

# 字符串常见操作

# + 字符串拼接
print(10 + 10)  # 这是整形相加，会输出20，+是运算符
print("10" + "10")  # 这是字符串相加 输出1010，+是字符串拼接符
num1 = "Hello"
num2 = "Python"
print(num1 + "" + num2)  # 输出：Hello Python
print(num1, num2, sep="")  # 输出:Hello Python

# *
print("好好学习，天天向上\n" * 100)
print("好好学习，天天向上\t" * 100)

# 成员运算符
# in 如果包含的话，返回True,否则返回False
# not in 如果包含的话，返回False，否则返回True
name = "bingbing"
print("a" in name)  # 输出：False
print("b" in name)  # 输出：True
print("a" not in name)  # 输出:True
print("b" not in name)  # 输出:False


# =====================================================================
# 下标
# python中下标从0开始
name = 'sixstar'
"""
    s   i  x  s  t  a  r
    0   1  2  3  4  5  6
    -7 -6 -5 -4 -3 -2 -1
"""
print(name[0])  # 输出：s
print(name[1])  # 输出：i
print(name[2])  # 输出：x
print(name[3])  # 输出：s
print(name[4])  # 输出：t
print(name[5])  # 输出：a
print(name[6])  # 输出：r
# NO print(name[7])
print(name[-1])  # 输出:r
print(name[-2])  # 输出:a
print(name[-3])  # 输出:t
print(name[-4])  # 输出:s
print(name[-5])  # 输出:x
print(name[-6])  # 输出:i
print(name[-7])  # 输出:s
# NO print(name[-8])


# =====================================================================
# 切片
# 语法:[开始位置:结束位置:步长]
# 包前不包后：即从起始位置开始，到结束位置前一位结束(不包含结束位置本身)
st = "g79j468abc789"
"""
    开始位置:
      原  g  7  9  j  4  6  8  a  b  c  7  8  9
    对应  0  1  2  3  4  5  6  7  8  9 10 11 12

    结束位置:
      原  g  7  9  j  4  6  8  a  b  c  7  8  9
    对应  1  2  3  4  5  6  7  8  9 10 11 12 13
"""
print(st[0:4])  # 输出：g79j
print(st[4:7])  # 输出：468
print(st[7:])  # 输出：abc789
print(st[:7])  # 输出：g79j468

print(st[-1:])  # 输出：9
print(st[:-2])  # 输出:g79j4

# 步长：表示选取间隔，不写步长，默认是1
# 步长的绝对值大小决定切取的间隔，正负号决定方向
# 正数从左往右，负数从右往左

# SO, WHY DO YOU RUN "print(st[-1:])" is 9?
st = "g79j468abc789"
"""
    开始位置如下
    g   7   9   j   4  6  8  a  b   c  7  8  9
    0   1   2   3   4  5  6  7  8   9  10 11 12
    -13 -12 -11 -10 -9 -8 -7 -6 -5 -4  -3 -2 -1
    -1::1
    那么开始位置是9,一直从左往右截取,
    发现9后面，已经没东西了
    并且，9是开始位置，根据包前不包后，那么只有9被截取到了
"""


# =====================================================================
# 查找

# find：检查某个子字符串是否包含在字符串中，如果存在就返回开始位置的下标，否则返回-1
name = "bingbing"
# find(self, sub, __start, __end) -> find(子字符串, 开始位置下标, 结束位置下标)
# 开始下标和结束下标可以省略，这样的话，会在整个字符查找
print(name.find("b"))  # -> 0
print(name.find("bing"))  # -> 0
print(name.find("b", 3))  # -> 4
print(name.find("b", 5))  # -> -1 找不到返回-1
print(name.find("b", 3, 5))  # -> -1
# 开始下标和结束下标遵循包前不包后

# index：检查某个子字符串是否包含在字符串中，如果存在就返回开始位置的下标，否则报错
# index(self, sub, __start, __end) -> index(子字符串, 开始位置下标, 结束位置下标)
name = "我命由我不由天"
print(name.index("我"))  # -> 0
print(name.index("命"))  # -> 1
print(name.index("命", 2))  # -> 报错：ValueError: substring not found
"""
    注意：
    1. find和index的区别
       find：如果找不到，返回-1
       index：如果找不到，就会报错
    2. find和index的参数
       find：可以省略开始和结束下标
       index：不可以省略开始和结束下标
"""


# =====================================================================
# count(): 统计某个子字符串在字符串中出现的次数，没有就返回0
# count(self, sub, __start, __end) -> count(子字符串, 开始位置下标, 结束位置下标)
name = "bingbing"
print(name.count("b"))  # -> 2
print(name.count("b", 3))  # -> 1
print(name.count("b", 3, 5))  # -> 0
# count同样遵循包前不包后


# =====================================================================
# startswith: 检查字符串是否以某个子字符串开头，如果是就返回True，否则返回False
name = "bingbing"
print(name.startswith("b"))  # -> True
print(name.startswith("bing"))  # -> True
print(name.startswith("b", 3))  # -> True
print(name.startswith("b", 5))  # -> False
print(name.startswith("b", 3, 5))  # -> True
print(name.startswith("b", 5, 7))  # -> False


# =====================================================================
# endswith: 检查字符串是否以某个子字符串结尾，如果是就返回True，否则返回False
name = "bingbing"
print(name.endswith("g"))  # -> True
print(name.endswith("bing"))  # -> True
print(name.endswith("g", 3))  # -> True
print(name.endswith("g", 5))  # -> False
print(name.endswith("g", 3, 5))  # -> True
print(name.endswith("g", 5, 7))  # -> False


# =====================================================================
# isupper(): 检查字符串中所有字母是否都是大写，如果是就返回True，否则返回False
print("HELLO".isupper())  # -> True
print("Hello".isupper())  # -> False
print("SIXSTAR".isupper())  # -> True
print("SIXSTAR123".isupper())  # -> True

# islower(): 检查字符串中所有字母是否都是小写，如果是就返回True，否则返回False
print("hello".islower())  # -> True
print("Hello".islower())  # -> False
print("sixstar".islower())  # -> True
print("sixstar123".islower())  # -> True


# =====================================================================
# isdigit(): 检查字符串是否只包含数字，如果是就返回True，否则返回False
print("123".isdigit())  # -> True
print("123abc".isdigit())  # -> False
print("123.45".isdigit())  # -> False
print("123.456".isdigit())  # -> False

# isalpha(): 检查字符串是否只包含字母，如果是就返回True，否则返回False
print("abc".isalpha())  # -> True
print("abc123".isalpha())  # -> False


# =====================================================================
# 修改元素

# replace(): 替换字符串中的某个子字符串，如果存在就替换，否则不替换
# replace(self, old, new, count) -> replace(旧子字符串, 新子字符串, 替换次数)
name = "好好学习，天天向上"
print(name.replace("天", "时"))  # -> 好好学习，时时向上
print(name.replace("天", "时", 1))  # -> 好好学习，时天向上
print(name.replace("天", "时", 2))  # -> 好好学习，时时向上
# 不写count，则替换所有


# =====================================================================
# split(): 指定分隔符来切字符串
st = "Hello Python"
print(st.split(" "))  # -> ['Hello', 'Python']
# 如果分割内容不包含分割内容，会作为一个整体返回
print(st.split("o"))  # -> ['Hell', ' ,Pyth ', 'n']
# 如果分割内容包含多个分割内容，会返回多个空字符串


# =====================================================================
# capitalize(): 将字符串的第一个字母大写，其余字母小写
st = "bingbing"
print(st.capitalize())  # -> Bingbing
# 如果字符串的第一个字母是数字，则不会大写
print("123bingbing".capitalize())  # -> 123bingbing
# 如果字符串的第一个字母是特殊字符，则不会大写
print("@bingbing".capitalize())  # -> @bingbing
# 如果字符串的第一个字母是中文，则不会大写
print("你好，世界".capitalize())  # -> 你好，世界


# =====================================================================
# lower(): 将字符串中的所有字母都转换为小写
st = "BINGBING"
print(st.lower())  # -> bingbing

# upper(): 将字符串中的所有字母都转换为大写
st = "bingbing"
print(st.upper())  # -> BINGBING


# =====================================================================
# 列表
"""
    1. 定义: 列表是Python中一个重要的数据结构，列表中的元素可以重复，
       列表中的元素可以是任意类型，列表中的元素可以有任意个，列表中的元素可以有任意位置
    2. 定义列表: 列表是由方括号[]括起来的，列表中的元素之间用逗号隔开
    3. 格式: list = [元素1, 元素2, 元素3, ...]
"""
# 列表名 = [元素1, 元素2, 元素3, ...]
li = [1, 2, 3, 4]
print(li, type(li))  # 输出：[1, 2, 3, 4] <class 'list'>

# 列表中的元素可以是任意类型
li = [1, 2, 3, 4, "hello", True]
print(li, type(li))  # 输出：[1, 2, 3, 4, 'hello', True] <class 'list'>

li = [1, 2, 'a', 4]
print(li[0])  # 输出：1
print(li[1])  # 输出：2
print(li[2])  # 输出：a
print(li[3])  # 输出：4
print(li[-1])  # 输出：4
print(li[-2])  # 输出：a
print(li[-3])  # 输出：2
print(li[-4])  # 输出：1

# 切片
print(li[0:2])  # 输出：[1, 2]
print(li[1:3])  # 输出：[2, 'a']
print(li[2:4])  # 输出：['a', 4]
print(li[3:5])  # 输出：[4]

# 列表是可迭代对象，可以for循环迭代取值
for i in li:
    print(i)


# =====================================================================
# 列表常见操作

# 添加元素: append(); extend(); insert()
li = ['one', 'two', 'three']
li.append('four')  # 在列表末尾添加一个元素
print(li)  # 输出：['one', 'two', 'three', 'four']

li.extend(['five', 'six'])  # 在列表末尾添加多个元素
# li.extend()只接受传入列表
li.insert(0, 'zero')  # 在列表指定位置添加一个元素，如果指定位置超过列表长度，则在列表末尾添加
print(li)  # 输出：['zero', 'one', 'two', 'three', 'four', 'five', 'six']

li = ['one', 'two', 'three']
li.append('five')
print(li)


# =====================================================================
# 修改元素
# 直接通过下标可以修改
li = ['one', 'two', 'three', 'four']
li[0] = 'zero'
print(li)  # 输出：['zero', 'two', 'three', 'five']


# =====================================================================
# 查找元素
# in: 判断元素是否在列表中
# not in: 判断元素是否不在列表中
li = ['one', 'two', 'three', 'four']
print('one' in li)  # 输出：True
print('five' in li)  # 输出：False

if 'one' in li:
    print('one在列表中')
else:
    print('one不在列表中')

# 用户输入昵称，昵称存在则不能使用
# 定义一个列表，保存已经存在的名称
name_list = ["bingbing", "susu", "ziyi"]
while True:
    name = input("请输入昵称：")
    if name in name_list:
        print("昵称已存在，请重新输入")
    else:
        print("昵称可以使用")
        break

# bingbing原版
"""
if name in name_list:
    print(f"昵称{name}已存在，请重新输入")
else:
    print(f"昵称{name}已经被您使用")
    name.append(name)
    print(name_list)
"""

# index(): 查找元素在列表中的索引位置
# count(): 查找元素在列表中的个数


# =====================================================================
# 删除元素

# del
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
del li
# 这时候再print(li)就会报错，因为li已经被删除了
del li[0]

# pop
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
li.pop()  # 删除列表末尾的元素
print(li)
li.pop(0)  # 删除列表指定位置的元素，只能根据下标删除，不能根据元素删除
# 下标不能超出范围

# remove: 根据元素删除
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
li.remove(2)  # 删除列表中的元素，列表中不存在元素的时候就会报错
li.remove(1)  # 删除列表中的元素，列表中存在多个元素的时候，只会删除第一个出现的元素

# clear: 清空列表
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
li.clear()


# =====================================================================
# 排序

# sort(): 对列表中的元素按特定顺序进行排序
li = [1, 6, 3, 8, 7, 9, 3]
li.sort()  # 默认升序(从小到大)排序 -> 1,2,3,3,6,7,8,9

# reverse(): 将列表中的元素反转，倒序
li.reverse()  # 将列表中的元素反转，倒序 -> 9,8,7,6,3,3,2,1


# =====================================================================
# 列表推导式
# 列表推导式是一种简洁的创建列表的方式，它可以在一行代码中创建一个列表，而不需要使用循环语句
# 列表推导式的基本语法是：[表达式 for 变量 in 列表/range()/可迭代对象]
li = [i for i in range(1, 10)]
[print(i) for i in li]  # 前面的i是表达式
[print(i * 5) for i in li]  # -> 5, 10, 15, 20, 25, 30, 35, 40, 45

# [表达式 for 变量 in 列表 if 条件]
li = []
for i in range(1, 10):
    if i % 2 == 1:
        li.append(i)
li = [i for i in range(1, 10) if i % 2 == 1]
print(li)


# =====================================================================
# 列表嵌套
li = [1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12, [13, 14, 15]]]]]
print(li[0])  # -> 1
print(li[3])  # -> [4, 5, 6, [7, 8, 9, [10, 11, 12, [13, 14, 15]]]]
print(li[3][0])  # -> 4
print(li[3][3][0])  # -> 7


# =====================================================================
# 元组
tua = (1, 2, 3, 4)
# 元组是不可变的，不能修改元组中的元素
print(type(tua))  # -> <class 'tuple'>

tub = (1)  # 这是整数类型
tub = (1,)  # 这是元组类型
# 元组只有一个数据时，必须加逗号

tuc = ()
# 定义空元组

# 只能查询元组，不能修改元组
print(tua[0])  # -> 1

# 元组可使用count(), index(), len(), in, not in ......和列表相同
# 应用场景:
# 函数的参数和返回值
# 格式化输出后面的()本质上是一个元组
# 保护数据的安全


# =====================================================================
# 字典
# 格式: dict = {key1: value1, key2: value2, key3: value3, ...}
# 字典中的键具备唯一性，但值可以重复
dic = {
    "name": "bingbing",
    "name": "susu"
}  # 如果这样写，name的值会被后面的值覆盖，name=susu

dic = {
    "name": ["susu", "bingbing"],
    "age": ["78", "18.8"]
}


# =====================================================================
# 字典常见操作

# 查看元素
# 变量名[键名]
dic = {'name': "bingbing", 'age': 18}
# 字典不可以使用索引，查找需要使用键名
# 如果键名存在，则会返回对应的值
# 如果键名不存在，则会返回默认值
print(dic.get('name'))  # -> bingbing
print(dic.get('age'))  # -> 18
print(dic.get('gender'))  # -> None
print(dic.get('gender', "7891"))  # -> 7891

# 或这样
print(dic['name'])
# 如果不存在键值，就会报错

# 修改字典
# 直接通过键名修改
dic['name'] = "susu"
print(dic)  # -> {'name': 'susu', 'age': 18}

# 添加元素
dic[7891] = 7891
print(dic)


# =====================================================================
# 删除元素
del dic  # 删除整个字典
dic = {'name': "bingbing", 'age': 18}  # 复活一下字典
del dic['name']  # 删除字典中的键值对
# 键名不存在会报错

dic.clear()
# 清空字典后仍可以查询到字典，只不过为空

dic = {1: 2, 3: 4, 5: 6}
dic.pop(1)  # 删除字典中的键值对
dic.popitem()  # 删除字典中的最后一个键值对

dic = {1: 2, 3: 4, 5: 6}
len(dic)  # 统计字典里的键值对数量

dic.keys()  # 返回字典里的所有键 -> dict_keys([1, 3, 5])
dic.values()  # 返回字典里的所有值 -> dict_values([2, 4, 6])
dic.items()  # 返回字典里的所有键值对 -> dict_items([(1, 2), (3, 4), (5, 6)])

# 用for推出所有键名
for i in dic.keys():  # 只取出键名
    print(i)

# 用for推出所有键值
for i in dic.values():  # 只取出键值
    print(i)

# 用for推出所有键值对
for i in dic.items():  # 取出键值对
    print(i)

# 字典可以保存一个物体的所有属性


# =====================================================================
# 集合
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 里面的元素是唯一的，不能重复，集合是无序的，可以用于元组或列表去重
# 可以是不同的数据类型

set1 = {}  # 这是空字典
set1 = set()  # 这是空集合
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # 数字运行结果一样
set1 = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}  # 字符串运行结果每次都不一样

# 集合无序的实现方式涉及哈希表
set1 = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}
for _ in range(78):
    print(hash("a"))  # 每次运行都不同
for _ in range(78):
    print(hash(1))  # 每次运行都一样
for _ in range(78):
    print(hash("1"))  # 每次运行都不同，"1"和1的哈希值不同

# 所以我们只能修改集合中的值

# 集合常见操作

# 添加元素
set1.add(11)  # 添加元素
set1.update([11, 12, 13])  # 添加多个元素

# 删除元素
set1.remove(11)  # 删除元素，元素不存在会报错
set1.discard(11)  # 删除元素，元素不存在不会报错
set1.pop()  # 随机删除元素
set1.clear()  # 清空集合
print(set1)
print(len(set1))
print(set1)


# =====================================================================
# 集合运算
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15}
print(set1 & set2)  # 交集 指：集合中同时存在的元素 -> {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1 | set2)  # 并集 指：集合中存在的元素 -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(set1 - set2)  # 差集 指：集合1中存在的元素，集合2中不存在的元素 -> {10}

set1 = {1, 7, 4, 5, 7, 3, 2, 5, 6, 7, 8}
print(set1)  # -> {1, 2, 3, 4, 5, 6, 7, 8} 集合可以自动去重


# =====================================================================
# 类型转换

# int(): 转换成一个整数，只能用于由纯数字组成的字符串
a = 1.2
print(a, type(a))
b = int(a)
print(b, type(b))  # -> 1 <class 'int'>
# 浮点型强转整形，会保留整数部分，舍弃小数部分

# str -> int
a = int("123")
print(a, type(a))  # -> 123 <class 'int'>
# print(int("123a"))  # -> ValueError: invalid literal for int() with base 10: '123a'
# 如果字符串中有除了+-号以外的其他字符，会报错，且+-号只能放在字符串前面
print(int("+123"))  # -> 123
print(int("-123"))  # -> -123
# print(int("123-"))  # -> ValueError: invalid literal for int() with base 10: '123-'

age = int(input("请输入你的年龄："))  # input默认输入的是字符串类型，需要转换成int类型
if age >= 18:
    print("你已成年")
else:
    print("你还未成年")


# =====================================================================
# float(): 转换成一个浮点数，只能用于由纯数字组成的字符串
a = 1
print(a, type(a))  # -> 1 <class 'int'>
b = float(a)
print(b, type(b))  # -> 1.0 <class 'float'>  float会自动加一位小数0

# str -> float
a = float("123.123")
print(a, type(a))  # -> 123.123 <class 'float'>
# print(float("123a"))  # -> ValueError: could not convert string to float: '123a'
print(float("+123.123"))  # -> 123.123


# =====================================================================
# str(): 转换成字符串类型，任何类型都可以转换成字符串类型
n = 100
print(n, type(n))  # -> 100 <class 'int'>
n2 = str(n)
print(n2, type(n2))  # -> 100 <class 'str'>

st = str(-1.80)
print(st, type(st))  # -> -1.8 <class 'str'>    浮点类型转换成字符串类型时，会去掉末尾的0

st = str(1.0)
print(st, type(st))  # -> 1.0 <class 'str'>     只有小数只有一位且这一位是0，这时，0才不会被去掉

li = str([1, 2, 3, 4, 5])
print(li, type(li))  # -> [1, 2, 3, 4, 5] <class 'str'>


# =====================================================================
# eval(): 将字符串转换成代码并执行
print(10 + 10)  # -> 20
print("10" + "10")  # -> 1010
print(eval("10" + "10"))  # -> 1010
print(eval("10+10"))  # -> 20
# print(eval("10" + 10))  # -> SyntaxError: invalid syntax   不要把整形和字符串相加

# eval()可以实现list(列表)，dict(字典)，tuple(元组)和str(字符串)之间的转换
st1 = "[1, 2, 3, 4, 5]"
st2 = eval(st1)
print(st2, type(st2))  # -> [1, 2, 3, 4, 5] <class 'list'>

dic = "{'name': 'bingbing', 'age': 18}"  # 注意：字典的键值对要用引号括起来，外双引号内单引号
dic2 = eval(dic)
print(dic2, type(dic2))  # -> {'name': 'bingbing', 'age': 18} <class 'dict'>
# eval()十分强大但不安全，容易被恶意修改数据，不建议使用


# =====================================================================
# list(): 将可迭代对象转换成列表
# 可迭代对象有：str, tuple, dict, set
# 能被for循环迭代取值的就是可迭代对象

# str -> list
a = "123456"
print(list(a))  # -> ['1', '2', '3', '4', '5', '6']
# print(list(123))  # -> TypeError: 'int' object is not iterable

# dict -> list
a = {1: 2, 3: 4, 5: 6}
print(list(a))  # -> [1, 3, 5]

# set -> list
a = {1, 2, 3, 4, 5, 6}
print(list(a))  # -> [1, 2, 3, 4, 5, 6]   集合是无序的，所以每次运行结果都不一样，并且会先去重，再转换成列表

# tuple -> list
a = (1, 2, 3, 4, 5, 6)
print(list(a))  # -> [1, 2, 3, 4, 5, 6]


# =====================================================================
# tuple(): 将可迭代对象转换成元组
# 可迭代对象有：str, tuple, dict, set
# 能被for循环迭代取值的就是可迭代对象

# str -> tuple
a = "123456"
print(tuple(a))  # -> ('1', '2', '3', '4', '5', '6')
# print(tuple(123))  # -> TypeError: 'int' object is not iterable


# =====================================================================
# 赋值
import copy

li = [1, 2, 3, 4]
print(li)
li2 = li  # 将li直接赋值给li2
print("li", li)
print("li2", li2)

li.append(5)
print("li", li)  # -> li [1, 2, 3, 4, 5]
print("li2", li2)  # -> li2 [1, 2, 3, 4, 5]  li2的值也跟着改变，因为li2和li指向的是同一个内存地址

# 浅拷贝
li = [1, 2, 3, 4]
print(li)
li2 = li.copy()  # 将li浅拷贝给li2
print("li", li)
print("li2", li2)

li.append(5)
print("li", li)  # -> li [1, 2, 3, 4, 5]
print("li2", li2)  # -> li2 [1, 2, 3, 4]  li2的值没有改变，因为li2和li指向的是不同的内存地址
print("l1内存地址", id(li))
print("l2内存地址", id(li2))
# 内存地址不一样，不是一个对象，所以改变li的值，li2的值不会改变

li = [1, 2, [1, 2, 3]]
li2 = li.copy()
li.append(3)
print(li)  # -> [1, 2, [1, 2, 3], 3]
print(li2)  # -> [1, 2, [1, 2, 3]]
# 只有最外层的列表是深拷贝，里面的列表是浅拷贝，所以li2的值没有改变
print("l1内存地址", id(li))
print("l2内存地址", id(li2))
# 内存地址不一样，不是一个对象，所以改变li的值，li2的值不会改变

li[2].append(4)
print(li)  # -> [1, 2, [1, 2, 3, 4], 3]
print(li2)  # -> [1, 2, [1, 2, 3, 4]]  li2的值也跟着改变，因为内嵌列表指向同一个内存地址
print("l1[2]内存地址", id(li[2]))
print("l2[2]内存地址", id(li2[2]))  # -> 内存地址一样，是一个对象，所以改变li[2]的值，li2[2]的值也会改变

# 所以，copy会把最外层的列表进行深拷贝（不指向li的最外层的内存地址），
# 里面的嵌套列表进行浅拷贝（还是指向li的内嵌列表的内存地址）


#########################################################################
#1.函数
#含义 ：将独立的代码组织成一个整体。使其具有特殊功能的代码块，在需要的时候再去调用
#作用：提高代码的重用性，是整体代码看上去更加简练
#基本格式：def 函数名():
#        函数体
def login():
    print("这是一个登录函数")
login()
#调用几次，函数里的代码就执行几次，每次调用的时候，函数都会开始执行
 
#编写一个打招呼的函数，并粘贴上去
def say_hello():
    print("Hello/你好")
    print("bingbign")
    print("age 18")
say_hello()
#调用函数前，必须保证函数已经存在

#返回值 return
#函数执行结束后，最后给调用者的一个结果
#作用：
#1.return会给函数的执行者提供返回值
def buy():
    return "hamburger"
buy()#没结果
print(buy())#->hamburger
#2.函数中遇到return，表示此函数结束，不继续执行
def buy():
    return "haburger"
    return 20  #不会执行
#函数中遇到return表示函数的结束，return一下的代码不会执行
def buy():
    return "haamburger",20 #返回一个元组

#如果一个返回值都没有，返回None
#print vs return
#return 表示函数结束  print会继续执行
#return是返回计算值   print是打印结果
def add():
    a =1
    b=1
    return a+b
print(add())

#参数
def add(a,b):#形参->a,b，仅在函数内部有效
    return a*b
add(1,2)#这时传入的参数叫做实参
#传参 就相当于把1赋值给a,把2赋值给b
add(3,4)#->12

#函数参数
#必备参数（位置参数）
#含义：传递和定义参数的顺序及个数必须一致

def funa(name,name1,name2):
    print(name,name1,name2)
funa(1,2,3)
#missing 丢失
#TypeError:funa() missing 2 required positional  arguments:'name' ,'name1 ','name2'   
#就是少了3个参数的意思
#不可以多传，也不能少传，顺序要一致
#sex性别
#所以叫位置参数

#默认参数
#有一个默认值
#含义，为参数提供默认值，条用函数时可不传该默认参数的值
#注意，所有的位置参数必须出现在默认参数前，包括函数定义和调用
def func(a=8):print(a)
func()#没有报错
func(300)#->300
#默认值没有传值会根据默认值来执行代码，传了值根据传入的值来执行代码
#def func(a=3,b)#报错，位置参数要在默认参数前面
def func(a=3,b=5):
    print(a,b)
func()

#可变参数
#含义：传入的值的数量是可变的，可以传入多个，也可以不传
def func(*args):#一定要加星号*,args是约定俗成的写法
    print(args)#以元组形式接收
    print(type(args))
func(1,2,3,4,5,6,7,8,9)
func('asd','asdfdsa','dadsfdfsafs')

#关键字参数
def func(**kargs):#kargs是约定俗成的，**代表特殊
    print(kargs)#以字典形式接收

func(name="bingbing",age=18)#传回的时候，需要采用键=值的形式

#func(1,2)#报错

#函数嵌套

#嵌套调用
#含义：在一个函数里调用另外一个函数
def study():
    print(1)
def course():
    print(2)

#也可以这样
def course():
    study()
    print(2)  #这就是嵌套调用


#嵌套定义
#含义：在一个函数里定义另一个函数
def study():
    print(1)
    def course():
        print(2)

#只会输出1
def study():
    print(1)
    def course():
        print(2)
    course()
    return None



"""
def study():
    print(1)
    def course():
        print(2)
        study()
    course()
#这样会形成一个死循环
study->print->course
  \              \
 < -   <-   <-    <-

"""

#作用域
#指变量生效的范围，分为两种，分别是全局变量和局部变量
#全局变量
#函数外部定义的变量，在整个文件中都是有效的
a =100
def test1():
    print("test1:",a)
def test2():
    a=120
    print("test2:",a)

print("调用函数前a的值:",a)
test1()
test2()
print("调用函数前a的值:",a)


#a的值没有被覆盖是因为函数内部如果要用变量
#会显存函数内部找，有的话直接使用，没有的话从外部找

#局部变量
#函数内部定义的变量，从定义位置到函数定义结束位置有效
def fun():
    num123num =10 #局部变量num
    print(num123num)

#print(num123num) #->报错  局部变量只能在被定义的函数中使用
#作用，在函数体内部，临时保存数据，当函数调用完之后，就消除局部变量

def funa():
    num = 10
    print("funa中的num:",num)

def funb():
    num=18
    print("funb的num:",num)

#num不冲突，因为作用域不同
funa()#->10
funb()#->18

#全局变量和局部变量名称相同，全局变量不会被影响

#global  关键字
#在函数内部修改全局变量
#将变量声明为全局变量
#global a ;a=120
a=10
def test():
    #global a  #如果加上这行，则输出11
    a=11
print(a)#->10



def study():
    global name #将name声明为全局变量
    
    name="python基础"
    print(f"我们在学习{name}。")

study()
print(name)#不报错

def work():
    print(name)#可以使用study里的变量
work()

def a():
    global a,age,b,sdf,sdfa,wfwerg,dsfgwe  #这些变量就都被声明了
a()

#nonlocal
#用来声明外层的局部变量，只能在嵌套函数中使用

a =10 #全局
def a():#外函数
    a=5 #局部变量
    def b():#内函数
        print("b中的a值",a)
    b()
    print("a中a的值：",a)
    
a()#->5,5

def a():#外函数
    a=5 #局部变量
    def b():#内函数
        nonlocal a
        a=20   #对外函数进行修改
        print("b中的a值",a)
    b()
    print("a中a的值：",a) #输出修改过的a
    
a()#->20,20

def a():#外函数
    a=5 #局部变量
    def b():#内函数
        #nonlocal a
        a=20   
        def c():
            nonlocal a ##对外函数进行修改
            a=30
            print("c中的a值",a)
        c()
        print("b中的a值",a)
    b()
    print("a中a的值：",a)     
a()#->30,30,5

#############################################
#匿名函数
#基本函数
#函数名=lambda形参：返回值（表达式）
#调用：结果 = 函数名（实参）

#普通函数
def add(a,b):
    return a+b
print(add(2,3))

#匿名函数
add = lambda a,b:a+b
print(add(13,123))
#lambda不需要写return来返回值，表达式本身就是返回

#lambda的参数形式
#无参数
funa = lambda : "123"
print(funa())#->123
#一个参数
funa = lambda a:a
print(funa(12))#->12
#默认参数
func = lambda a,age=18:(name,age)#返回值是元组形式的

print(func(12,2314))#->12,1214

#默认参数必须写在非默认参数后面

#关键字参数
f=lambda **kwargs:kargs
print(f(name=12,age=23,sex=452))#以赋值的形式来，双星号

#lambda结合if判断
a =5
b =8
#三目运算
#为真结果 if 条件 else 为假结果
print("a<b") if a<b else print("a>b")
comp =lambda a,b : "a<b" if a<b else "a>b"
#comp 比较
print(comp(5,8))

#内置函数
#查看所有的内置函数
import builtins
print(dir(builtins))
#大写字母开头一般为内置常量名，小写字母开头一般是内置函数名

#abs
#abs()返回绝对值
print(abs(-10))#->10   不管正负号，直接返回
print(abs(10))#->10

#sum()求和
#sum里需要放可迭代对象，no sum(123),报错

print(sum([1,2,3]))#->6
print(sum({1:1,2:2,3:3}))#->6

#min
print(mim([1,4,5]))#->1  最小值
print(mim([-8,5,key==abs]))#->5 比较两数的绝对值
#max() 最大值

#zip()将可迭代对象作为参数，将对象中的元素打包成一个元组

li=[1,2,3]
li2=["a",'b','c']
print(zip(li,li2))
for i in zip(li,li2):
    print(i)
    #->(1,'a') (2,'b') (3,'c')
#如果元素个数不一致，按长度最短的返回
print(list(zip(li,li2,range(5))))
