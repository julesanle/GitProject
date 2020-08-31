package com.util;

import java.util.List;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Underwritemethod {
	private Logger logger  = LogManager.getLogger( Underwritemethod. class );
	private WaitTime waittime=new WaitTime();
	private Checkelement checkelement=new Checkelement();
	private  GetElement getelement=new GetElement();
	//校验区间分布模块
	public void IntervalDistribution(WebDriver driver) {
		//等待饼图图出现	
		try{
			checkelement.Waitelement(driver,20,By.xpath("//*[@id='item0']/div[1]/div[1]/div[1]/canvas"));
			waittime.sleepNumSeconds(1);	
			driver.findElement(By.xpath("//*[@id='item0']/div[1]/div[1]/div[1]/canvas")).click();
			//action.moveToElement(canvas.perform();
			//等待饼图加载为100%
			checkelement.WaitelementContainstext(driver, 20, By.xpath("//*[@id='item0']/div[1]/div[1]/div[2]"), "100%");
			logger.info("饼图加载完成");		
		}
		catch(Exception e){
			logger.error("饼图未加载");
			driver.quit();
		}
		
		waittime.sleepNumSeconds(2);	
	}

	//检查概要信息
	public void Checkessinfo(WebDriver driver,String PaperNum){
		//投保单按钮校验
		driver.findElement(By.xpath("//*[@id='generalInfoForm']/div/div[2]/div/i[1]")).click();
		try{
		new WebDriverWait(driver,10).until(ExpectedConditions.textToBe(By.xpath("//*[@id='applInfoForm']/div/div[2]/div[1]/input"),PaperNum));
		}catch (Exception e){
		System.out.println("加载失败");	
		}
		driver.findElement(By.xpath("//*[@id='udwUwbps']/div[5]/div/ul/li[1]/a")).click();
		checkelement.isvalue(driver,10,By.id("sumPremium"), PaperNum+"总保费");
		checkelement.isvalue(driver,10,By.id("ipsnNum"), PaperNum+"投保人数");
		checkelement.isvalue(driver,10,By.id("majorSaleName"),  PaperNum+"销售员");
	    boolean tasknum=  checkelement.isvalue(driver,10,By.id("ipsnNum"),  PaperNum+"任务号");
	    if(tasknum){
	    	//点击按钮
	    }   
	}
	//投保人
	
	//下发生调通知书
	public void PolicyholderNotice(WebDriver driver){
		//生调
		//先获取浏览器竖向坐标：$(document).scrollTop()
		JavascriptExecutor driver_js= (JavascriptExecutor) driver;
		driver_js.executeScript("window.scrollTo(0,1279)");
		//点击tab“投保人”
		driver.findElement(By.xpath("//*[@id='underInformation']/div/div[1]/div[2]/div/ul/li[1]/a")).click();
		//点击后生调列表会刷新
		driver.findElement(By.xpath("//*[@id='tabpersonUwbps']/div/div[4]/ul/li[1]/a")).click();
		waittime.sleepNumSeconds(1);
		//判断生调列表为空时进行新增操作
		List<WebElement> element=driver.findElements(By.xpath("//*[@id='lifeUwbps']/tbody/tr/td[1]/input"));
		if(element.isEmpty()){
			driver.findElement(By.xpath("//*[@id='lifeSurveyId']/input")).click(); //新增
			//如果有报错，关掉错误提示，继续操作
			List<WebElement> alertcontainer=driver.findElements(By.xpath("/html/body/div[10]/div/div"));
			if(!alertcontainer.isEmpty()) {
				driver.findElement(By.xpath("/html/body/div[10]/div/button/span[1]")).click();
			}
			waittime.sleepNumSeconds(1);
			//选择生掉项目
			driver.findElement(By.id("L001")).click();
			driver.findElement(By.id("L008")).click();
			//填写生调重点		
			driver.findElement(By.id("lifeSurveyKeyPoint")).sendKeys("投保人与被保险人投保利益关系异常生调");
			//调查时限、调查类型、处理天数
			driver.findElement(By.xpath("//*[@id='lifeSurveyTime']/input[1]")).click();
			driver.findElement(By.xpath("//*[@id='surveyType']/input[3]")).click();
			driver.findElement(By.id("procDays")).clear();
			driver.findElement(By.id("procDays")).sendKeys("5");
			waittime.sleepNumSeconds(1);
			driver.findElement(By.id("submit")).click();
			checkelement.Waitelement(driver, 20, By.xpath("/html/body/div[9]/div/div"));
			waittime.sleepNumSeconds(1);
			getelement.Getalert(driver,"生调：");
			waittime.sleepNumSeconds(2);	
		}
		else{
			  logger.info("生调已经存在");
			waittime.sleepNumSeconds(1);
		}
	}

	//投保人补充资料
	public void SuppinfoNotice(WebDriver driver){
		driver.findElement(By.xpath("//*[@id='tabpersonUwbps']/div/div[4]/ul/li[2]/a")).click();
		waittime.sleepNumSeconds(1);
		//判断补充资料列表为空时进行新增操作
		List<WebElement> element=driver.findElements(By.xpath("//*[@id='informationUwbps']/tbody/tr/td[1]/input"));
		if(element.isEmpty()){
			driver.findElement(By.id("addInfo")).click();
			//若有报错，关掉报错提示
			List<WebElement> alertcontainer=driver.findElements(By.xpath("/html/body/div[10]/div/div"));
			if(!alertcontainer.isEmpty()) {
				driver.findElement(By.xpath("/html/body/div[10]/div/button/span[1]")).click();
			}
			waittime.sleepNumSeconds(1);
			checkelement.Waitelement(driver, 20, By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[1]/div/div[1]/label/input"));
			driver.findElement(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[1]/div/div[1]/label/input")).click();
			//健康类，选择第一个
			driver.findElement(By.id("health")).click();
			waittime.sleepNumSeconds(1);
			driver.findElement(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[2]/div/div[1]/label/input")).click();
			//其他类，选第一个
			driver.findElement(By.id("others")).click();
			waittime.sleepNumSeconds(1);
			driver.findElement(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[3]/div/div[1]/label/input")).click();
			driver.findElement(By.xpath("//*[@id='box2']/div[2]/div[2]/div[1]/label/input")).click();
			driver.findElement(By.xpath("//*[@id='addInfoForm']/div[2]/div/div[2]/textarea")).sendKeys("资料与通知书内容不符");
			waittime.sleepNumSeconds(1);
			driver.findElement(By.id("addSubmit")).click();
			checkelement.Waitelement(driver, 20, By.xpath("/html/body/div[9]/div/div"));
			waittime.sleepNumSeconds(1);
			String alertcontainer4=driver.findElement(By.xpath("/html/body/div[9]/div/div")).getText();
	    	logger.info("补充资料"+alertcontainer4);
			driver.findElement(By.xpath("/html/body/div[9]/div/button/span[1]")).click();
			waittime.sleepNumSeconds(1);
		}
		else{
			logger.warn("投保人补充资料已经存在");
			waittime.sleepNumSeconds(1);
		}
	}

	//查询所有被保人
	public void Addrecognizeeinfo(WebDriver driver){
		driver.findElement(By.xpath("//*[@id='underInformation']/div/div[1]/div[2]/div/ul/li[2]/a")).click();//点击被保人
		new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.id("btn_click")));
		driver.findElement(By.id("btn_click")).click();//点击查询按钮
		try{
			new WebDriverWait(driver,20).until( ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@id='beibaoTab']/tbody/tr[1]/td[13]/p/a[1]")));//等待查询结果出现
		    logger.info("查询被保人成功");
		}catch(Exception e){
			logger.error("加载被保人失败");
		}
	}
	
	//下发被保人体检通知书
	public void Addexamnotice(WebDriver driver){
		new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.id("1items")));
		driver.findElement(By.xpath("//*[@id='ipsnReason']/div[1]/input")).click();
		driver.findElement(By.id("1items")).click();//选择T1
		driver.findElement(By.id("1Or1items")).click();//取消物理体检
		driver.findElement(By.xpath("//*[@id='ipsnTime']/input[1]")).click();//选择紧急
		driver.findElement(By.id("treatmentHea")).clear();//
		driver.findElement(By.id("treatmentHea")).sendKeys("10");//选择处理天数
		driver.findElement(By.xpath("//*[@id='tabipsnUwbps']/div/div[1]/div/div/div[3]/button[1]")).click();//提交
		getelement.Getalert(driver,"");
		  
	}
	//下发被保人生调通知书
	public void AddInsurancepolicynotice(WebDriver driver,String PaperNum){
		driver.findElement(By.xpath("//*[@id='beibaoTab']/tbody/tr[1]/td[13]/p/a[2]")).click();//点击生调
		new WebDriverWait(driver,20).until(
				  ExpectedConditions.presenceOfElementLocated(By.id("ipsnL001")));
		driver.findElement(By.id("ipsnL001")).click();//选择前三个项目
		driver.findElement(By.id("ipsnL002")).click();
		driver.findElement(By.id("ipsnL003")).click();
		driver.findElement(By.xpath("//*[@id='InlifeInfoForm1']/div[3]/div/div[2]/div/div[1]/div[1]/input[2]")).click();//选择普通
		driver.findElement(By.xpath("//*[@id='InlifeInfoForm1']/div[3]/div/div[2]/div/div[1]/div[2]/input[1]")).click();//选择必掉件
		driver.findElement(By.id("procDaysIpsn")).clear();
		driver.findElement(By.id("procDaysIpsn")).sendKeys("10");//期限改为10天
		driver.findElement(By.id("btnSubmit")).click();//点击提交
		getelement.Getalert(driver,  PaperNum);
	}
	
	//下发被保人补充资料
	public void Addadditoninfonotice(WebDriver driver,String PaperNum){
		driver.findElement(By.xpath("//*[@id='beibaoTab']/tbody/tr[1]/td[13]/p/a[3]")).click();
		new WebDriverWait(driver,20).until(
				  ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[1]/div/div[1]/label/input")));
		driver.findElement(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[1]/div/div[1]/label/input")).click();//高保额财务问卷
		driver.findElement(By.id("health")).click();//进入健康类
		new WebDriverWait(driver,20).until(
				  ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[2]/div/div[1]/label/input")));
		driver.findElement(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[2]/div/div[13]/label/input")).click();//饮酒问卷
		driver.findElement(By.id("others")).click();//其他类
		new WebDriverWait(driver,20).until(
				  ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[3]/div/div[7]/label/input")));
		driver.findElement(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[3]/div/div[7]/label/input")).click();//个人告知
		driver.findElement(By.xpath("//*[@id='box2']/div[2]/div[2]/div[1]/label/input")).click();//资料与通知书内容不符
		driver.findElement(By.id("procDays")).clear();
		driver.findElement(By.id("procDays")).sendKeys("11");
		driver.findElement(By.id("ipsnIdadd")).click();
		getelement.Getalert(driver, PaperNum);
	}
	
	//下发通知书
    public void Send(WebDriver driver,String PaperNum,String out){
    	Actions action = new Actions(driver); 
    	new WebDriverWait(driver, 20).until( ExpectedConditions.presenceOfElementLocated(By.id("item0")));
	    waittime.sleepNumSeconds(1);
	    action.sendKeys(Keys.END).perform();
	    waittime.sleepNumSeconds(1);
		action.sendKeys(Keys.PAGE_UP).perform();
		waittime.sleepNumSeconds(1);
		driver.findElement(By.xpath("//*[@id='tabpersonUwbps']/div/div[4]/ul/li[2]/a")).click();//补充资料
		waittime.sleepNumSeconds(2);
		driver.findElement(By.id("addInfo")).click();//新增
	    new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[1]/div/div[1]/label"))	);
	    waittime.sleepNumSeconds(1);
		driver.findElement(By.xpath("//*[@id='box2']/div[1]/div[2]/div/div[1]/div/div[2]/label/input")).click();
		driver.findElement(By.id("addSubmit")).click();
	    new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@class='alert-container']"))	);
	    waittime.sleepNumSeconds(1);	
	    driver.findElement(By.xpath("//*[@class='alert-container']/div/button/span[1]")).click();
		waittime.sleepNumSeconds(1);
		action.sendKeys(Keys.PAGE_DOWN).perform();
		waittime.sleepNumSeconds(1);
		driver.findElement(By.id("optionData")).sendKeys("需要提交证明");
		driver.findElement(By.xpath("//*[@id='underInformation']/div/div[5]/button[1]")).click();//下发通知书
		new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@id='policyHolder']/tbody/tr/td[1]")));
		waittime.sleepNumSeconds(1);	
		driver.findElement(By.id("sendNot")).click();//下发
		new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@class='alert-container']"))	);
		waittime.sleepNumSeconds(1);	
		String res=driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
			driver.findElement(By.xpath("//*[@class='alert-container']/div/button/span[1]")).click();
	   logger.warn("'"+PaperNum+"':'"+res+"'");
		waittime.sleepNumSeconds(1);
    }
    
//回执
    public void  conclu(WebDriver driver,String PaperNum,String out){ 
    	new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.id("businessKey"))	);
    	waittime.sleepNumSeconds(1);	
    	driver.findElement(By.id("businessKey")).sendKeys(PaperNum);
		driver.findElement(By.id("queryButton")).click();
		new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@id='notice_receipt_table']/tbody/tr/td[2]/p/a[1]"))	);
		waittime.sleepNumSeconds(1);	
		driver.findElement(By.xpath("//*[@id='notice_receipt_table']/tbody/tr/td[2]/p/a[1]")).click();
		driver.findElement(By.id("receiptOpinionRemark")).sendKeys("资料合格");
		driver.findElement(By.id("comitButten")).click();
		new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@class='alert-container']"))	);
		waittime.sleepNumSeconds(1);	
		String res=driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
		driver.findElement(By.xpath("//*[@class='alert-container']/div/button/span[1]")).click();
		   logger.warn("'"+PaperNum+"':'"+res+"'");
		  waittime.sleepNumSeconds(1);
    }
    
