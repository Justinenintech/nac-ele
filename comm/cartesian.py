#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project : nac
# @Author  : Eagle
# @Site    : 
# @File    : cartesian.py
# @Time    : 2021/5/7 12:33
# @Software: PyCharm
import itertools
import weakref


class Cartesian:
    def __init__(self, data: str, use_weakref=None):
        """
        :param data: string
        :param use_weakref: flag for using weak reference
        """
        self.data = data
        self.use_weakref = use_weakref
        self.children = []

    def __repr__(self):
        """
        :return: print A object content
        """
        return '{}'.format(self.data)

    def __del__(self):
        """
        :return: delete massage
        """
        print('{}.__del__'.format(self.data))

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, a):
        """
        :param a: parent object
        :return: self._parent
        """
        if self.use_weakref:
            self._parent = weakref.ref(a)
        else:
            self._parent = a

    def add_child(self, child=None):
        """
        :param child: child object belongs to A class
        :return: self.children = [child]
        child's parent is parent self.
        """
        self.children.append(child)
        # child.parent = self

    def build_161215(self):  # 计算笛卡尔积
        # print('......................2')
        _item_list = []
        for item in itertools.product(*self.children):
            # print('......................3')
            if item[0] != item[1]:
                # print(item)
                # print('......................4')
                _item_list.append(item)
        return _item_list

    def build_161213(self):
        _item_list = []
        for item in itertools.product(*self.children):
            # print('item',item[0],item[1])
            set_list = set(item[1])
            if item[0] not in set_list:
                _item_list.append(item)
        # print(_item_list)
        return _item_list

    def build_duplex(self):
        _item_list = []
        for item in itertools.product(*self.children):
            _item_list.append(item)
        return _item_list

# if __name__ == "__main__":
#     use_weakref = True
#     ns = [['0', '2'], ['0', '6'], ['0', '7'], ['0', '9'], ['2', '6'], ['2', '7'], ['2', '9'], ['6', '7'], ['6', '9'],
#           ['7', '9']]
#     car = Cartesian('child', use_weakref)
#     car.add_child(['1', '2', '3', '4'])
#     car.add_child(ns)
#     # car.add_data([9,10,11,12])
#     print('len',len(car.build_161213()))
