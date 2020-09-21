from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.element_op.Click import Click
from selenium.webdriver.common.by import By
import time
import logging

class RichText:
    check_ele = Checkelement()
    get_element = GetElement()
    click = Click()

    def input_content(self,driver,wtime,locator):
        loc_type = locator[0]
        locator_ = locator[1].split('|')
        locator_frame = locator_[0]
        locator_content = locator_[1]
        all_handles = driver.window_handles
        # print(all_handles)
        if len(all_handles) > 1:
            driver.switch_to.window(all_handles[-1])  # 切换到新窗口
        content = '''
            This is a test content!

            This is a test content!

            This is a test content!
        '''
        try:
            if self.check_ele.wait_element(driver,60,(loc_type,locator_frame)):
                iframe = driver.find_element(loc_type,locator_frame)
                driver.switch_to.frame(iframe)
                time.sleep(0.5)
                driver.find_element(loc_type,locator_content).send_keys(content)
                return True
            else:
                logging.error('没找到frame\n')
                return False
        except Exception as e:
            logging.error(str(e))
            return False
