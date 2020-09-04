

# 页面截图
def take_screen_shot(self, driver, filepath):

	try:
		driver.get_screenshot_as_file(filepath)
	except Exception as e:
		print(str(e))

