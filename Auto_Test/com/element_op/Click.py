from selenium.webdriver import ActionChains

from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement

import logging
import time


class Click:

	checkelement = Checkelement()
	getelement = GetElement()

	def clickelement(self,driver,locator,Description):
		#locator须是tuple  (loc_type,locator)
		all_handles = driver.window_handles
		# print(all_handles)
		if len(all_handles) > 1:
			driver.switch_to.window(all_handles[-1])  # 切换到最新窗口操作
		try:
			if(self.checkelement.wait_element(driver, 20, locator)):
				ele = driver.find_element(locator[0],locator[1])
				self.getelement.scrollToElement(driver, locator)
				ele.click()
				time.sleep(1)
				return True
			else:
				logging.error("没有加载元素："+Description)
				return False

		except Exception as e:
			logging.error("点击元素"+Description+"报错；"+str(e))
			return False

