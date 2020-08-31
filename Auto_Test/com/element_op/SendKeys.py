from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
import logging
import time


class SendKeys:

	check_element = Checkelement()
	get_element = GetElement()

	def sendkeyelement(self, driver,locator,words,description):
		try:
			if self.check_element.Waitelement(driver, 20, locator):
				self.get_element.scrollToElement(driver, locator)
				time.sleep(1)
				driver.findElement(locator).sendKeys(words)
			else:
				logging.error("未找到元素:"+description)

		except Exception as e:
			logging.error("点击元素"+description+"报错；"+str(e))

