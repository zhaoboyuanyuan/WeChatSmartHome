# coding=utf-8
import unittest
from time import sleep

from selenium.webdriver.common.by import By

from process.commonProc import commonProc
from process.loginProc import loginProc
from public.openWeb import openWeb
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

o = openWeb()
com = commonProc()
lp=loginProc()


class loginTest(unittest.TestCase):
    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()


    def tearDown(self):
        o.writeTearDown()

    # 1、登录成功
    def testLoginSuccess(self):
        u"""登录成功测试用例"""
        lp.loginSuccess(self.driver)


    #2、 账号未注册
    def testWrongUser(self):
        u"""账号未注册测试用例"""
        lp.wrongUser(self.driver)

    #3、 密码错误
    def testWrongpass(self):
        u"""密码错误测试用例"""
        lp.wrongpass(self.driver)

    # 4、账号为空
    def testNoneUser(self):
        u"""账号为空测试用例"""
        lp.noneUser(self.driver)


    # 5、密码为空
    def testNonePass(self):
        u"""密码为空测试用例"""
        lp.nonePass(self.driver)


    # 6、验证码登录成功
    def testVeCodeLogin(self):
        u"""验证码登录成功测试用例"""
        lp.veCodeLogin(self.driver)


    #7、 账号未注册，条件苛刻，账号未注册，验证码还要对的
    def testAVeNoneUser(self):
        u"""手机验证码失效测试用例"""
        lp.AVeNoneUser(self.driver)


    # 8、验证码错误
    def testAVeCodeWrong(self):
        u"""手机验证码错误测试用例"""
        lp.AVeCodeWrong(self.driver)


if __name__ == '__main__':
    unittest.main
