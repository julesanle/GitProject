import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

QRCodePath = 'E:\QRCode.jpg'
chrome_options = Options()
# 指定浏览器的路径；也可不设置刚在默认路径下： python安装目录 python37下
path = 'E:\\chromedriver.exe'
# 无界模式
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
driver.get('http://d.7short.com/8af6')
driver.maximize_window()
time.sleep(2)
try:
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div').click()
except Exception as e:
    print(e)
time.sleep(2)
src_img = driver.find_element_by_xpath('/html/body/div[3]/div/header/div/div/div/div[1]/span[2]/img').get_attribute(
    'src')
print("取到的base64的二维码数据%s" % src_img)
img_base64 = str.split(src_img, ',')[1]
# 将base64格式的二维码图片解码成二进制文件写入png中
fir_img = base64.b64decode(img_base64)
f = open(QRCodePath, 'wb')
f.write(fir_img)
f.close()
time.sleep(2)
driver.quit()
