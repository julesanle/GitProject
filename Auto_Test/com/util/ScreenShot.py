import time


# 页面截图
def take_screen_shot(driver, filepath, ele_name):
    screen_time = int(time.time())
    try:
        driver.get_screenshot_as_file(filepath + ele_name + str(screen_time) + '.png')
    except Exception as e:
        print(str(e))
