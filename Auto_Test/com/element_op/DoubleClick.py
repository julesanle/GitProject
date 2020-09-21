from selenium.webdriver import ActionChains

from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.element_process.Scroll import Scroll

import logging
import time


class DoubleClick:
    check_element = Checkelement()
    get_element = GetElement()
    scroll = Scroll()

    def click_element(self, driver, locator, description):
        # locator须是tuple  (loc_type,locator)
        all_handles = driver.window_handles
        # print(all_handles)
        if len(all_handles) > 1:
            driver.switch_to.window(all_handles[-1])  # 切换到新窗口
        try:
            if self.check_element.wait_element(driver, 60, locator):
                self.scroll.scrollToElement(driver, locator)
                time.sleep(1)
                ActionChains(driver).double_click(locator).perform()
                return True
            else:
                return False
                logging.error("没有加载元素：" + description)
        except Exception as e:
            return False
            logging.error("双击元素：" + description + "报错；" + str(e))
