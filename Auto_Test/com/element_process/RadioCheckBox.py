import logging

from Auto_Test.com.util import Checkelement
from Auto_Test.com.util import GetElement
from Auto_Test.com.element_op import Click


class RadioCheckBox:
    click = Click()
    check_element = Checkelement()
    get_element = GetElement()

    def RadioCheckBoxProcess(self, driver, element):
        try:
            self.check_element.Waitelement(driver, 20, element.getElemetlocator())
            self.get_element.scrollToElement(driver, element.getElemetlocator())
            elementprocess = driver.findElement(element.getElemetlocator())
            if elementprocess.isEnabled():
                if not elementprocess.isSelected():
                    # 勾选复选框
                    self.click.clickelement(driver, element.getElemetlocator(), element.get_elementName())
                    if not elementprocess.isSelected():
                        if element.gettype().equals("Checkbox"):
                            logging.error("复选框:" + element.get_elementName() + "点击后未被选中")

                    else:
                        logging.error("单选按钮:" + element.get_elementName() + "点击后未被选中")


            elif element.gettype().equals("Checkbox"):
                logging.error("复选框:" + element.get_elementName() + "不可被操作")
            else:
                logging.error("单选按钮:" + element.get_elementName() + "不可被操作")

        except Exception as e:
            logging.error("点击元素" + element.get_elementName() + "报错：" + str(e))

    def RadioCheckBoxClick(self, driver, element):
        self.RadioCheckBoxProcess(driver, element)
