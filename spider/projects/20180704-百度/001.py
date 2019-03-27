from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# browser=webdriver.Chrome()
browser=webdriver.PhantomJS()
def search():
    url='https://map.baidu.com/mobile/webapp/place/detail/qt=s&wd=%E5%B0%8F%E5%8C%BA&c=75&searchFlag=bigBox&version=5&exptype=dep&src_from=webapp_all_bigbox&sug_forward=&src=0&uid=d63a9773c9c1673f081cc7db/i=0&showall=1&pos=0&da_ref=listclk&da_qrtp=36&da_adtp=&da_log=&da_adquery=%E5%B0%8F%E5%8C%BA&da_adtitle=%E4%B8%AD%E6%B5%B7%E5%9B%BD%E9%99%85%E7%A4%BE%E5%8C%BA&da_adindus=%E6%88%BF%E5%9C%B0%E4%BA%A7;%E4%BD%8F%E5%AE%85%E5%8C%BA&detail_from=list/?fromhash=1'
    # browser.get('http://www.taobao.com')
    browser.get(url)
    time.sleep(10)
    browser.save_screenshot('1.png')
    html=browser.page_source
    print(html)

    browser.close()
    return html

    # element = WebDriverWait(browser, 10).until(
    #     EC.presence_of_element_located((By.ID, "q"))
    # )
    # input=WebDriverWait(browser, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"))
    # )
def write_to_file(html,filePath):
    with open(filePath,'w') as f:
        f.write(html)
        return None

def read_from_file(filePath):
    with open(filePath,'r') as f:
        html=f.read()
        if html:
            return html
        return None

search()