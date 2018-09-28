# -*- coding=utf-8 -*-

class Node(object):
    """结点"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """链表是否为空"""
        return self._head == None
        # 如果链表为空self._head == None \
        # 为真，否在为假与是否为空情况相同

    def length(self):
        """链表长度"""
        # cur 游标，用来遍历节点
        cur = self._head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self._head
        self._head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next

            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素
        ：para pos 从0开始"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self._head
            count = 0
            node = Node(item)

            while count < pos:
                count += 1
                cur = cur.next
            #将上一个节点与待插入节点链接（双向）
            node.prev = cur.prev
            cur.prev.next = node
            #将原节点与插入节点链接（双向）
            cur.prev = node
            node.next = cur

    def remove(self, item):
        """删除节点"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头节点
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:
                        #判断链表是否只有一个元素
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                    #判断是否是链表最后一个元素
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self._head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next

        return False


if __name__ == "__main__":
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)  # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100)  # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200)  # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
