from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
import logging
import time


class SendKeys:

	check_element = Checkelement()
	get_element = GetElement()

	def send_keys(self, driver,locator,words,description):
		try:
			if self.check_element.wait_element(driver, 60, locator):
				self.get_element.scrollToElement(driver, locator)
				driver.find_element(locator[0],locator[1]).send_keys(words)
				return True
			else:
				return  False
				logging.error("未找到元素:"+description)

		except Exception as e:
			return False
			logging.error("点击元素"+description+"报错；"+str(e))

