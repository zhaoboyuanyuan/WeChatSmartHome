# -*- coding: utf-8 -*-
#  creaded by 赵永健
#  登录页面流程


from model.loginModel import loginModel
from process.commonProc import commonProc
from public import data
from public import excel

com=commonProc()
lg=loginModel()
class loginProc(object):

    def baseProc(self, driver, list=[]):
        for i in list:
            self.switch(driver, i)

    def switch(self, driver, num):
        if num == 0: #输入用户名
            # driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/input").send_keys(lg.userName)
            driver.find_element_by_xpath(excel.xpathCon("userName")).send_keys(lg.userName)
        elif num==1: #输入密码
            driver.find_element_by_xpath(excel.xpathCon("password")).send_keys(lg.password)
        elif num==2: #点击登录
            driver.find_element_by_xpath(excel.xpathCon("loginButton")).click()
        elif num==3: #登录是否成功
            if com.loginedORNot(driver) == False:
                com.messageShow("登录失败！")
        elif num==4:
            if com.findToast(driver, lg.message) == False:
                com.messageShow("未弹出"+lg.message+"!")
        elif num==5:
            if com.loginButtonDecide(driver) == False:
                com.messageShow("登录按钮未禁用")
        #验证码登录
        elif num==6:
            driver.find_element_by_class_name(excel.classNameCon("vecodeLogin")).click()
        elif num==7:
            driver.find_element_by_xpath(excel.xpathCon("VCUserName")).send_keys(lg.userName)
        elif num==8:
            driver.find_element_by_xpath(excel.xpathCon("vecode")).send_keys(lg.vecode)




    def loginSuccess(self,driver):
        lg.userName="15951644332"
        lg.password="123456abcd"
        self.baseProc(driver,[0,1,2,3])

        # 2、 账号未注册
    def wrongUser(self,driver):
        lg.userName="15951644333"
        lg.password="123456"
        lg.message="用户不存在"
        self.baseProc(driver,[0,1,2,4])

    # 3、 密码错误
    def wrongpass(self,driver):
        lg.userName = "15951644332"
        lg.password = "12356"
        lg.message = "用户密码错误"
        self.baseProc(driver, [0, 1, 2, 4])

        # 4、账号为空
    def noneUser(self,driver):
        lg.userName = ""
        lg.password = "12356"
        self.baseProc(driver,[0,1,5])

    # 5、密码为空
    def nonePass(self,driver):
        lg.userName = "15951644332"
        lg.password = ""
        self.baseProc(driver, [0, 1, 5])


    # 6、验证码登录成功
    def veCodeLogin(self,driver):
        lg.userName="15951644332"
        lg.vecode="123456"
        self.baseProc(driver,[6,7,8,2,3])

#7、 账号未注册，条件苛刻，账号未注册，验证码还要对的
    def AVeNoneUser(self,driver):
        lg.userName="13851693871"
        lg.vecode="123456"
        lg.message="手机验证码失效"
        self.baseProc(driver,[6,7,8,2,4])

# 8、验证码错误
    def AVeCodeWrong(self,driver):
        lg.userName = "15951644332"
        lg.vecode = "123455"
        lg.message = "手机验证码错误"
        self.baseProc(driver, [6, 7, 8, 2, 4])







