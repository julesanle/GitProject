import logging

from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.element_op.Click import Click


class RadioCheckBox:
    click = Click()
    check_element = Checkelement()
    get_element = GetElement()

    def RadioCheckBoxProcess(self, driver, element):
        element_name = element['element_name']
        element_type = element['type']
        loc_type = element['loc_type']
        locator = element['locator']
        try:
            self.check_element.wait_element(driver, 20, (eval(loc_type),locator))
            self.get_element.scrollToElement(driver, (eval(loc_type), locator))
            elementprocess = driver.find_element((eval(loc_type), locator))
            if elementprocess.isEnabled():
                if not elementprocess.isSelected():
                    # 勾选复选框
                    self.click.clickelement(driver, (eval(loc_type), locator), element_name)
                    if elementprocess.isSelected():
                        return True
                    elif element_type == "check_box":
                        logging.error("复选框:" + element_name + "点击后未被选中")
                    else:
                        logging.error("单选按钮:" + element_name+ "点击后未被选中")

            elif element_type == "check_box":
                logging.error("复选框:" + element_name + "不可被操作")
            else:
                logging.error("单选按钮:" + element_name + "不可被操作")
            return False
        except Exception as e:
            return False
            logging.error("点击元素" + element_name+ "报错：" + str(e))

    def RadioCheckBoxClick(self, driver, element):
        return self.RadioCheckBoxProcess(driver, element)
