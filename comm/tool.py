#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project : nac-ele
# @Author  : Eagle
# @Site    : 
# @File    : tool.py
# @Time    : 2021/6/26 14:46
# @Software: PyCharm
import decimal
import hashlib
import itertools

import operator
import os
import itertools as it
import re
from contextlib import closing
from datetime import datetime, timezone, timedelta
import random
import time
from decimal import Decimal, ROUND_DOWN
from os.path import dirname, abspath
from shutil import copyfile
from typing import List

import requests
from assertpy import assert_that
from dateutil.relativedelta import relativedelta
from interval import Interval
from ruamel.yaml import YAML

from comm.config import Config

WORKER_ID_BITS = 5
SEQUENCE_BITS = 12

# 最大取值计算
MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)

# 移位偏移计算
WORKER_ID_SHIFT = SEQUENCE_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
# print(WORKER_ID_SHIFT, TIMESTAMP_LEFT_SHIFT)

# 序号循环掩码
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)
# print(SEQUENCE_MASK)

# 起始时间
TWEPOCH = 1594977661913

# 读取[headers]参数信息
conf = Config()
app_id = conf.get('headers', 'appId')
app_key = conf.get('headers', 'appKey')
base_dir = dirname(dirname(abspath(__file__)))


class IdWorker(object):

    def __init__(self, worker_id, sequence=0):
        """

        :param worker_id: 机房和机器的ID 最大编号可为00 - 31  实际使用范围 00 - 29  备用 30 31
        :param sequence: 初始码
        """
        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError('worker_id值越界')

        self.worker_id = worker_id
        self.sequence = sequence
        self.last_timestamp = -1  # 上次计算的时间戳

    @staticmethod
    def get_timestamp() -> int:
        """
        生成毫秒级时间戳
        :return: 毫秒级时间戳
        """
        return int(time.time() * 1000)

    def wait_next_millis(self, last_timestamp) -> int:
        """
        等到下一毫秒
        """
        timestamp = self.get_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self.get_timestamp()
        return timestamp

    def get_id(self) -> str:
        """"""
        timestamp = self.get_timestamp()
        # 判断服务器的时间是否发生了错乱或者回拨
        if timestamp < self.last_timestamp:
            # 如果服务器发生错乱 应该抛出异常
            # 此处待完善
            pass

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self.wait_next_millis(self.last_timestamp)
        else:
            self.sequence = 0
        self.last_timestamp = timestamp
        new_id = ((timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT) | (self.worker_id << WORKER_ID_SHIFT) | self.sequence
        return new_id


class Tools(object):
    def __init__(self):
        self.worker = IdWorker(worker_id=1, sequence=0)
        self.headers = self.get_headers()
        self.session = requests.session()
        self.conf = Config()
        # 获取盈亏接口地址、路由和请求头
        self.profit_url = self.conf.get('url', 'profit_url')
        self.profit_rout = self.conf.get('rout', 'profit_rout')

        # 获取拆号接口地址、路由和请求头
        self.split_url = self.conf.get('url', 'split_url')
        self.split_rout = self.conf.get('rout', 'split_rout')

        # 获取奖期接口地址和路由
        self.issue_url = self.conf.get('url', 'issue_url')
        self.issue_rout = self.conf.get('rout', 'issue_rout')

        # 获取投注接口地址、路由和请求头
        self.bet_url = self.conf.get('url', 'bet_url')
        self.bet_rout = self.conf.get('rout', 'bet_rout')
        self._str = '_'
        self.num_list = None

        # 日期格式
        self.f_date = "%Y-%m-%d"
        self.f_time = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def add_file() -> str:
        """
        如果不存在测试报告目录，则创建测试报告文件目录，
        :return:
        """
        report_path = os.path.abspath(base_dir + '\\report')
        if not os.path.exists(report_path):
            os.mkdir(report_path)
        return report_path

    @staticmethod
    def copy_report(report_dir) -> str:
        """
        拷贝文件到指定目录
        :param report_dir: 目录地址
        :return:
        """
        # List all files in the directory
        all_file = os.listdir(report_dir)
        # Sort file modification time in ascending order
        all_file.sort(key=lambda fn: os.path.getmtime(report_dir + fn))
        all_file.sort(key=lambda fn: report_dir)
        # Get the file with the latest modification time
        filetime = datetime.fromtimestamp(os.path.getmtime(report_dir + all_file[-1]))
        # print('Get the file with the latest modification time : %s' % filetime)
        # Get the directory where the file is located
        filepath = os.path.join(report_dir, all_file[-1])
        # print("The latest modified file is：" + all_file[-1])
        print("time：" + filetime.strftime('%Y-%m-%d %H-%M-%S'))
        pro_copy = conf.get('copy', 'pro_copy')
        copyfile(filepath, pro_copy + all_file[-1])
        return all_file[-1]

    @staticmethod
    def get_yaml():
        """
        从data.yaml文件获取数据
        :return:
        """
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                            'yaml', 'data.yaml')
        test_data_file = os.path.abspath(path)
        file = open(test_data_file, 'r', encoding='utf-8')
        yaml = YAML(typ='safe')
        # data_yaml = YAML.load(file, Loader=yaml.RoundTripLoader)
        data_yaml = yaml.load(file)
        file.close()
        return data_yaml

    @staticmethod
    def get_random_str(num: int) -> str:
        """
        获取随机字符串
        :return:
        """
        chart = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        salt = ''
        for i in range(num):
            salt += random.choice(chart)
        return salt

    @staticmethod
    def get_timestamp() -> str:
        """
        获取日期的10位时间戳
        :return:
        """
        utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
        str_dt = (bj_dt + relativedelta(seconds=-3)).strftime("%Y-%m-%d %H:%M:%S")
        stp_dt = datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(stp_dt.timetuple()))
        return str(time_stamp)

    def generate_bet_time(self) -> str:
        """
        生成注单时间
        :return: 2021-05-13 13:34:49.938
        """
        return self.get_time_now('%Y-%m-%d %H:%M:%S.%f')[:-3]

    def generate_bet_ip(self) -> str:
        """
        获取固定IP地址
        :return: str 10.32.34.51
        """
        return self.get_yaml()['nac'].get('bet_ip')

    def generate_bet_id(self) -> str:
        """
        生成不重复订单号码
        :return:
        """
        _id = self.worker.get_id()
        _time = self.get_time_now('%Y%m%d')
        return str(_time) + str(_id)

    @staticmethod
    def generate_bet_amount(amount, num) -> str:
        """
        生成注单金额
        :param num:
        :param amount:  Decimal
        :return: String
        """
        # bets = self.generate_bets()
        return str(Decimal(Decimal(amount) * int(num)).quantize(Decimal('.0000'), rounding=ROUND_DOWN))

    def generate_bet_name(self) -> str:
        """
        获取固定的用户姓名
        :return: String
        """
        return self.get_yaml()['nac'].get('player_code')

    @staticmethod
    def get_time_now(formats: str) -> str:
        """
        获取当前日期 %Y-%m-%d %H:%M:%S
        :return: 2021-04-28 15:39:40 or 2021-04-29 ..
        """
        return (datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))).strftime(
            formats)

    @staticmethod
    def get_nac_signature(nonce_str=None, timestamp=None) -> str:
        """
        依据签名算法获取签名信息
        :param nonce_str: 随机字符串
        :param timestamp: 10位时间戳
        :return:
        """
        data = {
            "appId": "%s" % app_id,
            "nonce-str": "%s" % nonce_str,
            "timestamp": "%s" % str(timestamp)
        }
        # 定义空列表
        _lis = []
        # 定义空字符串
        stringA = ""
        # 循环遍历字典数据的键值，取出存放到列表中
        for key in data.keys():
            _lis.append(key)
        # 对列表的对象进行排序，默认升序，即按照ASCII码从小到大排序
        _lis.sort()
        # 循环遍历排序后的列表，根据键值取出字典键对应的值
        for i in _lis:
            stringA += i + "=" + data[i] + "&"
        # 参数拼接成需要加密的字符串
        # print('stringA', stringA)
        stringA += "appKey" + "=" + app_key
        # 创建对象md
        md = hashlib.md5()
        # 对stringA字符串进行编码
        md.update(stringA.encode('utf-8'))
        # 数据加密
        sign_value = md.hexdigest()
        # 把加密的结果，小写转换成大写，upper函数
        sign_value = sign_value.upper()
        return sign_value

    @staticmethod
    def check_split_equal(test_list: list, api_list: list):
        """
        比较两个数组的元素是否一致,如果一致，则返回Ture和[]。如果不一致则返回False和差集
        :param test_list: Test方法获取的拆号数据
        :param api_list:  API接口返回的拆号数据
        :return: 如果一致，则返回Ture。如果不一致则返回差值
        """
        test_list.sort()
        api_list.sort()
        print('test_list', test_list)
        print('api_list', api_list)
        print(len(test_list))
        print(len(api_list))
        isTure = operator.eq(set(test_list), set(api_list))
        if isTure:
            return True, []
        else:
            result = list(set(test_list).symmetric_difference(set(api_list)))
            return False, result

    @staticmethod
    def get_is_during(n_time: str, open_time: str, minute: int, second: int) -> bool:
        """
        通过当前时间与奖期开奖时间比较，判断是否
        :param n_time: 当前时间
        :param open_time: 奖期接口数据每期开奖时间
        :param minute: 分钟
        :param second: 秒
        :return:
        """
        o_time = datetime.fromisoformat(open_time.replace('T', ' '))
        s_time = o_time.strftime("%Y-%m-%d %H:%M:%S")
        e_time = (o_time + relativedelta(minutes=minute) - relativedelta(seconds=second)).strftime("%Y-%m-%d %H:%M:%S")
        b = Interval(s_time, e_time)
        # print('b', b)
        n = Interval(n_time, n_time)
        # print('n', n)
        if n in b:
            return True
        else:
            return False

    def is_during_date(self, n_time: str, open_time: str, dur: str, minute=None, second=None) -> int:
        """

        :param n_time: 当前时间
        :param open_time: 奖期api开奖时间
        :param dur: 调用的方法
        :param minute: 分钟
        :param second: 秒
        :return: 奖期
        """
        is_dict = {
            'dur': self.get_is_during(n_time, open_time, minute, second)
        }
        return is_dict.get(dur)

    @staticmethod
    def isInter(a, b):
        """
        判断是否存在交集
        :param a:
        :param b:
        :return:
        """
        result = list(set(a) & set(b))
        if result:
            return True
        else:
            return False

    @staticmethod
    def calculate_profit_loss(bet_amount: decimal, bets: int, amount: decimal, theory_bonus: decimal,
                              count: int) -> decimal:
        """
        获得拆号结果，依据开奖号码的中奖次数计算盈亏
        :param bet_amount: 投注金额
        :param bets: 注数
        :param amount: 单位
        :param theory_bonus: 理论奖金
        :param count: 中奖次数
        :return: 保留4位小数，向下取整
        """
        # getcontext().rounding = getattr(decimal, 'ROUND_DOWN')
        bonus = (Decimal(bet_amount).quantize(Decimal('0.0000')) / Decimal(bets) / Decimal(amount).quantize(
            Decimal('0.0000'))) * Decimal(theory_bonus).quantize(Decimal('0.0000')) * (
                        Decimal(amount).quantize(Decimal('0.0000')) / 2)
        # bonus = float(bet_amount) / float(bets) / float(amount) * float(theory_bonus) * (float(amount) / 2)
        print("bonus", Decimal(bonus).quantize(
            Decimal('0.0000'), decimal.ROUND_DOWN))
        print('amount', Decimal(amount).quantize(Decimal('0.0000')))
        print('theory_bonus', Decimal(theory_bonus).quantize(Decimal('0.0000')))
        print('bet_amount', Decimal(bet_amount).quantize(Decimal('0.0000')))
        print('bets', Decimal(bets))
        print('unit', Decimal(amount).quantize(Decimal('0.0000')) / 2)
        # bonus = Decimal(bonus).quantize(Decimal('0.0000'))
        if int(count) == 1:
            # betAmount/bets/0.01*theory_bonus = 实际奖金
            print("奖金1", Decimal(bonus).quantize(
                Decimal('0.0000'), decimal.ROUND_DOWN))
            test_profit_loss = Decimal(bet_amount).quantize(Decimal('0.0000')) - Decimal(bonus).quantize(
                Decimal('0.0000'), decimal.ROUND_DOWN)
            # test_profit_loss = float(bet_amount) - float(Decimal(bonus).quantize(Decimal('0.0000')))
            print('test_profit_loss1', test_profit_loss)
            return test_profit_loss
        else:
            # betAmount/bets/0.01*theory_bonus = 实际奖金
            print("奖金2", Decimal(bonus).quantize(
                Decimal('0.0000'), decimal.ROUND_DOWN))
            # bonus = Decimal(bonus).quantize(Decimal('0.0000'))
            # reg = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
            # res = reg.match(str(bonus))
            test_profit_loss = Decimal(bet_amount).quantize(Decimal('0.0000')) - Decimal(bonus).quantize(
                Decimal('0.0000'), decimal.ROUND_DOWN) * Decimal(count)
            print('test_profit_loss2', test_profit_loss)
            return test_profit_loss

    #
    # @staticmethod
    # def calculate_profit_loss_bullfight(bet_amount: decimal, bets: int, amount: decimal, theory_bonus: decimal,
    #                           count: int) -> decimal:
    #     """
    #     获得拆号结果，依据开奖号码的中奖次数计算盈亏
    #     :param bet_amount: 投注金额
    #     :param bets: 注数
    #     :param amount: 单位
    #     :param theory_bonus: 理论奖金
    #     :param count: 中奖次数
    #     :return: 保留4位小数，向下取整
    #     """
    #     # getcontext().rounding = getattr(decimal, 'ROUND_DOWN')
    #     bonus = (Decimal(bet_amount).quantize(Decimal('0.0000')) / Decimal(bets) / Decimal(amount).quantize(
    #         Decimal('0.0000'))) * Decimal(theory_bonus).quantize(Decimal('0.0000')) * (
    #                     Decimal(amount).quantize(Decimal('0.0000')) / 2)
    #     # bonus = float(bet_amount) / float(bets) / float(amount) * float(theory_bonus) * (float(amount) / 2)
    #     print('bonus', Decimal(bet_amount).quantize(Decimal('0.0000')))
    #     print('amount', Decimal(amount).quantize(Decimal('0.0000')))
    #     print('theory_bonus', Decimal(theory_bonus).quantize(Decimal('0.0000')))
    #     print('bet_amount', Decimal(bet_amount).quantize(Decimal('0.0000')))
    #     print('bets', Decimal(bets))
    #     print('unit', Decimal(amount).quantize(Decimal('0.0000')) / 2)
    #
    #     if int(count) == 1:
    #         # betAmount/bets/0.01*theory_bonus = 实际奖金
    #         print("奖金1", Decimal(bonus).quantize(Decimal('0.0000')))
    #         test_profit_loss = Decimal(bet_amount).quantize(Decimal('0.0000')) - Decimal(bonus).quantize(
    #             Decimal('0.0000'), decimal.ROUND_DOWN)
    #         # test_profit_loss = float(bet_amount) - float(Decimal(bonus).quantize(Decimal('0.0000')))
    #         print('test_profit_loss1', test_profit_loss)
    #         return test_profit_loss
    #     else:
    #         # betAmount/bets/0.01*theory_bonus = 实际奖金
    #         print("奖金2", Decimal(bonus).quantize(Decimal('0.0000')))
    #
    #         test_profit_loss = Decimal(bet_amount).quantize(Decimal('0.0000')) - Decimal(bonus).quantize(
    #             Decimal('0.0000'), decimal.ROUND_DOWN) * Decimal(count)
    #         print('test_profit_loss2', test_profit_loss)
    #         return test_profit_loss

    @staticmethod
    def calculate_profit_loss_sum(bet_amount: decimal, bets: int, amount: decimal, theory_bonus: decimal,
                                  count: int) -> decimal:
        """
        获得拆号结果，依据开奖号码的中奖次数计算盈亏,中了不同子玩法的盈亏计算法
        :param bet_amount: 投注金额
        :param bets: 注数
        :param amount: 单位
        :param theory_bonus: 理论奖金
        :param count: 中奖次数
        :return: 保留4位小数，向下取整
        """
        # getcontext().rounding = getattr(decimal, 'ROUND_DOWN')
        bonus = (Decimal(bet_amount).quantize(Decimal('0.0000')) / Decimal(bets) / Decimal(amount).quantize(
            Decimal('0.0000'))) * Decimal(theory_bonus).quantize(Decimal('0.0000')) * (
                        Decimal(amount).quantize(Decimal('0.0000')) / 2)
        # bonus = float(bet_amount) / float(bets) / float(amount) * float(theory_bonus) * (float(amount) / 2)
        print('bonus', Decimal(bet_amount).quantize(Decimal('0.0000')))
        print('amount', Decimal(amount).quantize(Decimal('0.0000')))
        print('theory_bonus', Decimal(theory_bonus).quantize(Decimal('0.0000')))
        print('bet_amount', Decimal(bet_amount).quantize(Decimal('0.0000')))
        print('bets', Decimal(bets))
        print('unit', Decimal(amount).quantize(Decimal('0.0000')) / 2)

        if int(count) == 1:
            # betAmount/bets/0.01*theory_bonus = 实际奖金
            print("奖金1", Decimal(bonus).quantize(Decimal('0.0000')))
            test_profit_loss = Decimal(bonus).quantize(Decimal('0.0000'), decimal.ROUND_DOWN)
            # test_profit_loss = float(bet_amount) - float(Decimal(bonus).quantize(Decimal('0.0000')))
            print('test_profit_loss1', test_profit_loss)
            return test_profit_loss
        else:
            # betAmount/bets/0.01*theory_bonus = 实际奖金
            print("奖金2", Decimal(bonus).quantize(Decimal('0.0000')))

            test_profit_loss = Decimal(bonus).quantize(Decimal('0.0000'), decimal.ROUND_DOWN) * Decimal(count)
            print('test_profit_loss2', test_profit_loss)
            return test_profit_loss

    @staticmethod
    def lottery_data_source() -> list:
        """
        获取包含所有5位数的数组
        :return:
        """
        _all = list(it.product(range(10), repeat=5))
        return [''.join(map(str, list(i))) for i in _all]

    def get_headers(self, content_type=1) -> dict:
        """
        获取指定的任意类型请求头
        :param content_type: -1,0,1,2,3
        :return:
        """
        nonce_str = self.get_random_str(6)
        timestamp = self.get_timestamp()
        signature = self.get_nac_signature(nonce_str, timestamp)
        headers = {}
        if content_type == -1:
            pass  # 无   Content-Type 属性
        elif content_type == 0:
            headers['Content-Type'] = "application/json; charset=UTF-8"
            headers['appId'] = app_id
            headers['appKey'] = app_key
            headers['nonce-str'] = nonce_str
            headers['timestamp'] = timestamp
            headers['signature'] = signature
            # headers['charset'] = "UTF-8"
        elif content_type == 1:
            headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
        elif content_type == 2:
            headers['Content-Type'] = "multipart/form-data"
        elif content_type == 3:
            headers['Content-Type'] = "application/json; charset=UTF-8"

        return headers

    def request(self, method: str, url: str, params=None, data=None, json=None, headers=None, **kwargs) -> map:
        """
        基础request请求方法
        :param method: 请求类型，如Post、get等
        :param url: 请求地址
        :param params: 请求参数
        :param data: 请求参数
        :param json: json类型请求参数
        :param headers: 请求头
        :param kwargs: 字典类型参数
        :return:
        """
        try:
            self.session.keep_alive = False
            # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
            with closing(self.session.request(method, url, params=params, data=data, json=json, headers=headers,
                                              **kwargs)) as res:
                res.close()
            # r.encoding = 'UTF-8'
        except Exception as e:
            print(f"请求都失败了，即将返回空值，请耐心等待...", e)
        else:
            self.session.close()
            res.close()
            return res
        return {}

    def close(self):
        """
        关闭连接
        :return:
        """
        return self.session.close()

    def get_draw_issue(self, code: str, date: str, days: int, _url: str, _rout: str):
        """
        获取奖期返回数据
        :param code: 彩种code
        :param date: 当前日期
        :param days: 天
        :param _url: 请求地址
        :param _rout: 请求路由
        :return:
        """
        url = _url + _rout
        params = {'code': code, 'date': date, 'days': days}
        header = self.get_headers(content_type=1)
        res = self.request("get", url, params, header)
        res.close()
        return res.json()

    def res_open_api(self):
        # 尚未实际用到nac
        tns_api_url = self.conf.get('tns', 'tns_openApi_pre')
        headers = self.get_headers(content_type=3)
        res = self.request('get', tns_api_url, headers)
        res.close()
        return res.json()

    def get_issue(self, code: str, dur: str, minute=None, second=None) -> str:
        """
        # 通过彩期接口获取期号，并检测期号与线上的期号是否正确
        :param code: 彩种code
        :param dur:
        :param minute: 分钟
        :param second: 秒
        :return:
        """

        # 获取彩期的
        date = self.get_time_now(self.f_date)
        days = 1
        n_time = self.get_time_now(self.f_time)
        draw_issue = self.get_draw_issue(code, date, days, self.issue_url, self.issue_rout)
        # print('draw_issue', draw_issue)

        for i in draw_issue:
            isTrue = self.is_during_date(n_time, i.get('openTime'), dur, minute, second)
            if isTrue:
                signature = i.get('signature')
                return signature

    def dur_issue(self, code: str, dur: str, minute=None, second=None):
        # 尚未使用
        date = self.get_time_now(self.f_date)
        days = 1
        n_time = self.get_time_now(self.f_time)
        draw_issue = self.get_draw_issue(code, date, days, self.issue_url, self.issue_rout)
        bol = []
        for i in draw_issue:
            isTrue = self.is_during_date(n_time, i.get('openTime'), dur, minute, second)
            bol.append(isTrue)
        return bol

    def compare_issue(self, par: str, dur: str, minute=None, second=None):
        # nac-尚未使用
        api = self.res_open_api()
        signature = self.get_issue(par, dur, minute, second)
        # print('signature',signature)
        lis = api['data']
        for i in lis:
            if i.get('code') == par:
                return assert_that(i.get('expect')).is_equal_to(signature)

    def get_api_profit(self, lot_code: str, open_number: list, issue: str):
        """
        通过盈亏API接口，获取对应玩法的盈亏返回数据
        :param lot_code: 彩种code
        :param open_number: 要查询的中奖号码
        :param issue: 奖期
        :return:
        """
        import json
        header = self.get_headers(content_type=0)
        url = self.profit_url + self.profit_rout
        json_data = {"lotteryCode": lot_code, "numberList": open_number, "issue": issue}
        # print('data',json_data)
        res = self.request('post', url, data=json.dumps(json_data), headers=header)
        # print('res',res)
        return res.json()

    def get_split_api(self, lot_code: str, bet_code: str, bet_detail: str):
        """
        获取普通玩法的API的拆号结果
        :param lot_code: 彩种code
        :param bet_code: 玩法code
        :param bet_detail: 投注号码
        :return:
        """
        import json
        header = self.get_headers(content_type=0)
        url = self.split_url + self.split_rout
        json_data = {"lotteryCode": lot_code, "betTypeCode": bet_code, "betDetail": bet_detail}
        res = self.request('post', url, data=json.dumps(json_data), headers=header)
        return len(res.json().get('data')), res.json().get('data')

    @staticmethod
    def get_profit_loss(_lis: list, open_number: str) -> dict:
        set_lst = set(_lis)
        profit = {}
        if len(set_lst) == len(_lis):
            print("不存在重复的值")
            for item in _lis:
                if item == open_number:
                    profit.update({item: _lis.count(item)})
            print('True', profit)
            return profit
        else:
            print('存在重复的元素!')
            for item in _lis:
                if item == open_number:
                    profit.update({item: _lis.count(item)})
            print('False', profit)
            return profit

    def get_split_api_double_sided(self, lot_code: str, bet_code: str, bet_detail: str):
        """
        获取双面盘新玩法的API的拆号结果
        :param lot_code: 彩种code
        :param bet_code: 玩法code
        :param bet_detail: 投注号码
        :return:
        """
        import json
        header = self.get_headers(content_type=0)
        url = self.split_url + self.split_rout
        # print('url', url)
        json_data = {"lotteryCode": lot_code, "betTypeCode": bet_code, "betDetail": bet_detail, 'type': 2}
        res = self.request('post', url, data=json.dumps(json_data), headers=header)
        print('res', res)
        res_json = res.json()
        # res_json.get('data')
        return len(res_json.get('data')), res_json.get('data')


    def get_split_api_pk10_sided(self, lot_code: str, bet_code: str, bet_detail: str,issue:str):
        """
        获取pk10玩法的API的拆号结果
        :param lot_code: 彩种code
        :param bet_code: 玩法code
        :param bet_detail: 投注号码
        :return:
        """
        import json
        header = self.get_headers(content_type=0)
        url = self.split_url + self.split_rout
        # print('url', url)
        json_data = {"lotteryCode": lot_code, "betTypeCode": bet_code, "betDetail": bet_detail, "issue": issue,'type': 3}
        res = self.request('post', url, data=json.dumps(json_data), headers=header)
        print('res', res)
        res_json = res.json()
        # res_json.get('data')
        return len(res_json.get('data')), res_json.get('data')

    def replace_params(self, **kwargs):
        """
        从yaml文件中读取普通玩法，注单请求的body参数
        :param kwargs: N个参数
        :return:
        """
        import json
        params = self.get_yaml()['nac'].get('bet_params')
        serialization = json.dumps(params)
        for key, value in kwargs.items():
            serialization = serialization.replace(f'${{{key}}}', value)
        deserialization = json.loads(serialization)
        return deserialization

    def replace_double_sided_params(self, **kwargs):
        """
        从yaml文件中读取双面盘新玩法，注单请求的body参数
        :param kwargs: N个参数
        :return:
        """
        import json
        params = self.get_yaml()['nac'].get('bet_double_sided_params')
        serialization = json.dumps(params)
        for key, value in kwargs.items():
            serialization = serialization.replace(f'${{{key}}}', value)
        deserialization = json.loads(serialization)
        return deserialization

    def get_params(self, minute: int, second: int, **kwargs):
        """
        普通玩法的投注请求方法
        :param second:
        :param minute:
        :param kwargs: N个传参
        :return: Json data
        """
        header = self.get_headers(content_type=0)
        betId = self.generate_bet_id()
        betIp = self.generate_bet_ip()
        betAmount = self.generate_bet_amount(kwargs.get('amount'), kwargs.get('bets'))
        betTime = self.generate_bet_time()
        playerCode = self.generate_bet_name()
        # 快3 如果不是快3 则不需要加1
        issue_result = self.get_issue(kwargs.get('lot_code'), 'dur', minute, second)
        # if kwargs.get('lot_code').find('k3') != -1:
        #     issue = str(int(issue_result) + 1)
        # else:
        #     issue = issue_result
        issue = str(int(issue_result) + 1)
        nac_bet_url = self.bet_url + self.bet_rout

        json_params = self.replace_params(
            lotteryCode=kwargs.get('lot_code'),
            betId=betId,
            betTypeCode=kwargs.get('bet_code'),
            betDetail=kwargs.get('betDetail'),
            bets=str(kwargs.get('bets')),
            betAmount=betAmount,
            playerCode=playerCode,
            issue=issue,
            betIp=betIp,
            betTime=betTime
        )
        up = {'bets': int(kwargs.get('bets')), 'betAmount': float(betAmount)}
        json_params.update(up)
        try:
            res = self.request('post', nac_bet_url, json=json_params, headers=header)
            _json = res.json()
        except Exception as e:
            print(e)
        else:
            self.close()
            res.close()
            return _json, json_params

    def get_double_sided_params(self, minute: int, second: int, **kwargs):
        """
        双面盘新玩法的投注请求方法
        :param second:
        :param minute:
        :param kwargs:
        :return: Json data
        """
        header = self.get_headers(content_type=0)
        betId = self.generate_bet_id()
        betIp = self.generate_bet_ip()
        betAmount = self.generate_bet_amount(kwargs.get('amount'), kwargs.get('bets'))
        betTime = self.generate_bet_time()
        playerCode = self.generate_bet_name()
        # if kwargs.get('lot_code') == 'txffc'
        issue_result = self.get_issue(kwargs.get('lot_code'), 'dur', minute, second)
        print('issue_result', issue_result)
        issue = str(int(issue_result) + 1)
        print('issue', issue)

        nac_bet_url = self.bet_url + self.bet_rout
        # type_value = 2
        json_params = self.replace_double_sided_params(
            lotteryCode=kwargs.get('lot_code'),
            betId=betId,
            betTypeCode=kwargs.get('bet_code'),
            # betDetail=kwargs.get('betDetail'),
            bets=str(kwargs.get('bets')),
            betAmount=betAmount,
            playerCode=playerCode,
            issue=issue,
            betIp=betIp,
            betTime=betTime,
            type=str(kwargs.get('type'))
        )
        # bet_detail = "[{\"numbers\":\"%s\",\"betPrice\":50}]" % kwargs.get('betDetail')
        up = {'bets': int(kwargs.get('bets')), 'betAmount': float(betAmount), 'type': int(kwargs.get('type')),
              'betDetail': kwargs.get('betDetail')}
        json_params.update(up)
        # # print('new_params', json_params)
        try:
            res = self.request('post', nac_bet_url, json=json_params, headers=header)
            _json = res.json()
        except Exception as e:
            print(e)
        else:
            self.close()
            res.close()
            return _json, json_params

    def get_rcs_excel_params(self, **kwargs):
        """
        从excel获取请求参数的，投注请求方法
        :param kwargs:
        :return:
        """
        header = self.get_headers(content_type=0)
        betId = self.generate_bet_id()
        betTime = self.generate_bet_time()
        playerCode = self.generate_bet_name()
        issue = self.get_issue(kwargs.get('lot_code'), 'dur', -1, 0)
        nac_bet_url = self.bet_url + self.bet_rout

        json_params = self.replace_params(
            lotteryCode=kwargs.get('lot_code'),
            betId=betId,
            betTypeCode=kwargs.get('bet_code'),
            betDetail=kwargs.get('betDetail'),
            bets=kwargs.get('bets'),
            betAmount=kwargs.get('betAmount'),
            playerCode=playerCode,
            issue=issue,
            betIp=kwargs.get('ip'),
            betTime=betTime
        )
        up = {'bets': int(kwargs.get('bets')), 'betAmount': float(kwargs.get('betAmount'))}
        json_params.update(up)
        try:
            res = self.request('post', nac_bet_url, json=json_params, headers=header)
            _json = res.json()
        except Exception as e:
            print(e)
        else:
            self.close()
            res.close()
            return _json, json_params

    @staticmethod
    def bet_detail_161213(bet_detail: str, lens: int, after_lis) -> list:
        """
        单式注单号码的处理方法，注单号码格式如：万|千|百|十|个_16|18|19|20
        :param bet_detail: 万|千|百|十|个_16|18|19|20 或者 万|千|百|十|个_118,119
        :param lens: 组合长度
        :return: list
        """
        _lis, str_lis, ls = ([] for j in range(3))
        before = bet_detail.split('_')[0]
        print("before", before)
        # 截取注单号码后半部分
        # after = bet_detail.split('_')[1]
        # print("after", after)
        # 想将位置转换为数组形式

        # 将前部分的位置中文信息替换成下标
        is_position = {'万': '0', '千': '1', '百': '2', '十': '3', '个': '4'}
        for v in before.split('|'):
            _lis.append(is_position.get(v))
        # 生成组合
        details = list(it.combinations(_lis, lens))
        # 将位置由元组转为字符串
        # if ',' in after:
        #     after_lis = after.split(',')
        # else:
        #     after_lis = after.split('|')
        for i in details:
            str_lis.append(''.join(list(i)))
        for index, value in enumerate(after_lis):  # index 是下标，key是a中的值，
            for i, k in enumerate(str_lis):
                dic = {}.fromkeys([k])
                if dic[k] is None:
                    dic[k] = value
                else:
                    dic[k].append(value)
                ls.append(dic)
        return ls

    @staticmethod
    def bet_detail_single(bet_detail: str, lens: int) -> list:
        """
        单式注单号码的处理方法，注单号码格式如：万|千|百|十|个_16|18|19|20
        :param bet_detail: 万|千|百|十|个_16|18|19|20 或者 万|千|百|十|个_118,119
        :param lens: 组合长度
        :return: list
        """
        _lis, str_lis, ls = ([] for j in range(3))
        before = bet_detail.split('_')[0]
        print("before", before)
        # 截取注单号码后半部分
        after = bet_detail.split('_')[1]
        print("after", after)
        # 想将位置转换为数组形式

        # 将前部分的位置中文信息替换成下标
        is_position = {'万': '0', '千': '1', '百': '2', '十': '3', '个': '4'}
        for v in before.split('|'):
            _lis.append(is_position.get(v))
        # 生成组合
        details = list(it.combinations(_lis, lens))
        # 将位置由元组转为字符串
        if ',' in after:
            after_lis = after.split(',')
        else:
            after_lis = after.split('|')
        for i in details:
            str_lis.append(''.join(list(i)))
        for index, value in enumerate(after_lis):  # index 是下标，key是a中的值，
            for i, k in enumerate(str_lis):
                dic = {}.fromkeys([k])
                if dic[k] is None:
                    dic[k] = value
                else:
                    dic[k].append(value)
                ls.append(dic)
        return ls

    @staticmethod
    def bet_detail_single_twin(bet_detail: str, lens: int, length: int) -> list:
        """
        单式注单号码的处理方法，注单号码格式如：万|千|百|十|个_0|1|3
        :param length: 注单后部分组合长度
        :param bet_detail: 万|千|百|十|个_0|1|3
        :param lens: 注单前部分组合长度
        :return: list
        """
        _lis, _ais, bef_lis, aft_lis, ls = ([] for j in range(5))
        before = bet_detail.split('_')[0]
        print("before", before)
        # 截取注单号码后半部分
        after = bet_detail.split('_')[1]
        print("after", after)
        # 想将位置转换为数组形式

        # 将前部分的位置中文信息替换成下标
        is_position = {'万': '0', '千': '1', '百': '2', '十': '3', '个': '4'}
        for v in before.split('|'):
            _lis.append(is_position.get(v))
        for v in after.split('|'):
            _ais.append(v)
        # 生成注单前部分组合
        details = list(it.combinations(_lis, lens))
        # 将位置由元组转为字符串
        for i in details:
            bef_lis.append(''.join(list(i)))
        # 生成注单后部分组合
        it_after = list(it.combinations(_ais, length))
        for i in it_after:
            aft_lis.append(''.join(i))
        for index, value in enumerate(aft_lis):  # index 是下标，key是a中的值，
            for i, k in enumerate(bef_lis):
                dic = {}.fromkeys([k])
                if dic[k] is None:
                    dic[k] = value
                else:
                    dic[k].append(value)
                ls.append(dic)
        return ls

    @staticmethod
    def bet_detail_131410(bet_detail: str, lens: int) -> list:
        """
        复式注单号码的处理方法，注单号码格式如：'1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
        :param bet_detail: '1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
        :param lens: 组合长度
        :return: list
        """
        ls, _lis, _vis, _ris = ([] for r in range(4))
        print(bet_detail.replace('|', '').split(','))
        for i, v in enumerate(bet_detail.replace('|', ' ').split(',')):
            ls.append({v: str(i)})
        # 通过上面的循环将注单数据转换成以下格式，并获取combinations组合：[({'1 2 3': '0'}, {'1 3 4': '1'}, {'2 4 6': '2'})]
        print('ls', ls)
        _cis = list(it.combinations(ls, lens))
        print('_cis', _cis)
        idx = 0
        print('_cis', _cis)
        print('len', len(_cis))
        while len(_cis) < len(_cis) + 1:
            print('c[y]', _cis[idx])
            for bbc in _cis[idx]:
                # print('keys', list(map(str, ''.join(bbc.keys()).split())))
                # print('values', ''.join(bbc.values()))
                _lis.append(list(map(str, ''.join(bbc.keys()).split())))
                _vis.append(''.join(bbc.values()))
            # print('_lis', _lis)
            # print('_vls', ''.join(_vis))
            for item in itertools.product(_lis[0], _lis[1]):
                print('item', {''.join(_vis): ''.join(item)})
                # _ris.append({''.join(_vis): ''.join(item)})
                _ris.append(''.join(item))
            _lis.clear()
            _vis.clear()
            idx = idx + 1
            if idx >= len(_cis):
                break
        # # print('_ris',_ris)
        return _ris

    @staticmethod
    def bet_detail_121410(bet_detail: str, lens: int) -> list:
        """
        复式注单号码的处理方法，注单号码格式如：'1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
        :param bet_detail: '1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
        :param lens: 组合长度
        :return: list
        """
        ls, _lis, _vis, _ris = ([] for r in range(4))
        print(bet_detail.replace('|', '').split(','))
        for i, v in enumerate(bet_detail.replace('|', ' ').split(',')):
            ls.append({v: str(i)})
        # 通过上面的循环将注单数据转换成以下格式，并获取combinations组合：[({'1 2 3': '0'}, {'1 3 4': '1'}, {'2 4 6': '2'})]
        print('ls', ls)
        _cis = list(it.combinations(ls, lens))
        print('_cis', _cis)
        idx = 0
        print('_cis', _cis)
        print('len', len(_cis))
        while len(_cis) < len(_cis) + 1:
            print('c[y]', _cis[idx])
            for bbc in _cis[idx]:
                # print('keys', list(map(str, ''.join(bbc.keys()).split())))
                # print('values', ''.join(bbc.values()))
                _lis.append(list(map(str, ''.join(bbc.keys()).split())))
                _vis.append(''.join(bbc.values()))
            # print('_lis', _lis)
            # print('_vls', ''.join(_vis))
            for item in itertools.product(_lis[0], _lis[1], _lis[2]):
                print('item', {''.join(_vis): ''.join(item)})
                # _ris.append({''.join(_vis): ''.join(item)})
                _ris.append(''.join(item))
            _lis.clear()
            _vis.clear()
            idx = idx + 1
            if idx >= len(_cis):
                break
        # # print('_ris',_ris)
        return _ris

    @staticmethod
    def bet_detail_duplex(bet_detail: str, lens: int) -> list:
        """
        复式注单号码的处理方法，注单号码格式如：'1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
        :param bet_detail: '1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
        :param lens: 组合长度
        :return: list
        """
        ls, _lis, _vis, _ris = ([] for r in range(4))
        # print(bet_detail.replace('|', '').split(','))
        for i, v in enumerate(bet_detail.replace('|', ' ').split(',')):
            if v != '#':
                ls.append({v: str(i)})
        # 通过上面的循环将注单数据转换成以下格式，并获取combinations组合：[({'1 2 3': '0'}, {'1 3 4': '1'}, {'2 4 6': '2'})]
        print('ls', ls)
        _cis = list(it.combinations(ls, lens))
        idx = 0
        print('_cis', _cis)
        print('len', len(_cis))
        while len(_cis) < len(_cis) + 1:
            # print('c[y]', _cis[idx])
            for bbc in _cis[idx]:
                # print('keys', list(map(str, ''.join(bbc.keys()).split())))
                # print('values', ''.join(bbc.values()))
                _lis.append(list(map(str, ''.join(bbc.keys()).split())))
                _vis.append(''.join(bbc.values()))
            # print('_lis', _lis)
            # print('_vls', ''.join(_vis))
            for item in itertools.product(_lis[0], _lis[1], _lis[2]):
                # print('item', {''.join(_vis): ''.join(item)})
                _ris.append({''.join(_vis): ''.join(item)})
            _lis.clear()
            _vis.clear()
            idx = idx + 1
            if idx >= len(_cis):
                break
        # print('_ris',_ris)
        return _ris

    @staticmethod
    def bet_detail_duplex_four(bet_detail: str, lens: int) -> list:
        """
        复式注单号码的处理方法，注单号码格式如：'1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
        :param bet_detail: '1|2|3,1|3|4,2|4|6,3|7|9,6|7|8'
        :param lens: 组合长度
        :return: list
        """
        ls, _lis, _vis, _ris = ([] for r in range(4))
        # print(bet_detail.replace('|', '').split(','))
        for i, v in enumerate(bet_detail.replace('|', ' ').split(',')):
            if v != '#':
                ls.append({v: str(i)})
        # 通过上面的循环将注单数据转换成以下格式，并获取combinations组合：[({'1 2 3': '0'}, {'1 3 4': '1'}, {'2 4 6': '2'})]
        # print('ls',ls)
        _cis = list(it.combinations(ls, lens))
        idx = 0
        # print('_cis',_cis)
        # print('len',len(_cis))
        while len(_cis) < len(_cis) + 1:
            # print('c[y]', _cis[idx])
            for bbc in _cis[idx]:
                # print('keys', list(map(str, ''.join(bbc.keys()).split())))
                # print('values', ''.join(bbc.values()))
                _lis.append(list(map(str, ''.join(bbc.keys()).split())))
                _vis.append(''.join(bbc.values()))
            # print('_lis', _lis)
            # print('_vls', ''.join(_vis))
            for item in itertools.product(_lis[0], _lis[1], _lis[2], _lis[3]):
                # print('item', {''.join(_vis): ''.join(item)})
                _ris.append({''.join(_vis): ''.join(item)})
            _lis.clear()
            _vis.clear()
            idx = idx + 1
            if idx >= len(_cis):
                break
        # print('_ris',_ris)
        return _ris

    @staticmethod
    def bet_11x5_number(numbers: List[str], num: int) -> list:
        return list(it.combinations(numbers, num))

    @staticmethod
    def bet_11x5_701010(bet_detail: str) -> list:
        ls, ls1 = ([] for _ in range(2))
        _DETAIL = bet_detail.split(',')
        for i in _DETAIL:
            # print(i.split('|'))
            ls.append(i.split('|'))
        # print('ls',ls)

        # print(list(it.product(ls[0],ls[1],ls[2])))
        tlt, _clc = ({} for _ in range(2))
        for num in set(list(it.product(ls[0], ls[1], ls[2]))):
            # print(i)
            [_clc.setdefault(i, num.count(i)) for i in num]
            # print('_clc',_clc)
            if max(_clc.values()) == 1:
                ls1.append(num)
            _clc.clear()
        return ls1

    @staticmethod
    def bet_11x5_711010(bet_detail: str) -> list:
        ls, ls1 = ([] for _ in range(2))
        _DETAIL = bet_detail.split(',')
        for i in _DETAIL:
            # print(i.split('|'))
            ls.append(i.split('|'))
        # print('ls',ls)

        # print(list(it.product(ls[0],ls[1],ls[2])))
        tlt, _clc = ({} for _ in range(2))
        for num in set(list(it.product(ls[0], ls[1]))):
            # print(i)
            [_clc.setdefault(i, num.count(i)) for i in num]
            # print('_clc',_clc)
            if max(_clc.values()) == 1:
                ls1.append(num)
            _clc.clear()
        return ls1

    @staticmethod
    def bet_11x5_701011(bet_detail: str) -> list:
        ls = []
        _DETAIL = bet_detail.split(',')
        for i in _DETAIL:
            # print(i.split('|'))
            ls.append(tuple(i.split('_')))
        return ls

    @staticmethod
    def bet_ssc_161213(numbers: List[str]):
        ls = []
        for i in set(list(it.combinations(list(numbers[0].split('|')), 1))):
            for j in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                if not set(i).intersection(set(j)):
                    ls.append(dict({i[0]: list(j)}))
        return ls

    @staticmethod
    def bet_ssc_161215(numbers: List[str]):
        ls = []
        for i in set(list(it.combinations(list(numbers[0].split('|')), 1))):
            for j in set(list(it.combinations(list(numbers[1].split('|')), 1))):
                if not set(i).intersection(set(j)):
                    ls.append(dict({i[0]: list(j)}))
        return ls

        # if numbers[0].find('|') != -1:
        #     for i in set(list(it.combinations(list(numbers[0].split('|')), 2))):
        #         for j in set(list(numbers[1].split('|'))):
        #             ls.append(tuple(list(i) + [j]))
        #     return ls
        # else:
        #     num1 = [numbers[0]]
        #     for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
        #         ls.append(tuple(num1 + list(i)))
        #     return ls

    @staticmethod
    def bet_11x5_701112(numbers: str):
        ls = []
        if numbers[0].find('|') != -1:
            for i in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                for j in set(list(numbers[1].split('|'))):
                    ls.append(tuple(list(i) + [j]))
            return ls
        else:
            num1 = [numbers[0]]
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                ls.append(tuple(num1 + list(i)))
            return ls

    @staticmethod
    def bet_11x5_751210(numbers: str):
        ls = []
        if numbers[0].find('|') != -1:
            for i in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                for j in set(list(numbers[1].split('|'))):
                    ls.append(tuple(list(i) + [j]))
            return ls
        else:
            num1 = [numbers[0]]
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                ls.append(tuple(num1 + list(i)))
            return ls

    @staticmethod
    def bet_11x5_751212(numbers: str):
        ls = []
        # [_clc.setdefault(i, num.count(i)) for i in num]
        # print('numbers[0]',set(list(numbers[0].split('|'))))
        # print('numbers[0]', set(list(numbers[1].split('|'))))
        # print('numbers[0]',numbers[0].count('|'))
        if numbers[0].count('|') == 2:
            for i in set(list(numbers[1].split('|'))):
                # print(i)
                # print(tuple(list(numbers[0].split('|')) + [i]))
                ls.append(tuple(list(numbers[0].split('|')) + [i]))
        elif numbers[0].count('|') == 1:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        else:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                # print(i)
                # print('numbers[0]', list(numbers[0].split('|'))+ list(i))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        return ls

    @staticmethod
    def bet_11x5_751213(numbers: str):
        ls = []
        # [_clc.setdefault(i, num.count(i)) for i in num]
        # print('numbers[0]',set(list(numbers[0].split('|'))))
        # print('numbers[0]', set(list(numbers[1].split('|'))))
        # print('numbers[0]',numbers[0].count('|'))
        if numbers[0].count('|') == 3:
            for i in set(list(numbers[1].split('|'))):
                # print(i)
                # print(tuple(list(numbers[0].split('|')) + [i]))
                ls.append(tuple(list(numbers[0].split('|')) + [i]))
        elif numbers[0].count('|') == 2:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 1:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        else:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                # print(i)
                # print('numbers[0]', list(numbers[0].split('|'))+ list(i))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        return ls

    @staticmethod
    def count_11x5_751214(numbers: str):
        ls = []
        if numbers[0].count('|') == 4:
            for i in set(list(numbers[1].split('|'))):
                # print(i)
                # print(tuple(list(numbers[0].split('|')) + [i]))
                ls.append(tuple(list(numbers[0].split('|')) + [i]))
        elif numbers[0].count('|') == 3:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                # print(i)
                # print(tuple(list(numbers[0].split('|')) + [i]))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 2:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 1:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        else:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print(i)
                # print('numbers[0]', list(numbers[0].split('|'))+ list(i))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        return ls

    @staticmethod
    def bet_11x5_751214(numbers: str):
        ls = []
        # [_clc.setdefault(i, num.count(i)) for i in num]
        # print('numbers[0]',set(list(numbers[0].split('|'))))
        # print('numbers[0]', set(list(numbers[1].split('|'))))
        # print('numbers[0]',numbers[0].count('|'))
        if numbers[0].count('|') == 4:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 1))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 4))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 3))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[0].split('|')), 5))):
                # print('i',i)
                ls.append(i)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
        elif numbers[0].count('|') == 3:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 1))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 4))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 3))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
                    # print(list(j) + [i])
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                # ls.append(tuple(list(numbers[0].split('|')) + list(i)))
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        elif numbers[0].count('|') == 2:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 3))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        elif numbers[0].count('|') == 1:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        else:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        return ls

    @staticmethod
    def count_11x5_751215(numbers: str):
        ls = []
        if numbers[0].count('|') == 5:
            for i in set(list(numbers[1].split('|'))):
                # print(i)
                # print(tuple(list(numbers[0].split('|')) + [i]))
                ls.append(tuple(list(numbers[0].split('|')) + [i]))
        elif numbers[0].count('|') == 4:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                # print(i)
                # print(tuple(list(numbers[0].split('|')) + [i]))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 3:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 2:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 1:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        else:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 6))):
                # print(i)
                # print('numbers[0]', list(numbers[0].split('|'))+ list(i))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        return ls

    @staticmethod
    def bet_11x5_751215(numbers: str):
        ls = []
        if numbers[0].count('|') == 5:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 1))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 4))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 3))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[0].split('|')), 5))):
                # print('i',i)
                ls.append(i)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        elif numbers[0].count('|') == 4:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 1))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 4))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 3))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[0].split('|')), 5))):
                # print('i',i)
                ls.append(i)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        elif numbers[0].count('|') == 3:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 1))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 4))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 3))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        elif numbers[0].count('|') == 2:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 3))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        elif numbers[0].count('|') == 1:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 2))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        else:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                for j in set(list(it.combinations(list(numbers[0].split('|')), 1))):
                    # print(i)
                    # print(j)
                    # print(i+j)
                    ls.append(i + j)
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('i',i)
                ls.append(i)
        return ls

    @staticmethod
    def count_11x5_751216(numbers: str):
        ls = []
        if numbers[0].count('|') == 6:
            for i in set(list(numbers[1].split('|'))):
                # print(i)
                # print(tuple(list(numbers[0].split('|')) + [i]))
                ls.append(tuple(list(numbers[0].split('|')) + [i]))
        elif numbers[0].count('|') == 5:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 2))):
                # print(i)
                # print(tuple(list(numbers[0].split('|')) + [i]))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 4:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 3))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 3:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 4))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 2:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 5))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        elif numbers[0].count('|') == 1:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 6))):
                # print('list1',list(i))
                # print(tuple(list(numbers[0].split('|')) + list(i)))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        else:
            for i in set(list(it.combinations(list(numbers[1].split('|')), 7))):
                # print(i)
                # print('numbers[0]', list(numbers[0].split('|'))+ list(i))
                ls.append(tuple(list(numbers[0].split('|')) + list(i)))
        return ls

    @staticmethod
    def bet_11x5_751214x16(numbers: List[tuple]):
        ls = []
        for parameter in numbers:
            print(parameter)
            # print(list(it.combinations(parameter, 5)))
            ls.extend(list(it.combinations(parameter, 5)))
        return ls

    @staticmethod
    def bet_11x5_711112(numbers: List[str]):
        ls = []
        num1 = [numbers[0]]
        for i in set(list(numbers[1].split('|'))):
            ls.append(tuple(num1 + [i]))
        return ls

    @staticmethod
    def bet_11x5_741010(numbers: str):
        ls, cs = ([] for _ in range(2))
        SPLIT_DETAIL = numbers.split(',')
        # print('SPLIT_DETAIL', SPLIT_DETAIL)
        for i in SPLIT_DETAIL:
            # print(i.split('|'))
            ls.append(i.split('|'))
        # print('ls', ls)
        _tlt, _clc = ({} for _ in range(2))
        cs = []
        dict_detail = [dict({idx: item}) for idx, item in enumerate(ls)]
        # print(dict_detail)
        for i in dict_detail:
            if list(i.values())[0] != ['#']:
                cs.append(i)
        return cs
# t = Tools()
# print(t.get_timestamp())
