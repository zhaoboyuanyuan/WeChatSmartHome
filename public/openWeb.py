# coding=utf-8

import unittest
from time import sleep

from selenium import webdriver


class openWeb():
    def writeSetUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://sharewx.wulian.cc/index.html#/login"
        self.verificationErrors =[]
        self.accept_next_alert = True
        self.driver.get(self.base_url)

    def writeTearDown(self):
        self.driver.quit()
        # assertEqual([], self.verificationErrors)

    def getDr(self):
        return self.driver


    def testLogin(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/input").send_keys("15951644332")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/input").send_keys("123456abcd")
        self.driver.find_element_by_xpath("/html/body/div[1]/div/button").click()
        print self.driver.title
        sleep(5)

# o=openWeb()
# o.writeSetUp()
# o.testLogin()
# o.writeTearDown()

