import logging
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkelement:

    # 等待元素加载完成
    def wait_element(self,driver,time,locator):
        try:
            WebDriverWait(driver,time).until(EC.presence_of_element_located(locator))
            return True
            # logger.info("加载完成");
        except Exception as e:
            logging.error("未加载成功"+str(e))
            return False

    #等待的元素不存在
    def wait_noelement(self, driver, time, locator):
        try:
            WebDriverWait(driver, time).until(EC.NoSuchElementException)
            return True
        except Exception as e:
            logging.error("元素还存在" + str(e))
            return False
    # 等待元素不可见
    def WaitelementInvisib(self,driver,time, locator):
        try:
            self.wait_element(driver,time,locator)
            WebDriverWait(driver,time).until(EC.text_to_be_present_in_element)
            return True
        except Exception as e:
            logging.error("元素在页面仍可见"+str(e))
                # Filemethod.writefile("[error]"+locator.toString()+"元素在页面仍可见"+e.toString(), out);
            return False

    # 等待元素包含特定值
    def WaitelementContainstext(self,driver,wtime,locator,text):
        try:
            wait_time=0
            ele=driver.find_element(locator[0],locator[1])
            self.wait_element(driver, time, locator)
            while(wait_time<wtime):
                time.sleep(1)
                print('准备获取 text')
                elementtext=driver.find_element(locator[0],locator[1]).text
                print('已获取 text')
                print(text)
                print(elementtext)
                if text in elementtext:
                    return True
            return False
        except Exception as e:
            logging.error(str(e))
            return False

    # 等待元素不为定值
    def WaitelementtextNotToBe(self,driver,time,locator,text):
        try:
             b=self.wait_element(driver, time, locator)
             print(b)
             a = driver.find_element(locator).text
             print(a)
             for i in range(0, time):
                 if a== text:
                     time.sleep(1)
                 else:
                     return True
                 logging.error("等待元素不包含" + text + "超时")
                 time += 1
                 return False
        except Exception as e:
            logging.error(str(e))
            return False

    # 等待元素与特定值相同
    def WaitelementtextToBe(self,driver,time,locator,text):
        try:
            WebDriverWait(driver,time).until(EC.text_to_be_present_in_element(locator,text))
            return True
        except Exception as e:
            logging.error("元素值不为："+text+'\n'+str(e))
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
