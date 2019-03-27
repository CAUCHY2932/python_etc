# -*- coding:utf-8 -*-
import os, pymysql,csv,configparser,pickle
from selenium import webdriver
from user_agent import generate_user_agent


global csvpath
global companypath
global cookiedumped,csvinited
global debugmode
global browser_loaded
global export
global chromedriver

browser_loaded=0
csvinited=0

#读取配置文件
config=configparser.RawConfigParser()
config.read('config.cfg')
debugmode=int(config.get("config",'debugmode'))
cookiedumped=int(config.get("config",'cookiedumped'))
csvpath=config.get("config",'csvpath')
export=int(config.get("config",'export'))
companypath=config.get("config",'companypath')
chromedriver=config.get("config","chromedriver")


import time
def dur( op=None, clock=[time.time()] ):
  if op != None:
    duration = time.time() - clock[0]
    print ('%s finished. Duration %.6f seconds.' % (op, duration))
  clock[0] = time.time()

def durt( op=None, clock=[time.time()] ):
  if op != None:
    duration = time.time() - clock[0]
    print ('%s finished. Duration %.6f seconds.' % (op, duration))
  clock[0] = time.time()

def init_db():
    global CONNECTION
    CONNECTION = pymysql.connect("地址", "用户名", "密码", "数据库", use_unicode=True, charset="utf8")


def close_db():
    CONNECTION.close()


def init_web_driver(opt1=0):
    global DRIVER, browser_loaded
    user_agent = generate_user_agent()
    co = webdriver.ChromeOptions()
    # Chrome driver default setting under Windows OS
    co.add_argument('--disable-gpu')

    if opt1 == 0:
        # Set the Chrome in headless mode
        co.add_argument('--headless')
        # Disable images loading
    co.add_argument('blink-settings=imagesEnabled=false')

    # Add User-Agent Profile
    co.add_argument('--user-agent={}'.format(user_agent))

    # Initialize Chrome
    DRIVER = webdriver.Chrome(
        chrome_options=co,
        executable_path=chromedriver,
        service_log_path=os.path.devnull
    )
    browser_loaded=1
    print('Chrome process loaed.')


def close_web_driver():
    DRIVER.quit()


def spider_create_cookie():
    init_web_driver(debugmode)
    DRIVER.get('https://www.qichacha.com/user_login')
    DRIVER.find_element_by_xpath('//*[@id="verifyLoginPanel"]/div[1]/a').click()
    time.sleep(10)
    print(DRIVER.current_url)
    cookie = [item["name"] + "=" + item["value"] for item in DRIVER.get_cookies()]
    print('Cookies Loaded' + '/n' + cookie)
    pickle.dump(DRIVER.get_cookies(), open("cookies.pkl", "wb"))
    close_web_driver()
    browser_loaded=0
    print('Cookies created.')


