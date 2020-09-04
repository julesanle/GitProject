from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
import logging
import time


class Click:

	checkelement = Checkelement()
	getelement = GetElement()

	def clickelement(self,driver,locator,Description):
		#locator须是tuple  (loc_type,locator)
		try:
			if(self.checkelement.wait_element(driver, 20, locator)):
				self.getelement.scrollToElement(driver, locator)
				time.sleep(1)
				driver.find_element(locator[0],locator[1]).click()
				return True
			else:
				return False
				logging.error("没有加载元素："+Description)

		except Exception as e:
			return False
			logging.error("点击元素"+Description+"报错；"+str(e))

