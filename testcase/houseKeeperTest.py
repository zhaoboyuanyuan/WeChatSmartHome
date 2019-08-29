# -*- coding: utf-8 -*-
#  creaded by 赵永健,管家测试页面
import unittest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from process.commonProc import commonProc
from public.openWeb import openWeb

o=openWeb()
com=commonProc()
class houseKeeperTest(unittest.TestCase):
    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()
        com.login(self.driver)

    def tearDown(self):
        o.writeTearDown()

    # 1、定时任务开关控制
    def testTimedTask(self):
        u'''定时任务开关控制测试用例'''
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[4]").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[2]").click()
        a=self.driver.find_element_by_xpath("//*[@id='app']/div/section[1]/div/section[2]").text
        if a!=u"我的管家":
            com.messageShow("未进入我的管家页面！")
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[2]/div/div[2]/p/label").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[2]/p/ul/li[1]/div[2]/input").click()
        sleep(5)

    # 2、情景任务开关控制
    def testsceneTask(self):
        u'''情景任务开关控制测试用例'''
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[4]").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[2]").click()
        a=self.driver.find_element_by_xpath("//*[@id='app']/div/section[1]/div/section[2]").text
        if a!=u"我的管家":
            com.messageShow("未进入我的管家页面！")
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[3]/div/div[2]/p/label").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[3]/p/ul/li/div[2]/input").click()
        sleep(5)

    #3、版本信息
    def testVersion(self):
        u'''版本信息测试用例'''
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[4]").click()
        a=self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[3]/span").text
        if a!=u"V6.0.0":
            com.messageShow("版本不是V6.0.0！")

    #4、退出登录
    def testQuitLogin(self):
        u'''退出登录测试用例'''
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[4]").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[4]").click()
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"login-btn")))
        except:
            com.messageShow("退出登录失败！")

if __name__ == '__main__':
    unittest.main





