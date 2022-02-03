#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project : nac
# @Author  : Eagle
# @Site    :
# @File    : utils.py
# @Time    : 2021/5/8 16:36
# @Software: PyCharm

import pymysql
from dbutils.pooled_db import PooledDB
from pymysql.cursors import DictCursor
from comm.config import Config


class BaseMysqlPool(object):
    def __init__(self, host, port, user, password, db_name=None):
        self.db_host = host
        self.db_port = int(port)
        self.user = user
        self.password = str(password)
        self.db = db_name
        self.conn = None
        self.cursor = None


class MysqlPool(BaseMysqlPool):
    """
    MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现获取连接对象：conn = Mysql.getConn()
            释放连接对象;conn.close()或del conn
    """
    # 连接池对象
    __pool = None

    def __init__(self, conf_name=None):
        self.conf = Config().get_content(conf_name)
        super(MysqlPool, self).__init__(**self.conf)
        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        self._conn = self.__getConn()
        self._cursor = self._conn.cursor()

    def __getConn(self):
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        if MysqlPool.__pool is None:
            __pool: PooledDB = PooledDB(creator=pymysql,
                                        mincached=1,
                                        maxcached=20,
                                        host=self.db_host,
                                        port=self.db_port,
                                        user=self.user,
                                        passwd=self.password,
                                        db=self.db,
                                        use_unicode=True,
                                        charset="utf8",
                                        cursorclass=DictCursor)
        return __pool.connection()

    def get_all(self, sql, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def get_one(self, sql, param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return count, result

    def get_many(self, sql, num, param=None):
        """
        @summary: 执行查询，并取出num条结果
        @param sql:查询ＳＱＬ，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = False
        return result

    def insert_many(self, sql, values):
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的ＳＱＬ格式
        @param values:要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        count = self._cursor.executemany(sql, values)
        return count

    def __query(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        return count

    def update(self, sql, param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def insert(self, sql, param=None):
        """
        @summary: 更新数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def delete(self, sql, param=None):
        """
        @summary: 删除数据表记录
        @param sql: ＳＱＬ格式及条件，使用(%s,%s)
        @param param: 要删除的条件 值 tuple/list
        @return: count 受影响的行数
        """
        return self.__query(sql, param)

    def begin(self):
        """
        @summary: 开启事务
        """
        self._conn.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, is_end=1):
        """
        @summary: 释放连接池资源
        """
        if is_end == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()

    def nac_bet_detail_received_record_one(self, bet_id):

        sql = "select * from nac_bet_detail_received_record where bet_id = %s" % bet_id
        # bet_id = res[1].get('betId')
        bet = {"bet_id": bet_id}
        # print(sql)
        result = self.get_one(sql, bet)
        # print(result[0] == 1)
        return result

    def nac_theory_bonus(self, bet_type_code):
        # sql = "select * from nac_theory_bonus where bet_type_code = %s" % type_code
        sql = "select theory_bonus from nac_theory_bonus where bet_type_code = %(bet_type_code)s"
        code = {"bet_type_code": bet_type_code}
        result = self.get_one(sql, code)
        return result

    def insert_split_detail_ture(self, **kwargs):
        sql = 'insert into split_detail(split_lottery_code,split_type_code,split_bet_detail,split_api_result,split_test_result,split_status,submission_date) values (%s,%s,%s,%s,%s,%s,%s)'
        # bet_id = res[1].get('betId')
        bet = (kwargs.get('lot_code'), kwargs.get('bet_code'), kwargs.get('bet_detail'), kwargs.get('api_result'),
               kwargs.get('test_result'), kwargs.get('isTrue'), kwargs.get('datetime'))
        # print(sql)
        try:
            self.insert(sql, bet)
            self.end(option='commit')
        except Exception as e:
            self.end(option='rollback')
            print(e)
        else:
            self.end(option='commit')
        finally:
            self.dispose(is_end=1)

    def insert_split_detail(self, **kwargs):
        sql = 'insert into split_detail(split_lottery_code,split_type_code,bet_id,split_bet_detail,split_api_result,split_test_result,difference,split_status,submission_date,issue) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # bet_id = res[1].get('betId')
        bet = (kwargs.get('lot_code'), kwargs.get('bet_code'), kwargs.get('bet_id'), kwargs.get('bet_detail'),
               kwargs.get('api_result'),
               kwargs.get('test_result'), kwargs.get('difference'), kwargs.get('isTrue'), kwargs.get('datetime'),
               kwargs.get('issue'))
        # print(sql)
        try:
            self.insert(sql, bet)
            self.end(option='commit')
        except Exception as e:
            # self.end(option='rollback')
            print(e)
        # else:
        #     self.end(option='commit')
        # finally:
        #     self.dispose(isEnd=1)

    def update_profit(self, **kwargs):
        sql = 'UPDATE split_detail SET query_num=%s,api_profit_loss=%s,test_profit_loss=%s,is_profit_loss=%s where bet_id=%s'
        bet = (kwargs.get('query_num'), kwargs.get('api_profit_loss'), kwargs.get('test_profit_loss'),
               kwargs.get('is_profit_loss'), kwargs.get('bet_id'))
        try:
            self.update(sql, bet)
            self.end(option='commit')
        except Exception as e:
            # self.end(option='rollback')
            print(e)
        # else:
        #     self.end(option='commit')
        # finally:
        #     self.dispose(isEnd=1)
#
# if __name__ == '__main__':
#     _sql = MysqlPool("database")
# mysql = MysqlPool("splitbase")
# tool = Tools()
# api_result = ['66664', '44444', '44443']
# test_result = ['66664', '44444', '44443']
# _datetime = tool.get_time_now('%Y-%m-%d %H:%M:%S')
# code = '10_10_11'
# _sql.nac_theory_bonus(code)
# _sql.nac_bet_detail_received_record_one('202105153422295581265920')
# print(_sql.nac_bet_detail_received_record_one('202105193466284501307392'))
# print(1* _sql.nac_theory_bonus('10_10_11')[1].get('theory_bonus'))
# mysql.insert_split_detail_ture(lot_code='txffc', bet_code='16_12_15', bet_detail='万|千|百|十_1,2',
#                                api_result=[','.join(api_result)], test_result=[','.join(test_result)], isTrue=True,
#                                datetime=_datetime)
#     #
#     sqlAll = "select * from nac_bet_detail_received_record where bet_id = %(bet_id)s"
#     bet = {"bet_id": "202105153422295581265920"}

#     #
#     sqlAll = "select * from split_detail"
#     bet = {"bet_id": "202105153422295581265920"}
#     print(sqlAll)
#     result = mysql.get_one(sqlAll)
#     print(result)

# mysql.insert("insert into split_detail set split_lottery_code=%s", (1))
# sqlAll = "select * from nac_bet_detail_received_record;"
# result = mysql.getMany(sqlAll, 2)
# print(result)
#
# result = mysql.getOne(sqlAll)
# print(result)

# mysql.insert("insert into myTest.aa set a=%s", (1))

# 释放资源
#     mysql.dispose()
