# -*- coding: utf-8 -*-
#  creaded by 赵永健，场景页面测试

import unittest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from process.commonProc import commonProc
from public.openWeb import openWeb

o=openWeb()
com=commonProc()
class sceneTest(unittest.TestCase):
    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()
        com.login(self.driver)

    def tearDown(self):
        o.writeTearDown()

    # 1、场景显示
    def testSceneShow(self):
        u'''场景显示测试用例'''
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[2]/i").click()
        self.driver.refresh()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/div/ul/li[1]/span").click()
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//img[@class='run-gif']")))
        except:
            com.messageShow("场景未显示已执行")

    # 2、场景执行记录
    def testSceneRecord(self):
        u'''场景执行记录测试用例'''
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[2]/i").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/div/div/p[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section/div/div/input").click()
        self.driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section/div[2]/div/div/table/tbody/tr[1]/td[3]/span").click()
        a=self.driver.find_element_by_class_name("dataType").text
        print a
        if a!=u"2018-07-03":
            com.messageShow("未显示正确的执行时间")


if __name__ == '__main__':
    unittest.main





