# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """链表为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        # cur 游标，用来遍历节点
        count = 0
        # count 用于记录数量
        cur = self._head
        while cur != None:
            count += 1
            cur = cur.next
        print(count)
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node

        else:
            node.next = self._head
            self._head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        count = 1
        cur = self._head
        node = Node(item)
        while cur:
            if count+1 < pos:
                cur = cur.next
                count += 1
                continue
            node.next = cur.next
            cur.next = node
            break

        return "{}位置大于顺序表长度".format(pos)



    def remove(self, item):
        """删除节点"""
        if self.search(item):
            pre = None
            cur = self._head
            while cur:
                if cur.elem != item:
                    pre = cur
                    cur = cur.next
                elif cur.elem == item:
                    print(cur.elem)
                    pre.next = cur.next
                    print(pre.next.elem)
                    break
        return "需要移除的元素不存在"

    def search(self, item):
        """查找制定节点是否存在"""
        if self._head != None:
            cur = self._head
            count = 1
            while cur:
                if cur.elem != item:
                    cur = cur.next
                    count += 1
                else:
                    return count


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    #ll.travel()
    print("-----")
    #ll.add(7)
    #print("----")
    ll.length()
    print("---")
    ll.travel()
    ll.insert(3, 8)
    ll.travel()
    print("#####")
    print(ll.remove(9))
    print("*************")
    ll.travel()
    print(ll.search(6))
