package com.util;

import java.util.List;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class Mainmenu {
	   static Logger logger = LogManager.getLogger(Mainmenu.class);
	//进入菜单(需要确保可显示)
	public  Boolean enter(WebDriver driver,int first,int second,int thrid){
		Checkelement check=new Checkelement();
		if(first<0||second<0||thrid<0){//有值小于零
			logger.error("打开左侧菜单参数不符合要求");
			return false;
		}else{
		if(first==0){//第一个参数为0
			logger.warn("未对左侧菜单做任何改变");
			return true;
		}else{
		if(second==0&&thrid!=0){//第二个参数为0,且第三个参数不为0
			logger.error("打开左侧菜单参数不符合要求");
			return false;
		}else{//检查所有表格状态
			check.Waitelement(driver, 10, By.xpath("//*[@id='mainMenu']/li[3]"));
		    int num=first*2-1;
		    if(num>18){
				logger.error("没有这个一级菜单");
				return false;
			}
		    for(int i=0;i<9;i++){	
				int a=i*2+1;
				if(a!=first){//如果不是要操作的菜单
					//关闭一级菜单
					CloseLeftmenu(driver,By.xpath("//*[@id='mainMenu']/li["+a+"]"));
				}
			}
			//打开一级菜单
			 OpenLeftmenu(driver,By.xpath("//*[@id='mainMenu']/li["+num+"]"));
				if(second==0){
					return true;
				}else{//打开两级菜单
					WebElement secondtable = driver.findElement(By.xpath("//*[@id='mainMenu']/li["+num+"]/ul"));  
					List<WebElement> secondrows = secondtable.findElements(By.cssSelector("[data-level='1']"));
				    if(second>secondrows.size()){
				    	logger.error("没有这个二级菜单");
				    	return false;
				    }
				    for(int i=1;i<=secondrows.size();i++){
					   if(i!=second){
						   CloseLeftmenu(driver,By.xpath("//*[@id='mainMenu']/li["+num+"]/ul/li["+i+"]"));   
					   }
				   }
				OpenLeftmenu(driver,By.xpath("//*[@id='mainMenu']/li["+num+"]/ul/li["+second+"]"));
			   if(thrid==0){
				return true;
				}else{
					WebElement thridtable =driver.findElement(By.xpath("//*[@id='mainMenu']/li["+num+"]/ul/li["+second+"]/ul"));	
				    List<WebElement> thridrows=thridtable.findElements(By.cssSelector("[data-level='2']"));
				    if(thrid>thridrows.size()){
				    	logger.error("没有这个三级菜单");
				    	return false;
				    }
				    for(int i=0;i<thridrows.size();i++){
						   if(i!=thrid){
							   int a=i+1;
							   CloseLeftmenu(driver,By.xpath("//*[@id='mainMenu']/li["+num+"]/ul/li["+second+"]/ul/li["+a+"]"));   
						   }
					   }
				   OpenLeftmenu(driver,By.xpath("//*[@id='mainMenu']/li["+num+"]/ul/li["+second+"]/ul/li["+thrid+"]"));
				return true;
				}          
			   }
	}

		}}}
//打开左侧菜单
	private void OpenLeftmenu(WebDriver driver,By locator){
		Checkelement check=new Checkelement();
		check.Waitelement(driver, 10, locator);
		if(isopen(driver,locator)){//判断是否已经打开
		}else{
			scrollToLeftmenu(driver, locator);
			clickelement(driver, locator,"左侧主菜单");
		}
	}
	
	
//关闭左侧菜单
	private  void CloseLeftmenu(WebDriver driver,By locator){
		Checkelement check=new Checkelement();
		check.Waitelement(driver, 10, locator);
		if(isopen(driver,locator)){//判断是已经打开
			scrollToLeftmenu(driver, locator);
			clickelement(driver, locator,"左侧主菜单");
		}else{
			
		}
	}
	
//判断左侧菜单是否打开	
	private  boolean isopen(WebDriver driver,By locator){
	 String statue=driver.findElement(locator).getAttribute("class");
		if(statue.contains("open")){//判断是否已经打开
		return true; 	
		}else{
		return false;
		}
		}
	
	private void clickelement(WebDriver driver,By locator,String Description){
		Checkelement checkelement=new Checkelement();
		WaitTime waittime=new WaitTime();
		try{if(checkelement.Waitelement(driver, 20, locator)){
			waittime.sleepNumSeconds(1);
			driver.findElement(locator).click();
		}else{
			logger.error("没有加载元素："+Description);
		}}catch(Exception e){
			logger.error("点击元素"+Description+"报错；"+e.toString());
		}
	}
	
	private void scrollToLeftmenu(WebDriver driver, By locator) {
		WebElement e = driver.findElement(locator);
		JavascriptExecutor js = (JavascriptExecutor) driver;
		// roll down and keep the element to the center of browser
		js.executeScript("arguments[0].scrollIntoView(true);", e);
		js.executeScript("$('.main').scrollTop(100);");
	}
	 
	}
