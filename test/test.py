import itertools
import re
from typing import List
import itertools as it
from comm.tool import Tools
from split.split import Split

tool = Tools()
ls = []
ls1 = []
# number = tool.lottery_data_source()
# print(list(itertools.islice(range(7), 1, 7)))
numbers1 = list(it.combinations_with_replacement(list(itertools.islice(range(7), 1, 7)), 3))
print('len', len(numbers1))
_tool = Tools()
_yaml = _tool.get_yaml()
PROJECT = 'nac'
BET_CODE = '58_13_10'
BET_DETAIL = _yaml['detail'].get(PROJECT + '_' + BET_CODE)
print('BET_DETAIL', BET_DETAIL)
LOT_CODE = _yaml[PROJECT].get('lot_code')
print(LOT_CODE)
re_results = re.findall(r"\d+\.?\d*", str(re.findall(r":\d+\.?\d*", BET_DETAIL)))
print('re_results', re_results)
AMOUNT = sum(list(map(int, re_results)))
print('AMOUNT', AMOUNT)

_LIST = list(map(str, re.findall(r"\d+\.?\d*", str(re.findall(r'"\d+"', BET_DETAIL)))))
print(_LIST)


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


print("split_581010(numbers1,'12')", split_581310(numbers1, '14'))
