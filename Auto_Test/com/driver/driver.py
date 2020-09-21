from Auto_Test.com.util.BrowserDriverFactory import BrowserDriverFactory
from Auto_Test.com.util.ScreenShot import take_screen_shot
from Auto_Test.config.rw_config import ConfigParser
from Auto_Test.com.util.Login import Login


class Driver:
    '''
            用js打开一个窗口
            driver=webdriver.Chrome(executable_path='E:\\chromedriver.exe')
            js="window.open('https://www-dev.3ren.cn/um/std/login.do?')"
            driver.execute_script(js)
            '''
    driver = None
    login = Login()

    def driver_initial(self, driver,config_path,log_info,log_error):
        # driver初始化
        browserdriverfactory = BrowserDriverFactory()
        con = ConfigParser()
        local_driver = con.get_config(config_path, 'Initial', 'local_driver')
        remote_driver = con.get_config(config_path, 'Initial', 'remote_driver')
        visit_url = con.get_config(config_path, 'Initial', 'url')
        driver_type = con.get_config(config_path, 'Initial', 'local')
        if driver_type.__eq__('1'):
            driver = browserdriverfactory.get_webdriver(local_driver)

        elif driver_type.__eq__('2'):
            driver = browserdriverfactory.get_remotedriver(remote_driver)
        else:
            log_error.logger.error('driver类型参数有误')
        # 访问要测试的地址
        browserdriverfactory.open_chrome(driver, visit_url)
        self.login.login(driver, config_path,log_info,log_error)
        return driver
