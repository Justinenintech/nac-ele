#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project : nac-ele
# @Author  : Eagle
# @Site    : 
# @File    : lru_cache.py
# @Time    : 2021/7/8 0:59
# @Software: PyCharm
from collections import deque
from typing import Any


class LRUCache:
    def __init__(self, cache_size: int):
        """

        :param cache_size:  LRU 队列的大小，超过当前大小时，最近最不常使用的元素将过期
        """
        self.cache_size = cache_size
        self.queue = deque()
        self.hash_map = dict()

    def is_queue_full(self):
        return len(self.queue) == self.cache_size

    def set(self, key: str, value: Any):
        if key not in self.hash_map:
            if self.is_queue_full():
                pop_key = self.queue.pop()
                self.hash_map.pop(pop_key)
                self.queue.appendleft(key)
                self.hash_map[key] = value
            else:
                self.queue.appendleft(key)
                self.hash_map[key] = value

    def get(self, key: str):
        if key not in self.hash_map:
            return -1
        else:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.hash_map[key]