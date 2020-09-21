from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.element_op.Click import Click
from selenium.webdriver.common.by import By
from Auto_Test.com.element_op.SendKeys import SendKeys
from selenium.webdriver.common.action_chains import ActionChains

import logging
import time


class Input:
	click = Click()
	check_element = Checkelement()
	get_element = GetElement()
	send_keys = SendKeys()


	# element是个字典
	def InputKeys(self, driver,element,input_keys):
		element_name = element['element_name']
		element_type = element['type']
		loc_type = element['loc_type']
		locator = element['locator']
		wait_parameter = (eval(loc_type),locator)
		all_handles = driver.window_handles
		# print(all_handles)
		if len(all_handles)>1:
			driver.switch_to.window(all_handles[-1])  # 切换到新窗口
		if self.check_element.wait_element(driver, 60, wait_parameter):
			time.sleep(1)
			try:
				# self.click.clickelement(driver,wait_parameter,element_name)
				# 文件上传，直接赋值：地址值
				# Actions(driver).sendKeys(Keys.ENTER).perform()
				self.send_keys.send_keys(driver,wait_parameter,input_keys,element_name)
				js2 = "arguments[0].value="+ input_keys
				driver.execute_script(js2,driver.find_element(eval(loc_type),locator))
			except Exception as e:
				logging.error(str(e))
				logging.error("复选框:" + element_name + "不可被操作")
				return False
			return True
		else:
			print("找不到元素")
			return False

	def InputCheck(self,driver,element):
		input_check=False
		time1=0
		# 点击此输入框返回值
		self.click.clickelement(driver,element.getElemetlocator(),element.get_elementName())
		time.sleep(1)
		# 校验是否有值
		elementExist=self.check_element.isvalue(driver,60,element.getElemetlocator(),element.get_elementName());
		if elementExist:
			input_check=True

		else:
			while time1<30:
				time1+=1
				if self.check_element.isvalue(driver,60,element.getElemetlocator(),element.get_elementName()):
					input_check=True
					break
		return input_check