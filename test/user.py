# import itertools
# import itertools as it
# import re
# import time
# from typing import List
#
import numpy as np

from comm.tool import Tools
import itertools as it
import itertools
#
# start = time.time()
# # tool = Tools()
# # number = tool.generate_11x5_number()
_tool = Tools()
_yaml = _tool.get_yaml()
PROJECT = 'nac'
BET_CODE = '32_10_10'
print('BET_CODE',BET_CODE)
BET_DETAIL = _yaml['detail'].get(PROJECT + '_' + BET_CODE)
print('BET_DETAIL', BET_DETAIL)
LOT_CODE = _yaml[PROJECT].get('lot_code')
print(LOT_CODE)
AMOUNT = _yaml[PROJECT].get('amount')
print(AMOUNT)
# SPLIT_DETAIL = _tool.bet_detail_duplex_four(BET_DETAIL, 4)
# print('SPLIT_DETAIL',SPLIT_DETAIL)
# BETS = len(SPLIT_DETAIL)
# print(BETS)
SPLIT_LIST = []
OPEN_NUMBER = '99999'
PROFIT_LIST = []

ls, _lis, _vis, _ris = ([] for r in range(4))
# print(bet_detail.replace('|', '').split(','))
for i, v in enumerate(BET_DETAIL.replace('|', ' ').split(',')):
    if v != '#':
        ls.append({v: str(i)})
print(ls)
# 通过上面的循环将注单数据转换成以下格式，并获取combinations组合：[({'1 2 3': '0'}, {'1 3 4': '1'}, {'2 4 6': '2'})]
# print('ls',ls)
# _cis = list(it.combinations(ls, 4))
# idx = 0
# print('_cis',_cis)
# print('len',len(_cis))

for parameter in ls:
    print('i',parameter)
    print('parameter_1',parameter.keys())
    print('parameter_1]3', ''.join(parameter.keys()).split(' '))
    print('parameter_14', ''.join(parameter.values()))


# while len(_cis) < len(_cis) + 1:
#     # print('c[y]', _cis[idx])
#     for bbc in _cis[idx]:
#         # print('keys', list(map(str, ''.join(bbc.keys()).split())))
#         # print('values', ''.join(bbc.values()))
#         _lis.append(list(map(str, ''.join(bbc.keys()).split())))
#         _vis.append(''.join(bbc.values()))
#     # print('_lis', _lis)
#     # print('_vls', ''.join(_vis))
#     for item in itertools.product(_lis[0], _lis[1
#     ], _lis[2], _lis[3]):
#         # print('item', {''.join(_vis): ''.join(item)})
#         _ris.append({''.join(_vis): ''.join(item)})
#     _lis.clear()
#     _vis.clear()
#     idx = idx + 1
#     if idx >= len(_cis):
#         break
# print('_ris',_ris)