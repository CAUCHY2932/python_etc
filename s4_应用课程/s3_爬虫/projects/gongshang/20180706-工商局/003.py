from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.PhantomJS()# 这个路径就是你添加到PATH的路径
url = "http://search.saic.gov.cn/"

driver.get(url)
# iframe = driver.find_elements_by_id('DataList')
# driver.switch_to_frame(iframe)
# driver.switch
driver.switch_to.frame('DataList')
print(driver.page_source)# 最重要的一步
soup = BeautifulSoup(driver.page_source, "html.parser")