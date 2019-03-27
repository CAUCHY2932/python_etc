# database setting


## oracle

### some knowledge

umber 数据类型

number (precision,scale)

a)    precision表示数字中的有效位，如果没有指定precision的话，oracle将使用38作为精度；

b)    如果scale大于零，表示数字精度到小数点右边的位数；scale默认设置为0；如果scale小于零，oracle将把该数字取舍到小数点左边的指定位数。

c)    Precision 的取值范围是[1-38];scale的取值范围是[-84-127].

d)    Number整数部分允许的长度为(precision –scale),无论scale是正数还是负数。

e)    如果precision小于scale，表示存储的是没有正数的小数。

f)     Precision表示有效位数，有效数位：从左边第一个不为0的数算起，小数点和负号不计入有效位数；scale表示精确到多少位，指精确到小数点左边还是右边多少位（由+-决定）。


a)    关于precision，scale也可以做如下表述：

定点数的精度(p)和刻度(s)遵循以下规则：

1） 当一个数的整数部分长度 >p-s时，oracle就会报错；

2） 当一个数的小数部分的长度 >s时，oracle就会舍入；

3） 当s(scale)为负数时，oracle就会对小数点左边的s进行舍入；

4） 当s > p 时, p表示小数点后第s位向左最多可以有多少位数字，如果大于p则Oracle报错，小数点后s位向右的数字被舍入。

Number类型的子类：

a)    Oracle本来就没有int类型，为了与别的数据库兼容，新增了Int类型作为number类型的子集；

b)    Int类型只能存储整数，number可以存储浮点数，也可以存整数。

c)    在oracle数据库建表的时候，decimal，numeric不带精度，oralce会自动把它处理成integer；带精度，oracle会自动把它处理成number。

d)    Oracle只用number(m,n)就可以表示任何复杂的数字数据。

Decimal，numeric，int等都为sql,db2等数据库的数据类型，Oracle为了兼容才将其引入；但实际上在oracle内部还是以number的形式将其存入的。



## mysql


## mongodb


## redis



