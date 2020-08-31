from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
import logging
import time


class Click:

	checkelement = Checkelement()
	getelement = GetElement()

	def clickelement(self,driver,locator,Description):
		try:
			if(self.checkelement.Waitelement(driver, 20, locator)):
				self.getelement.scrollToElement(driver, locator)
				time.sleep(1)
				driver.findElement(locator).click()
				time.sleep(1)

			else:
				logging.error("没有加载元素："+Description)

		except Exception as e:
			logging.error("点击元素"+Description+"报错；"+str(e))

