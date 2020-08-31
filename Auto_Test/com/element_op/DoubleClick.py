from selenium.webdriver import ActionChains

from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
import logging
import time


class DoubleClick:

	check_element = Checkelement()
	get_element = GetElement()

	def click_element(self, driver,locator,description):
		try:
			if self.check_element.Waitelement(driver, 20, locator):
				self.check_element.scrollToElement(driver, locator)
				time.sleep(1)
				ActionChains(driver).double_click(locator).perform()
			else:
				logging.error("没有加载元素："+description)
		except Exception as e:
			logging.error("双击元素："+description+"报错；"+str(e))
