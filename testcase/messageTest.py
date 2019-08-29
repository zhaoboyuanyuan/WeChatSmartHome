# -*- coding: utf-8 -*-
#  creaded by 赵永健
import unittest
from time import sleep

from process.commonProc import commonProc
from public.openWeb import openWeb

o=openWeb()
com=commonProc()
class messageTest(unittest.TestCase):

    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()
        com.login(self.driver)

    def tearDown(self):
        o.writeTearDown()

    # 1、报警消息
    def testAlarm(self):
        u'''报警消息测试用例'''
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[3]").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[2]/ul/li[1]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section/div/div/input").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section/div[2]/div/div/table/tbody/tr[1]/td[4]/span").click()
        a = self.driver.find_element_by_class_name("dataType").text
        print a
        if a != u"2018-07-04":
            com.messageShow("未显示正确的执行时间")
        self.driver.find_element_by_class_name("leftbtn").click()

    # 2、日志
    def testLog(self):
        u'''日志测试用例'''
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[3]").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[1]/div/a[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[2]/ul/li[1]").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section/div/div/input").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section/div[2]/div/div/table/tbody/tr[1]/td[4]/span").click()
        a = self.driver.find_element_by_class_name("dataType").text
        print a
        if a != u"2018-07-04":
            com.messageShow("未显示正确的执行时间")
        self.driver.find_element_by_class_name("leftbtn").click()


