from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
import logging
import time


class Getattribute:

	def get_element_attribute(self,driver,locator,attribute,description):
		try:
			if self.checkelement.Waitelement(driver, 20, locator):
				time.sleep(1)
				return driver.findElement(locator).getAttribute(attribute)
			else:
				logging.error("未找到元素:"+description)
			return None
		except Exception as e:
			logging.error("获取元素"+description+"属性"+attribute+"报错；"+str(e))
			return None
