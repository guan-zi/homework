# -*- coding=utf-8 -*-


class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self._head == None

    def length(self):
        if self.is_empty():
            return 0
        cur = self._head
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=" ")
            cur = cur.next
        #退出循环，cur指向尾节点，但是尾节点的
        #元素未打印
        print(cur.elem)

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            #退出循环，cur指向尾节点
            cur.next = node
            node.next = self._head
            self._head = node

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head
            #noed.next = self._head


    def insert(self, pos, item):
        """指定为止添加元素
        :param pos 从零开始"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next

            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self._head
        pre = None

        while cur.next != self._head:
            if cur.elem == item:
                #先判断此节点是否为头节点
                if cur == self._head:
                    #头节点的情况
                    #找尾节点
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    rear.next = cur.next
                    self._head = cur.next
                else:
                    #中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self._head:
                #链表只有一个节点
                self._head = None
            else:
                pre.next = self._head
                #pre.next = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        #退出循环，尾节点cur指向尾节点
        if cur.elem == item:
            return True
        return False


if __name__ == "__main__":
    ll = SingleCycleLinkList()
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
    ll.insert(-1, 9) # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100) # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200) # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()


