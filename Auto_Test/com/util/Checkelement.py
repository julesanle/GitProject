import  logging
import  time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkelement:

    # 等待元素加载完成
    def wait_element(self,driver,time,locator):
        try:
            WebDriverWait(driver,time).until(EC.presence_of_element_located((locator)))
            return True
            # logger.info("加载完成");
        except Exception as e:
            logging.error("未加载成功"+str(e))
            return False

    # 等待元素不可见
    def WaitelementInvisib(self,driver,time, locator):
        try:
            self.wait_element(driver,time,locator)
            WebDriverWait(driver,time).until(EC.presence_of_element_located(locator))
            # logger.info("元素已消失");
            return True
        except Exception as e:
            logging.error("元素在页面仍可见"+str(e))
                # Filemethod.writefile("[error]"+locator.toString()+"元素在页面仍可见"+e.toString(), out);
            return False

    # 等待元素包含特定值
    def WaitelementContainstext(self,driver,time,locator,text):
        try:
            wait_time=0
            self.wait_element(driver, time, locator)
            while(wait_time<time):
                time.sleep(1)
                elementtext=driver.findElement(locator).getText()
                if elementtext.contains(text):
                    return True
            return False
        except Exception as e:
            logging.error(str(e))
            logging.warn("元素值不包含："+text)
            return False

    # 等待元素不为定值
    def WaitelementtextNotToBe(self,driver,time,locator,text):
        try:
             self.wait_element(driver, time, locator)
             a = driver.findElement(locator).getText()
             for i in range(0, time):
                 if (a.equals(text)):
                     time.sleep(1)
                 else:
                     return True
                 logging.error("等待元素不包含" + text + "超时");
                 time += 1
                 return False
        except Exception as e:
            logging.error(e.toString())
            return False

    # 等待元素与特定值相同
    def WaitelementtextToBe(self,driver,time,locator,text):
        try:
            self.wait_element(driver,time,locator);
            WebDriverWait(driver,time).until(EC.textToBe(locator, text))
            return True
            # logger.info("校验成功");
        except Exception as e:
            logging.error("元素值不为："+text)
            logging.error(str(e))
            return False

    # 检查元素是否刷新
    def waitEleRefresh(self,trigger):
        is_refresh =False
        try:
            for i in range(1,20):
                trigger.getTagName()
                i += 1
                time.sleep(1)
        except StaleElementReferenceException as e:
            is_refresh = True
        return is_refresh


     # 检查元素是否有值
    def isvalue(self,driver,time,locator,notice):
        try:
            wait_time=0
            self.wait_element(driver,time,locator)
            while(wait_time<time):
                time.sleep(1)
                premium=driver.findElement(locator).getAttribute("value")
                if premium.equals!="":
                    logging.info(notice+"校验成功")
                    return True

            logging.error(notice+"未显示")
            return False

        except Exception as e:
            logging.error(str(e))
            return False

    # 等待元素属性值是否为特定值
    def isAttributeValue(self,driver,time,locator,AttributeValue):
        try:
            wait_time = 0
            self.wait_element(driver, time, locator)
            while (wait_time < time):
                wait_time+=1
            time.sleep(1)
            if (driver.findElement(locator).getAttribute("value").equals(AttributeValue)):
                return True
            value = driver.findElement(locator).getAttribute("value")
            logging.error("属性值不为：" + AttributeValue, "属性值为：" + value)
            return False

        except Exception as e:
            logging.error(str(e))
            return False

    # # 检查系统弹框是否存在
    # def isAlertPresent(self):
    # 	pass
    #
    # def acceptallalert(self,driver):
    #     while (self.isAlertPresent(driver)):
    #         driver.switchTo().alert().accept()
    #         time.sleep(1)
