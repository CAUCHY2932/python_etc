# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from selenium.webdriver import ActionChains
import requests
import re

driver = webdriver.Chrome()
user_name = 'haochen2932'
user_pw = 'win2017ustc'
content='白酒消费升级，前路何方'
title='白酒消费，价格持续走高'
# qrcode='qrcode'
try:
    url = 'http://www.jiushang.cn/member.php?mod=logging&action=login'
    driver.get(url)
    time.sleep(5)
    """
    输入账号
    """
    input_account = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    for i in user_name:
        time.sleep(0.5)
        input_account.send_keys(i)
    """
    输入密码
    """
    input_pw = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    for i in user_pw:
        time.sleep(0.5)
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
        time.sleep(0.5)
        input_qrcode.send_keys(i)
    """
    提交输入
    """
    login_button = driver.find_element_by_name('loginsubmit')
    login_button.click()
    time.sleep(5)

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
    # 发帖请求网址
    url = 'http://www.jiushang.cn/forum.php?mod=post&action=newthread&fid=359&extra=&topicsubmit=yes'
    headers={
        'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    cookie=driver.get_cookies()
    # cookie='Hm_lvt_26ee52824fc066385669129fd0e9a98f=1532317155,1532329478; Hm_lvt_c22ca145f6a1e37c5b5b73dbc41dba31=1532317155,1532329478; Hm_lvt_bc3b85cbeeedb7417e1b98e85a071286=1532317570,1532329478; jFzT_e363_saltkey=rJU0kF0a; jFzT_e363_lastvisit=1532314360; jFzT_e363_sid=DCLCLY; jFzT_e363_lastact=1532334159%09forum.php%09ajax; jFzT_e363_shenlan_area_title=%C8%AB%B2%BF; jFzT_e363_ulastactivity=1a2dT9oWdrYUmYRjK1AkTccS1D4gFqAZp%2FneCUQsSEH4XGQcnGfZ; jFzT_e363_lastcheckfeed=29117%7C1532329501; jFzT_e363_editormode_e=1; jFzT_e363_smile=1D1; jFzT_e363_visitedfid=685D359; bdshare_firstime=1532318822952; Hm_lpvt_26ee52824fc066385669129fd0e9a98f=1532334127; Hm_lpvt_bc3b85cbeeedb7417e1b98e85a071286=1532334127; Hm_lpvt_c22ca145f6a1e37c5b5b73dbc41dba31=1532334128; jFzT_e363_seccode=93.280574fe4ef768b8a4; jFzT_e363_auth=a048vP2Dj%2Fa3%2Fi5%2B9suAItGuWuRQkLrA%2FaGiBz46rkjs7F54XKRYGk2%2FmA2cuefAyqMhgQUnZOEI2fvTf2cg7JHZjA; jFzT_e363_st_t=29117%7C1532334123%7C3f9c29bed048e87d5584a6d6c66dea3d; jFzT_e363_lip=125.70.76.3%2C1532334126; jFzT_e363_st_p=29117%7C1532332430%7C29f17100ffe9c43bb441bf315fccf65d; jFzT_e363_viewid=tid_56318; jFzT_e363_sendmail=1; jFzT_e363_noticeTitle=1'
    # 获取formhash
    pg_src=driver.page_source
    pattern=re.compile('formhash=(.*?)"')
    ret=re.search(pattern,pg_src)
    print(ret.group(1))
    # 获取时间戳
    formhash=ret.group(1)
    time_stamp=int(time.time())
    print(time_stamp)
    form_data={
        "allownoticeauthor": 1,
        "formhash": formhash,
        "message": content,
        "newalbum": "%C7%EB%CA%E4%C8%EB%CF%E0%B2%E1%C3%FB%B3%C6",
        "posttime": time_stamp,
        "replycredit_extcredits": 0,
        "replycredit_membertimes": 1,
        "replycredit_random":100,
        "replycredit_times": 1,
        "save": "",
        "subject": title,
        "uploadalbum": -2,
        "usesig": 1,
        "wysiwyg": 1,

    }

    # print(cookie)
    response=requests.post(url,headers=headers,cookies=cookie,data=form_data)
    time.sleep(3)
    # driver.find_element_by_css_selector('#pgt > a > img').click()

    pass
except Exception as e:
    print(e)

finally:
    driver.close()
    pass
