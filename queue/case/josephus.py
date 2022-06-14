# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/9
# Copyright (c) 2022 Lazy. All rights reserved.

from queue.queue import Queue


def hot_potato(num_list, num):
    q = Queue()
    for item in num_list:
        q.enqueue(item)
    i = 0
    while True:
        element = q.dequeue()
        if q.is_empty():
            print(element)
            break
        i += 1
        if i % num == 0:
            print(element)
            continue
        q.enqueue(element)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    hot_potato(nums, 3)

