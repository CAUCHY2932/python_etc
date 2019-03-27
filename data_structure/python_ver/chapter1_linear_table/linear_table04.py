# coding:utf-8
__author__ = 'young'


class SingleNode:
    """
    :define a single node link list

    """

    def __init__(self, item):
        # item to store the data item
        self.item = item
        # next is next node signature
        self.next = None


class SingleLinkList:
    """
    :define a single link list

    """

    def __init__(self):
        self._head = None

    def is_empty(self):
        """
            judge a link list is empty or not

        """
        return self._head is None

    @property
    def length(self):
        """
        :get the link list length
        """
        # cur is head to head node when it is initial
        cur = self._head
        count = 0
        # tail node head to None and not achieve to tail
        while cur is not None:
            count += 1
            # put the cur node back
            cur = cur.next
            return count

    def travel(self):
        """
        : travel the link list

        """
        cur = self._head
        while cur is not None:
            print(cur.item)
            cur = cur.next
            print('')

    def add(self, item):
        """
        : add node to head
        """
        # create a node to store the item value
        node = SingleNode(item)
        # put the next field to head node
        node.next = self._head
        # put the head field to the new node
        self._head = node

    def append(self, item):
        """
        : add node to the tail
        """
        node = SingleNode(item)
        # judge the link is empty or not, if empty, put head to the new
        # node
        if self.is_empty():
            self._head = node
        # if not empty, find the tail, and put next of tail node to new node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """
        : insert item in position
        """
        # if pos is the first node forward, insert the head
        if pos <= 0:
            self.add(item)
        # if pos excess link length, insert the tail
        elif pos > self.length - 1:
            self.append(item)
        # find the insert position
        else:
            node = SingleNode(item)
            count = 0
            # pre is design to head to the pos-1, and move from start to end
            # when it is initial
            pre = self._head
            while count < pos - 1:
                count += 1
                pre = pre.next
            # arrange the next filed value to insert pos
            node.next = pre.next
            # put the pos-1 next filed value to new node
            pre.next = node

        def remove(self):
            """
            delete a node
            cur is represent to the address of node

            """
            cur = self._head
            pre = None
            while cur != None:
                # find item
                if cur.item == item:
                    if not pre:
                        self._head = cur.next
                    else:
                        pre.next = cur.next
                    break
                else:
                    pre = cur
                    cur = cur.next