def write_csv(inputstr, filename='result.csv',opt='a+'):

    if filename.strip()=='':
         filename='result.csv'
    #with open(filename, 'a+',newline='') as f:
    with open(filename, opt, newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(inputstr)
    f.close()
    print('CSV writed.')

def init_csv():
    headline=['搜索项','企业名称', '电话', '官网', '地址', '注册资本', '实缴资本',
              '经营状态', '成立日期', '统一社会信用代码', '纳税人识别号',
              '注册号', '组织机构代码', '公司类型', '所属行业', '核准日期',
              '登记机关', '所属地区', '英文名', '曾用名', '经营方式', '人员规模',
              '营业期限', '企业地址','经营范围']
    write_csv(headline,csvpath,'w+')
    global csvinited
    csvinited=1
    print('Output CSV ready.')



#def write_sql():



def get_companylist(filename='company.csv'):


    company_list = []
    f = open(filename, 'r')
    # company_list=f.readlines()
    for line in f.readlines():
        company_list.append(line.replace('\n', ''))
    return company_list
    print('Company list loaded.')

def table_reduction(searchitem,table, opt=1):
    table_rows = table.find_elements_by_tag_name('tr')

    #table_rows = table.find_elements_by_tag_name('tr')
    query_result = []
    query_result.append(searchitem)
    # 企业名称:
    query_result.append(DRIVER.find_element_by_xpath('//*[@id="company-top"]/div/div[2]/div[1]/h1').text)
    # 电话:
    query_result.append(DRIVER.find_element_by_xpath('//*[@id="company-top"]/div[1]/div[2]/div[2]/span[1]/span[2]/span').text)
    # 官网:
    query_result.append(DRIVER.find_element_by_xpath('//*[@id="company-top"]/div[1]/div[2]/div[2]/span[3]').text)
    # 地址:
    query_result.append(DRIVER.find_element_by_xpath('//*[@id="company-top"]/div[1]/div[2]/div[3]/span[3]/a[1]').text)

    # 注册资本：
    query_result.append(table_rows[0].find_elements_by_tag_name('td')[1].text)

    # 实缴资本：
    query_result.append(table_rows[0].find_elements_by_tag_name('td')[3].text)

    # 经营状态：
    query_result.append(table_rows[1].find_elements_by_tag_name('td')[1].text)

    # 成立日期：
    query_result.append(table_rows[1].find_elements_by_tag_name('td')[3].text)

    # 统一社会信用代码：
    query_result.append(table_rows[2].find_elements_by_tag_name('td')[1].text)

    # 纳税人识别号：
    query_result.append(table_rows[2].find_elements_by_tag_name('td')[3].text)

    # 注册号：
    query_result.append(table_rows[3].find_elements_by_tag_name('td')[1].text)

    # 组织机构代码：
    query_result.append(table_rows[3].find_elements_by_tag_name('td')[3].text)

    # 公司类型：
    query_result.append(table_rows[4].find_elements_by_tag_name('td')[1].text)

    # 所属行业：
    query_result.append(table_rows[4].find_elements_by_tag_name('td')[3].text)

    # 核准日期：
    query_result.append(table_rows[5].find_elements_by_tag_name('td')[1].text)

    # 登记机关：
    query_result.append(table_rows[5].find_elements_by_tag_name('td')[3].text)

    # 所属地区：
    query_result.append(table_rows[6].find_elements_by_tag_name('td')[1].text)

    # 英文名：
    query_result.append(table_rows[6].find_elements_by_tag_name('td')[3].text)

    # 曾用名：
    query_result.append(table_rows[7].find_elements_by_tag_name('td')[1].text)

    # 经营方式：
    query_result.append(table_rows[7].find_elements_by_tag_name('td')[3].text)

    # 人员规模：
    query_result.append(table_rows[8].find_elements_by_tag_name('td')[1].text)

    # 营业期限：
    query_result.append(table_rows[8].find_elements_by_tag_name('td')[3].text)

    # 企业地址：
    query_result.append(table_rows[9].find_elements_by_tag_name('td')[1].text)

    # 注册资本：
    query_result.append(table_rows[10].find_elements_by_tag_name('td')[1].text)



    #if export == 1:  # Write in MYSQL

    if export == 0:  # Write in local csv
        write_csv(query_result,csvpath)

#使用前获取Cookie
def spider_create_cookie():
    init_web_driver(1)
    DRIVER.get('https://www.qichacha.com/user_login')
    DRIVER.find_element_by_xpath('//*[@id="verifyLoginPanel"]/div[1]/a').click()
    time.sleep(10)
    print(DRIVER.current_url)
    cookie = [item["name"] + "=" + item["value"] for item in DRIVER.get_cookies()]
    pickle.dump(DRIVER.get_cookies(), open("cookies.pkl", "wb"))
    print('Cookies loaded.')
    global cookiedumped,browser_loaded
    cookiedumped=1
    DRIVER.close()
    browser_loaded = 0
def visit_webpage(company_name):

    '''
    Dump Logined Cookies
    '''
    if cookiedumped==0:
        spider_create_cookie()
    if browser_loaded==1:
        DRIVER.find_element_by_id("headerKey").send_keys(company_name)
        DRIVER.find_element_by_xpath('/html/body/header/div/form/div/div/span/button').click()

    if cookiedumped==1 and browser_loaded==0:
        init_web_driver(debugmode)
        DRIVER.get('https://www.qichacha.com/')
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            DRIVER.add_cookie(cookie)
        DRIVER.find_element_by_id("searchkey").send_keys(company_name)
        DRIVER.find_element_by_id("V3_Search_bt").click()




    DRIVER.get(DRIVER.find_element_by_class_name("ma_h1").get_attribute("href"))
    table = DRIVER.find_element_by_xpath('//*[@id="Cominfo"]/table[2]')
    if csvinited==0:
        init_csv()
    table_reduction(company_name,table)
def main():
    import array
    global companys
    filename = './log/'+str(time.strftime('%Y-%m-%d_%H-%M', time.localtime(time.time()))) + '_ERROR.log'
    fp = open(filename, 'a+')
    companys=[]
    companys=get_companylist(companypath)
    i=1
    amount = len(companys)
    for items in companys:

        try:
            dur()
            visit_webpage(items)
           # t=timeit(visit_webpage(items))
            dur(str(i)+' of '+str(amount)+' '+items)
            i=i+1
        except:
            print(items+' FAILED TO CATCH')
            fp.write(str(time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time())))+' items '+'FAILED TO LOAD')
    fp.close()



#
#
#
#
#



if __name__ == '__main__':
    durt()
    main()
    DRIVER.close()
    DRIVER.quit()
    print(str(len(companys))+' items finieshed! ')
    durt('TOTALY')