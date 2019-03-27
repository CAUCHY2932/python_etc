# coding:utf-8


from lxml import etree
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
# from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import re


chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
# url='http://ai.datahoop.cn/details.html?207'
url2='http://ai.datahoop.cn/details.html?206'

driver.get(url2)

time.sleep(20)

pgSrc=driver.page_source
driver.quit()
print(pgSrc)



