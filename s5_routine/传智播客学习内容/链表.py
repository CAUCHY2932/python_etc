#单链表节点实现和操作
class SingleNode(object):

	def __init__(self,item):
		self.item=item
		self.next=None

#单链表操作
class SingleLinkList(object):
	"""单链表"""
	def __init__(self):
		self._head = None

	def is_empty(self):
		"""判断链表是否为空"""
		return self._head==None

	def length(self):
		"""链表长度"""
		#cur初始时指向头节点
		cur=self._head
		count=0
		#尾节点指向None,当未到达尾部时
		while cur !=None:
			count+=1

			cur=cur.next

		return count

	def travel(self):
		"""遍历链表"""
		cur=self._head
		while cur != None:
			print(cur.item)
			cur=cur.next
		print("")

	def add(self,item):
		"""头部添加元素"""
		#先创建一个保存item值的节点
		node=SingleNode(item)
		#将新节点的链接域next指向头节点，即_head指向的位置
		node.next=self._head
		#将链表的头_head指向新节点
		self._head=node

	def append(self,item):
		"""尾部添加元素"""
		node=SingleNode(item)
		#先判断链表是否为空，若是空链表，则将_head指向新节点
		if self.is_empty():
			self._head=node
			#若不为空，则找到尾部，将尾节点的next指向新节点
        else:
        	cur=self._head
        	while cur.next !=None:
        		cur.next=node

    def insert(self,pos,item):
    	"""指定位置添加元素"""
    	#若指定位置pos为第一个元素之前，则执行头部插入
        if pos <=0:
        	self.add(item)
        #若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        #找到指定位置
        else:
        	node=SingleNode(item)
        	count=0
        	#pre用来指向指定位置pos的前一个位置的pos-1,初始从头节点开始移动到指定位置
        	pre=self._head
        	while count <(pos-1):
        		count+=1
        		pre=pre.next

        	#先将新节点node的next指向插入位置的节点
        	node.next=pre.next
        	pre.next=node

    def remove(self,item):
    	"""删除节点"""
    	cur=self._head
    	pre=None
    	while cur != None:
    		#找到了指定元素
    		if cur.item==item:
    			#如果第一个就是删除的节点
    			

            



