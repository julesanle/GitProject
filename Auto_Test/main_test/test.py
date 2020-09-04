from Auto_Test.com.driver.driver import Driver
from Auto_Test.com.util.Login import *
from Auto_Test.com.element_executor.ExecutorCase import ExecutorCase
from Auto_Test.com.util import Create_Report
import unittest


class MyTest(unittest.TestCase):
    driver = Driver()
    login = Login()
    case = ExecutorCase()
    config_path = 'E:\\default.ini'

    # 初始化driver
    driver = driver.driver_initial(config_path)

    def test1(self):
        #登录
        flag=self.login.login(self.driver, self.config_path)
        self.assertTrue(flag)
        self.driver.quit()

    def test2(self):
        flag = False
        self.assertTrue(flag)

    def test3(self):
        #读用例 执行
        print(type(By.XPATH))
        flag = self.case.read_excel(self.driver,self.config_path)
        self.assertTrue(flag)
        self.driver.quit()

if __name__ == '__main__':
     mytest = MyTest()
     mytest.test3()
    # Create_Report.create_report(MyTest('test3'))
    # Create_Report.create_report(MyTest)