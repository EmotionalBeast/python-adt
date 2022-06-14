# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/9
# Copyright (c) 2022 Lazy. All rights reserved.


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return self.items == []

    def enqueue(self, item: any):
        self.items.insert(0, item)

    def dequeue(self) -> any:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def __str__(self):
        return '<Queue> ' + str(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(12)
    q.enqueue(13)
    q.dequeue()
    print(q.is_empty())
    print(q.size())
    q.enqueue('lazy')
    print(q)
