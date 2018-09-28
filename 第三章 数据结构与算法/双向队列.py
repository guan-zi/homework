# -*- coding=utf-8 -*-


class DoubleQueue(object):
    """双端队列"""

    def __init__(self):
        self.__list = []

    def add_rear(self, item):
        """往队列里面添加一个item元素"""
        return self.__list.append(item)

    def add_front(self, item):
        """往队列尾部添加一个元素"""
        return self.__list.insert(0, item)

    def pop_front(self):
        """删除队列头部元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """删除尾部元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(len(self.__list))


if __name__ == "__main__":
    s = DoubleQueue()
    s.add_front(1)
    s.add_front(2)
    s.add_front(3)
    s.add_front(4)
    print(s.pop_rear())
    print(s.pop_rear())
    print(s.pop_rear())
    print(s.pop_rear())
