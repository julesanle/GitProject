from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
from Auto_Test.com.element_op import Click
import time


class Scroll:
	check_element = Checkelement()

	def scrollProcess(self, driver,element):
		if self.check_element.Waitelement(driver,20,element.getElemetlocator()):
			time.sleep(1)
			e = driver.findElement(element.getElemetlocator())
			# js = "document.getElementsByClassName('form-control')[0].value='%s';" % (requestCode[i][0].value)
			js="e.value='%s'"%("arguments[0].scrollIntoView(true)")
			 # roll down and keep the element to the center of browser
			driver.execute_script(js)
		time.sleep(1)
	def scrollToElement(self, driver, element):
		self.scrollProcess(driver,element)
