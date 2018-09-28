# -*- coding=utf-8 -*-


class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)


    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
        # 每次打印一个节点，然后判断是否有子节点，
        # 如果有加入队列，待下次循环打印并判断是否有孙节点
            # print('inprelop')
            cur_node = queue.pop(0)
            print(cur_node.elem, end="")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_order(self, node):
        """先序遍历"""
        if node is None:
            #print("the first")
            return
        # 先序遍历一下为固定顺序
        print(node.elem, end=" ")
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node):
        """中序遍历"""
        if node is None:
            return
        # 以下为固定顺序
        self.in_order(node.lchild)
        print(node.elem, end=" ")
        self.in_order(node.rchild)
        #print(node.elem, end=" ")

    def post_order(self, node):
        """后序遍历"""
        if node is None:
            return
        # 后序遍历，以下为固定顺序
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.pre_order(tree.root)
    print(" ")
    tree.in_order(tree.root)
    print(" ")

    tree.breadth_travel()
    tree.post_order(tree.root)
    print(" /")

