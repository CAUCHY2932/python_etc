#数据结构与算法

兵法

组合，三重循环和两重循环
for a in range(0,1001):
	for b in range(0,1001):
		for c in range(0,1001):
			if a**2 + b**2 ==c**2 and a+b+c=1000:
				print('a,b,c:%d,%d,%d'%(a,b,c))
end_time=time.time()
print('elapsed:%f'%(end_time-start_time))
print('complete!')

算法的概念
算法是计算机处理信息的本质

第二次尝试
import time
start_time=time.time()

for a in range(0,1001):
	for b in range(0,1001):
		c=1000-a-b
		if a**2+b**2==c**2:
			print('a,b,c:%d,%d,%d'%(a,b,c))
end_time=time.time()
print('elapsed:%f'%(end_time-start_time))
print('complete!')
算法效率衡量
执行时间反应算法效率
单靠时间值并不客观
时间复杂度与'大O记法'
线性阶和常数阶
最坏时间复杂度

基本操作
常数项
顺序结构，加法
循环结构，乘法
分支结构，取其中最大值
判断一个算法的效率时，往往只需要关注操作数量的最高次项
没有特殊说明，我们一般都指的是最坏时间复杂度

常见的时间复杂度：
常数阶，线性阶，平方阶，对数阶，nlogn阶，立方阶，指数阶
阶乘大于指数阶，n的n次方大于阶乘

timeit 模块

算法和数据结构等于程序

抽象数据类型
插入删除，修改，查找排序


单向链表。单链表，是链表中最简单的一种形式，它的节点包含两个域，数据域和链接域





