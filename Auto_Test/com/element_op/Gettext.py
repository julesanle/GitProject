from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
import logging
import time


class GetText:

	check_element = Checkelement()
	def getelementtext(self,driver,locator,description):
		try:
			if self.check_element.Waitelement(driver, 20, locator):
				return driver.findElement(locator).getText()
			else:
				logging.error("未找到元素:"+description)
				return None

		except Exception as e:
			logging.error("获取元素"+description+"值"+"报错；"+str(e))
			return None

