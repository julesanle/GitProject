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
			if self.checkelement.wait_element(driver,60,locator):
				self.getelement.scrollToElement(driver, locator)
				time.sleep(1)
				driver.find_element(locator).clear()
				return True
			else:
				logging.error("未找到元素:" + description)
				return False


		except Exception as e:
			logging.error("清除元素" + description + "值报错；" + str(e))
			return False


