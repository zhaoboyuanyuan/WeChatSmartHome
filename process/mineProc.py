# -*- coding: utf-8 -*-
#  creaded by 赵永健
from time import sleep

from process.commonProc import commonProc
from public.openWeb import openWeb

com=commonProc()
# o=openWeb()
# driver=o.getDr()
class mineProc(object):
    def baseProc(self, driver, list=[]):
        for i in list:
            self.switch(driver, i)

    def switch(self,driver,num):
        if num==0:
            driver.find_element_by_xpath("//*[@id='app']/div/section[3]/div/ul/li[4]").click()
        elif num==1:
            driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[1]").click()
        elif num==2:#网关列表点击
            driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[2]").click()
            sleep(3)
        elif num==3:
            js = "var q=document.documentElement.scrollTop=60000"
            driver.execute_script(js)
            sleep(3)
        elif num==4:
            driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[8]").click()
            driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[6]").click()
        elif num==5:#绑定用户点击
            driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[3]").click()
            sleep(3)
        elif num==6:
            a=driver.find_element_by_xpath("//*[@id='app']/div/section[1]/div/section[2]").text
            if a!=u"绑定用户":
                com.messageShow("未进入绑定用户页面！")
        elif num==7:#点击网关信息
            driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/section[4]").click()
        elif num==8:
            a=driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[1]/i[1]").text
            b=driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/ul/li[2]/i[1]").text
            print a,b
            if a!=u"产品名称" or b!=u"固件版本":
                com.messageShow("未显示网关信息！")




    # 1、网关列表
    def gateWayList(self,driver):
        self.baseProc(driver,[0,1,2,3,4,])

    # 2、绑定用户
    def bandCount(self,driver):
        self.baseProc(driver,[0,1,5,6])

    # 3、网关信息
    def gateWayMessage(self,driver):
        self.baseProc(driver,[0,1,7,8])








