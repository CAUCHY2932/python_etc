# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="C:/Users/msi/Desktop/chromedriver.exe")
user_name = 'haochen2932'
user_pw = 'win2017ustc'
content='白酒消费升级，前路何方，北国风光，千里冰封，万里雪飘'
title='白酒消费，价格持续走高'
# qrcode='qrcode'
try:
    url = 'http://www.jiushang.cn/member.php?mod=logging&action=login'
    driver.get(url)
    time.sleep(2)
    """
    输入账号
    """
    input_account = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    for i in user_name:
        input_account.send_keys(i)
    """
    输入密码
    """
    input_pw = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    for i in user_pw:
        input_pw.send_keys(i)
    """
    提取验证码
    """
    input_qr_code = driver.find_element_by_name('loginsubmit')
    # for i in user_pw:
    #     time.sleep(0.5)
    #     input_account.send_keys(i)
    # input_qr_code.send_keys(qrcode)
    src = input_qr_code.get_attribute('src')
    print(src)
    """
    输入验证码
    """
    input_qrcode = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "seccodeverify"))
    )
    qrcode = input('输入验证码:\n')
    for i in qrcode:
        input_qrcode.send_keys(i)
    """
    提交输入
    """
    login_button = driver.find_element_by_name('loginsubmit')
    login_button.click()
    time.sleep(2)

    """
    链接发帖
    """
    # 查看我的帖子
    # url_send='http://www.jiushang.cn/forum.php?mod=guide&view=my'
    # driver.get(url_send)
    # 酒商圈，分类其他话题板块发帖
    # url_jiushangquan_other = 'http://www.jiushang.cn/forum.php?mod=post&action=newthread&fid=685'
    # driver.get(url_jiushangquan_other)
    # time.sleep(5)

    # 酒商品牌综合讨论区，白酒，剑南春板块发帖
    url_jiannanchun = "http://www.jiushang.cn/forum.php?mod=post&action=newthread&fid=359"
    driver.get(url_jiannanchun)

    input_subject = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "subject"))
    )
    for i in title:
        input_subject.send_keys(i)

    iframe = driver.find_element_by_id('e_iframe')
    driver.switch_to.frame(iframe)
    input_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body"))
    )
    for i in content:
        input_content.send_keys(i)
    driver.switch_to.default_content()
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'postsubmit'))
    )
    submit_button.click()


    pass
except Exception as e:
    print(e)

finally:
    driver.close()
    pass
