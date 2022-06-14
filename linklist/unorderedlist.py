# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/10
# Copyright (c) 2022 Lazy. All rights reserved.
from linklist.node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node

    def size(self):
        temp_node = self.head
        count = 0
        while temp_node is not None:
            count += 1
            temp_node = temp_node.next
        return count

    def exist(self, item):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.data == item:
                return True
            temp_node = temp_node.next
        return False

    def remove(self, item):
        temp_node = self.head
        pre_temp_node = None
        while temp_node is not None:
            if temp_node.data == item:
                if pre_temp_node is None:
                    self.head = temp_node.next
                    break
                else:
                    pre_temp_node.set_next(temp_node.next)
                    break
            pre_temp_node = temp_node
            temp_node = temp_node.next

    def append(self, item):
        new_node = Node(item)
        temp_node = self.head
        pre_temp_node = None
        while temp_node is not None:
            pre_temp_node = temp_node
            temp_node = temp_node.next
        if pre_temp_node is None:
            self.head = new_node
        else:
            pre_temp_node.set_next(new_node)

    def index(self, item):
        temp_node = self.head
        count = 0
        while temp_node is not None:
            if temp_node.data == item:
                return count
            temp_node = temp_node.next
            count += 1
        return None

    def insert(self, pos, item):
        new_node = Node(item)
        temp_node = self.head
        pre_temp_node = None
        count = 0
        while temp_node is not None:
            if count == pos:
                if pre_temp_node is None:
                    new_node.set_next(temp_node)
                    self.head = new_node
                    break
                else:
                    new_node.set_next(temp_node)
                    pre_temp_node.set_next(new_node)
                    break
            pre_temp_node = temp_node
            temp_node = temp_node.next
            count += 1

    def pop(self):
        temp_node = self.head
        pre_temp_node = None
        if self.head is None:
            return
        while temp_node.next is not None:
            pre_temp_node = temp_node
            temp_node = temp_node.next
        if pre_temp_node is None:
            self.head = None
        else:
            pre_temp_node.set_next(None)
        return temp_node.data

    def slice(self, start, stop):
        temp_node = self.head
        slice_head = UnorderedList()
        count = 0
        while temp_node is not None:
            if count in range(start, stop):
                slice_head.add(Node(temp_node.data))
            temp_node = temp_node.next
            count += 1
        return slice_head

    def __str__(self):
        temp_node = self.head
        description = 'UnorderedList object <'
        while temp_node is not None:
            value = ' ' + str(temp_node.data) + ' '
            description += value
            temp_node = temp_node.next
        description += '>'
        return description


if __name__ == '__main__':
    # head = Node(1)
    # print(head.data)
    # print(head.next)
    # node_2 = Node(2)
    # head.set_next(node_2)
    # print(head.data)
    # print(head.next)
    l = UnorderedList()
    l.add(1)
    print(l.exist(1))
    l.add(2)
    print(l.size())
    l.insert(1, 3)
    l.add(10)
    l.add(11)
    s = l.slice(1, 4)
    print(s)
    print(s.size())
    print(l.size())
    # print(l.size())
    # print(l.exist(2))
    # print(l.is_empty())
    # print(l.index(2))
    # l.append(3)
    # print(l.index(3))
    # l.insert(1, 4)
    # print(l.index(4))
    # l.pop()
    # print(l.index(3))
    # print(l.size())
