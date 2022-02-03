# from typing import List
#
# from comm.tool import Tools
#
# tool = Tools()
# number = tool.lottery_data_source()
#
# _yaml = tool.get_yaml()
# PROJECT = 'nac'
# BET_CODE = '18_10_10'
# BET_DETAIL = _yaml['detail'].get(PROJECT + '_' + BET_CODE)
# print('BET_DETAIL', BET_DETAIL)
# # number = ['01488', '00236', '34301', '00001', '87363']  # ['00227','00236','34301','00001','87363']
# # number = [ '00444']  #'00109', '00009', '81626', '98399',
# SPLIT_DETAIL = tool.bet_detail_single(BET_DETAIL, 2)
# print('SPLIT_DETAIL', SPLIT_DETAIL)
# # number = tool.lottery_data_source()
# SPLIT_LIST = []
#
#
# def split_181010(nums: List[str], *args) -> list:
#     """
#     任选-任选三-组六单式，选择3个号码0,1,2，顺序不限
#     :param nums: 10W条5位数的数组
#     :param args: 5位数字的下标
#     :return: list
#     """
#
#     heap = []
#     for num in set(nums):
#         is_dict = {'龙': num[args[0]] > num[args[1]],
#                    '虎': num[args[0]] < num[args[1]],
#                    '和': num[args[0]] == num[args[1]]
#                    }
#         if is_dict.get(args[2]):
#             heap.append(num)
#     return heap
#
#
# for parameter in SPLIT_DETAIL:
#     before = ''.join(parameter.keys())
#     print('before', before)
#     afters = ''.join(parameter.values())
#     print('afters', afters)
#     result = split_181010(number, int(before[0]), int(before[1]), afters)
#     SPLIT_LIST.extend(result)
# print('SPLIT_LIST', SPLIT_LIST)
# print('len', len(SPLIT_LIST))
# # bet_detail = "[{\"numbers\":\"和\",\"betPrice\":50}]"
# # api_results = tool.get_split_api_double_sided('txffc', '20_11_10', bet_detail)
# # test_result = san_gong(number)
# # test_split_result = list({}.fromkeys(test_result).keys())
# #
# # print('test_split_result', test_split_result)
# #
# # # print('api_results', api_results)
# # api_split_result = []
# # for i in api_results[1]:
# #     lis = i.replace(',', '')
# #     api_split_result.append(lis)
# # api_split_result.sort()
# # print('api_split_result',api_split_result)
# # print('len', len(test_split_result))
# # print('len', len(api_split_result))
# #
# # isTure = tool.check_split_equal(list(test_result),list(api_split_result))
# # print(isTure)
# # print(len(isTure[1]))
import decimal
import itertools
import time
from decimal import Decimal
from typing import List, Dict
import itertools as it

from comm.tool import Tools

tool = Tools()
nums = 100.0000
print("Decimal(nums).quantize(Decimal('0.0000'))", Decimal(nums).quantize(Decimal('0.0000'), decimal.ROUND_DOWN))
# numbers = ['15798', '54043', '08932', '79683', '76683', '02900']
numbers = tool.lottery_data_source()

def prefixInteger(n, m):
    _lice_list = []
    for item in itertools.islice(range(m), n, m):
        _lice_list.append(str(item))
    return list(_lice_list)

# def pk10_guanya_sum(numbers: List[str], types: str, bonus_type: str) -> list:
#     """
#     双面盘-前三|后三 - 和值，“后三和|前三和”可能出现的结果为6～27，投中对应第八名、第九名、第十名数字之和的视为中奖，其余视为不中奖。
#     :param bonus_type: 几等奖
#     :param numbers: 10W条5位数数组
#     :param types:前三|中三|后三
#     :return:list
#     """
#     ls = []
#     bonus = {
#         '一等奖': [3, 4, 18, 19],
#         '二等奖': [5, 6, 16, 17],
#         '三等奖': [7, 8, 14, 15],
#         '四等奖': [9, 10, 12, 13],
#         '五等奖': [11],
#     }
#     for num in set(numbers):
#         type_dict: Dict[str, str] = {
#             '前三': num[0] + num[1] + num[2],
#             '后三': num[2] + num[3] + num[4]
#         }
#         if sum(list(map(int, type_dict.get(types)))) in bonus.get(bonus_type):
#             ls.append(num)
#     return ls

c = time.time()
# print(pk10_guanya_sum(numbers, '前三', '一等奖'))
num = [1,2,3,4,5,6,7,8,9,10]
# del num[2:10]
# print('num =',num)
# print("it.combinations('1,2,3,4,5,6,7,8,9,10', 3)",list(it.permutations(num, 10)))
# print('len1',len(list(it.permutations(num, 10))))
# print('setlen',len(set(list(it.permutations(num, 10)))))
# def prefixInteger( n, m):
#     _lice_list = []
#     # print('Start at 5, Stop at 10:')
#     for item in itertools.islice(range(m), n, m):
#         # print(item, end=' ')0kvfs
#         _lice_list.append(str(item))
#     # print('\n')
#     # print('prefixInteger', self._item_list)
#     return list(_lice_list)
ls = []
# print('list(it.permutations(num, 10))',list(it.combinations(num, 10)))
for item in list(it.permutations(num, 10)):
    # str_item = ''.join(list(map(str,item)))
    # print('list(map(str,item))',list(map(int,item)))
    del_num = list(map(int,item))
    del del_num[2:10]
    if sum(del_num) in [3, 4, 18, 19]:
        ls.append(''.join(list(map(str,item))))
    # if int(list(map(str,item))[0])
    # break
    # str_item[0] str_item[1]
    # print('str_item',str_item)
    # ls.append(str_item[0]+str_item[1])
    # if int(str_item[0])+int(str_item[1]) in  [3, 4, 18, 19]:
    #     ls.append(str_item)
print(ls)
print(len(ls))
    # break
print(time.time() - c)


# print()
    # def lottery_data_source() -> list:
    #     """
    #     获取包含所有5位数的数组
    #     :return:
    #     """
    #     _all = list(it.permutations(range(1,11), 10))
    #     # print('all',_all)
    #     return [''.join(map(str, list(i))) for i in _all]
    #
    # print('lottery_data_source()',lottery_data_source())