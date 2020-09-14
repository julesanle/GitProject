import logging

from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.element_op.Click import Click
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class RadioCheckBox:
    click = Click()
    check_element = Checkelement()
    get_element = GetElement()

    def RadioCheckBoxProcess(self, driver, element):
        element_name = element['element_name']
        element_type = element['type']
        loc_type = element['loc_type']
        locator = element['locator']
        all_handles = driver.window_handles
        # print(all_handles)
        if len(all_handles) > 1:
            driver.switch_to.window(all_handles[-1])  # 切换到最新窗口操作
        try:
            self.check_element.wait_element(driver, 20, (eval(loc_type),locator))
            self.get_element.scrollToElement(driver, (eval(loc_type), locator))
            element_process = driver.find_element(eval(loc_type), locator)
            if not element_process.is_selected():
                # 勾选复选框
                time.sleep(1)
                self.click.clickelement(driver, (eval(loc_type), locator), element_name)
                return True
                #..........后续添加校验...........
                # if element_process.is_selected():
                #     return True
                # elif element_type == "check_box":
                #     logging.error("复选框:" + element_name + "点击后未被选中")
                # else:
                #     logging.error("单选按钮:" + element_name + "点击后未被选中")
            return False
        except Exception as e:
            logging.error("点击元素" + element_name + "报错：" + str(e))
            return False


    def RadioCheckBoxClick(self, driver, element):
        return self.RadioCheckBoxProcess(driver, element)
