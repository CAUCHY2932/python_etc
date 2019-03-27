from selenium import webdriver


# driver=webdriver.PhantomJS()
# driver.get('http://www.baidu.com')
# print(driver.page_source)
# driver.close()

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
print(driver.page_source)
driver.quit()