//确认核保完成(审核)
    public void receipt(WebDriver driver,String PaperNum,String out){
    	Actions action = new Actions(driver);
    	waittime.sleepNumSeconds(1);	
		new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.id("item0")));
		waittime.sleepNumSeconds(1);	
		action.sendKeys(Keys.END).perform();
		waittime.sleepNumSeconds(1);	
		action.sendKeys(Keys.PAGE_UP).perform();
		waittime.sleepNumSeconds(1);	
		driver.findElement(By.xpath("//*[@id='insuredPersonal']/div/div[2]/button")).click();//全部标准体
		waittime.sleepNumSeconds(1);	
		driver.findElement(By.xpath("//*[@id='myModal']/div/div/div/button[1]")).click();//弹框确认
		new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@class='alert-container']")));
		waittime.sleepNumSeconds(1);	
		driver.findElement(By.xpath("//*[@class='alert-container']/div/button/span[1]")).click();
		waittime.sleepNumSeconds(1);	
		action.sendKeys(Keys.PAGE_DOWN).perform();
		waittime.sleepNumSeconds(1);	
		driver.findElement(By.xpath("//*[@id='underInformation']/div/div[5]/button[8]")).click();//核保完成
		waittime.sleepNumSeconds(1);
		driver.switchTo().alert().accept();  
	    new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@class='alert-container']")));
	    waittime.sleepNumSeconds(1);	
	    String res=driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
	    driver.findElement(By.xpath("//*[@class='alert-container']/div/button/span[1]")).click();
	    logger.warn("'"+PaperNum+"':'"+res+"'");
	    waittime.sleepNumSeconds(1);
    }
    
 //核保审核（非必须）
    public void exUnWrite(WebDriver driver,String PaperNum,String out){
    	Actions action = new Actions(driver);
    	new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("item0"))	);
    	waittime.sleepNumSeconds(1);	
    	action.sendKeys(Keys.END).perform();
		waittime.sleepNumSeconds(1);	
		action.sendKeys(Keys.PAGE_UP).perform();
		waittime.sleepNumSeconds(1);	
	    driver.findElement(By.xpath("//*[@id='insuredPersonal']/div/div[2]/button")).click();//全部标准体
		waittime.sleepNumSeconds(1);	
		driver.findElement(By.xpath("//*[@id='myModal']/div/div/div/button[1]")).click();//弹框确认
	    driver.findElement(By.xpath("//*[@id='underInformation']/div/div[5]/button[8]")).click();
	    driver.switchTo().alert().accept();  
	    new WebDriverWait(driver, 20).until( 
			     ExpectedConditions.presenceOfElementLocated(By.xpath("item0"))	);
	    waittime.sleepNumSeconds(1);	
	    String res1=driver.findElement(By.xpath("//*[@class='alert-container']/div/div")).getText();
	    driver.findElement(By.xpath("//*[@class='alert-container']/div/button/span[1]")).click();
	   
			logger.warn("'"+PaperNum+"':'"+res1+"'");
	    waittime.sleepNumSeconds(2);
    }
}
