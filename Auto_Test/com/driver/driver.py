
from Auto_Test.com.util.BrowserDriverFactory import BrowserDriverFactory
from Auto_Test.config.read_config import ConfigParser


class Driver:
    '''
            用js打开一个窗口
            driver=webdriver.Chrome(executable_path='E:\\chromedriver.exe')
            js="window.open('https://www-dev.3ren.cn/um/std/login.do?')"
            driver.execute_script(js)
            '''
    driver = None
    def driver_initial(self,config_path):
        # driver初始化
        browserdriverfactory = BrowserDriverFactory()
        con = ConfigParser()
        local_driver = con.get_config(config_path,'LoginElement', 'local_driver')
        remote_driver = con.get_config(config_path,'LoginElement', 'remote_driver')
        visit_url = con.get_config(config_path,'LoginElement','url')
        driver_type = con.get_config(config_path,'LoginElement','local')
        if driver_type.__eq__('1'):
            driver =  browserdriverfactory.get_webdriver(local_driver)

        elif driver_type.__eq__('2'):
            driver = browserdriverfactory.get_remotedriver(remote_driver)
        else:
            print('参数有误')
        # 访问要测试的地址
        browserdriverfactory.open_chrome(driver, visit_url)
        return driver




