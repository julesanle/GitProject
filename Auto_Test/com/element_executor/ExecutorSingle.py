from Auto_Test.com.element_process.Input import Input
from Auto_Test.com.element_process.Select import Select
from Auto_Test.com.element_process.CheckBox import CheckBox
from Auto_Test.com.element_op.Click import Click
from Auto_Test.com.element_op.DoubleClick import DoubleClick
from Auto_Test.com.element_process.Date import DateEntry
from Auto_Test.com.util.Checkelement import Checkelement
from Auto_Test.com.util.GetElement import GetElement
from Auto_Test.com.util.ScreenShot import take_screen_shot
from Auto_Test.config.rw_config import ConfigParser
from Auto_Test.com.util.GetDate import GetDate
from selenium.webdriver.common.by import By
from Auto_Test.com.element_process.RichText import RichText
from Auto_Test.com.element_executor.Parameter import Parameter
from Auto_Test.config.rw_config import ConfigParser
from Auto_Test.com.util.Log import Log
import logging
import ast
import time


class ExecutorSingleCase:
    input = Input()
    select = Select()
    check_box = CheckBox()
    click = Click()
    doubleclick = DoubleClick()
    date = DateEntry()
    checkelement = Checkelement()
    getelement = GetElement()
    con = ConfigParser()
    get_date = GetDate()
    rich_text = RichText()
    par_exe = Parameter()
    con = ConfigParser()

    def element_executor(self, driver, case_module, list_element, config_path, screen_path, log_path, log_info,
                         log_error):  # access_token:
        executor = True
        for element in list_element:
            # 转换元素格式
            ele_str = element.replace('\n', '')
            str0 = "'" + ele_str[0]
            str1 = ele_str[len(ele_str) - 1] + "'"
            list_0 = str0
            for i in range(1, len(ele_str) - 1):
                str2 = ele_str[i]
                if ele_str[i] == ':' or ele_str[i] == ',':
                    str2 = "'" + ele_str[i]+"'"
                list_0 += str2
            list_element = '{' + list_0 + str1 + '}'
            element_dic = ast.literal_eval(list_element)
            element_name = element_dic['element_name']
            element_type = element_dic['type']
            loc_type = None
            locator = None
            try:
                loc_type = element_dic['loc_type']
                locator = element_dic['locator']
                print('本次操作的元素：%s,%s' % (element_name, locator))
            except Exception as e:
                logging.info('元素：'+element_name+'没有此属性')
            # 非校验的input,输入值
            if element_type == 'input':
                if 'input_val' not in element_dic.keys():
                    input_keys = ''
                elif self.con.get_config(config_path, case_module, element_dic['input_val']) == -1:
                    input_keys = element_dic['input_val']
                    #创建一些特殊数据名称后加了 时间戳
                    if 'timestap' in input_keys:
                        stime = str(int(time.time()))
                        input_keys = input_keys.replace('timestap',stime)
                        self.con.write_config(config_path, case_module, element_dic['input_val'], input_keys)
                else:
                    input_keys = self.con.get_config(config_path, case_module, element_dic['input_val'])
                    if 'timestap' in input_keys:
                        stime = str(int(time.time()))
                        input_keys = input_keys.replace('timestap', stime)
                        # 替换完参数要保存到地址去
                        self.con.write_config(config_path, case_module, element_dic['input_val'], input_keys)

                if not self.input.InputKeys(driver, element_dic, input_keys):
                    executor = False
                    take_screen_shot(driver, screen_path, element_name)
                    log_error.logger.error(element_name + "：输入失败")

            # 日期输入
            elif element_type == 'date':
                if not self.date.date_input(driver, element_dic):
                    executor = False
                    log_error.logger.error(element_name + "：日期输入失败")
                    take_screen_shot(driver, screen_path, element_name)


            # 日期输入
            elif element_type == 'time':
                if not self.date.time_input(driver, element_dic):
                    executor = False
                    log_error.logger.error(element_name + "：时间输入失败")
                    take_screen_shot(driver, screen_path, element_name)


            # Button Link 执行点击操作
            elif element_type == 'button' or element_type == 'link' or element_type == 'radio':
                if not self.click.clickelement(driver, (eval(loc_type), locator), element_name):
                    executor = False
                    log_error.logger.error(element_name + "：点击操作失败")
                    take_screen_shot(driver, screen_path, element_name)


            # 支持模糊查询的Select 执行下拉列表选择操作
            elif element_type == 'fuzzy_query_select':
                if not self.select.dropDownManage(driver, element_dic):
                    executor = False
                    log_error.logger.error(element_name + "选择数据失败")
                    take_screen_shot(driver, screen_path, element_name)


            # 不带模糊查询的select， 执行下拉列表选择操作
            elif element_type == 'select':
                if not self.select.usual_select(driver, element_dic):
                    executor = False
                    log_error.logger.error(element_name + "选择数据失败")
                    take_screen_shot(driver, screen_path, element_name)


            # Checkbox、Radio，执行点击操作
            elif element_type == 'check_box':
                if not self.check_box.CheckBoxClick(driver, element_dic):
                    executor = False
                    log_error.logger.error(element_name + "点击操作失败")
                    take_screen_shot(driver, screen_path, element_name)


            # DoubleClick,进行双击操作
            elif element_type == 'double_click':
                if not self.doubleclick.check_element(driver, (eval(loc_type), locator), element_name):
                    executor = False
                    log_error.logger.error(element_name + "点击操作失败")
                    take_screen_shot(driver, screen_path, element_name)


            # Scroll用于滚动至页面元素可见
            elif element_type == 'scroll':
                if not self.getelement.scrollToElement(driver, (eval(loc_type), locator)):
                    executor = False

            elif element_type == 'list_click':  # 在列表获取需要的元素，并点击操作
                # 从配置中服务
                # li_num = int(self.con.get_config(config_path, case_module, element_dic['li_num']))
                if 'list_num' not in element_dic.keys():
                    li_num = '-1'
                else:
                    li_num = element_dic['list_num']
                loc = self.getelement.get_eleloc(driver, (eval(loc_type), locator), li_num)
                if loc:
                    self.click.clickelement(driver, (By.XPATH, loc), element_name)
                else:
                    executor = False
                    log_error.logger.error(element_name + "获取列表元素失败")
                    take_screen_shot(driver, screen_path, element_name)

            elif element_type == 'list_check':  # 在列表获取需要的元素，并行校验
                # 从配置中服务
                if 'list_num' not in element_dic.keys():
                    li_num = '-1'
                else:
                    li_num = element_dic['list_num']
                check_val = self.con.get_config(config_path, case_module, element_dic['check_val'])
                loc = self.getelement.get_eleloc(driver, (eval(loc_type), locator), li_num)
                if loc is not None:
                    if not self.checkelement.contains_text(driver, 80, (By.XPATH, loc), check_val):
                        executor = False
                        log_error.logger.error(element_name + "没找到操作的元素")
                        take_screen_shot(driver, screen_path, element_name)
                else:
                    executor = False
                    log_error.logger.error(element_name + "获取列表元素失败，校验失败")
                    take_screen_shot(driver, screen_path, element_name)

            # 判断元素是否为富文本
            elif element_type == 'rich_text':
                if not self.rich_text.input_content(driver, 80, (eval(loc_type), locator)):
                    executor = False
                    log_error.logger.error(element_name + "输入内容失败")
                    take_screen_shot(driver, screen_path, element_name)
            # 直接进入一个页面
            elif element_type == 'open':
                url = self.con.get_config(config_path, case_module, element_dic['url'])
                if not self.par_exe.enter_page(driver,url):
                    executor = False
                    log_error.logger.error("进入页面失败:%s"%url)
                    take_screen_shot(driver, screen_path, element_name)

            # 判断元素值是否为给定的值
            elif element_type == 'text_tobe':
                check_value = element_dic['text']
                if not self.checkelement.WaitelementtextToBe(driver, 80, (eval(loc_type), locator), check_value):
                    executor = False
                    log_error.logger.error(element_name + "与给定值:%s不相同"%check_value)
                    take_screen_shot(driver, screen_path, element_name)
                    # self.log.WriteWronglog(driver, screen_path,"未找到值为："+check_value+"的元素")


            # 判断元素值是不为给定的值
            elif element_type == 'text_notbe':
                check_text = element_dic['text']
                print(check_text)
                if not self.checkelement.WaitelementtextNotToBe(driver, 60, (eval(loc_type), locator), check_text):
                    log_error.logger.error(element_name + "与给定值：%s相同了"%check_text)
                    take_screen_shot(driver, screen_path, element_name)
                    executor = False

            # 判断元素值是否包含给定的值
            elif element_type == 'contains_text':
                text = None
                if 'text' not in element_dic.keys():
                    text = ''
                elif self.con.get_config(config_path, case_module, element_dic['text']) == -1:
                    text = element_dic['text']
                else:
                    text = self.con.get_config(config_path, case_module, element_dic['text'])
                if not self.checkelement.contains_text(driver, 60,(eval(loc_type), locator),text):
                    executor = False
                    log_error.logger.error(element_name + "校验失败")
                    take_screen_shot(driver, screen_path, element_name)

            # 判断数据不包含给定值
            elif element_type == 'no_contains_text':
                text = None
                if 'text' not in element_dic.keys():
                    text = ''
                elif self.con.get_config(config_path, case_module, element_dic['text']) == -1:
                    text = element_dic['text']
                else:
                    text = self.con.get_config(config_path, case_module, element_dic['text'])

                if not self.checkelement.not_contains_text(driver, 30, (eval(loc_type), locator),text):
                    executor = False
                    log_error.logger.error(element_name + "校验失败")
                    take_screen_shot(driver, screen_path, element_name)

            # 判断元素是否存在
            elif element_type == 'element_exist':
                if not self.checkelement.wait_element(driver, 60, (eval(loc_type), locator)):
                    executor = False

            # 判断元素是否不存在
            elif element_type == 'element_noexist':
                a = self.checkelement.wait_noelement(driver, 60, (eval(loc_type), locator))
                print(a)
                if not a:
                    # self.log.WriteWronglog(driver, screen_path, element_name + "元素是存在的")
                    executor = False

            # 红绿框
            elif element_type == 'AlertContainer':
                if not self.getelement.Getalert(driver, element_name):
                    # self.log.WriteWronglog(driver, screen_path, "提交失败")
                    executor = False
            else:
                # 其他可能出现的操作
                print('其他类型')
        if executor is True:
            print(element_name+' 操作成功~~~')
        return executor
