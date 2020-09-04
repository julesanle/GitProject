from Auto_Test.com.element_process.Input import Input
from Auto_Test.com.element_process.Select import Select
from Auto_Test.com.element_process.RadioCheckBox import RadioCheckBox
from Auto_Test.com.element_op.Click import Click
from Auto_Test.com.element_op.DoubleClick import DoubleClick
from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.util.Log import Log
from Auto_Test.config.read_config import ConfigParser
from selenium.webdriver.common.by import By

import logging
import os
from os.path import *
import ast


class ExecutorSingleCase:
    input = Input()
    select = Select()
    radiocheck = RadioCheckBox()
    click = Click()
    doubleclick = DoubleClick()
    checkelement = Checkelement()
    getelement = GetElement()
    con = ConfigParser()
    log = Log()

    def element_executor(self, driver, case_module, list_element, config_path):  # access_token:
        directory = "test-output"
        if not exists(directory):
            os.mkdir(directory)
        screenPath = dirname(abspath(__file__)) + "/img/"
        executor = True
        list = iter(list_element)
        for element in list_element:
            element_dic = ast.literal_eval(element)
            element_name = element_dic['element_name']
            element_type = element_dic['type']
            loc_type = element_dic['loc_type']
            locator = element_dic['locator']
            print('本次操作的元素：%s,%s'%(element_name,locator))
            # elementValue=element.getvalue()
            # status=element.getStatus()
            # 非校验的input,输入值
            if element_type == 'input':
                input_keys = self.con.get_config(config_path, case_module, element_dic['input_val'])
                if not self.input.InputKeys(driver, element_dic, input_keys):
                    executor = False
                    self.log.WriteWronglog(driver, screenPath, element_name + "：输入失败")

            # 校验input,点击该input校验是否有值,不影响流程-影响流程
            elif element_type == 'Inputcheck':
                if not self.input.InputCheck(driver, element_dic):
                    self.log.WriteWronglog(driver, screenPath, element_name + "无数据")
                    executor=False

            # Button Link 执行点击操作
            elif element_type == 'button' or element_type == 'link':
                executor= self.click.clickelement(driver, (eval(loc_type), locator), element_name)

            # 支持模糊查询的Select 执行下拉列表选择操作
            elif element_type == 'drop_down':
                if not self.select.dropDownManage(driver, element_dic):
                    self.log.WriteWronglog(driver, screenPath, element_name + "选择数据失败")
                    executor = False

            # 不带模糊查询的select， 执行下拉列表选择操作
            elif element_type == 'select':
                if not self.select.usual_select(driver, element_dic):
                    self.log.WriteWronglog(driver, screenPath, element_name + "选择数据失败")
                    executor = False

            # Checkbox、Radio，执行点击操作
            elif element_type == 'radio' or element_type == 'check_box':
                executor= self.radiocheck.RadioCheckBoxClick(driver, element_dic)

            # DoubleClick,进行双击操作
            elif element_type == 'double_click':
                executor= self.doubleclick.check_element(driver, (eval(loc_type), locator), element_name)

            # Scroll用于滚动至页面元素可见
            elif element_type == 'scroll':
                executor= self.getelement.scrollToElement(driver, (eval(loc_type), locator))

            # 判断元素值是否为给定的值
            # elif element_type.equals('text_tobe'):
            #     if not self.checkelement.WaitelementtextToBe(driver,60,element.getElemetlocator(),elementValue):
            #         self.log.WriteWronglog(driver, screenPath,"未找到值为："+elementValue+"的"+element_name)
            # if status.equals(Statustype.Effect):
            #     executor=False
            #     break

            # 判断元素值是否包含给定的值
            # elif element_type.equals('contains_text'):
            #     if not self.checkelement.WaitelementContainstext(driver,60,element.getElemetlocator(), elementValue):
            #         self.log.WriteWronglog(driver,screenPath,element_name+"不包含值："+elementValue)
            # if status.equals(Statustype.Effect):
            #     executor=false
            #     break

            # 判断元素是否有值
            elif element_type == 'value_exist':
                if not self.checkelement.isvalue(driver, 20, element.getElemetlocator(), element.getelement_name()):
                    self.log.WriteWronglog(driver, screenPath, element_name + "元素值不存在")
                    executor = False

            # 判断元素是否存在
            elif element_type == 'element_exist':
                if not self.checkelement.wait_element(driver, 20, (eval(loc_type), locator)):
                    self.log.WriteWronglog(driver, screenPath, element_name + "元素不存在")
                    executor= False

            # 红绿框
            elif element_type == 'AlertContainer':
                if not self.getelement.Getalert(driver, element_name):
                    self.log.WriteWronglog(driver, screenPath, "提交失败")
                    executor = False

            # 判断是否有系统弹窗，若存在全部关闭
            elif element_type == 'SystemAlert':
                self.checkelement.acceptallalert(driver)

            else:
                # 其他可能出现的操作
                print('其他类型')
                pass

        return executor
