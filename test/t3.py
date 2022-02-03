# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @project : nac-ele
# # @Author  : Eagle
# # @Site    :
# # @File    : t3.py
# # @Time    : 2021/6/28 1:34
# # @Software: PyCharm
# from test_junkie.decorators import Suite, beforeTest, afterTest, test, beforeClass, afterClass
#
#
# @Suite()
# class ExampleTestSuite:
#     @beforeClass()
#     def before_class(self):
#         cs = {'88383': 6}
#         parameter = ''.join(cs.keys())
#         print([str(','.join(parameter))] )
#         print(list(cs.values())[0])
#         print(type(list(cs.values())[0]))
#
#     # @beforeTest()
#     # def before_test(self):
#     #     print("Hi, I'm optional before test")
#     #
#     # @afterTest()
#     # def after_test(self):
#     #     print("Hi, I'm optional after test")
#     #
#     # @afterClass()
#     # def after_class(self):
#     #     print("Hi, I'm optional after class")
#     #
#     # @test()
#     # def something_to_test1(self):
#     #     print("Hi, I'm test #1")
#     #
#     # @test()
#     # def something_to_test2(self):
#     #     print("Hi, I'm test #2")
#     #
#     # @test()
#     # def something_to_test3(self):
#     #     print("Hi, I'm test #3")
#
#
# if "__main__" == __name__:
#     from test_junkie.runner import Runner
#
#     runner = Runner([ExampleTestSuite])
#     runner.run()
