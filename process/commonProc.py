# coding=utf-8
from datetime import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class commonProc(object):

# 登录按钮判断能否点击
    def loginButtonDecide(self,driver):
        try:
            a=driver.find_element_by_xpath("//button[@style='background-image: none;']")
            print (a)
            return True
        except:
            return False

# 登录页toast捕捉
    def findToast(self,driver,message):
        sleep(2)
        ele = driver.find_element_by_class_name("weui-toast__content").text
        me=message.decode("utf-8")
        if ele == me:
            return True
        else:
            return False

# 登录成功首页判断
    def loginedORNot(self,driver):
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "area-class-cell-span")))
            return True
        except:
            return False

# 抛出错误信息
    def messageShow(self,message):
        raise NameError(message)

    def login(self,driver):
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/input").send_keys("15951644332")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/input").send_keys("123456abcd")
        driver.find_element_by_xpath("/html/body/div[1]/div/button").click()
        if self.loginedORNot(driver) == False:
            self.messageShow("登录失败！")

    #首页检查
    def homeCheck(self,driver):
        a = driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/div[2]/span[1]").text
        b = driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/div[3]/span[1]").text
        if a == u"全部分区" and b == u"全部类别":
            return True
        else:
            return False





