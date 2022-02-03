#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project : nac-ele
# @Author  : Eagle
# @Site    : 
# @File    : test1.py
# @Time    : 2021/6/27 20:10
# @Software: PyCharm
import itertools
import operator
import random
import re
from itertools import combinations

#
# def generate_bet_detail(bet_detail, n):
#     before = bet_detail.split('_')[0]
#     print("bet_detail.split('_')", bet_detail.split('_')[0])
#     # 截取注单号码后半部分
#     after = bet_detail.split('_')[1]
#     print("bet_detail.split('_')", bet_detail.split('_')[1])
#     # 想将位置转换为数组形式
#     before_list = before.split('|')
#     # print("''.join(before)", before.split('|'))
#     # 将前部分的位置中文信息替换成下标
#     is_position = {'万': '0', '千': '1', '百': '2', '十': '3', '个': '4', }
#     _lis = []
#     for v in before_list:
#         # print('is_position.get(v)', is_position.get(v))
#         _lis.append(is_position.get(v))
#     # 生成组合
#     details = list(combinations(_lis, n))
#     str_lis = []
#     for i in details:
#         str_lis.append(''.join(list(i)))
#     ls = []
#     for index, value in enumerate(after.split('|')):  # index 是下标，key是a中的值，
#         for i, k in enumerate(str_lis):
#             dic = {}.fromkeys([k])
#             if dic[k] is None:
#                 dic[k] = value
#             else:
#                 dic[k].append(value)
#             ls.append(dic)
#     return ls


# bet_detail = '万|千|百|十|个_16|18|19|20'
#
# bet_detail1 = '1|2|3,1|2|3,1|2|3,1|2|3,1|2|3'
# print(generate_bet_detail(bet_detail,3))
# after = bet_detail1.split('_')[1]
# print(after)
# if ',' in after:
#     print(''.join(after.split(',')))
# # print("bet_detail.split('_')", bet_detail.split('_')[1])
# # print('after.split()',after.split('|'))
from typing import Union, Any

from comm.cartesian import Cartesian
# from comm.tool import Tools
#
#
# def generate_bets_duplex(bet_detail: str):
#     ls, _lis, _vis, _ris = ([] for r in range(4))
#     # print(bet_detail.replace('|', '').split(','))
#     for i, v in enumerate(bet_detail.replace('|', ' ').split(',')):
#         if v != '#':
#             ls.append({v: str(i)})
#     _cis = list(
#         combinations(ls, 3))  # 通过上面的循环将注单数据转换成以下格式，并获取combinations组合：[({'1 2 3': '0'}, {'1 3 4': '1'}, {'2 4 6': '2'})]
#     idx = 0
#     # print('_cis',_cis)
#     # print('len',len(_cis))
#     while len(_cis) < len(_cis) + 1:
#         # print('c[y]', _cis[idx])
#         for bbc in _cis[idx]:
#             # print('keys', list(map(str, ''.join(bbc.keys()).split())))
#             # print('values', ''.join(bbc.values()))
#             _lis.append(list(map(str, ''.join(bbc.keys()).split())))
#             _vis.append(''.join(bbc.values()))
#         # print('_lis', _lis)
#         # print('_vls', ''.join(_vis))
#         for item in itertools.product(_lis[0], _lis[1], _lis[2]):
#             # print('item', {''.join(_vis): ''.join(item)})
#             _ris.append({''.join(_vis): ''.join(item)})
#         _lis.clear()
#         _vis.clear()
#         idx = idx + 1
#         if idx >= len(_cis):
#             break
#     # print('_ris',_ris)
#     return _ris
#     # return child.build_duplex()
#
#
# # generate_bets_duplex()
# bet_detail = '1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
# print("generate_bets_duplex()", generate_bets_duplex(bet_detail))
# print("generate_bets_duplex()", len(generate_bets_duplex(bet_detail)))
# str1 = '1 2 3 4'
# l = list(map(int, str1.split()))
# print(l)

# print('child.build_duplex()',child.build_duplex())
# print(array)
# for i in range(len(c)):
#     p = 0
#     if i == p:
#         print(c[p])
#         p=p+1
#     break
# for i in c:
#     for item,k in enumerate(i):
#         d = 0
#         # print(''.join(k.keys()),k.values())
#         if item == 0:
#             print(''.join(k.keys()), k.values())

# for item in itertools.product(''.join(k.keys()),''.join(k.keys()),''.join(k.keys())):
#     print("''.join(item)",''.join(item))
#     d = d+1
#     break

# for item in itertools.product(*self.children):
#     _item_list.append(item)
# for idx in c:
#     print(idx)
#     for i,v in enumerate(idx):
#         print(v)


# befores = ['0', '1', '2', '3', '4']
# b = list(combinations(befores, 3))
# # b = self.it_combinations(before, n)
#
# print('b', b)
import itertools as it

from comm.tool import Tools

