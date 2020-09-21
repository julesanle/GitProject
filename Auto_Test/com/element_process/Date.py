from Auto_Test.com.util.GetDate import GetDate
from selenium.webdriver.common.by import By
import time
import datetime

class DateEntry:
    get_date = GetDate()

    def date_input(self, driver, element):
        element_name = element['element_name']
        element_type = element['type']
        loc_type = element['loc_type']
        locator = element['locator']
        input_date = None
        all_handles = driver.window_handles
        # print(all_handles)
        if len(all_handles) > 1:
            driver.switch_to.window(all_handles[-1])  # 切换到新窗口
        try:
            page_element = driver.find_element(eval(loc_type),locator)
            js1 = "arguments[0].removeAttribute('readonly')"
            driver.execute_script(js1,page_element)
            if '开始' in element_name:
                input_date = self.get_date.start_datetime()
                print(element_name+'-----'+input_date)
            elif '结束' in element_name or '截止' in element_name:
                input_date =self.get_date.end_datetime()
            else:
                print('时间控件取名有误')
                return False
            js2 = "arguments[0].value='';"
            driver.execute_script(js2,page_element)
            page_element.send_keys(input_date)
            time.sleep(0.5)
            return True
        except Exception as e:
            print(str(e))
            return False

    def time_input(self, driver, element):
        element_name = element['element_name']
        element_type = element['type']
        loc_type = element['loc_type']
        locator = element['locator']
        input_date = None
        all_handles = driver.window_handles
        # print(all_handles)
        if len(all_handles) > 1:
            driver.switch_to.window(all_handles[-1])  # 切换到新窗口
        try:
            page_element = driver.find_element(eval(loc_type),locator)
            js1 = "arguments[0].removeAttribute('readonly')"
            driver.execute_script(js1,page_element)
            if '开始' in element_name:
                input_date = self.get_date.start_time()
                print(element_name+'-----'+input_date)
            elif '结束' in element_name or '截止' in element_name:
                input_date =self.get_date.end_time()
                print(element_name+'-----'+input_date)
            else:
                print('时间控件取名有误')
                return False
            js2 = "arguments[0].value='';"
            driver.execute_script(js2,page_element)
            page_element.send_keys(input_date)
            time.sleep(0.5)
            return True
        except Exception as e:
            print(str(e))
            return False