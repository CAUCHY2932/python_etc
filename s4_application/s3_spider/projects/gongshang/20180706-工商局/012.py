from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.PhantomJS()# 这个路径就是你添加到PATH的路径
url = "http://www.gsxt.gov.cn/%7BD5647A52B2028BDF5E76D060E17137D7FFC48504B48F1F352B9B7B5368FD2B03A59E0E243A8ACB9F7C9CC82B6ACC8D3DF91B1533E4D2E7FEC8C6C9D0E6F4AF3311B011B0118DAF0EFE8D8A2B8A2B8AA805A4861A381A382D8C2DDD8CAE9D7731A45EE869F9BFDB7D9D1CA280A2A50483C29675340F49C87654F554F554F5-1530858702910%7D"

driver.get(url)
time.sleep(30)
# iframe = driver.find_elements_by_id('DataList')
# driver.switch_to_frame(iframe)
# driver.switch
# driver.switch_to.frame('DataList')
print(driver.page_source)# 最重要的一步
# soup = BeautifulSoup(driver.page_source, "html.parser")