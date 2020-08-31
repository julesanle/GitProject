import logging
import time
from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
from Auto_Test.com.element_op import Click


class Select:

	def NormalSelectProcess(self, driver, element):
		# 点击按钮
		self.click.clickelement(driver,element.getElemetlocator(),element.getElementName())
		# 等待下拉列表数据加载
		if self.checkelement.Waitelement(driver,10,element.getElemetlocator2()):
			time.sleep(1)
			# new Actions(driver).sendKeys(element.getvalue()).perform()
			time.sleep(1)
			# new Actions(driver).sendKeys(Keys.ENTER).perform()
			return True
		else:
			logging.error(element.getElementName()+"：下拉列表未加载")
			return False
		

	def SelectProcess(self, driver, element):
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

	def unusualDropDownManage(self, driver, element):
		return self.SelectProcess(driver,element)
