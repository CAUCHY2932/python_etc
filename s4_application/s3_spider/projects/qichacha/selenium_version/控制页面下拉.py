from selenium import webdriver
import os, time
 
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
 
# 设置最长的超时时间
driver.set_page_load_timeout(10)
 
#打开网页
driver.get('https://www.baidu.com/')
driver.maximize_window()
input_box = driver.find_element_by_xpath('//*[@id="kw"]')
input_box.send_keys('selenium')
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(3)
driver.save_screenshot('perpic/original.png')
 
# 将页面滚动条拖到底部
js = "var q=document.body.scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
driver.save_screenshot('perpic/buttom.png')
 
# 将滚动条移动到页面的顶部
js = "var q=document.body.scrollTop=0"
driver.execute_script(js)
time.sleep(3)
driver.save_screenshot('perpic/top.png')
 
# 将滚动条移动到页面的任意位置
js = "var q=document.body.scrollTop=55555"
driver.execute_script(js)
time.sleep(3)
driver.save_screenshot('perpic/mid.png')
 
driver.quit()
