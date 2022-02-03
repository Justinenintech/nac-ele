#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project : nac-ele
# @Author  : Eagle
# @Site    : 
# @File    : split.py
# @Time    : 2021/6/27 23:20
# @Software: PyCharm
import itertools as it

from typing import List, Dict

import numpy as np

from comm.tool import Tools


class Split(object):
    @staticmethod
    def split_101210(nums: List[str], value: str) -> list:
        """
        五星-不定位-二码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter)):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_101211(nums: List[str], value: str) -> list:
        """
        五星-不定位-三码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter)):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_111210(nums: List[str], value: str) -> list:
        """
        四星-不定位-后四一码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[-4:])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_111211(nums: List[str], value: str) -> list:
        """
        四星-不定位-后四二码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[-4:])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_111212(nums: List[str], value: str) -> list:
        """
        四星-不定位-前四一码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[:4])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_111213(nums: List[str], value: str) -> list:
        """
        四星-不定位-前四二码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[:4])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121114(nums: List[str], value: str) -> list:
        """
        三星	组选	前三组选包胆	从0-9中任意选择1个包胆号码，开奖号码的万位、千位、百位中任意1位只要和所选包胆号码相同(不含豹子号)，即为中奖。
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for parameter in set(nums):
            [tlt.setdefault(i, parameter[:3].count(i)) for i in parameter[:3]]
            # print('tlt',tlt)
            if set(value).issubset(set(parameter[:3])) and max(set(tlt.values())) < 3:
                heap.append(parameter)
            tlt.clear()
        return heap

    @staticmethod
    def split_121121(nums: List[str], value: str) -> list:
        """
        三星	组选	后三组选包胆	从0-9中任意选择1个包胆号码，开奖号码的万位、千位、百位中任意1位只要和所选包胆号码相同(不含豹子号)，即为中奖。
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for parameter in set(nums):
            [tlt.setdefault(i, parameter[-3:].count(i)) for i in parameter[-3:]]
            # print('tlt',tlt)
            if set(value).issubset(set(parameter[-3:])) and max(set(tlt.values())) < 3:
                heap.append(parameter)
            tlt.clear()
        return heap

    @staticmethod
    def split_121128(nums: List[str], value: str) -> list:
        """
        三星	组选	中三组选包胆	从0-9中任意选择1个包胆号码，开奖号码的万位、千位、百位中任意1位只要和所选包胆号码相同(不含豹子号)，即为中奖。
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for parameter in set(nums):
            [tlt.setdefault(i, parameter[1:4].count(i)) for i in parameter[1:4]]
            # print('tlt',tlt)
            if set(value).issubset(set(parameter[1:4])) and max(set(tlt.values())) < 3:
                heap.append(parameter)
            tlt.clear()
        return heap

    @staticmethod
    def split_121210(nums: List[str], value: str) -> list:
        """
        三星-不定位-中三一码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[1:4])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121211(nums: List[str], value: str) -> list:
        """
        三星-不定位-中三-二码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[1:4])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121212(nums: List[str], value: str) -> list:
        """
        三星-不定位-前三一码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[:3])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121213(nums: List[str], value: str) -> list:
        """
        三星-不定位-前三二码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[:3])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121214(nums: List[str], value: str) -> list:
        """
        三星-不定位-后三一码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[-3:])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121215(nums: List[str], value: str) -> list:
        """
        三星-不定位-后三二码不定位，8，****2
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            if set(value).issubset(set(parameter[-3:])):
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121113(nums: List[str], value: str) -> list:
        """
        三星	组选	前三混合组选	手动输入一个3位数号码组成一注(不含豹子号)，开奖号码的万位、千位、百位符合前三组三或组六均为中奖。
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            ls1 = list(value)
            ls1.sort()
            # print('ls1',ls1)
            ls2 = list(parameter[:3])
            ls2.sort()
            # print('ls2', ls2)
            if ls1 == ls2:
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121120(nums: List[str], value: str) -> list:
        """
        三星	组选	后三混合组选	手动输入一个3位数号码组成一注(不含豹子号)，开奖号码的万位、千位、百位符合前三组三或组六均为中奖。
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            ls1 = list(value)
            ls1.sort()
            # print('ls1',ls1)
            ls2 = list(parameter[-3:])
            ls2.sort()
            # print('ls2', ls2)
            if ls1 == ls2:
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_121127(nums: List[str], value: str) -> list:
        """
        三星	组选	中三混合组选	手动输入一个3位数号码组成一注(不含豹子号)，开奖号码的万位、千位、百位符合前三组三或组六均为中奖。
        :param nums:
        :param value:
        :return: List or Ture
        """
        _lis = []
        for parameter in set(nums):
            ls1 = list(value)
            ls1.sort()
            # print('ls1',ls1)
            ls2 = list(parameter[1:4])
            ls2.sort()
            # print('ls2', ls2)
            if ls1 == ls2:
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_161013(nums: List[str], *args) -> list:
        """
        任选-任选二-组二复式，选择2个号码1、8，组成118和188
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        _lis = []
        for parameter in set(nums):
            is_three = (parameter[args[0]] + parameter[args[1]])

            ls1 = list(is_three)
            ls2 = list(map(str, args[2][0]))
            ls1.sort()
            ls2.sort()
            if ls1 == ls2:
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_161014(nums: List[str], *args) -> list:
        """
        任选-任选二-组二单式，选择2个号码1、8，组成18和18
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        _lis = []
        for parameter in set(nums):
            is_three = (parameter[args[0]] + parameter[args[1]])

            ls1 = list(is_three)
            ls2 = list(map(str, args[2][0]))
            ls1.sort()
            ls2.sort()
            if ls1 == ls2:
                _lis.append(parameter)
        return _lis

    @staticmethod
    def split_161110(nums: List[str], *args) -> list:
        """
        任选-任选三-直选复式
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_eq = (num[args[0]] + num[args[1]] + num[args[2]]) == str(args[3])
            if is_eq:
                heap.append(num)
        return heap

    @staticmethod
    def split_161111(nums: List[str], *args) -> list:
        """
        任选-任选三-直选单式，
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_eq = (num[args[0]] + num[args[1]] + num[args[2]]) == str(args[3])
            if is_eq:
                heap.append(num)
        return heap

    @staticmethod
    def get_bet_number_161112(num):
        is_num = {
            '0': 1,
            '1': 3,
            '2': 6,
            '3': 10,
            '4': 15,
            '5': 21,
            '6': 28,
            '7': 36,
            '8': 45,
            '9': 55,
            '10': 63,
            '11': 69,
            '12': 73,
            '13': 75,
            '14': 75,
            '15': 73,
            '16': 69,
            '17': 63,
            '18': 55,
            '19': 45,
            '20': 36,
            '21': 28,
            '22': 21,
            '23': 15,
            '24': 10,
            '25': 6,
            '26': 3,
            '27': 1

        }
        return is_num.get(num)

    @staticmethod
    def split_161112(nums: List[str], *args) -> list:
        """
        任选-任选三-直选和值，3个位置之和
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_sum = (int(num[args[0]]) + int(num[args[1]]) + int(num[args[2]])) == args[3]
            if is_sum:
                heap.append(num)
        return heap

    @staticmethod
    def split_161113(nums: List[str], *args) -> list:
        """
        任选-任选三-组三复式，选择2个号码1、8，组成118和188
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_three = (num[args[0]] + num[args[1]] + num[args[2]])
            is_count = (is_three.count(args[3]) == 2 and is_three.count(args[4]) == 1) or (
                    is_three.count(args[3]) == 1 and is_three.count(args[4]) == 2)
            if is_count:
                heap.append(num)
        return heap

    @staticmethod
    def split_161114(nums: List[str], *args) -> list:
        """
        任选-任选三-组三单式，输入3个号码118，组成118
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_three = (num[args[0]] + num[args[1]] + num[args[2]])
            is_count = (is_three.count(args[3]) == 2 and is_three.count(args[4]) == 1)
            if is_count:
                heap.append(num)
        return heap

    @staticmethod
    def get_bet_number_161115(num):
        is_num = {
            '1': 1,
            '2': 2,
            '3': 2,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 8,
            '8': 10,
            '9': 11,
            '10': 13,
            '11': 14,
            '12': 14,
            '13': 15,
            '14': 15,
            '15': 14,
            '16': 14,
            '17': 13,
            '18': 11,
            '19': 10,
            '20': 8,
            '21': 6,
            '22': 5,
            '23': 4,
            '24': 2,
            '25': 2,
            '26': 1

        }
        return is_num.get(num)

    @staticmethod
    def split_161115(nums: List[str], *args) -> list:
        """
        任选-任选三-组选和值，3个位置之和，不含豹子号
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        leopard = {}
        for num in set(nums):
            is_sum = (int(num[args[0]]) + int(num[args[1]]) + int(num[args[2]])) == args[3]
            is_leopard = num[args[0]] == num[args[1]] == num[args[2]] and num[args[0]] == num[args[2]]
            # [leopard.setdefault(i, is_str.count(i)) for i in is_str]  # 重复次数统计，字典形式
            # is_leopard = leopard.get(''.join(leopard.keys())) == 3  # 判断重复次数等于3，则为豹子号
            if is_sum and not is_leopard:
                heap.append(num)
        return heap

    @staticmethod
    def split_161116(nums: List[str], *args) -> list:
        """
        任选-任选三-组六复式，选择3个号码0,1,2，顺序不限
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_three = (num[args[0]] + num[args[1]] + num[args[2]])
            is_count = is_three.count(args[3], 0, len(is_three)) == 1 and is_three.count(args[4], 0, len(
                is_three)) == 1 and is_three.count(args[5], 0, len(is_three)) == 1
            if is_count:
                heap.append(num)
        return heap

    @staticmethod
    def split_161117(nums: List[str], *args) -> list:
        """
        任选-任选三-组六单式，选择3个号码0,1,2，顺序不限
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_three = (num[args[0]] + num[args[1]] + num[args[2]])
            is_count = is_three.count(args[3], 0, len(is_three)) == 1 and is_three.count(args[4], 0, len(
                is_three)) == 1 and is_three.count(args[5], 0, len(is_three)) == 1
            if is_count:
                heap.append(num)
        return heap

    @staticmethod
    def split_161118(nums: List[str], *args) -> list:
        """
        任选-任选三-混合组选，选择3个号码0,1,2，顺序不限
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_three = (num[args[0]] + num[args[1]] + num[args[2]])
            clt = {}
            str_three = (args[3] + args[4] + args[5])
            [clt.setdefault(i, str_three.count(i)) for i in str_three]
            if 2 in clt.values():
                new_clt = {v: k for k, v in clt.items()}
                is_ds = is_three.count(new_clt.get(2), 0, len(is_three)) == 2 and is_three.count(new_clt.get(1), 0,
                                                                                                 len(is_three)) == 1
                if is_ds:
                    heap.append(num)
            else:
                is_count = is_three.count(args[3], 0, len(is_three)) == 1 and is_three.count(args[4], 0, len(
                    is_three)) == 1 and is_three.count(args[5], 0, len(is_three)) == 1
                if is_count:
                    heap.append(num)
        return heap

    @staticmethod
    def split_161210(nums: List[str], *args) -> list:
        """
        任选-任选四-直选复式
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_eq = (num[args[0]] + num[args[1]] + num[args[2]] + num[args[3]]) == str(args[4])
            if is_eq:
                heap.append(num)
        return heap

    @staticmethod
    def split_161211(nums: List[str], *args) -> list:
        """
        任选-任选四-直选单式
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_eq = (num[args[0]] + num[args[1]] + num[args[2]] + num[args[3]]) == str(args[4])
            if is_eq:
                heap.append(num)
        return heap

    @staticmethod
    def split_161212(nums: List[str], *args) -> list:
        """
        任选-任选四-组选24，选择4个号码0123，顺序不限
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标 以及四个数字
        :return: list
        """
        heap = []
        for num in set(nums):
            is_four = (num[args[0]] + num[args[1]] + num[args[2]] + num[args[3]])
            is_count = is_four.count(args[4], 0, len(is_four)) == 1 and is_four.count(args[5], 0, len(
                is_four)) == 1 and is_four.count(args[6], 0, len(is_four)) == 1 and is_four.count(args[7], 0,
                                                                                                  len(is_four)) == 1
            if is_count:
                heap.append(num)
        return heap

    @staticmethod
    def split_161213(nums: List[str], *args) -> list:
        """
        任选-任选四-组选12，从万位、千位、百位、十位、个位中任意勾选四个位置，然后从0-9中选择2个二重号组成一注，所选4个位置的开奖号码与所选号码一致，并且所选的2个二重号码在所选4个位置的开奖号码中分别出现了2次，顺序不限，即为中奖。
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            is_four = (num[args[0]] + num[args[1]] + num[args[2]] + num[args[3]])
            # [tlt.setdefault(i, num.count(i)) for i in is_four]
            first_count = is_four.count(str(args[4]), 0, len(is_four))
            # second_count = is_four.count(str(args[5]), 0, len(is_four))
            is_equal = first_count == 2 and set(args[5]).issubset(is_four)
            if is_equal:
                heap.append(num)
            tlt.clear()
        return heap

    @staticmethod
    def split_161214(nums: List[str], *args) -> list:
        """
        任选-任选四-组选6，选择2个号码01，顺序不限
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            is_four = (num[args[0]] + num[args[1]] + num[args[2]] + num[args[3]])
            # [tlt.setdefault(i, num.count(i)) for i in is_four]
            first_count = is_four.count(str(args[4]), 0, len(is_four))
            second_count = is_four.count(str(args[5]), 0, len(is_four))
            is_equal = first_count == 2 and second_count == 2
            if is_equal:
                heap.append(num)
            tlt.clear()
        return heap

    @staticmethod
    def split_161215(nums: List[str], *args) -> list:
        """
        任选-任选四-组选4，从万位、千位、百位、十位、个位中任意勾选四个位置，然后从0-9中选择1个三重号和1个单号组成一注，所选4个位置的开奖号码与所选号码一致，并且所选三重号码在所选4个位置的开奖号码中出现了3次，顺序不限，即为中奖。
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            is_four = (num[args[0]] + num[args[1]] + num[args[2]] + num[args[3]])
            # [tlt.setdefault(i, num.count(i)) for i in is_four]
            first_count = is_four.count(str(args[4]), 0, len(is_four))
            # second_count = is_four.count(str(args[5]), 0, len(is_four))
            is_equal = first_count == 3 and set(args[5]).issubset(is_four)
            if is_equal:
                heap.append(num)
            tlt.clear()
        return heap

    @staticmethod
    def split_171010(nums: List[str], *args) -> list:
        """
        根据万位、千位的数值比大小。万位号码大于千位号码为龙，千位号码大于万位号码为虎，号码相同则为和。开奖形态与开奖形态一致，即为中奖。（万百、万十、万个、千百、千十、千个、百十、百个、十个同理）
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """

        heap = []
        for num in set(nums):
            is_dict = {'龙': num[args[0]] > num[args[1]],
                       '虎': num[args[0]] < num[args[1]],
                       '和': num[args[0]] == num[args[1]]
                       }
            if is_dict.get(args[2]):
                heap.append(num)
        return heap

    @staticmethod
    def split_171110(nums: List[str], *args) -> list:
        """
        万位、千位的数值之和的个位，范围（0-4）为小，范围（5-9）为大，（13579）为单，（02468）为双。所选类型一致即为中奖（万百、万十、万个、千百、千十、千个、百十、百个、十个同理）
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        idle_dict: Dict[str, list] = {
            '大': [5, 6, 7, 8, 9],
            '小': [0, 1, 2, 3, 4],
            '单': [1, 3, 5, 7, 9],
            '双': [0, 2, 4, 6, 8]
        }

        heap = []
        for num in set(nums):
            if (int(num[args[0]]) + int(num[args[1]])) % 10 in idle_dict.get(args[2]):
                heap.append(num)
        return heap

    @staticmethod
    def split_121410x12(nums: List[str], type_idx, type_num) -> list:
        """
        三星	大小单双	前三大小单双 中三大小单双 后三大小单双	对万位、千位和百位的“大（56789）小（01234）、单（13579）双（02468）”形态进行购买，所选号码的位置、形态与开奖号码的位置、形态相同，即为中奖。
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        idle_dict: Dict[str, list] = {
            '大': [5, 6, 7, 8, 9],
            '小': [0, 1, 2, 3, 4],
            '单': [1, 3, 5, 7, 9],
            '双': [0, 2, 4, 6, 8]
        }

        heap = []
        for num in set(nums):
            type_dict = {
                '前三': num[0] + num[1] + num[2],
                '中三': num[1] + num[2] + num[3],
                '后三': num[2] + num[3] + num[4]
            }
            if int(type_dict.get(type_idx)[0]) in idle_dict.get(type_num[0]) and int(
                    type_dict.get(type_idx)[1]) in idle_dict.get(type_num[1]) and int(
                type_dict.get(type_idx)[2]) in idle_dict.get(type_num[2]):
                heap.append(num)
        return heap

    @staticmethod
    def split_131410x11(nums: List[str], type_idx, type_num) -> list:
        """
        二星 大小单双	前二大小单双	后二大小单双 对万位和千位“大（56789）小（01234）、单（13579）双（02468）”形态进行购买，所选号码的位置、形态与开奖号码的位置、形态相同，即为中奖。
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        idle_dict: Dict[str, list] = {
            '大': [5, 6, 7, 8, 9],
            '小': [0, 1, 2, 3, 4],
            '单': [1, 3, 5, 7, 9],
            '双': [0, 2, 4, 6, 8]
        }

        heap = []
        for num in set(nums):
            type_dict = {
                '前二': num[0] + num[1],
                # '中三': num[1] + num[2] + num[3],
                '后二': num[3] + num[4]
            }
            if int(type_dict.get(type_idx)[0]) in idle_dict.get(type_num[0]) and int(
                    type_dict.get(type_idx)[1]) in idle_dict.get(type_num[1]):
                heap.append(num)
        return heap

    @staticmethod
    def split_181010(nums: List[str], *args) -> list:
        """
        新龙虎（龙虎），根据万位、千位的数值比大小。万位号码大于千位号码为龙，千位号码大于万位号码为虎，号码相同则自动撤单。开奖形态与开奖形态一致，即为中奖。（万百、万十、万个、千百、千十、千个、百十、百个、十个同理）
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """

        heap = []
        for num in set(nums):
            is_dict = {'龙': num[args[0]] > num[args[1]] or num[args[0]] == num[args[1]],
                       '虎': num[args[0]] < num[args[1]] or num[args[0]] == num[args[1]]
                       # '和': num[args[0]] == num[args[1]]
                       }
            if is_dict.get(args[2]):
                heap.append(num)
        return heap

    @staticmethod
    def split_201010(nums: List[str]) -> list:
        """
        棋牌-德州扑克-豹子，即开出的五个号码都相同。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            [tlt.setdefault(i, num.count(i)) for i in num]
            if 5 in set(tlt.values()):
                heap.append(num)
            tlt.clear()
        return heap

    @staticmethod
    def not_adjacent(numbers: List[str]) -> list:
        """
        获取不相邻的数据
        :param numbers:数组
        :return:
        """
        _ls1, _ls2 = ([] for i in range(2))
        for num in set(numbers):
            combination = list(it.combinations(num, 2))
            for comb in set(combination):
                _ls1.append(int(max(comb)) - int(min(comb)) not in [1, 9])
            if all(_ == True for _ in _ls1):
                _ls2.append(num)
            _ls1.clear()
        return _ls2

    def split_201011(self, nums: List[str]) -> list:
        """
        棋牌-德州扑克-五离，即开出的五个号码不能够组成对子，并且没有任何相邻的两个数。如：28064，19573。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            [tlt.setdefault(i, num.count(i)) for i in num]
            if max(set(tlt.values())) == 1:
                heap.append(num)
            tlt.clear()
        results = self.not_adjacent(heap)
        return results

    @staticmethod
    def split_201012(nums: List[str]) -> list:
        """
        棋牌-德州扑克-四张，即五个开奖号码中有四个为一样，如00001、77797。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            [tlt.setdefault(i, num.count(i)) for i in num]
            if max(set(tlt.values())) == 4:
                heap.append(num)
            tlt.clear()
        return heap

    @staticmethod
    def split_201013(nums: List[str]) -> list:
        """
        棋牌-德州扑克-葫芦，即五个开奖号码中三个相同（三条）及两个号码相同（一对），如77997、45544。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            [tlt.setdefault(i, num.count(i)) for i in num]
            if max(set(tlt.values())) == 3 and min(set(tlt.values())) == 2:
                heap.append(num)
            tlt.clear()
        return heap

    @staticmethod
    def leopard(nums: List[str], types: str) -> list:
        """
        双面盘-前三|中三|后三-豹子，万千百位同号，例如：111、222。----如开奖号码的三位数字相同，则视为中奖
        :param types: 前三|中三|后三
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            type_dict = {
                '前三': num[0] + num[1] + num[2],
                '中三': num[1] + num[2] + num[3],
                '后三': num[2] + num[3] + num[4]
            }
            [tlt.setdefault(i, type_dict.get(types).count(i)) for i in type_dict.get(types)]
            if 3 in set(tlt.values()):
                heap.append(num)
            tlt.clear()
        return heap

    @staticmethod
    def straight_semi_smooth(numbers: List[str], types: str, ran: int) -> list:
        """
        双面盘-前三|中三|后三 - 顺子，获取顺子数据的方法:万千百位相连，不分顺序。----如开奖号码为123、901、321、546等，则视为中奖
        双面盘-前三|中三|后三 - 半顺，万千百位任意两位数字相连，不分顺序（不包括顺子、对子）。----如开奖号码为125、540、390、706，则视为中奖。如果开奖号码为顺子、对子,则投注半顺视为不中奖
        :param ran: ran:1 半顺，ran：2 顺子
        :param numbers: 10W条5位数数组
        :param types:前三|中三|后三
        :return:list
        """
        _tlt, _clc = ({} for j in range(2))
        _ls1, _ls2 = ([] for i in range(2))
        for num in set(numbers):
            type_dict: Dict[str, str] = {
                '前三': num[0] + num[1] + num[2],
                '中三': num[1] + num[2] + num[3],
                '后三': num[2] + num[3] + num[4]
            }
            combination = list(it.combinations(type_dict.get(types), 2))
            for comb in set(combination):
                _ls1.append(int(max(comb)) - int(min(comb)) in [1, 9])
            [_tlt.setdefault(i, _ls1.count(i)) for i in _ls1]
            [_clc.setdefault(i, type_dict.get(types).count(i)) for i in type_dict.get(types)]
            if _tlt.get(True) == ran and max(_clc.values()) == 1:
                _ls2.append(num)
            _ls1.clear()
            _tlt.clear()
            _clc.clear()
        return _ls2

    @staticmethod
    def miscellaneous(numbers: List[str], types: str) -> list:
        """
        双面盘-前三|中三|后三 - 杂六，千百十位不包括豹子、顺子、对子、半顺的所有开奖号码形态。----如中奖号码为157，中奖号码位数之间无关联性，则视为中奖
        :param numbers: 10W条5位数数组
        :param types:前三|中三|后三
        :return:list
        """
        _tlt, _clc = ({} for j in range(2))
        _ls1, _ls2 = ([] for i in range(2))
        for num in set(numbers):
            type_dict = {
                '前三': num[0] + num[1] + num[2],
                '中三': num[1] + num[2] + num[3],
                '后三': num[2] + num[3] + num[4]
            }
            combination = list(it.combinations(type_dict.get(types), 2))
            for comb in set(combination):
                _ls1.append(int(max(comb)) - int(min(comb)) not in [0, 1, 9])
            [_tlt.setdefault(i, _ls1.count(i)) for i in _ls1]
            [_clc.setdefault(i, type_dict.get(types).count(i)) for i in type_dict.get(types)]
            if _tlt.get(True) == 3 and max(_clc.values()) == 1:
                _ls2.append(num)
            _ls1.clear()
            _tlt.clear()
            _clc.clear()
        return _ls2

    @staticmethod
    def pair(nums: List[str], types: str) -> list:
        """
        双面盘-前三|中三|后三-对子，万千百位任意两位数字相同（不包括豹子）。----如开奖号码为001，112、696，则视为中奖。如果开奖号码为豹子,则投注对子视为不中奖。
        :param types: 前三|中三|后三
        :param nums: 10W条5位数的数组
        :return: list
        """
        _tlt, _clc = ({} for _ in range(2))
        heap = []
        for num in set(nums):
            type_dict = {
                '前三': num[0] + num[1] + num[2],
                '中三': num[1] + num[2] + num[3],
                '后三': num[2] + num[3] + num[4]
            }
            [_clc.setdefault(i, type_dict.get(types).count(i)) for i in type_dict.get(types)]
            second_str = ''.join(list(map(str, _clc.values())))
            [_tlt.setdefault(i, second_str.count(i)) for i in second_str]
            is_count = int(max(_tlt.keys())) == 2 and int(min(_tlt.keys())) == 1
            if is_count:
                heap.append(num)
            _tlt.clear()
            _clc.clear()
        return heap

    @staticmethod
    def straight(numbers: List[str]) -> list:
        """
        棋牌-德州扑克-获取顺子数据的方法
        :param numbers:
        :return:
        """
        _tlt, _clc = ({} for j in range(2))
        _ls1, _ls2 = ([] for i in range(2))
        for num in set(numbers):

            combination = list(it.combinations(num, 2))
            for comb in set(combination):
                _ls1.append(int(max(comb)) - int(min(comb)) in [1, 9])
            [_tlt.setdefault(i, _ls1.count(i)) for i in _ls1]
            [_clc.setdefault(i, num.count(i)) for i in num]
            if _tlt.get(True) == 4 and max(_clc.values()) == 1:
                _ls2.append(num)
            _ls1.clear()
            _tlt.clear()
            _clc.clear()
        return _ls2

    def split_201014(self, nums: List[str]) -> list:
        """
        棋牌-德州扑克-顺子，即开出的五个号码是一串顺序的数字。09213、65743。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        results = self.straight(nums)
        return results

    @staticmethod
    def split_201015(nums: List[str]) -> list:
        """
        棋牌-德州扑克-三张，即开出的五个号码中三个相同，且余下的两个号码完全不同，如：87477、65455。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        tlt = {}
        heap = []
        for num in set(nums):
            [tlt.setdefault(i, num.count(i)) for i in num]
            if max(set(tlt.values())) == 3 and min(set(tlt.values())) == 1:
                heap.append(num)
            tlt.clear()
        return heap

    @staticmethod
    def split_201016(nums: List[str]) -> list:
        """
        棋牌-德州扑克-两对，即开奖五个号码，能组成两个对子，如：97789、01022。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        _tlt, _clc = ({} for _ in range(2))
        heap = []
        for num in set(nums):
            [_clc.setdefault(i, num.count(i)) for i in num]
            second_str = ''.join(list(map(str, _clc.values())))
            [_tlt.setdefault(i, second_str.count(i)) for i in second_str]
            is_count = second_str.count(str(max(_tlt.values())), 0, len(second_str)) == 2 and second_str.count(
                str(min(_tlt.values())), 0, len(second_str)) == 1
            if is_count:
                heap.append(num)
            _tlt.clear()
            _clc.clear()
        return heap

    # @staticmethod
    def split_201017(self, nums: List[str]) -> list:
        """
        棋牌-德州扑克-杂牌，即开出的五个号码全部都不一样，不能够组成任意对子、顺子或五离，如：06587、98763。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        _tlt, _clc = ({} for _ in range(2))
        heap = []
        straights = self.straight(nums)
        adjacent = self.split_201011(nums)
        for num in set(nums):
            [_clc.setdefault(i, num.count(i)) for i in num]
            second_str = ''.join(list(map(str, _clc.values())))
            [_tlt.setdefault(i, second_str.count(i)) for i in second_str]
            if max(_tlt.values()) == 5:
                heap.append(num)
            _tlt.clear()
            _clc.clear()
        result1 = set(heap).symmetric_difference(set(straights))

        results = result1.symmetric_difference(set(adjacent))
        return list(results)

    @staticmethod
    def split_201018(nums: List[str]) -> list:
        """
        棋牌-德州扑克-一对，即开出的五个号码，能够组成一个对子，如：65877、01322。所选类型一致即为中奖
        :param nums: 10W条5位数的数组
        :return: list
        """
        _tlt, _clc = ({} for _ in range(2))
        heap = []
        for num in set(nums):
            [_clc.setdefault(i, num.count(i)) for i in num]
            second_str = ''.join(list(map(str, _clc.values())))
            [_tlt.setdefault(i, second_str.count(i)) for i in second_str]
            if max(_tlt.values()) == 3 and min(_tlt.values()) == 1:
                heap.append(num)
            _tlt.clear()
            _clc.clear()
        return heap

    @staticmethod
    def is_there_cattle(nums: List[str]) -> list:
        """
        判断是否有牛
        :return: 返回所有符合有牛的数据
        """
        ls = []
        _clc = {}
        three_ls = []
        for num in set(nums):
            [_clc.setdefault(i, num.count(i)) for i in num]
            for i in list(it.combinations(num, 3)):
                three_ls.append(sum(list(map(int, i))))
            if 10 in three_ls or 20 in three_ls or (0 in three_ls and _clc.get('0') >= 3):
                ls.append(num)
            three_ls.clear()
            _clc.clear()
        return ls

    @staticmethod
    def split_201211(nums: List[str]) -> list:
        """
        判断是否有牛
        :return: 返回所有符合有牛的数据
        """
        ls = []
        _clc = {}
        three_ls = []
        for num in set(nums):
            [_clc.setdefault(i, num.count(i)) for i in num]
            for i in list(it.combinations(num, 3)):
                three_ls.append(sum(list(map(int, i))))
            if 10 in three_ls or 20 in three_ls or (0 in three_ls and _clc.get('0') >= 3):
                ls.append(num)
            three_ls.clear()
            _clc.clear()
        result = list(set(nums).symmetric_difference(set(ls)))
        return result

    def split_201210(self, nums: List[str], cattle_type: str) -> list:

        cattle = self.is_there_cattle(nums)
        ls = []
        cattle_dict = {
            '牛牛': 0,
            '牛1': 1,
            '牛2': 2,
            '牛3': 3,
            '牛4': 4,
            '牛5': 5,
            '牛6': 6,
            '牛7': 7,
            '牛8': 8,
            '牛9': 9,
        }

        for value in cattle:
            for v in list(it.combinations(value, 5)):
                # print(sum(tuple(map(int, v))))
                if sum(list(map(int, v))) >= 30:
                    if sum(list(map(int, v))) % 30 == cattle_dict.get(cattle_type):
                        ls.append(value)
                elif sum(list(map(int, v))) >= 20 and sum(
                        list(map(int, v))) < 30:  # sum(tuple(map(int, v))) >= 20 and sum(tuple(map(int, v))) < 30
                    if sum(list(map(int, v))) % 20 == cattle_dict.get(cattle_type):
                        ls.append(value)
                else:
                    if sum(list(map(int, v))) % 10 == cattle_dict.get(cattle_type):
                        ls.append(value)
        return ls

    @staticmethod
    def san_gong_sum(nums):
        """
        三公-和
        :param nums:
        :return:
        """
        ls = []
        for num in set(nums):
            left_idle = str(sum(list(map(int, num[0:3]))) % 10)
            right_idle = str(sum(list(map(int, num[-3:]))) % 10)
            if left_idle == '0' or right_idle == '0':
                new_left_idle = left_idle.replace('0', '10')
                new_right_idle = right_idle.replace('0', '10')
                if int(new_right_idle) == int(new_left_idle):
                    ls.append(num)
            elif int(right_idle) == int(left_idle):
                ls.append(num)
        return ls

    @staticmethod
    def san_gong_left_idle(nums):
        """
        三公-左闲方法
        :param nums:
        :return:
        """
        ls = []
        for num in set(nums):
            left_idle = str(sum(list(map(int, num[0:3]))) % 10)
            right_idle = str(sum(list(map(int, num[-3:]))) % 10)
            if left_idle == '0' or right_idle == '0':
                new_left_idle = left_idle.replace('0', '10')
                new_right_idle = right_idle.replace('0', '10')
                if int(new_left_idle) > int(new_right_idle):
                    ls.append(num)
            elif int(left_idle) > int(right_idle):
                ls.append(num)
        return ls

    @staticmethod
    def san_gong_right_idle(nums):
        """
        三公-右闲方法
        :param nums:
        :return:
        """
        ls = []
        for num in set(nums):
            left_idle = str(sum(list(map(int, num[0:3]))) % 10)
            right_idle = str(sum(list(map(int, num[-3:]))) % 10)
            if left_idle == '0' or right_idle == '0':
                new_left_idle = left_idle.replace('0', '10')
                new_right_idle = right_idle.replace('0', '10')
                if int(new_right_idle) > int(new_left_idle):
                    ls.append(num)
            elif int(right_idle) > int(left_idle):
                ls.append(num)
        return ls

    #
    # def san_gong_tail_left_big(self,nums,idle_type):
    #     ls =[]
    #     idle_dict = {
    #         '左闲尾大': [5,6,7,8,9],
    #         '左闲尾小': [0,1,2,3,4],
    #         '左闲尾单': [1,3,5,7,9],
    #         '左闲尾双': [0,2,4,6,8],
    #         '左闲尾质': [1,2,3,5,7],
    #         '左闲尾合': [0,4,6,8,9],
    #         '牛6': 6,
    #         '牛7': 7,
    #         '牛8': 8,
    #         '牛9': 9,
    #     }
    #     results = self.san_gong_left_idle(nums)
    #     for num in set(results):
    #         left_idle = str(sum(list(map(int, num[0:3]))) % 10)
    #         right_idle = str(sum(list(map(int, num[-3:]))) % 10)
    #         if idle_type[0:2] == '左闲':
    #             if int(left_idle) in idle_dict.get(idle_type):
    #                 ls.append(num)
    #         else:
    #             if int(right_idle) in idle_dict.get(idle_type):
    #                 ls.append(num)
    #     return ls
    def split_201110(self, idle: str, nums: List[str]) -> list:
        """
        棋牌-左右和，左闲点数：取开奖五个数字的前三位（万、千、百）之和的个位数。右闲点数：取开奖五个数字的后三位（百、十、个）之和的个位数。左闲点数与右闲点数相同时，则为和。比对的点数中0点为10点视为最大，9点为次大，1点为最小
        :param idle: 左闲|右闲|和
        :param nums: 10W条5位数的数组
        :return: list
        """
        idle_dict = {
            '左闲': self.san_gong_left_idle(nums),
            '右闲': self.san_gong_right_idle(nums),
            '和': self.san_gong_sum(nums)
        }
        return idle_dict.get(idle)

    @staticmethod
    def split_201111(idle: str, nums: List[str]) -> list:
        """
        棋牌-三公-大小单双质合，左闲点数/右闲点数的尾数：大小 0~4为小，5~9为大；单双 1、3、5、7、9为单，0、2、4、6、8为双；质合 1、2、3、5、7为质数，0、4、6、8、9为合数。可下注左闲尾大、小、单、双、质、合（右闲同理）等12种方式
        :param idle: 左闲|右闲|和
        :param nums: 10W条5位数的数组
        :return: list
        """
        ls = []
        idle_dict: Dict[str, list] = {
            '左大': [5, 6, 7, 8, 9],
            '左小': [0, 1, 2, 3, 4],
            '左单': [1, 3, 5, 7, 9],
            '左双': [0, 2, 4, 6, 8],
            '左质': [1, 2, 3, 5, 7],
            '左合': [0, 4, 6, 8, 9],
            '右大': [5, 6, 7, 8, 9],
            '右小': [0, 1, 2, 3, 4],
            '右单': [1, 3, 5, 7, 9],
            '右双': [0, 2, 4, 6, 8],
            '右质': [1, 2, 3, 5, 7],
            '右合': [0, 4, 6, 8, 9],
        }
        for num in set(nums):
            if idle[0:1] == '左':
                left_idle = str(sum(list(map(int, num[0:3]))) % 10)
                if int(left_idle) in idle_dict.get(idle):
                    ls.append(num)
            else:
                right_idle = str(sum(list(map(int, num[-3:]))) % 10)
                if int(right_idle) in idle_dict.get(idle):
                    ls.append(num)
        return ls

    def split_201212(self, numbers: List[str], bonus_type: str) -> list:
        """
        快3-大小单双，选择1个或者多个结果，如果开奖号码的和值与所选结果符合即中奖（3-10为小；11-18为大）
        :param bonus_type: 几等奖
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls = []
        bonus = {
            '牛大': ['牛6', '牛7', '牛8', '牛9', '牛牛'],
            '牛小': ['牛1', '牛2', '牛3', '牛4', '牛5'],
            '牛单': ['牛1', '牛3', '牛5', '牛7', '牛9'],
            '牛双': ['牛2', '牛4', '牛6', '牛8', '牛牛']
        }
        for value in bonus.get(bonus_type):
            result = self.split_201210(numbers, value)
            ls.extend(result)
        return ls

    @staticmethod
    def pk10_sum(numbers: List[str], types: str, bonus_type: str) -> list:
        """
        双面盘-前三|后三 - 和值，“后三和|前三和”可能出现的结果为6～27，投中对应第八名、第九名、第十名数字之和的视为中奖，其余视为不中奖。
        :param bonus_type: 几等奖
        :param numbers: 10W条5位数数组
        :param types:前三|中三|后三
        :return:list
        """
        ls = []
        bonus = {
            '一等奖': [6, 7, 26, 27],
            '二等奖': [8, 25],
            '三等奖': [9, 24],
            '四等奖': [10, 23],
            '五等奖': [11, 22],
            '六等奖': [12, 21],
            '七等奖': [13, 20],
            '八等奖': [14, 19],
            '九等奖': [15, 16, 17, 18]
        }
        for num in set(numbers):
            type_dict: Dict[str, str] = {
                '前三': num[0] + num[1] + num[2],
                '后三': num[2] + num[3] + num[4]
            }
            if sum(list(map(int, type_dict.get(types)))) in bonus.get(bonus_type):
                ls.append(num)
        return ls

    @staticmethod
    def split_321010(nums: List[str], *args) -> list:
        """
        任选-任选四-直选复式
        :param nums: 10W条5位数的数组
        :param args: 5位数字的下标
        :return: list
        """
        heap = []
        for num in set(nums):
            is_eq = (num[args[0]] + num[args[1]] + num[args[2]] + num[args[3]]) == str(args[4])
            if is_eq:
                heap.append(num)
        return heap

    @staticmethod
    def split_501010(numbers: List[tuple], bonus_type: List[int]) -> list:
        """
        快3-和值，至少选择1个和值（3个号码之和）进行投注，所选和值与开奖的3个号码的和值相同即中奖
        :param bonus_type: 几等奖
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls = []
        # bonus = {
        #     '一等奖': [3, 18],
        #     '二等奖': [4, 17],
        #     '三等奖': [5, 16],
        #     '四等奖': [6, 15],
        #     '五等奖': [7, 14],
        #     '六等奖': [8, 13],
        #     '七等奖': [9, 12],
        #     '八等奖': [10, 11]
        # }
        for num in set(numbers):
            if sum(num) in bonus_type:
                ls.append(num)
        return ls

    @staticmethod
    def split_511010(numbers: List[tuple], bonus_type: str) -> list:
        """
        快3-大小单双，选择1个或者多个结果，如果开奖号码的和值与所选结果符合即中奖（3-10为小；11-18为大）
        :param bonus_type: 几等奖
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls = []
        bonus = {
            '大': [11, 12, 13, 14, 15, 16, 17, 18],
            '小': [3, 4, 5, 6, 7, 8, 9, 10],
            '单': [3, 5, 7, 9, 11, 13, 15, 17],
            '双': [4, 6, 8, 10, 12, 14, 16, 18]
        }
        for num in set(numbers):
            if sum(num) in bonus.get(bonus_type):
                ls.append(num)
        return ls

    @staticmethod
    def split_521010(numbers: List[tuple], detail: List[str]) -> list:
        """
        快3-三同号，对豹子号（111，222，333，444，555，666）进行单选或通选投注，选号与开奖号相同即中奖
        :param detail:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):

            [_clc.setdefault(i, num.count(i)) for i in num]
            for i in num:
                ls1.append(str(i))
            if max(_clc.values()) == 3 and ''.join(ls1) in detail:
                ls.append(num)
            _clc.clear()
            ls1.clear()
        return ls

    @staticmethod
    def split_521011(numbers: List[tuple]) -> list:
        """
        快3-三同号通选，对豹子号进行通选投注，结果为豹子号即中奖
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):
            [_clc.setdefault(i, num.count(i)) for i in num]
            if max(_clc.values()) == 3:
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_531010(numbers: List[tuple], detail: List[str]) -> list:
        """
        快3-二同号，"分为2个部分，第一部分为2同号，选择 1-6 其中一个，2个相同数字为一注，多选用|分隔第二部分为单号，选择 1-6 其中一个，多选用|分隔"
        :param detail:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        # _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):

            # [_clc.setdefault(i, num.count(i)) for i in num]
            for i in num:
                ls1.append(str(i))
            if ''.join(ls1) in detail:
                ls.append(num)
            # _clc.clear()
            ls1.clear()
        return ls

    @staticmethod
    def split_531011(numbers: List[tuple], parameter: int) -> list:
        """
        快3-二同号二同号二同号复选，选择对子（1，2，3，4，5，6）进行投注，只要出现该对子（不含豹子）即中奖
        :param parameter:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):

            [_clc.setdefault(i, num.count(i)) for i in num]
            # print('parameter',type(parameter))
            # print(' list(_clc.keys())',_clc.keys())
            # print('items',_clc.items)
            for key, values in _clc.items():
                print('key', key)
                print('values', values)
                if key == parameter and values == 2:
                    ls.append(num)
            # if max(_clc.values()) == 2 and int(parameter) in list(_clc.keys()):
            #     ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_541010(numbers: List[tuple], detail: List[str]) -> list:
        """
        快3-三不同号，选择 1-6 其中一个，多选用|分隔
        :param detail:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        # _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):

            # [_clc.setdefault(i, num.count(i)) for i in num]
            for i in num:
                ls1.append(str(i))
            if ''.join(ls1) in detail:
                ls.append(num)
            # _clc.clear()
            ls1.clear()
        return ls

    @staticmethod
    def split_551010(numbers: List[tuple], num1: int, num2: int) -> list:
        """
        快3-二不同号，选择 1-6 其中一个，多选用|分隔
        :param num2:
        :param num1:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):
            [_clc.setdefault(i, num.count(i)) for i in num]
            n = [num1, num2]
            if set(n) <= set(_clc.keys()):
                # print(num)
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_561010(numbers: List[tuple], detail: List[str]) -> list:
        """
        快3-三连号，选择 123，234，345，456 其中一个，多选用|分隔
        :param detail:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        for num in set(numbers):
            for i in num:
                ls1.append(str(i))
            if ''.join(ls1) in detail:
                ls.append(num)
            ls1.clear()
        return ls

    @staticmethod
    def split_561011(numbers: List[str], ran: int) -> list:
        """
        双面盘-前三|中三|后三 - 顺子，获取顺子数据的方法:万千百位相连，不分顺序。----如开奖号码为123、901、321、546等，则视为中奖
        双面盘-前三|中三|后三 - 半顺，万千百位任意两位数字相连，不分顺序（不包括顺子、对子）。----如开奖号码为125、540、390、706，则视为中奖。如果开奖号码为顺子、对子,则投注半顺视为不中奖
        :param ran: ran:1 半顺，ran：2 顺子
        :param numbers: 10W条5位数数组
        :return:list
        """
        _tlt, _clc = ({} for j in range(2))
        _ls1, _ls2 = ([] for i in range(2))
        for num in set(numbers):
            # type_dict: Dict[str, str] = {
            #     '前三': num[0] + num[1] + num[2],
            #     '中三': num[1] + num[2] + num[3],
            #     '后三': num[2] + num[3] + num[4]
            # }
            combination = list(it.combinations(num, 2))
            for comb in set(combination):
                _ls1.append(int(max(comb)) - int(min(comb)) in [1, 9])
            [_tlt.setdefault(i, _ls1.count(i)) for i in _ls1]
            [_clc.setdefault(i, num.count(i)) for i in num]
            if _tlt.get(True) == ran and max(_clc.values()) == 1:
                _ls2.append(num)
            _ls1.clear()
            _tlt.clear()
            _clc.clear()
        return _ls2

    @staticmethod
    def split_571010(numbers: List[tuple], num1: int) -> list:
        """
        快3-单挑一骰，选择 1-6 其中一个，多选用|分隔
        :param num1:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):
            [_clc.setdefault(i, num.count(i)) for i in num]
            if num1 in set(_clc.keys()):
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_581010(numbers: List[tuple], num1: int) -> list:
        """
        快3-双面盘三军猜数字，三个开奖号码其中一个与所选号码相同时、即为中奖。相同号码只计算一次，(若开出豹子号只中奖一注)
        :param num1:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):
            [_clc.setdefault(i, num.count(i)) for i in num]
            if num1 in set(_clc.keys()):
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_581011(numbers: List[tuple], bonus_type: str) -> list:
        """
        快3-双面盘三军大小，三个开奖号码总和值小：3.4.5.6.7.8.9.10大：11.12.13.14.15.16.17.18三军大小包含豹子号码，如：投注小，开奖号码111，为和值3，视为中奖
        :param bonus_type: 几等奖
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls = []
        bonus = {
            '大': [11, 12, 13, 14, 15, 16, 17, 18],
            '小': [3, 4, 5, 6, 7, 8, 9, 10]
        }
        for num in set(numbers):
            if sum(num) in bonus.get(bonus_type):
                ls.append(num)
        return ls

    @staticmethod
    def split_581110(numbers: List[tuple], detail: List[str]) -> list:
        """
        快3-双面盘-围骰，对豹子号（111，222，333，444，555，666）进行单选或通选投注，选号与开奖号相同即中奖
        :param detail:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):

            [_clc.setdefault(i, num.count(i)) for i in num]
            for i in num:
                ls1.append(str(i))
            if max(_clc.values()) == 3 and ''.join(ls1) in detail:
                ls.append(num)
            _clc.clear()
            ls1.clear()
        return ls

    @staticmethod
    def split_581210(numbers: List[tuple], list1: int) -> list:
        """
        快3-双面盘-短牌，开奖号码任两字同号、且与所选择的短牌组合相符时，即为中奖，短牌号码不包含 豹子号。举例：投注短牌一一；开奖号码为1、1、3、即为中奖。
        :param list1:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):

            [_clc.setdefault(i, num.count(i)) for i in num]
            list2 = [2]
            ls1.append(list1)
            dict_name = dict(zip(ls1, list2))
            if set(dict_name.items()).issubset(set(_clc.items())):
                ls.append(num)
            _clc.clear()
            ls1.clear()
        return ls

    @staticmethod
    def split_581111(numbers: List[tuple]) -> list:
        """
        快3-双面盘-全骰，对豹子号（111，222，333，444，555，666）进行单选或通选投注，选号与开奖号相同即中奖
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):

            [_clc.setdefault(i, num.count(i)) for i in num]
            if max(_clc.values()) == 3:
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_581310(numbers: List[tuple], num1: str) -> list:
        """
        快3-双面盘-长牌，任选一长牌组合、当开奖结果任2码与所选组合相同时，即为中奖。举例：开奖号码为1、2、3、则投注长牌12、长牌23、长牌13皆视为中奖
        :param num1:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):
            [_clc.setdefault(i, num.count(i)) for i in num]
            n = [int(num1[0]), int(num1[1])]
            if set(n) <= set(_clc.keys()) and (num[1] > num[0] or num[2] > num[1]):
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_581410(numbers: List[tuple], bonus_type: List[int]) -> list:
        """
        快3-双面盘点数和点数和，至少选择1个和值（3个号码之和）进行投注，所选和值与开奖的3个号码的和值相同即中奖
        :param bonus_type: 几等奖
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls = []
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):
            [_clc.setdefault(i, num.count(i)) for i in num]
            if sum(num) in bonus_type and not max(_clc.values()) == 3:
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_591010(numbers: List[tuple], parameter: List[str]) -> list:
        """
        快3-猜必不出猜必不出猜必不出
        :param parameter:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        for num in set(numbers):
            if set(parameter) <= set(map(str, num)):
                pass
            else:
                ls.append(num)
        return ls

    @staticmethod
    def split_601010(numbers: List[tuple]) -> list:
        """
        快3-颜色全红全红,开奖号码全是1或4即中奖
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls = []
        lis = [1, 4]
        _tlt, _clc = ({} for _ in range(2))
        for num in set(numbers):
            [_clc.setdefault(i, num.count(i)) for i in num]
            print('_clc.keys()', _clc.keys())
            if list(_clc.keys()) == lis or (max(_clc.values()) == 3 and list(_clc.keys())[0] in lis):
                # print('_clc.keys()',_clc.keys())
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_601110(numbers: List[tuple], parameter) -> list:
        """
        快3-颜色全黑,开奖号码全是2、3、5、6即中奖
        :param parameter:
        :param numbers: 10W条5位数数组
        :return:list
        """
        ls = []
        lis = [2, 3, 5, 6]
        _tlt, _clc = ({} for _ in range(2))

        for num in set(numbers):
            [_clc.setdefault(i, num.count(i)) for i in num]

            if set(parameter) == set(num) or (max(_clc.values()) == 3 and list(_clc.keys())[0] in lis):
                ls.append(num)
            _clc.clear()
        return ls

    @staticmethod
    def split_701010(numbers: List[tuple]) -> list:
        """
        三码直选前三直选复式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                str_number1 = ''.join(map(str, set(j)))
                str_number2 = ''.join(map(str, set(i[:3])))
                if str_number1 == str_number2:
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_701011(numbers: List[tuple]) -> list:
        """
        三码直选前三直选单式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                str_number1 = ''.join(map(str, set(j)))
                str_number2 = ''.join(map(str, set(i[:3])))
                if str_number1 == str_number2:
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_701110(numbers: List[tuple]) -> list:
        """
        三码直选前三组选复式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                # str_number1 = ''.join(map(str, set(j)))
                # str_number2 = ''.join(map(str, set(i[:3])))
                if set(j) == set(i[:3]):
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_701111(numbers: List[tuple]) -> list:
        """
        三码直选前三组选单式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                # str_number1 = ''.join(map(str, set(j)))
                # str_number2 = ''.join(map(str, set(i[:3])))
                if set(j) == set(i[:3]):
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_711010(numbers: List[tuple]) -> list:
        """
        二码直选前二直选复式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                str_number1 = ''.join(map(str, set(j)))
                str_number2 = ''.join(map(str, set(i[:2])))
                if str_number1 == str_number2:
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_711011(numbers: List[tuple]) -> list:
        """
        二码直选前二直选单式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                str_number1 = ''.join(map(str, set(j)))
                str_number2 = ''.join(map(str, set(i[:2])))
                if str_number1 == str_number2:
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_711110(numbers: List[tuple]) -> list:
        """
        二码直选前二组选复式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                # str_number1 = ''.join(map(str, set(j)))
                # str_number2 = ''.join(map(str, set(i[:3])))
                if set(j) == set(i[:2]):
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_711111(numbers: List[tuple]) -> list:
        """
        二码直选前二组选单式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                # str_number1 = ''.join(map(str, set(j)))
                # str_number2 = ''.join(map(str, set(i[:3])))
                if set(j) == set(i[:2]):
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_711112(numbers: List[tuple]) -> list:
        """
        二码直选前二组选单式
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                # str_number1 = ''.join(map(str, set(j)))
                # str_number2 = ''.join(map(str, set(i[:3])))
                if set(j) == set(i[:2]):
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_75104x7(numbers: List[str], num: int) -> list:
        """
        任选复式任选  五中五复式 、六中五复式、七中五复式、八中五复式
        :param numbers:选择的号码
        :param num: 长度
        :return: List
        """
        return list(it.permutations(numbers, num))

    @staticmethod
    def split_751010(numbers: List[str]) -> list:
        """
        任选复式任选  一中一
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        print('set(numbers)', set(numbers))
        for i in set(list(it.permutations(lst1, 5))):

            for j in set(numbers):
                if set(j).issubset(set(i)):
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_721010(num: str) -> list:
        """
        11选5，不定位
        :param num: 选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            param = [num]
            if set(param).issubset(set(i[:3])):
                lst2.append(i)
        return lst2

    @staticmethod
    def split_731010_1() -> list:
        """
        趣味型趣味型定单双（一等奖：0单5双）
        :return:list
        """
        ls = []
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = ['02', '04', '06', '08', '10']
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(list(it.combinations(lst2, 5))):
                if set(j).issubset(set(i)):
                    ls.append(i)
        return ls

    @staticmethod
    def split_731010_2() -> list:
        """
        趣味型趣味型定单双（二等奖：5单0双）
        :return:list
        """
        ls = []
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = ['01', '03', '05', '07', '09', '11']
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(list(it.combinations(lst2, 5))):
                if set(j).issubset(set(i)):
                    ls.append(i)
        return ls

    @staticmethod
    def split_731010_3() -> list:
        """
        趣味型趣味型定单双（四等奖：1单4双）
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = ['01', '03', '05', '07', '09', '11']
        lst3 = ['02', '04', '06', '08', '10']
        for i in set(list(it.combinations(lst3, 4))):
            for j in lst2:
                num = [j]
                ls1.append(i + tuple(num))
        for parameter in set(list(it.permutations(lst1, 5))):
            for k in ls1:
                if set(k).issubset(set(parameter)):
                    ls.append(parameter)
        return ls

    @staticmethod
    def split_731010_4() -> list:
        """
        趣味型趣味型定单双（四等奖：4单1双）
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = ['01', '03', '05', '07', '09', '11']
        lst3 = ['02', '04', '06', '08', '10']
        for i in set(list(it.combinations(lst2, 4))):
            for j in lst3:
                num = [j]
                ls1.append(i + tuple(num))
        for parameter in set(list(it.permutations(lst1, 5))):
            for k in ls1:
                if set(k).issubset(set(parameter)):
                    ls.append(parameter)
        return ls

    @staticmethod
    def split_731010_5() -> list:
        """
        趣味型趣味型定单双（五等奖：2单3双）
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = ['01', '03', '05', '07', '09', '11']
        lst3 = ['02', '04', '06', '08', '10']
        for i in set(list(it.combinations(lst2, 2))):
            for j in set(list(it.combinations(lst3, 3))):
                ls1.append(i + j)
        for parameter in set(list(it.permutations(lst1, 5))):
            for k in ls1:
                if set(k).issubset(set(parameter)):
                    ls.append(parameter)
        return ls

    @staticmethod
    def split_731010_6() -> list:
        """
        趣味型趣味型定单双（六等奖：3单2双）
        :return:list
        """
        ls, ls1 = ([] for _ in range(2))
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = ['01', '03', '05', '07', '09', '11']
        lst3 = ['02', '04', '06', '08', '10']
        for i in set(list(it.combinations(lst2, 3))):
            for j in set(list(it.combinations(lst3, 2))):
                ls1.append(i + j)
        for parameter in set(list(it.permutations(lst1, 5))):
            for k in ls1:
                if set(k).issubset(set(parameter)):
                    ls.append(parameter)
        return ls

    @staticmethod
    def split_731011(num: str) -> list:
        """
        趣味型趣味型猜中位（一等奖：3/9）
        :return:list
        """
        ls = []
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        for parameter in set(list(it.permutations(lst1, 5))):
            ls_parameter = list(parameter)
            ls_parameter.sort()
            ls_parameter.reverse()
            if num == ls_parameter[2]:
                ls.append(parameter)
        return ls

    @staticmethod
    def split_741010(numbers: List[str], num: int) -> list:
        """
        定位胆定位胆定位胆
        :param num: 位置
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):

            for j in set(numbers):
                str_number1 = ''.join(map(str, set(j)))
                str_number2 = ''.join(map(str, i[num]))
                if str_number1 == str_number2:
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_75100x3(numbers: List[tuple]) -> list:
        """
        任选复式任选  一中一复式、二中二复式、三中三复式、四中四复式
        :param numbers:选择的号码
        :param num: 长度
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            for j in set(numbers):
                if set(j).issubset(set(i)):
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_751210(numbers: List[tuple]) -> list:
        """
        11选5，任选胆拖任选二中二胆拖
        :param num: 选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            # param = [num]
            for j in set(numbers):
                if set(j).issubset(set(i)):
                    lst2.append(i)
        return lst2

    @staticmethod
    def split_761010(bonus_type: str, num: str) -> list:
        """
        11选5-双面盘 于特码（最后一位）、正一码（第一位）、正二码、正三码、正四码任选一码，自1~10任选1个号进行投注，当开奖结果与所选号码相同且顺序一致时，即为中奖。（开出号码11时玩家不中奖，则平台通杀）
        :param bonus_type: 第几位
        :param num: 位置的号码
        :return:list
        """
        ls = []
        bonus = {
            '正一': 0,
            '正二': 1,
            '正三': 2,
            '正四': 3,
            '特码': 4
        }
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        for i in set(list(it.permutations(lst1, 5))):
            if i[bonus.get(bonus_type)] == num:
                ls.append(i)
        return ls

    @staticmethod
    def split_761011(bonus_type: str, num_type: str) -> list:
        """
        11选5-双面盘 开出相应号码即为中奖，其中：小（1-5）、大（6-10）、质（12357）、合（468910），11均不计算中奖
        :param bonus_type: 第几位
        :param num: 位置的号码
        :return:list
        """
        ls = []
        bonus = {
            '正一': 0,
            '正二': 1,
            '正三': 2,
            '正四': 3,
            '特码': 4
        }
        calculate = {
            '小': ['01', '02', '03', '04', '05'],
            '大': ['06', '07', '08', '09', '10'],
            '质': ['01', '02', '03', '05', '07'],
            '合': ['04', '06', '08', '09', '10']
        }
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        for i in set(list(it.permutations(lst1, 5))):
            if i[bonus.get(bonus_type)] in calculate.get(num_type):
                ls.append(i)
        return ls

    @staticmethod
    def split_761110(bonus_type: str, num_type: str) -> list:
        """
        11选5-双面盘 开出相应号码即为中奖，其中：小（1-5）、大（6-10）、质（12357）、合（468910），11均不计算中奖
        :param bonus_type: 第几位
        :param num: 位置的号码
        :return:list
        """
        ls = []
        bonus = {
            '正一': 0,
            '正二': 1,
            '正三': 2,
            '正四': 3,
            '特码': 4
        }

        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        # print(bonus_type.split('|'))
        # print('0',bonus_type.split('|')[0])
        # print('1', bonus_type.split('|')[1])
        # print(num_type)
        for i in set(list(it.permutations(lst1, 5))):
            calculate = {
                '龙': i[bonus.get(bonus_type.split('|')[0])] > i[bonus.get(bonus_type.split('|')[1])],
                '虎': i[bonus.get(bonus_type.split('|')[0])] < i[bonus.get(bonus_type.split('|')[1])]
            }
            if calculate.get(num_type):
                ls.append(i)
        return ls

    @staticmethod
    def split_761210(numbers: List[tuple]) -> list:
        """
        双面盘  双面盘全五中一全五中一
        :param numbers:选择的号码
        :return: List
        """
        lst1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
        lst2 = []
        for i in set(list(it.permutations(lst1, 5))):
            # print('numbers',numbers)
            parameter = [numbers]
            # print('parameter',parameter)
            if set(parameter).issubset(set(i)):
                lst2.append(i)
        return lst2
