# -*- coding: utf-8 -*-
#  creaded by 赵永健,首页测试用例
import unittest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from process.commonProc import commonProc
from public.openWeb import openWeb

o = openWeb()
com = commonProc()
class homePageTest(unittest.TestCase):
    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()
        com.login(self.driver)

    def tearDown(self):
        o.writeTearDown()

    #首页显示
    def testShowHome(self):
        u"""首页显示测试用例"""
        if com.homeCheck(self.driver)==False:
            com.messageShow("首页检查失败！")


    #设备详情
    # @unittest.skip("设备刷新慢，暂时跳过该方法")
    def testDeviceDetail(self):
        u"""设备详情测试用例"""
        self.driver.refresh()
        sleep(5)
        self.driver.find_element_by_xpath("//img[@src='static/img/icon_normal.c2a12e0.png']").click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"controlBtn")))


    #搜索设备
    def testSearchDevice(self):
        u"""搜索设备测试用例"""
        self.driver.find_element_by_xpath("//input[@placeholder='搜索']").send_keys(u"红")
        a=self.driver.find_element_by_class_name("nameText").text
        if a!=u"红外入侵探测器001":
            com.messageShow("未找到红外")


if __name__ == '__main__':
    unittest.main
