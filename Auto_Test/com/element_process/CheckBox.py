import logging
from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.element_op.Click import Click
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class CheckBox:
    click = Click()
    check_element = Checkelement()
    get_element = GetElement()

    def CheckBoxClick(self, driver, element):
        element_name = element['element_name']
        element_type = element['type']
        loc_type = element['loc_type']
        locator = element['locator']
        all_handles = driver.window_handles
        # print(all_handles)
        if self.click.clickelement(driver, (eval(loc_type), locator), element_name):
            element_process = driver.find_element(eval(loc_type), locator)
            # if not element_process.is_selected():
            # 勾选或取消勾选复选框
            # ..........后续添加校验...........
            # if element_process.is_selected():
            #     return True
            # elif element_type == "check_box":
            #     logging.error("复选框:" + element_name + "点击后未被选中")
            # else:
            #     logging.error("单选按钮:" + element_name + "点击后未被选中")
            return True

        else:
            return False