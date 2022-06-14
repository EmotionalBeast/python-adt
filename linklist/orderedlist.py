# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/13
# Copyright (c) 2022 Lazy. All rights reserved.
from linklist.node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    # def add(self, item):
    #     new_node = Node(item)
    #     temp_node = self.head
    #     pre_temp_node = None
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         is_added = False
    #         while temp_node is not None:
    #             if temp_node.data >= item:
    #                 if pre_temp_node is None:
    #                     new_node.set_next(temp_node)
    #                     self.head = new_node
    #                     is_added = True
    #                     break
    #                 else:
    #                     pre_temp_node.set_next(new_node)
    #                     new_node.set_next(temp_node)
    #                     is_added = True
    #                     break
    #             pre_temp_node = temp_node
    #             temp_node = temp_node.next
    #         if not is_added:
    #             pre_temp_node.set_next(new_node)

    def add(self, item):
        """
        循环的2种思维模式：
            1、在循环体中，找到想要的位置直接进行操作
            2、在循环体中，找到想要的位置，break退出，在循环体外处理 （如果判断的条件太多，建议使用这一种方式）
        :param item:
        :return:
        """
        new_node = Node(item)
        temp_node = self.head
        pre_temp_node = None
        while temp_node is not None:
            if temp_node.data >= item:
                break
            pre_temp_node = temp_node
            temp_node = temp_node.next
        if pre_temp_node is None:
            if self.head is None:
                self.head = new_node
            else:
                new_node.set_next(temp_node)
                self.head = new_node
        else:
            pre_temp_node.set_next(new_node)
            new_node.set_next(temp_node)

    def remove(self, item):
        temp_node = self.head
        pre_temp_node = None
        while temp_node is not None:
            if temp_node.data == item:
                break
            pre_temp_node = temp_node
            temp_node = temp_node.next
        if temp_node is None:
            pass
        else:
            if pre_temp_node is None:
                self.head = temp_node.next
            else:
                pre_temp_node.set_next(temp_node.next)

    def exist(self, item):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.data == item:
                return True
            if temp_node.data > item:
                return False
            temp_node = temp_node.next

    def is_empty(self):
        return self.head is None

    def size(self):
        temp_node = self.head
        count = 0
        while temp_node is not None:
            count += 1
            temp_node = temp_node.next
        return count

    def index(self, item):
        temp_node = self.head
        count = 0
        while temp_node is not None:
            if temp_node.data == item:
                return count
            count += 1
            temp_node = temp_node.next

    def pop(self):
        temp_node = self.head
        pre_temp_node = None
        while temp_node.next is not None:
            pre_temp_node = temp_node
            temp_node = temp_node.next
        if pre_temp_node is None:
            self.head = None
        else:
            pre_temp_node.set_next(None)


if __name__ == '__main__':
    l = OrderedList()
    print(l.size())
    print(l.is_empty())
    l.add(1)
    print(l.size())
    l.pop()
    print(l.size())
    l.add(2)
    l.add(1)
    print(l.index(2))
    print(l.exist(1))
    print(l.is_empty())
    l.add(54)
    l.add(45)
    print(l.index(45))
    l.remove(45)
    l.remove(45)
    print(l.exist(45))




