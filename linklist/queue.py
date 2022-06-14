# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/14
# Copyright (c) 2022 Lazy. All rights reserved.
from linklist.unorderedlist import UnorderedList


class Queue:
    def __init__(self):
        self._items = UnorderedList()

    def enqueue(self, item):
        self._items.add(item)

    def dequeue(self):
        return self._items.pop()

    def is_empty(self):
        return self._items.is_empty()

    def size(self):
        return self._items.size()


