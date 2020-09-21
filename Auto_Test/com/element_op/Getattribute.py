from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
import logging
import time


class Getattribute:

	def get_element_attribute(self,driver,locator,attribute,description):
		# locator须是tuple  (loc_type,locator)

		try:
			if self.checkelement.wait_element(driver, 60, locator):
				time.sleep(1)
				return driver.find_element(locator).get_attribute(attribute)
			else:
				logging.error("未找到元素:"+description)
			return False
		except Exception as e:
			logging.error("获取元素"+description+"属性"+attribute+"报错；"+str(e))
			return False
