import logging

class Parameter:
    def get_url(self,driver):
        now_url = driver.current_url
        return '{0}'.format(now_url)
    def enter_page(self,driver,url):
        # js2="window.open('https://www-dev.3ren.cn/um/std/login.do?')"
        try:
            driver.execute_script("window.open('"+url+"')")
            # driver.execute_script(js2)
            return True
        except Exception as e:
            logging.error(str(e))
            return False

