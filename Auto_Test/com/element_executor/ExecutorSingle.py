from Auto_Test.com.element_process.Input import Input
from Auto_Test.com.element_process.Select import Select
from Auto_Test.com.element_process.RadioCheckBox import RadioCheckBox
from Auto_Test.com.element_op.Click import Click
from Auto_Test.com.element_op.DoubleClick import DoubleClick
from Auto_Test.com.element_process.Date import DateEntry
from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.util.ScreenShot import take_screen_shot
from Auto_Test.config.read_config import ConfigParser
from Auto_Test.com.util.GetDate import GetDate
from selenium.webdriver.common.by import By
from Auto_Test.com.element_process.RichText import RichText
from Auto_Test.com.util.Log import Log
import logging
import ast


class ExecutorSingleCase:
    input = Input()
    select = Select()
    radiocheck = RadioCheckBox()
    click = Click()
    doubleclick = DoubleClick()
    date = DateEntry()
    checkelement = Checkelement()
    getelement = GetElement()
    con = ConfigParser()
    get_date = GetDate()
    rich_text = RichText()

    def element_executor(self, driver, case_module, list_element, config_path,screen_path,log_path,log_info,log_error):  # access_token:

        executor = True
        list = iter(list_element)
        for element in list_element:
            element_dic = ast.literal_eval(element)
            element_name = element_dic['element_name']
            element_type = element_dic['type']
            loc_type = element_dic['loc_type']
            locator = element_dic['locator']
            print('本次操作的元素：%s,%s'%(element_name,locator))

            # 非校验的input,输入值
            if element_type == 'input':
                if 'input_val' not in element_dic.keys():
                    input_keys = ''
                elif self.con.get_config(config_path, case_module, element_dic['input_val']) == -1:
                    input_keys = element_dic['input_val']
                else:
                    input_keys = self.con.get_config(config_path, case_module, element_dic['input_val'])
                if not self.input.InputKeys(driver, element_dic, input_keys):
                    executor = False
                    take_screen_shot(driver, screen_path, element_name)
                    log_error.logger.error(element_name+ "：输入失败")

            #日期输入
            elif element_type == 'date':
                if not self.date.date_input(driver, element_dic):
                    log_error.logger.error(element_name + "：日期输入失败")
                    take_screen_shot(driver, screen_path, element_name)
                    executor=False

            # Button Link 执行点击操作
            elif element_type == 'button' or element_type == 'link':
                if not self.click.clickelement(driver, (eval(loc_type), locator), element_name):
                    log_error.logger.error(element_name + "：点击操作失败")
                    take_screen_shot(driver, screen_path, element_name)

            # 支持模糊查询的Select 执行下拉列表选择操作
            elif element_type == 'fuzzy_query_select':
                if not self.select.dropDownManage(driver, element_dic):
                    log_error.logger.error(element_name + "选择数据失败")
                    executor = False

            # 不带模糊查询的select， 执行下拉列表选择操作
            elif element_type == 'select':
                if not self.select.usual_select(driver, element_dic):
                    log_error.logger.error(element_name + "选择数据失败")
                    take_screen_shot(driver, screen_path, element_name)
                    executor = False

            # Checkbox、Radio，执行点击操作
            elif element_type == 'radio' or element_type == 'check_box':
                if not self.radiocheck.RadioCheckBoxClick(driver, element_dic):
                    log_error.logger.error(element_name + "点击操作失败")
                    executor = False

            # DoubleClick,进行双击操作
            elif element_type == 'double_click':
                if not self.doubleclick.check_element(driver, (eval(loc_type), locator), element_name):
                    log_error.logger.error(element_name + "点击操作失败")
                    executor = False

            # Scroll用于滚动至页面元素可见
            elif element_type == 'scroll':
                if not self.getelement.scrollToElement(driver, (eval(loc_type), locator)):
                    executor = False

            elif element_type == 'list_click': #在列表获取需要的元素，并点击操作
                #从配置中服务
                # li_num = int(self.con.get_config(config_path, case_module, element_dic['li_num']))
                if 'list_num' not in element_dic.keys():
                    li_num = '-1'
                else:
                    li_num = element_dic['list_num']
                loc = self.getelement.get_eleloc(driver,(eval(loc_type), locator),li_num)
                if loc:
                    self.click.clickelement(driver, (By.XPATH,loc), element_name)
                else:
                    log_error.logger.error(element_name + "获取列表元素失败")
                    take_screen_shot(driver, screen_path, element_name)

            elif element_type == 'list_check': #在列表获取需要的元素，并行校验
                print('进入list_check')
                #从配置中服务
                if 'list_num' not in element_dic.keys():
                    li_num = '-1'
                else:
                    li_num = element_dic['list_num']
                check_val = self.con.get_config(config_path, case_module, element_dic['check_val'])

                loc = self.getelement.get_eleloc(driver,(eval(loc_type), locator), li_num)
                print('loc-------：' + loc)
                if loc:
                    if not self.checkelement.WaitelementContainstext(driver, 20,(By.XPATH,loc),check_val):
                        log_error.logger.error(element_name + "没找到操作的元素")
                        take_screen_shot(driver, screen_path, element_name)
                else:
                    log_error.logger.error(element_name + "获取列表元素失败，校验失败")
                    take_screen_shot(driver, screen_path, element_name)

            # 判断元素是否为富文本
            elif element_type == 'rich_text':
                if not self.rich_text.input_content(driver,20,(eval(loc_type), locator)):
                    log_error.logger.error(element_name + "输入内容失败")
                    take_screen_shot(driver, screen_path, element_name)

            # 判断元素值是否为给定的值
            elif element_type == 'text_tobe':
                check_value = element_dic['text']
                if not self.checkelement.WaitelementtextToBe(driver,20,(eval(loc_type), locator),check_value):
                    take_screen_shot(driver, screen_path, element_name)
                    # self.log.WriteWronglog(driver, screen_path,"未找到值为："+check_value+"的元素")
                    executor= False

            # 判断元素值是不为给定的值
            elif element_type == 'text_notbe':
                check_text = element_dic['text']
                print(check_text)
                if not self.checkelement.WaitelementtextNotToBe(driver, 20, (eval(loc_type), locator), check_text):
                    log_error.logger.error(element_name + "元素一直存在")
                    take_screen_shot(driver, screen_path, element_name)
                    executor = False

            # 判断元素值是否包含给定的值
            elif element_type == 'contains_text':
                if not self.checkelement.WaitelementContainstext(driver, 60, element.getElemetlocator()):
                    pass
                    # self.log.WriteWronglog(driver, screen_path, element_name + "不包含值：")

            # 判断元素是否有值
            elif element_type == 'value_exist':
                if not self.checkelement.isvalue(driver, 20, element.getElemetlocator(), element.getelement_name()):
                    # self.log.WriteWronglog(driver, screen_path, element_name + "元素值不存在")
                    executor = False

            # 判断元素是否存在
            elif element_type == 'element_exist':
                if not self.checkelement.wait_element(driver, 20, (eval(loc_type), locator)):
                    # self.log.WriteWronglog(driver, screen_path, element_name + "元素不存在")
                    executor= False

            # 判断元素是否不存在
            elif element_type == 'element_noexist':
                a= self.checkelement.wait_noelement(driver, 20, (eval(loc_type), locator))
                print(a)
                if not a:
                    # self.log.WriteWronglog(driver, screen_path, element_name + "元素是存在的")
                    executor= False

            # 红绿框
            elif element_type == 'AlertContainer':
                if not self.getelement.Getalert(driver, element_name):
                    # self.log.WriteWronglog(driver, screen_path, "提交失败")
                    executor = False

            # 判断是否有系统弹窗，若存在全部关闭
            elif element_type == 'SystemAlert':
                self.checkelement.acceptallalert(driver)

            else:
                # 其他可能出现的操作
                print('其他类型')
                pass
            print('操作元素：%s,%s'%(element_name,locator)+'成功~~~~')

        # return executor
