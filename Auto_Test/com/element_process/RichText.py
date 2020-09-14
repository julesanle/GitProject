from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.element_op.Click import Click
import time
import logging

class RichText:
    check_ele = Checkelement()
    get_element = GetElement()
    click = Click()

    def input_content(self,driver,locator):
        loc_type = locator[0]
        locator_ = locator[1].split(',')
        locator_frame = locator_[0]
        locator_content = locator[1]
        content = '''
            This is a test content!

            This is a test content!

            This is a test content!
        '''
        if self.check_ele.wait_element(driver,20,locator_frame):
            driver.switch_to.frame("locator_frame")
            time.sleep(0.5)
            driver.find_element(loc_type,locator_content).send_keys(content)
        else:
            logging.error('没找到frame')
