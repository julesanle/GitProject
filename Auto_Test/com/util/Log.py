import  logging

class Log:
	private Logger logger = LogManager.getLogger(Log.class);
	private ScreenShot screenshot=new ScreenShot();
	public  void WriteWronglog(WebDriver driver,String screenPath,String description){
		logger.error(description)
		Reporter.log(description)
		screenshot.TakeScreenShot(driver, screenPath+description+".png")
	}
}
