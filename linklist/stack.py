# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/14
# Copyright (c) 2022 Lazy. All rights reserved.
from linklist.unorderedlist import UnorderedList


class Stack:
    def __init__(self):
        self._items = UnorderedList()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        start = self._items.size() - 1
        stop = self._items.size()
        s = self._items.slice(start, stop)
        return s.pop()

    def is_empty(self):
        return self._items.is_empty()

    def size(self):
        return self._items.size()


if __name__ == '__main__':
    test = Stack()
    test.push(1)
    test.push(2)
    print(test.size())
    print(test.pop())
    print(test.pop())
    print(test.pop())
    print(test.is_empty())
    test.push(12)
    print(test.peek())
    test.push(32)
    print(test.peek())
    print(test.is_empty())
    print(test.size())

