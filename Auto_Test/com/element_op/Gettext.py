from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
import logging
import time


class GetText:
    check_element = Checkelement()

    def get_text(self, driver, locator, description):
        # locator须是tuple  (loc_type,locator)
        try:
            if self.check_element.wait_element(driver, 20, locator):
                return driver.find_element(locator).get_text()
            else:
                logging.error("未找到元素:" + description)
                return False

        except Exception as e:
            logging.error("获取元素" + description + "值" + "报错；" + str(e))
            return False
