# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/10
# Copyright (c) 2022 Lazy. All rights reserved.

from queue.deque import Deque


def is_pal(word):
    d = Deque()
    word_length = len(word)
    for letter in word:
        d.add_rear(letter)
    i = 0
    flag = True
    while i < int(word_length / 2):
        if d.remove_front() != d.remove_rear():
            flag = False
            break
        i += 1
    return flag


if __name__ == '__main__':
    print(is_pal('toot'))
    print(is_pal('radar'))
    print(is_pal('confident'))
