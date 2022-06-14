# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/13
# Copyright (c) 2022 Lazy. All rights reserved.
class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, node):
        self._next = node

    def __str__(self):
        return str(self._data)