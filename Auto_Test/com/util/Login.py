import time
from selenium.webdriver.common.by import By
# from Auto_Test.com.element_op import Click
from Auto_Test.config.read_config import ConfigParser
from Auto_Test.com.util.Checkelement import *
import logging
from selenium.webdriver.common.action_chains import ActionChains


class Login:

	check_element = Checkelement()
	# click = Click()
	con = ConfigParser()
	locator_user = ''
	locator_pawd = ''
	locator_login = ''

	def login(self,driver,config_path,log_info,log_error):
		# 此处对应的ini文件中[登录] 节点的数据，用例中 模块也须对应
		try:
			visit_url = self.con.get_config(config_path, 'Initial', 'url')
			user =  self.con.get_config(config_path, '登录', 'login_user')
			psw = self.con.get_config(config_path, '登录', 'login_pwd')
			if '3ren.cn' in visit_url: #三人行登录页
				locator_user = "/html/body/section/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input[1]"
				locator_pawd = '/html/body/section/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input[2]'
				locator_login = '/html/body/section/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/a'
				locator_uname = '/html/body/section/div[2]/div[1]/header/section/div[2]/div[3]/div/div/div[1]/div/a/span'
			else: #其他系统
				pass
			if self.check_element.wait_element(driver, 20,(By.XPATH,locator_user)):
				driver.find_element(By.XPATH,locator_user).send_keys(user)
				time.sleep(0.5)
				driver.find_element(By.XPATH,locator_pawd).send_keys(psw)
				time.sleep(0.5)
				driver.find_element(By.XPATH,locator_login).click()
				if self.check_element.wait_element(driver,20,(By.XPATH,locator_uname)):
					log_info.logger.info('登录成功，已进入首页')
					time.sleep(0.5)
					return True
			return False
		except Exception as e:
			# test screenshot
			log_error.logger.error('登录失败'+'\n'+str(e))
			return False

	# 退出
	def Logout(self,driver):
		actions = ActionChains(driver)
		time.sleep(0.5)
		element = driver.find_element(By.XPATH,'/html/body/section/div[2]/div[1]/header/section/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div[3]/a/img')
		actions.move_to_element(element)
		time.sleep(0.5)
		element.click()
