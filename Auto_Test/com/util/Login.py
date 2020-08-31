import time
from selenium.webdriver.common.by import By
# from Auto_Test.com.element_op import Click
from Auto_Test.config.read_config import ConfigParser
from Auto_Test.com.util.Checkelement import *
import logging

class Login:

	check_element = Checkelement()
	# click = Click()
	con = ConfigParser()

	def login(self,driver,config_path):
		user =  self.con.get_config(config_path, 'LoginElement', 'login_user')
		psw = self.con.get_config(config_path, 'LoginElement', 'login_pwd')
		if self.check_element.wait_element(driver, 20,
			(By.XPATH,"/html/body/section/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input[1]")):
			driver.find_element(By.XPATH,
				'/html/body/section/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input[1]').send_keys(user)
			time.sleep(1)
			driver.find_element(By.XPATH,
				'/html/body/section/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input[2]').send_keys(
				psw)
			time.sleep(1)
			driver.find_element(By.XPATH,
				'/html/body/section/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/a').click()
			# self.click.clickelement(driver,By.XPATH(
			# 	'/html/body/section/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/a'))
			if self.check_element.wait_element(driver,20,(By.XPATH,'/html/body/section/div[2]/div[1]/header/section/div[2]/div[3]/div/div/div[1]/div/a/span')):
				print('登录成功，已进入首页')
				return True
		return False

	# 退出
	# def Logout(self,driver):
	# 	js = ''
	# 	# 左侧拉到最顶层使退出可见
	# 	js.executeScript("$('.main').scrollTop(0);")
	# 	self.click.clickelement(driver, By.ID("logout"),"退出按钮")
	# 	return self.check_element.Waitelement(driver,10,By.ID("login_id"))

