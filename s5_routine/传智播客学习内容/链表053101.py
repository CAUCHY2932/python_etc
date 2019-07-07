#-*-coding:utf-8-*-

#双向链表删除元素
def remove(self,item):
	"""删除元素"""
	if self.is_empty():
		return
	else:
		cur=self._head
		if cur.item==item:
			#如果首节点的元素是要删除的元素
			if cur.next==None:
				self._head=None
			else:
				#将第二个节点的prev设置为None
				cur.next.prev=None
				#将_head指向第二个节点
				self._head=cur.next
			return
		while cur !=None:
			if  cur.item==item:
				#将cur的前一个节点的next指向cur的后一个节点
				cur.prev.next=cur.next
				#将cur的后一个节点的prev指向cur的前一个节点
				cur.next.prev=cur.prev
				break
			cur=cur.next
#栈
class stack(object):
	"""栈"""
	def __init__(self):
		self.items=[]
	def is_empty(self):
		"""判断是否为空"""
		ruturn self.item==[]
	def push(self,item):
		"""加入元素"""
		self.items.append(item)

	def pop(self):
		"""弹出元素"""
		return self.items.pop()

	def peak(self):
		"""返回栈顶元素"""
		 return self.items[len(self.items)-1]

	def size(self):
		"""返回栈的大小"""
		return len(self.items)


	if __name__== '__main__':
		stack=Stack()
		stack.push("hello")
		stack.push("world")
		stack.push("itcast")
		print(stack.size())
		print(stack.peak())
		print(stack.pop())

class Queue(object):
	"""队列"""
	def __init__(self):
		self.items=[]

	def is_empty(self):
		return self.items==[]

	def enqueue(self,item):
		"""进队列"""
		self.items.insert(0,item)

	def dequeue(self):
		"""出队列"""
		return self.items.pop()

	def size(self):
		"""返回大小"""
		return len(self.items)

if __name__== "__main__":
	q=Queue
	q.enqueue("hello")
	q.enqueue("world")
	q.enqueue("itcast")
	print(q.size())
	print(q.dequeue)

#双端队列
class Dqueue(object):
	"""双端队列"""
	def __init__(self):
		self.items=[]

	def is_empty(self):
		"""判断队列是否为空"""
		return self.items==[]

	def add_front(self,item):
		"""在队头添加元素"""
		self.items.insert(0,item)

	def add_rear(self,item):
		"""在队尾添加元素"""
		self.items.append()

	def remove_front(self):
		"""从队头删除元素"""
		return self.items.pop(0)

	def remove_rear(self):
		"""从队尾删除元素"""
		return self.items.pop()
	
	def size(self):
		"""返回队列大小"""
		return len(self.items)

if __name__ == "__main__":
	dque=Dqueue()
	dque.add_front()
	dque.add_front(1)



#排序与搜索

#稳定性

#冒泡排序
# bubble sort
def bubble_sort(alist):
	for j in range(len(alist)-1,0,-1):
		#j表示每次遍历需要比较的次数，是逐渐减少的
		for i in range(j):
			if alist[i] >alist[i+1]:
				alist[i],alist[i+1]=alist[i+1],alist[i]
li=[23,34,56,56,77,88,54,26]
bubble_sort(li)
print(li)

时间复杂度
最优时间复杂度 O(n)
最坏时间复杂度 O(n**2)
稳定性：稳定

#选择排序


def selection_sort(alist):
	n=len(alist)
	#需要进行n-1次选择操作
	for i in range(n-1):
		#记录最小位置
		min_index=i
		#从i+1位置到末尾选择出最小数据
		for j in range(i+1,n):
			if alist[j]<alist[min_index]:
				min_index=j
		#如果选择出的数据不在正确位置，进行交换
		if min_index!=i:
			alist[i],alist[min_index]=alist[min_index],alist[i]


alist=[5464,64648,6,88,6876,679687967,13131,6466]

selection_sort(alist)
print(alist)

# 时间复杂度
# 最优时间复杂度 O(n**2)
# 最坏时间复杂度 O(n**2)
# 数组实现的不稳定，链表实现的不稳定，我们提到的默认是使用数组实现的，所以是不稳定的

# 稳定性 不稳定

# 插入排序
def insert_sort(alist):
	#从第二个位置，即下标为1的元素开始向前插入
	for i in range(i,len(alist)):
		#从第一个元素开始向前比较，如果小于前一个元素，交换位置
		for j in range(i,0,-1):
			if alist[j]<alist[j-1]:
				alist[j],alist[j-1]=alist[j-1],alist[j]

alist=[52,56,87,656,87987,215,646,45]
insert_sort(alist)
print(alist)

# 时间复杂度


# 最优时间复杂度： O(n)
# 最坏时间复杂度： O(n**2)
# 稳定性：稳定

#快速排序
# quicksort

# 又称划分交换排序
# partition-exchange sort

# 基准pivot
# 比基准小的放左侧，比基准大的放右侧，那么每次总有一个在最终位置上
# 这个操作成为分区
# 递归调用，最底部情形是数列的大小是零或一，所以每次迭代，至少有一个是在最后位置上
# 即，是一定会结束，收敛的

def quick_sort(alist,start,end):
	"""快速排序"""
	#递归的退出条件
	if start >=end:
		return 
	#起始元素为要寻找位置的基准元素
	mid=alist[start]
	#low 为序列左边的由左向右移动的游标
	low=start
	#high 为序列右边的由右边向左边移动的游标
	while low < high:
		#如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
		while low <high and alist[high]>=mid:
			high-=1
		#将high指向的元素放在low上



