from openpyxl import workbook
from openpyxl import load_workbook
from Auto_Test.config.read_config import ConfigParser
from Auto_Test.com.util.Login import Login

from Auto_Test.com.element_executor.ExecutorSingle import ExecutorSingleCase


class ExecutorCase:
    con = ConfigParser()
    single_case = ExecutorSingleCase()
    login = Login()

    def read_excel(self, driver,config_path):
        case_url = self.con.get_config(config_path, 'Case', 'case_url')
        wb = load_workbook(case_url)
        # 循环遍历所有sheet
        sheets = wb.sheetnames
        for i in range(len(sheets)):
            sheet = wb[sheets[i]]
            print('第' + str(i + 1) + '个sheet: ' + sheet.title + '->>>')
            self.sheet_data(driver,sheet,config_path)
        return True

    def sheet_data(self, driver,sheet,config_path):
        case_data = None
        for row in range(sheet.min_row + 1, sheet.max_row + 1):
            for line in range(1, sheet.max_column):
                case_num = sheet.cell(row, 1).value
                case_module = sheet.cell(row,2).value
                if case_num is not None:
                    case_data = sheet.cell(row, line).value
                    if sheet.cell(sheet.min_row, line).value == '测试数据(element_name,type,loc_type,locator)':
                        print('---准备执行用例：%s' % case_num +' 测试模块:%s'%case_module+'---')#+'的对应元素：\n%s' % case_data
                        # if case_module != '登录' and access_token is None:
                        #     #先登录一下
                        #     self.login.login(driver,config_path)
                        list_element = case_data.strip('\n').split(';')
                        self.single_case.element_executor(driver,case_module,list_element,config_path)
                else:
                    # 空的行不执行
                    break