#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project : nac-ele
# @Author  : Eagle
# @Site    : 
# @File    : test_split_profit_161112.py
# @Time    : 2021/6/28 0:59
# @Software: PyCharm
import random
import time
import itertools as it
from decimal import Decimal

from assertpy import assert_that
from test_junkie.decorators import beforeClass, test, Suite
from test_junkie.runner import Runner

from comm.tool import Tools
from comm.utils import MysqlPool
from split.split import Split

_tool = Tools()
_yaml = _tool.get_yaml()
PROJECT = 'nac'
BET_CODE = '16_11_15'
print('BET_CODE', BET_CODE)
BET_DETAIL = _yaml['detail'].get(PROJECT + '_' + BET_CODE)
print('BET_DETAIL', BET_DETAIL)
LOT_CODE = _yaml[PROJECT].get('lot_code')
print(LOT_CODE)
AMOUNT = _yaml[PROJECT].get('amount')
print(AMOUNT)
SPLIT_DETAIL = _tool.bet_detail_single(BET_DETAIL, 3)
print(SPLIT_DETAIL)
# BETS = len(SPLIT_DETAIL)
# print(BETS)
SPLIT_LIST = []
OPEN_NUMBER = '99999'
PROFIT_LIST = []


@Suite(feature=BET_CODE, parallelized=False)
class NacSplitProfit161115(object):
    def __init__(self):
        self._sql = MysqlPool('DATA_BASE')
        self.mysql = MysqlPool("SPLIT_BASE")
        self.split = Split()
        self.number = _tool.lottery_data_source()

    # noinspection PyGlobalUndefined
    @beforeClass()
    def get_split_number(self):
        rlt = {}
        ls = []
        cs = []
        global BETS
        for parameter in SPLIT_DETAIL:
            before = ''.join(parameter.keys())
            afters = ''.join(parameter.values())
            ls.append(''.join(parameter.values()))
            result = self.split.split_161115(self.number, int(before[0]), int(before[1]), int(before[2]), int(afters))
            SPLIT_LIST.extend(result)

        [rlt.setdefault(i, ls.count(i)) for i in ls]
        [cs.append(int(self.split.get_bet_number_161115(v)) * int(list(rlt.values())[i])) for i, v in
         enumerate(rlt.keys())]
        print('cs', cs)
        BETS = sum(cs)
        print('BETS', BETS)
        # print('BETS', type(BETS))
        # print('SPLIT_LIST',SPLIT_LIST)
        print('SPLIT_LIST',len(SPLIT_LIST))
        return SPLIT_LIST

    # noinspection PyGlobalUndefined
    @beforeClass(retry_on=[AssertionError, IndexError, ConnectionError])
    def search_profit_loss(self):
        # print(' random.choice(SPLIT_LIST)', random.choice(SPLIT_LIST))
        rec = _tool.get_profit_loss(SPLIT_LIST, '80882')
        print('profit_dict', rec)
        PROFIT_LIST.append(rec)
        return PROFIT_LIST
        # return profit_list

    # noinspection PyGlobalUndefined
    @beforeClass(retry_on=[AssertionError, IndexError, ConnectionError])
    def res_be_detail(self):
        global res
        while True:
            try:
                # concatenate(a="Real", b="Python", c="Is", d="Great", e="!")
                res = _tool.get_params(1,3,lot_code=LOT_CODE, bet_code=BET_CODE,
                                       amount=AMOUNT,
                                       betDetail=BET_DETAIL, bets=BETS)
                print('res', res)
                # print('res', type(res))
                assert_that(res[0].get('code')).is_equal_to(20000)  # 校验请求返回code是否正确
                break
                # return res
            except AssertionError:
                print("Oops!  That was no valid issue.  Try again...")

    def is_split(self, **kwargs):
        # print('isTure[0]', kwargs.get('isTrue'))
        self.mysql.insert_split_detail(lot_code=kwargs.get('lottery_code'), bet_code=kwargs.get('bet_type_code'),
                                       bet_id=kwargs.get('bet_id'),
                                       bet_detail=kwargs.get('bet_detail'),
                                       api_result=[','.join(kwargs.get('api_split_result'))],
                                       test_result=[','.join(kwargs.get('test_split_result'))],
                                       difference=[','.join(kwargs.get('diff'))],
                                       isTrue=kwargs.get('isTrueOrFalse'),
                                       datetime=kwargs.get('datetime'), issue=kwargs.get('issue'))

    @test(owner='Eagle', priority=1, skip=False, component='Check whether the betting order is successfully stored')
    def check_bet_detail(self):
        """
        检测投注数据是否成功入库，依据bet_id查询数据库表中是否存在数据，并且"split_status": 1
        :return:
        """
        time.sleep(1)
        # res = self.before_class()
        bet_id = res[1].get('betId')
        result = self._sql.nac_bet_detail_received_record_one(bet_id)  # 数据库查询语句，查询条件bet_id
        assert_that(result[0] == 1).is_true()  # 校验是否成功存入数据库
        assert_that(result[1].get('split_status') == 1).is_true()  # 拆号状态为1才是成功入库的数据

    @test(owner='Eagle', priority=2, component='Check whether the number splitting data is correct')
    def check_split_detail(self):
        """
        检测拆号数据是否正确，由API返回结果和校验数据进行比较，如果正确则返回True，如果不正确则返回差集
        :return:
        """
        api_split_result = []
        bet_type_code = res[1].get('betTypeCode')  # 获取玩法code
        betId = res[1].get('betId')  # 获取注单唯一ID
        issue = res[1].get('issue')  # 获取投注期号
        bet_detail = res[1].get('betDetail')  # 获取投注号码
        lottery_code = res[1].get('lotteryCode')  # 获取彩种code
        datetime = _tool.get_time_now('%Y-%m-%d %H:%M:%S')
        result = _tool.get_split_api(lottery_code, bet_type_code, bet_detail)  # 获取API拆号结果

        # 处理API返回的拆号结果
        for i in result[1]:
            lis = i.replace(',', '')
            api_split_result.append(lis)

        test_split_result = list({}.fromkeys(SPLIT_LIST).keys())
        isTure = _tool.check_split_equal(test_split_result, api_split_result)
        print('isTure', isTure[1])
        self.is_split(lottery_code=lottery_code, bet_type_code=bet_type_code, bet_id=betId,
                      bet_detail=bet_detail,
                      api_split_result=api_split_result, test_split_result=test_split_result, diff=isTure[1],
                      isTrueOrFalse=isTure[0],
                      datetime=datetime, issue=issue)
        assert_that(isTure[0]).is_equal_to(True)  # 拆号数据是否不一致

    # noinspection PyGlobalUndefined
    @test(owner='Eagle', priority=3, parallelized_parameters=True,
          parameters=PROFIT_LIST, component='Check whether the profit and loss are correct')
    def check_profit_loss(self, parameter):
        global test_profit_loss, api_profit_loss
        # print('parameter',''.join(parameter.keys()))
        # 获取投注接口的返回值
        bet_id = res[1].get('betId')
        bet_amount = res[1].get('betAmount')
        issue = res[1].get('issue')
        print('issue', issue)
        # 从数据库获取玩法对应的奖金
        tlt = {}
        ppt = {}
        sums = []
        after_key = []
        print("''.join(parameter.keys())", ''.join(parameter.keys()))  # 获取中奖号码
        _cis = list(it.combinations(''.join(parameter.keys()), 3))  # 获取中奖号码，任意三个字符的组合
        print('_cis', _cis)
        for v in _cis:
            [tlt.setdefault(i, ''.join(v).count(i)) for i in ''.join(v)]  # 统计每组三位数的重复次数
            print('list(tlt.values())', list(tlt.values()))
            if 2 in list(tlt.values()):
                print('组三')  # 将符合组三的每组数据的之和，依照字典形式{keys：sums}保存到数组
                sums.append({'组三': str(int(''.join(v)[0]) + int(''.join(v)[1]) + int(''.join(v)[2]))})
            else:
                print('组六')  # 将符合组六的每组数据的之和，依照字典形式{keys：sums}保存到数组
                sums.append({'组六': str(int(''.join(v)[0]) + int(''.join(v)[1]) + int(''.join(v)[2]))})
            tlt.clear()  # 每次循环初始化字典
        # 循环字典和值{keys：sums}数组
        print('sums', sums)
        print("BET_DETAIL.split('_')[1].split('|')", BET_DETAIL.split('_')[1].split('|'))
        for c in sums:
            # 判断和值是否在注单号码和值数组内，将符合条件的keys存在到数组
            if ''.join(c.values()) in BET_DETAIL.split('_')[1].split('|'):
                print(c.keys())
                after_key.extend(c.keys())
        print('after_key', after_key)
        [ppt.setdefault(i, after_key.count(i)) for i in after_key]  # 统计重复次数
        ls_bonus = []
        for i in ppt:
            if i == '组六':
                theory_bonus = self._sql.nac_theory_bonus('16_11_15_2')[1].get('theory_bonus')  # 获取组六理论奖金
                count = int(ppt.get('组六'))  # 获取中奖次数
                print('theory_bonus-组六', theory_bonus)
                print('count-组六', count)
                group_six = _tool.calculate_profit_loss_sum(bet_amount, BETS, AMOUNT, theory_bonus, count)
                ls_bonus.append(group_six)
                # print('test_profit_loss_6',test_profit_loss_6)
            else:
                theory_bonus = self._sql.nac_theory_bonus('16_11_15_1')[1].get('theory_bonus')  # 获取组三理论奖金
                count = int(ppt.get('组三'))  # 获取中奖次数
                print('theory_bonus-组三', theory_bonus)
                print('count-组三', count)
                group_three = _tool.calculate_profit_loss_sum(bet_amount, BETS, AMOUNT, theory_bonus, count)
                ls_bonus.append(group_three)
                # print('test_profit_loss_3', test_profit_loss_3)
        test_profit_loss = Decimal(bet_amount).quantize(Decimal('0.0000')) - sum(ls_bonus)

        # 盈亏API查询结果
        open_number = ''.join(parameter.keys())  # 提取键
        ls_profit = [str(','.join(open_number))]  # 获取查询号码 ['1','2','3','4','5']
        print('ls_profit', ls_profit)
        api_profit = _tool.get_api_profit(LOT_CODE, ls_profit, issue)
        print('api_profit', api_profit)
        while api_profit.get('message') == '只能查询已开奖奖期':
            try:
                time.sleep(1)
                print('a', api_profit.get('message'))
                new_api_profit = _tool.get_api_profit(LOT_CODE, ls_profit, issue)
                if new_api_profit.get('message') == '操作成功':
                    api_profit_loss = new_api_profit.get('data').get(''.join(ls_profit))
                    break
            except AssertionError:
                print("Oops!  只能查询已开奖奖期.  Try again...")
        else:
            time.sleep(1)
            api_profit_loss = api_profit.get('data').get(''.join(ls_profit))
            print('api_profit_loss', api_profit_loss)
        print('float(test_profit_loss)', float(test_profit_loss))
        print('float(api_profit_loss)', float(api_profit_loss))
        print('test_profit_loss_type', type(test_profit_loss))
        print('api_profit_loss_type', type(api_profit_loss))
        is_profit_loss = float(test_profit_loss) == float(api_profit_loss)
        self.mysql.update_profit(query_num=open_number, api_profit_loss=api_profit_loss,
                                 test_profit_loss=test_profit_loss,
                                 is_profit_loss=is_profit_loss, bet_id=bet_id)
        assert_that(is_profit_loss).is_equal_to(True)  # 判断盈亏数据是否一致


if "__main__" == __name__:
    # tool = Tools()
    report = _tool.add_file()
    runner = Runner([NacSplitProfit161115], html_report=report + "\\nac_split_profit_report.html",
                    monitor_resources=True)
    # runner.run(features='ffc_issue',test_multithreading_limit=len(aly_code),quiet=True)
    aggregator = runner.run()
    # aggregator = runner.run(test_multithreading_limit=1)