_ais = []
bet_detail = '万|千|百|十|个_118,199'
# after = bet_detail.split('_')[1]
# print(after)
# for v in after.split('|'):
#     _ais.append(v)
# print(_ais)
# it_after = list(it.combinations(_ais, 2))
# print('it_after', it_after)
tool = Tools()
print("tool.bet_detail_twin_single(bet_detail,3,2)", tool.bet_detail_single(bet_detail, 3))
# twin = ''
# single = ''
rlt = {}
# SPLIT_DETAIL = tool.bet_detail_single(bet_detail, 3)
# for parameter in SPLIT_DETAIL:
#     before = ''.join(parameter.keys())
#     afters = ''.join(parameter.values())
#     # print('after', afters)
#     # 统计每个字符出现的次数
#     [rlt.setdefault(i, afters.count(i)) for i in afters]
#     print(rlt)
#     # 反转字典
#     reverse_dict = {v: k for k, v in rlt.items()}
#
#     rlt.clear()
#     print("重复: %s,单值：%s" % (reverse_dict.get(2), reverse_dict.get(1)))
    # break
#
# def get_bet_number_161112(num):
#     is_num = {
#         '0': 1,
#         '1': 3,
#         '2': 6,
#         '3': 10,
#         '4': 15,
#         '5': 21,
#         '6': 28,
#         '7': 36,
#         '8': 45,
#         '9': 55,
#         '10': 63,
#         '11': 69,
#         '12': 73,
#         '13': 75,
#         '14': 75,
#         '15': 73,
#         '16': 69,
#         '17': 63,
#         '18': 55,
#         '19': 45,
#         '20': 36,
#         '21': 28,
#         '22': 21,
#         '23': 15,
#         '24': 10,
#         '25': 6,
#         '26': 3,
#         '27': 1
#
#     }
#     return is_num.get(num)

# BET_DETAIL= '万|千|百|十|个_16|18|19|20'
#
# SPLIT_DETAIL = tool.bet_detail_single(BET_DETAIL, 3)
# ls = []
# print(SPLIT_DETAIL)
# for i in SPLIT_DETAIL:
#     ls.append(''.join(i.values()))
#     # print(ls.append(i.values()))
# # [rlt.setdefault(i, SPLIT_DETAIL..count(i)) for i in SPLIT_DETAIL]
# print(ls)
# [rlt.setdefault(i, ls.count(i)) for i in ls]
# print('rlt',rlt)
# # reverse_dict = {v: k for k, v in rlt.items()}
# print(rlt.keys())
# ls = []

# for i in rlt:
#     print(i)
#     rlt.update()
# print('rlt',rlt)
# print('rlt')
# dn = {}
# [ls.append(int(get_bet_number_161112(v))*int(list(rlt.values())[i])) for i,v in enumerate(rlt.keys())]
# nd = {}
# nbd = '888'
# [nd.setdefault(i, nbd.count(i)) for i in nbd]
# # rev_dict = {v: k for k, v in nd.items()}
# print('nbd',nd.get(''.join(nd.keys()))==3)
# # print('rev_dict',rev_dict.keys())
# print('ls',sum(ls))
# print('dn',dn.keys())
# cd = {}
# cds = '21717'
# [cd.setdefault(i, cds.count(i)) for i in cds]
# print('cd',2 in cd.values())
# cd_dict = {str(v): k for k, v in cd.items()}
# print('count',cd_dict.keys())
#
#
# dc = {'21784': 2}
# print('dc',''.join(dc.keys()))
# content = '118'
# # clt = {}
# twin =''
# single = ''
# clt = {}
# [clt.setdefault(i,content.count(i)) for i in content]
# print('clt.keys()',clt)
# print('clt.keys()',clt.values())
# if 2 in clt.values():
#     print('真')
#     new_d = {v: k for k, v in clt.items()}
#     print('new_d', new_d)
#     print('new_d', new_d.get(2))
#     print('new_d', new_d.get(1))
# else:
#     print('假')

