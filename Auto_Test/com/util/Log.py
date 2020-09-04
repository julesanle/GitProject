import  logging


class Log:

	def WriteWronglog(self, driver,screenPath, description):

		logging.error(description)
		self.screenshot(driver, screenPath+description+".png")