
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
import time


class BrowserDriverFactory:

	def get_webdriver(self,url):
		driver = webdriver.Chrome(executable_path=url)
		return driver

	def get_remotedriver(self,url):
		chrome_options = Options()
		chrome_options.add_argument('--headless') # 无界模式
		driver = Remote(command_executor=url,
						chrome_options=chrome_options,
						desired_capabilities={'platform': 'ANY',
											  'browserName': 'chrome',
											  'version': '',
											  'javascriptEnabled': True,
											  'marionette': False})
		return driver

	def open_chrome(self,driver,url):
		driver.maximize_window()
		driver.get(url)
