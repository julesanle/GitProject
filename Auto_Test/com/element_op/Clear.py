from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
import  logging
import  time


class Clear:

	checkelement = Checkelement()
	getelement = GetElement()

	def clearelement(self,driver,locator,description):
		try:
			if self.checkelement.Waitelement(driver, 20, locator):
				self.getelement.scrollToElement(driver, locator)
				time.sleep(1)
				driver.findElement(locator).clear()
			else:
			 logging.error("未找到元素:"+description)

		except Exception as e:
			logging.error("清除元素"+description+"值报错；"+str(e))

