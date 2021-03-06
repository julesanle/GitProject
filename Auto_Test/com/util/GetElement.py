from Auto_Test.com.util.Checkelement import Checkelement
from selenium.webdriver.common.by import By
import time
import logging

class GetElement:
	checkelement = Checkelement()
	def acceptAlert(self, driver, num):
		i = 1
		while i < num :
			try:
				alert = driver.switchTo().alert()
				alert.accept()
				return True
			except Exception as e:
				time.sleep(1)
				continue
			finally:
				i += 1
		if i == num:
			logging.error("加载系统弹框超时")
		return False


	# 等待获取弹框内容(绿色弹框返回true,红色弹框或未取到返回false)
	def Getalert(self, driver, Writenotice):
		# 获取弹框
		self.checkelement.Waitelement(driver, 60, (By.xpath,"//*[@class='alert-container']/div/div"))
		a = self.driver.find_element_by_xpath("//*[@class='alert-container']/div").getattr('class')
		alerttext = self.driver.findElement_by_xpath("//*[@class='alert-container']/div/div").getText()
		if (a.contains("info")):
			logging.info(Writenotice + alerttext)
			return True
		else:
			logging.error(Writenotice + alerttext)
			return False

	# 等待获取弹框内容(红色且包含指定内容返回true)
	def GetRedAlert(self, driver, Writenotice):
		# 获取弹框
		self.checkelement.Waitelement(driver, 20, (By.xpath,"//*[@class='alert-container']/div/div"))
		a = driver.findElement(By.xpath,"//*[@class='alert-container']/div").getAttribute("class")
		alerttext = driver.findElement(By.xpath,"//*[@class='alert-container']/div/div").getText()
		if a.contains("danger"):
			if alerttext.contains(Writenotice):
				logging.info(alerttext)
				return True
			else:
				logging.error(alerttext)
				return False

		else:
			logging.error(alerttext)
			return False


	# 等待获取弹框内容(绿色弹框且不包含指定内容返回true,红色弹框或未取到返回false)
	def GetalertContext(self, driver,  Writenotice):
		 # 获取弹框
		self.checkelement.Waitelement(driver, 20, By.xpath("//*[@class='alert-container']/div/div"))
		a = driver.findElement(By.xpath("//*[@class='alert-container']/div")).getAttribute("class")
		alerttext = driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText()
		if a.contains("info"):
			if alerttext.contains(Writenotice):
				return False
			logging.info(alerttext)
			return True
		else:
			logging.error(alerttext)
			return False


	# /获取弹框内容(绿色弹框和红色框返回false,未取到返回true)
	def getAlert(self, driver,  Writenotice):
		try:
			# /获取弹框
			self.checkelement.Waitelement(driver, 20, By.xpath("//*[@class='alert-container']/div/div"))
			a = driver.findElement(By.xpath("//*[@class='alert-container']/div")).getAttribute("class")
		except Exception as e:
			return True
		alerttext = driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText()
		if a.contains("info") | a.contains("danger"):
			logging.error(Writenotice + alerttext)
			return False
		else:
			logging.info(Writenotice + alerttext)
			return True

	# 获取弹框内容(红色框返回false,绿色弹框和未取到返回true)
	def getRedAlert(self, driver,  Writenotice) :
		try:
			# /获取弹框
			self.checkelement.Waitelement(driver, 60, By.xpath("//*[@class='alert-container']/div/div"))
			a = driver.findElement(By.xpath("//*[@class='alert-container']/div")).getAttribute("class")
		except Exception as e:
			return True

		alerttext = driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText()
		if a.contains("danger"):
			logging.error(Writenotice + alerttext)
			return False
		else:
			logging.info(Writenotice + alerttext)
			return True


	def scrollToElement(self, driver, locator):
		all_handles = driver.window_handles
		# print(all_handles)
		if len(all_handles) > 1:
			driver.switch_to.window(all_handles[-1])  # 切换到新窗口
		try:
			ele = driver.find_element(locator[0],locator[1])
			js = "arguments[0].scrollIntoView();"
			driver.execute_script(js,ele)
			time.sleep(0.5)
			return True
		except Exception as e:
			logging.error(str(e))
			return False

	def get_eleloc(self,driver,locator,i):
		try:
			ul = driver.find_element(locator[0],locator[1])
			li = ul.find_elements_by_xpath('li')

			if i == '-1':
				loc=locator[1]+'/li['+str(len(li))+']'
			else:
				loc = locator[1]+'/li['+i+']'
			return loc
		except Exception as e:
			logging.error(str(e))
			return None

