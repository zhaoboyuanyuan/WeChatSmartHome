#coding=utf-8
import sys, re, os, math

sys.path.append("D:/code/WeChatSmartHome/testcase")

import unittest, doctest, site
import HTMLTestRunner

# 将用例组建成数组
alltestnames = [
    'loginTest.loginTest',
    'homePageTest.homePageTest',
    'houseKeeperTest.houseKeeperTest',
    'messageTest.messageTest',
    'mineTest.mineTest',
    'sceneTest.sceneTest'
    # 'sutie.test_youdao.Youdao',
    # 'sutie.sogou.test_sogou.Sogou',  # 注意这个用例是二级目录下的
]
suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite())
if __name__ == '__main__':
    # 这里我们可以使用 defaultTestLoader.loadTestsFromNames(),
    # 但如果不提供一个良好的错误消息时，它无法加载测试
    # 所以我们加载所有单独的测试，这样将会提高脚本错误的确定。
    for test in alltestnames:
        try:
    # 最关键的就是这一句，循环执行数据数的里的用例。
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print ('ERROR: Skipping tests from "%s".' % test)
            try:
                __import__(test)
            except ImportError:
                print ('Could not import the test module.')
            else:
                print ('Could not load the test suite.')
            from traceback import print_exc
            print_exc()

    print ('Running the tests...')
    filename = 'D:\\code\\WeChatSmartHome\\result\\result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'微信版web智能家居测试报告',
        description=u'用例执行情况')
    runner.run(suite)
