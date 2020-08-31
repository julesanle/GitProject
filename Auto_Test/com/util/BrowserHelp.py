import time
import logging
import os
import  sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserHelp:
	# 此方法用于打开多个窗口时，切换到新窗口,int为窗口序号，0为主窗口
	currentWindow = None
	def SwitchToNewWindow(self, driver,i, time):
		# 等待页面加载完毕
		try:
			time.sleep(1)
			currentWindow=driver.current_window_handle      #获取当前窗口句柄
			winHandles=driver.getWindowHandles() #获取所有窗口句柄
			driver.switch_to.window(winHandles[i])#切换到新窗口

		except Exception as e:
			logging.error(str(e))
			logging.error("新页面加载失败")

	# 此方法用于切回主窗口，currentWindow为主窗口的句柄
	def SwitchToDefaultWindow(self, driver):
		driver.switchTo().window(self.currentWindow)#切换到新窗口
	
	# 打开新的tab页
		def opennewtab(self, driver, url):
			   # JavascriptExecutor oJavaScriptExecutor = (JavascriptExecutor)driver
		       #  oJavaScriptExecutor.executeScript("window.open('"+url+"')");
			js="window.open(url)"
			driver.execute_script(js)

	# 判断当前打开的窗口数
		def WindowCount(self,driver,windownum):
			try:
				WebDriverWait(driver,30).until(
						  EC.numberOfWindowsToBe(windownum))
				return True
			except Exception as e:
				logging.error("新页面加载失败："+str(e));
				return False

