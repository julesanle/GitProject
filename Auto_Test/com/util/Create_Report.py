import unittest
import time
import HTMLTestRunner


def create_report(testcase):
    file_name = 'E:\\Report.html'
    testsuite = unittest.TestSuite()
    testsuite.addTest(testcase)
    # testsuite = unittest.makeSuite(testcase)
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='AutoTestResult', description='Test_Report')
    runner.run(testsuite)
    fp.close()
