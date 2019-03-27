from selenium import webdriver
url = "http://search.saic.gov.cn/"
# driver = webdriver.PhantomJS(executable_path='E:/phantomjs/bin/phantomjs.exe')//这个路径就是你添加到PATH的路径
driver = webdriver.PhantomJS()# 这个路径就是你添加到PATH的路径

driver.get(url)
print (driver.page_source)