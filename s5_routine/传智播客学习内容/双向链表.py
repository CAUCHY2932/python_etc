#双向链表
is_empty()链表是否为空
length()链表长度
travel()遍历
add(item)链表头部添加
insert(pos,item)指定位置添加
remove(item)删除节点
search(item)查找结点是否存在
实现
class Node(object):
	"""双向链表节点"""
	def __init__(self,item):
		self.item=item
		self.next=None
		self.prev=None
class Dlinklist(object):
	"""双向链表"""
	def __init__(self):
		self_head=None
	def is_empty(self):
		"""判断链表为空"""
		return self._head==None
	def length(self):
		"""返回链表的长度"""
		cur=self._head
		count=0
		while cur!=None
		count +=1
		cur=cur.next
	return count
	def travel(self):
		"""遍历链表"""
		cur=self._head
		while cur !=None:
			print cur.item
			cur=cur.next
		print("")
	def add(self,item):
		"""头部插入元素"""
		node=Node(item)
		if self.is_empty():
			#如果是空链表，将_head指向node
			self._head=node
		else:
			#将node的next指向_head的头节点
			node.next=self._head
			#将_head的next的头节点的prev指向node
			self._head.prev=node
			#将_head指向node
			self._head=node
	def append(self,item):
		"""尾部插入元素"""
		node=Node(item)
		if self.is_empty():
			#如果是空链表，将_head指向node
			self._head=node
		else:
			#移动到链表尾部
			cur=self._head
			while cur.next!=None:
				cur=cur.next
			#将尾节点cur的next指向node
			cur.next=node
			#将node的prev指向cur
			node.prev=cur
	def search(self,item):
		"""查找元素是否存在"""
		cur=self._head
		while cur!=None:
			if cur.item==item:
				ret=Ture
				break
			cur=cur.next
		if cur==None:
			ret=False
		retun ret


			cur=




