from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
from Auto_Test.com.element_op import Click

import logging
import time

class Input:
	click = Click()
	check_element = Checkelement()
	get_element = GetElement()

	def InputKeysProcess(self, driver,element):
		if self.check_element.Waitelement(driver, 10, element.getElemetlocator()):
			try:
				self.get_element.scrollToElement(driver, element.getElemetlocator())
				time.sleep(1)
				pageElement=driver.findElement(element.getElemetlocator())
				# 文件上传，直接赋值：地址值
				if pageElement.getAttribute("type").equals("file"):
					pageElement.sendKeys(element.getvalue())
				# 日期选择
				else:
					# driver_js.executeScript("arguments[0].value='"+element.getvalue()+"'",driver.findElement(element.getElemetlocator()));
					if element.get_elementName().contains("日期"):
						  time.sleep(1)
						  # Actions(driver).sendKeys(Keys.ENTER).perform()
					else:
						  # 触发输入框校验
						self.click.clickelement(driver,element.getElemetlocator(),element.get_elementName())
			     return True
			 # except Exception as e:
				# logging.error("复选框:" + element.get_elementName() + "不可被操作")

	def InputProcess(self,driver,element):
		inputCheck=False
		time1=0
		# 点击此输入框返回值
		self.click.clickelement(driver,element.getElemetlocator(),element.get_elementName())
		time.sleep(1)
		# 校验是否有值
		elementExist=self.check_element.isvalue(driver,20,element.getElemetlocator(),element.get_elementName());
		if elementExist:
			inputCheck=True

		else:
			while time1<30:
				time1+=1
				if self.check_element.isvalue(driver,20,element.getElemetlocator(),element.get_elementName()):
					inputCheck=True
					break

		return inputCheck

	
	def InputCheck(self, driver,element):
		return self.InputProcess(driver,element)

	def InputKeys(self, driver,element):
		return self.InputKeysProcess(driver,element)
