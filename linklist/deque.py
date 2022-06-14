# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/14
# Copyright (c) 2022 Lazy. All rights reserved.
from linklist.unorderedlist import UnorderedList


class Deque:
    def __init__(self):
        self._items = UnorderedList()

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.add(item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        s = self._items.slice(0, 1)
        item = s.pop()
        self._items.remove(item)
        return item

    def is_empty(self):
        return self._items.is_empty()

    def size(self):
        return self._items.size()


if __name__ == '__main__':
    d = Deque()
    d.add_front(1)
    d.add_rear(2)
    print(d.remove_rear())
