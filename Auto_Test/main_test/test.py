from selenium import webdriver
from Auto_Test.com.driver.driver import Driver
from Auto_Test.com.util import Create_Report
from Auto_Test.com.util.Login import *
import time
import unittest


class MyTest(unittest.TestCase):
    driver = Driver()
    login = Login()
    config_path = 'E:\\default.ini'
    def test1(self):
        # 初始化driver，登录
        driver = self.driver.driver_initial(self.config_path)
        self.login.login(driver, self.config_path)
        time.sleep(5)
        driver.quit()
    def test2(self):
        pass
if __name__ == '__main__':
    # mytest = MyTest()
    # mytest.test1()
    Create_Report.create_report(MyTest('test1'))