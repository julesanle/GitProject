from Auto_Test.com.util.GetDate import GetDate


class DateEntry:
    get_date = GetDate()

    def date_input(self, driver, element):
        element_name = element['element_name']
        element_type = element['type']
        loc_type = element['loc_type']
        locator = element['locator']
        input_date = None
        try:
            page_element = driver.find_element(eval(element_type),locator)
            js1 = "arguments[0].removeAttribute('readonly')"
            driver.execute_script(js1, page_element)
            if '开始' in element_name:
                input_date = self.get_date.start_datetime()
            elif '截止' in element_name or '结束' in element_name:
                input_date =self.get_date.end_datetime()
            else:
                print('时间控件取名有误')
                return False
            js2 = "document.querySelector('css selector').value=%s"%input_date
            driver.execute_script(js2)
            return True
        except Exception as e:
            print(str(e))
            return False

        def other(self):
            if '开始日期' in element_name:
                input_keys = self.get_date.start_date()
            elif '开始时间' in element_name:
                input_keys = self.get_date.start_time()
                print(input_keys)
            elif '结束日期' in element_name:
                input_keys = self.get_date.end_date()
            elif '结束时间' in element_name:
                input_keys = self.get_date.end_time()
            elif '开始日期时间' in element_name:
                input_keys = self.get_date.start_datetime()
            elif '结束日期时间' in element_name:
                input_keys = self.get_date.end_datetime()
