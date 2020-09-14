import logging
import time
from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from selenium.webdriver.common.by import By
from Auto_Test.com.element_op.Click import Click


class Select:

	check_ele =  Checkelement()
	get_element = GetElement()
	click = Click()

	def usual_select(self, driver,element):
		name = element['element_name']
		loc_type = element['loc_type']
		locator = element['locator'].split(',')
		print(locator)
		try:
			# 点击按钮
			self.click.clickelement(driver, (eval(loc_type), locator[0]), name)
			# 等待下拉列表数据加载
			if self.check_ele.wait_element(driver, 10, (eval(loc_type), locator[1])):
				time.sleep(0.5)
				# 选择第一个点击
				loc = self.get_element.get_eleloc(driver, (eval(loc_type), locator[1]),'1')
				self.click.clickelement(driver, (By.XPATH, loc), name)
				return True
			else:
				logging.error(locator[1] + "：下拉列表未加载")
				return False
		except Exception as e:
			logging.error(str(e))
			return False

	def dropDownManage(self, driver, element):
		# 点击按钮
		self.click.clickelement(driver,element.getElemetlocator(),element.getElementName())
		# 等待下拉列表数据加载
		if self.check_ele.wait_element(driver,10,element.getElemetlocator2()):
			time.sleep(1)
			self.click.clickelement(driver,element.getElemetlocator2(),element.getElementName())
			return True

		else:
			logging.error(element.getElementName()+"：下拉列表未加载")
			return False



