

class GetElement:
	checkelement = Checkelement()
	def acceptAlert(WebDriver driver, int num):
		int i = 0
		while (i++ < num) {
			try {
				Alert alert = driver.switchTo().alert();
				alert.accept();
				return true;
			} catch (NoAlertPresentException e) {
				waittime.sleepNumSeconds(1);
				continue;
			}
		}
		if (i == num) {

			Reporter.log("加载系统弹框超时");
			return false;
		}
		return false;

	}

	//
	def isalertpre(self, driver):
		List<WebElement> ele = driver.findElements(By.xpath("//*[@class='alert-container']/div/div"));
		if (ele.size() > 0) {// 有弹框
			ele.clear();
			return true;
		} else {
			return false;// 无弹框
		}

	}

	// 等待获取弹框内容(绿色弹框返回true,红色弹框或未取到返回false)
	public Boolean Getalert(WebDriver driver, String Writenotice) {
		String alerttext = null;
		// 获取弹框
		checkelement.Waitelement(driver, 60, By.xpath("//*[@class='alert-container']/div/div"));
		String a = driver.findElement(By.xpath("//*[@class='alert-container']/div")).getAttribute("class");
		alerttext = driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
		if (a.contains("info")) {
			logger.info(Writenotice + alerttext);
			return true;
		} else {
			logger.error(Writenotice + alerttext);
			return false;
		}
	}
	// 等待获取弹框内容(红色且包含指定内容返回true)
	public Boolean GetRedAlert(WebDriver driver, String Writenotice) {
		String alerttext = null;
		// 获取弹框
		checkelement.Waitelement(driver, 20, By.xpath("//*[@class='alert-container']/div/div"));
		String a = driver.findElement(By.xpath("//*[@class='alert-container']/div")).getAttribute("class");
		alerttext = driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
		if (a.contains("danger")) {
			if(alerttext.contains(Writenotice)){
				logger.info(alerttext);
			return true;
			}else{
				logger.error(alerttext);
				return false;
			}			
		} else {
			logger.error(alerttext);
			return false;
		}
	}

	// 等待获取弹框内容(绿色弹框且不包含指定内容返回true,红色弹框或未取到返回false)
	public Boolean GetalertContext(WebDriver driver, String Writenotice) {
		String alerttext = null;
		// 获取弹框
		checkelement.Waitelement(driver, 20, By.xpath("//*[@class='alert-container']/div/div"));
		String a = driver.findElement(By.xpath("//*[@class='alert-container']/div")).getAttribute("class");
		alerttext = driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
		if (a.contains("info")) {
			if (alerttext.contains(Writenotice)) {
				return false;
			}
			logger.info(alerttext);
			return true;
		} else {
			logger.error(alerttext);
			return false;
		}
	}

	// 获取弹框内容(绿色弹框和红色框返回false,未取到返回true)
	public Boolean getAlert(WebDriver driver, String Writenotice) {
		String alerttext = null;
		String a;
		try {
			// 获取弹框
			checkelement.Waitelement(driver, 20, By.xpath("//*[@class='alert-container']/div/div"));
			a = driver.findElement(By.xpath("//*[@class='alert-container']/div")).getAttribute("class");
		} catch (Exception e) {
			return true;
		}
		alerttext = driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
		if (a.contains("info") || a.contains("danger")) {
			logger.error(Writenotice + alerttext);
			return false;
		} else {
			logger.info(Writenotice + alerttext);
			return true;
		}
	}

	// 获取弹框内容(红色框返回false,绿色弹框和未取到返回true)
	public Boolean getRedAlert(WebDriver driver, String Writenotice) {
		String alerttext = null;
		String a;
		try {
			// 获取弹框
			checkelement.Waitelement(driver, 60, By.xpath("//*[@class='alert-container']/div/div"));
			a = driver.findElement(By.xpath("//*[@class='alert-container']/div")).getAttribute("class");
		} catch (Exception e) {
			return true;
		}
		alerttext = driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
		if (a.contains("danger")) {
			logger.error(Writenotice + alerttext);
			return false;
		} else {
			logger.info(Writenotice + alerttext);
			return true;
		}
	}

	public void scrollToElement(WebDriver driver, By locator) {
		WebElement e = driver.findElement(locator);
		JavascriptExecutor js = (JavascriptExecutor) driver;
		// roll down and keep the element to the center of browser
		js.executeScript("arguments[0].scrollIntoView(true);", e);
		js.executeScript("window.scrollBy(0,-180)");
	}
	
	
}
