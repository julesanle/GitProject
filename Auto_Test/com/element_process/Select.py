import logging
import time
from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.element_op.Click import Click


class Select:

	def select_process(self, driver,loctor,name):
		# 点击按钮
		self.click.clickelement(driver,loctor,name)
		# 等待下拉列表数据加载
		if self.checkelement.wait_element(driver,10,loctor):
			time.sleep(1)
			# new Actions(driver).sendKeys(element.getvalue()).perform()
			time.sleep(1)
			# new Actions(driver).sendKeys(Keys.ENTER).perform()
			return True
		else:
			logging.error(loctor+"：下拉列表未加载")
			return False
		

	def select2_process(self, driver, element):
		# 点击按钮
		self.click.clickelement(driver,element.getElemetlocator(),element.getElementName())
		# 等待下拉列表数据加载
		if self.checkelement.Waitelement(driver,10,element.getElemetlocator2()):
			time.sleep(1)
			self.click.clickelement(driver,element.getElemetlocator2(),element.getElementName())
			return True

		else:
			logging.error(element.getElementName()+"：下拉列表未加载")
			return False

	def dropDownManage(self, driver, element):
		return self.NormalSelectProcess(driver,element)

	def usual_select(self, driver, element):
		element_name = element['element_name']
		loc_type = element['loc_type']
		locator = element['locator']
		return self.select_process(driver,(eval(loc_type),locator),element_name)