# print("12",{v:k for k,v in rlt.items()}.get(2),{v:k for k,v in rlt.items()}.get(1))
# twin = ''
# single = ''
# for i in range(len(str)):
#     if str.count(str[i]) > 1:
#         twin += str[i]
#     else:
#         single += str[i]
# print('重复的元素有：%s' % twin)
# print('不重复的元素有：%s' % single)
#
# bet_detail = '万|千|百|十|个_123,124'
# detail = '万|千|百|十|个_001,134'
# SPLIT_DETAIL = tool.bet_detail_single(bet_detail,3)
# print('SPLIT_DETAIL =',SPLIT_DETAIL)
# print('len',len(SPLIT_DETAIL))
# prrf = '39843'
# print('prrf',prrf[3])
# SPLIT_LIST = ['13900','19381','03019']
#
# plt = {}
# [plt.setdefault(x,SPLIT_LIST.count(x)) for i in SPLIT_LIST for x in i]
# print('plt',plt)
# for i in SPLIT_LIST:
#     print('i',i)
#
#     for k in '001':
#         if operator.contains(i, k):
#             print(i)
#             break
#
# random.choice(SPLIT_LIST)
#
# BET_DETAIL = '0|1|2|3|4|5|6|7|8|9,0|1|2|3|4|5|6|7|8|9,0|1|2|3|4|5|6|7|8|9,0|1|2|3|4|5|6|7|8|9,0|1|2|3|4|5|6|7|8|9'
# SPLIT_DETAIL = tool.bet_detail_duplex_four(BET_DETAIL, 4)
# print('SPLIT_DETAIL',SPLIT_DETAIL)
# print('SPLIT_DETAIL',len(SPLIT_DETAIL))
#
# _cis = list(it.combinations('84754', 3))
# print(_cis)
# ddk = '847'
# ldd = []
# tlt = {}
# klt = {}
# o= []
#
# for v in _cis:
#     print(''.join(v))
#     [tlt.setdefault(i, ''.join(v).count(i)) for i in ''.join(v)]
#
#     print('tlt',tlt)
#
#     print('list(tlt.values())',list(tlt.values()))
#     if 2 in list(tlt.values()):
#         print('组三')
#         o.append({'组三':str(int(''.join(v)[0])+int(''.join(v)[1])+int(''.join(v)[2]))})
#     else:
#         print('组六')
#         o.append({'组六':str(int(''.join(v)[0])+int(''.join(v)[1])+int(''.join(v)[2]))})
#     # print(int(''.join(v)[0]),int(''.join(v)[1]),int(''.join(v)[2]))
#     tlt.clear()
#     # ldd.append(int(''.join(v)[0])+int(''.join(v)[1])+int(''.join(v)[2]))
# # print(ldd)
# # print(tlt)
# io = '万|千|百|十|个_16|18|19|26'
# ld = ['16','18','19','26']
#
# # after = io.split('_')[1]
# print('after',io.split('_')[1].split('|'))
# print('o',o)
# cccs = []
# for c in o:
#     # print(''.join(c.values()))
#     if ''.join(c.values()) in io.split('_')[1].split('|'):
#         print(c.keys())
#         cccs.extend(c.keys())
# print('cccs',cccs)
# ppt = {}
# [ppt.setdefault(i, cccs.count(i)) for i in cccs]
# print('ppt',ppt)
# print(ppt.keys())
# print(ppt.get('组六'))
# for i in ppt:
#     print('i',i)
#     if i == '组六':
#         print('计算组六实际奖金*4', ppt.get('组六'))
#     else:
#         print('计算组三实际奖金*1',  ppt.get('组三'))
# if '组六' in ppt.keys():
#     print('计算组六实际奖金*4',ppt.values())
# else:
#     print('计算组组三实际奖金*1',ppt.values())
tlt ={}
# ts = ['12345','11111','88888']
# for v in ts:
#     # for
#     # print('v',v)
#     [tlt.setdefault(i, v.count(i)) for i in v]
#     # print(set(tlt.values()))
#     if 5 in set(tlt.values()):
#         print(v)
#     # break
# # print(tlt)
#     tlt.clear()
#
# str1 = "[{\"numbers\":\"豹子\",\"betPrice\":50},{\"numbers\":\"豹子\",\"betPrice\":50}]"
# print('str1',str1)
# results = list(map(int, re.findall(r"\d+\.?\d*",str1)))
# print(sum(list(map(int, re.findall(r"\d+\.?\d*",str1)))))
# # print(new_list)
# # print (''.join(re.findall(r"\d+\.?\d*",str1)))
# print (len(re.findall(r"\d+\.?\d*",str1)))
# print(type(list(str1)))
# for i in list(str1):
#     print(i)
nums = ['00000','11837','28064','19573','19301','12345']
for num in set(nums):
    # print(num)
    [tlt.setdefault(i, num.count(i)) for i in num]
    print(max(set(tlt.values())))
    if max(set(tlt.values())) ==1:
        print(num)
    # break
    tlt.clear()
    # if not is_pair:
    #     print(num)

str3 = '19573'
print("''.join(str3)",map(int,''.join(str3)))
print('str3 = ',list(map(int,''.join(str3))))
stack = []
for item in str3:
    if len(stack) > 0 and stack[-1] == item:  # 同时判断两个逻辑，可以减少一行代码
        stack.pop(-1)
    else:
        stack.append(item)

print("''.join(stack)",''.join(stack))

list_1 = [1, 3, 5, 2, 6, 8, 9, 6, 8, 4]
list_1 = set(list_1)  # 把列表变成集合，去重
list_2 = [22, 5, 4, 65, 8, 9, 3]
list_2 = set(list_2)
print(list_1, list_2)
print(list(list_1.symmetric_difference(list_2)))