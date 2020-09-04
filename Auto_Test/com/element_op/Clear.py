from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
import logging
import time


class Clear:

	checkelement = Checkelement()
	getelement = GetElement()

	# locator须是tuple  (loc_type,locator)
	def clearelement(self,driver,locator,description):
		try:
			if self.checkelement.wait_element(driver,20,locator):
				self.getelement.scrollToElement(driver, locator)
				time.sleep(1)
				driver.find_element(locator).clear()
				return True
			else:
				return False
			 	logging.error("未找到元素:"+description)

		except Exception as e:
			return False
			logging.error("清除元素"+description+"值报错；"+str(e))

