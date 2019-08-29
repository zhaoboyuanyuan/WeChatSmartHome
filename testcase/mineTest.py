# -*- coding: utf-8 -*-
#  creaded by 赵永健
import unittest

from process.commonProc import commonProc
from process.mineProc import mineProc
from public.openWeb import openWeb

o=openWeb()
com=commonProc()
min=mineProc()
class mineTest(unittest.TestCase):

    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()
        com.login(self.driver)

    def tearDown(self):
        o.writeTearDown()

    # 1、网关列表
    def testGatewayList(self):
        u'''网关列表测试用例'''
        min.gateWayList(self.driver)

    # 2、绑定用户
    def testBandCount(self):
        u'''绑定用户测试用例'''
        min.bandCount(self.driver)

    # 3、网关信息
    def testGateWayMessage(self):
        u'''网关信息测试用例'''
        min.gateWayMessage(self.driver)



if __name__ == '__main__':
    unittest.main

