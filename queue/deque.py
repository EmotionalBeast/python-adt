# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/10
# Copyright (c) 2022 Lazy. All rights reserved.

class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item: any):
        self.items.append(item)

    def add_rear(self, item: any):
        self.items.insert(0, item)

    def remove_front(self) -> any:
        return self.items.pop()

    def remove_rear(self) -> any:
        return self.items.pop(0)

    def is_empty(self) -> bool:
        return self.items == []

    def size(self) -> int:
        return len(self.items)

    def __str__(self):
        return '<deque> ' + str(self.items)


if __name__ == '__main__':
    d = Deque()
    d.add_front(1)
    d.add_rear(2)
    d.add_front(3)
    print(d)
    print(d.remove_front())
    print(d.remove_rear())
    print(d.remove_front())
    print(d)
