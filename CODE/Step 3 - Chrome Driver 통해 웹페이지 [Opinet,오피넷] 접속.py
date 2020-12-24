#####################################
# 오피넷 접속
#####################################
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/Sung/Downloads/chromedriver.exe")
driver.get("http://www.opinet.co.kr")

#####################################
# 선택 사항 #
# headless option
#####################################
# WEBSITE 열지 않고 Background에서 돌리는 옵션 가능
# from selenium import webdriver
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# driver = webdriver.Chrome("C:/Users/Sung/Downloads/chromedriver.exe", options = options)
# print ("Headless Chrome Initialized")
# params = {'behavior': 'allow', 'downloadPath': r'C:\Users\Sung\Downloads'}
# driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
# driver.get("http://www.opinet.co.kr") #오피넷 접속