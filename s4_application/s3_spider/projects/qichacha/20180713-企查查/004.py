import requests
# from bs4 import BeautifulSoup
# import sys
from urllib.parse import urlencode

from lxml import etree
# from config2 import *
from requests.exceptions import ConnectionError
import pymongo
# from multiprocessing import Pool

# 公共变量
MONGO_URL = 'localhost'

client = pymongo.MongoClient(MONGO_URL, connect=False)
# 设置表结构，同时建立区县级单位

# chengdu={'jinjiang':jinjiang,'qingyang':qingyang,}
# chengdu=['成都市锦江区','成都市青羊区','成都市金牛区','成都市武侯区','成都市成华区','成都市龙泉驿区','成都市青白江区','成都市新都区','成都市温江区','都江堰市','彭州市','邛崃市','崇州市','成都市金堂县','成都市双流县','成都市郫县','成都市大邑县','成都市蒲江县','成都市新津县']

chengdu=['成都市锦江区','成都市青羊区','成都市金牛区','成都市武侯区','成都市成华区','成都市龙泉驿区','成都市青白江区','成都市新都区','成都市温江区','都江堰市','彭州市','邛崃市','崇州市','成都市金堂县','成都市双流县','成都市郫县','成都市大邑县','成都市蒲江县','成都市新津县']
# 四川下辖市
# sichuan={'chengdu':chengdu,'zigong':zigong,}
sichuan={'chengdu':chengdu,}

# DBS={'sichuan':sichuan,'henan':henan,}
DBS={'sichuan':sichuan,}


def mongodb_build(func):
    def wrapper():
        for k1,v1 in DBS.items():
            MONGO_DB = k1 # 建立省级数据库
            db = client[MONGO_DB]
            for k2,v2 in v1.items():
                MONGO_TABLE = k2 # 建立市级表
                for item in v2:
                    print('正在检索{0}-{1}-{2}的信息，请稍候'.format(k1,k2,item))
                    keyword=item
                    func(keyword)
    return wrapper



class Qichacha(object):
    def __init__(self):
        
        pass

    def get_page_index_2(self,offset,keyword):
        data={
            'key':keyword,
            'ajaxflag':1,
            'p':offset,
        }
        url = "https://www.qichacha.com/search_index?"+urlencode(data)+'&'
        print('正在抓取的链接是：{url}'.format(url=url))
        cookies = {'zg_did': '%7B%22did%22%3A%20%2216487437c273e8-0413314e2517fa-47e1039-1fa400-16487437c282b9%22%7D', 'UM_distinctid': '16487437d2950a-09cd6201472eb3-47e1039-1fa400-16487437d2a5a2', '_uab_collina': '153127770461080556196559', 'acw_tc': 'AQAAABEwxVSl2QwAeyKFt/sTJPFNt/GZ', 'PHPSESSID': 'uf8su39s1gqih8mprdgae00cm7', 'CNZZDATA1254842228': '365813708-1531272679-%7C1531380682', 'Hm_lvt_3456bee468c83cc63fb5147f119f1075': '1531277705,1531384905', '_umdata': 'E2AE90FA4E0E42DE678753C00902C7634FB4C01605ECA0DEC853CB53EAE241AD0048FA0EE29EFE8CCD43AD3E795C914C84EBCF9DD6D83ECAC99BB46A6983EF24', 'hasShow': '1', 'zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f': '%7B%22sid%22%3A%201531384904648%2C%22updated%22%3A%201531385631486%2C%22info%22%3A%201531277704237%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22a7e270aada464adf9d3868cda4ff8866%22%7D', 'Hm_lpvt_3456bee468c83cc63fb5147f119f1075': '1531385632'}
        Request_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531202479; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1531194042,1531204802,1531205674,1531207182; zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531204802020%2C%22updated%22%3A%201531207181085%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; hasShow=1; _uab_collina=153119431866858685479222; PHPSESSID=tkpr2hukcmiscab8fumssquht6; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1531207182; acw_tc=AQAAADExS1W3dwAA9DiUtmrKklYEYCqV; _umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9',
            'Host': 'www.qichacha.com',
            'Upgrade-Insecure-Requests': '1',
            # 'Referer': 'https://www.qichacha.com/search?key=%E6%88%90%E9%83%BD%E9%AB%98%E6%96%B0%E5%8C%BA',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }

        try:
            response = requests.get(url=url,headers=Request_headers,cookies=cookies)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                # print(response.text)
                return response.text
            return None
        except ConnectionError:
            print('Error occurred')
            return None
    

    def parse_page_index(self,text):
        html=etree.HTML(text)
        data_lsit = html.xpath("//table[@class='m_srchList']/tbody/tr")
        for item in data_lsit:
            link = item.xpath('./td[2]/a/@href')[0]
            title = item.xpath('./td[2]/a/text()')[0]
            print(link, title)
            link_new = 'https://www.qichacha.com' + link
            tup=(link_new,title)
            yield tup

    def get_page_detail(self, url):
        Request_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531202479; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1531194042,1531204802,1531205674,1531207182; zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531204802020%2C%22updated%22%3A%201531207181085%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; hasShow=1; _uab_collina=153119431866858685479222; PHPSESSID=tkpr2hukcmiscab8fumssquht6; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1531207182; acw_tc=AQAAADExS1W3dwAA9DiUtmrKklYEYCqV; _umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9',
            'Host': 'www.qichacha.com',
            'Upgrade-Insecure-Requests': '1',
            # 'Referer': 'https://www.qichacha.com/search?key=%E6%88%90%E9%83%BD%E9%AB%98%E6%96%B0%E5%8C%BA',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }
        try:
            response = requests.get(url, headers=Request_headers)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response.text
            return None
        except ConnectionError:
            print('Error occurred')
            return None

    def parse_page_detail(self, html):
        # print(html)
        result = etree.HTML(html)
        
        # key=result.xpath('//*[@id="Cominfo"]/div[@class="tcaption"]/span[@class="title"]/text()')[0]
        # 登记信息关键字
        key_log=result.xpath('//section[@id="Cominfo"]/div[@class="tcaption"]/span[@class="title"]')
        # 工商信息关键字
        key_com=result.xpath('//*[@id="Cominfo"]/div[1]/h3/text()')
        if len(key_com)!=0:
            print('在网页中查找到关键词:"{}"'.format(key_com[0]))
            base_info = {}
            # print('工商信息提取')
            # result = etree.HTML(html)
            table_lst = result.xpath("//section[@id='Cominfo']/table[2]/tr")

            log_amount_name = table_lst[0].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 注册资本
            log_amount_value = table_lst[0].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            real_amount_name = table_lst[0].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 实缴资本
            real_amount_value = table_lst[0].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            organize_state_name = table_lst[1].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 经营状态
            organize_state_value = table_lst[1].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            build_date_name = table_lst[1].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 成立日期
            build_date_value = table_lst[1].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            universal_num_name = table_lst[2].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 统一社会信用代码
            universal_num_value = table_lst[2].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            taxpayer_name = table_lst[2].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 纳税人识别号
            taxpayer_value = table_lst[2].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            auth_num_name = table_lst[3].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 注册号
            auth_num_value = table_lst[3].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            organ_code_name = table_lst[3].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 组织结构代码
            organ_code_value = table_lst[3].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            firm_type_name = table_lst[4].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 公司类型
            firm_type_value = table_lst[4].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            belong_vocation_name = table_lst[4].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 所属行业
            belong_vocation_value = table_lst[4].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            check_date_name = table_lst[5].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 核准日期
            check_date_value = table_lst[5].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            log_organ_name = table_lst[5].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 登记机关
            log_organ_value = table_lst[5].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            addr_name = table_lst[6].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 所属地区
            addr_value = table_lst[6].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            en_name = table_lst[6].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 英文名
            en_value = table_lst[6].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            used_name = table_lst[7].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 曾用名
            used_value = table_lst[7].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            attend_amount_name = table_lst[7].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 参保人数
            attend_amount_value = table_lst[7].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            employee_anmount_name = table_lst[8].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 人员规模
            employee_anmount_value = table_lst[8].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            manage_timeout_name = table_lst[8].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 营业期限
            manage_timeout_value = table_lst[8].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            firm_addr_name = table_lst[9].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 企业地址
            firm_addr_value = table_lst[9].xpath('./td[2]/text()')[0].strip().replace("\n", "")

            manage_range_name = table_lst[10].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 经营范围
            manage_range_value = table_lst[10].xpath('./td[2]/text()')[0].strip().replace("\n", "")

            base_info = {
                log_amount_name: log_amount_value,
                real_amount_name: real_amount_value,
                organize_state_name: organize_state_value,
                build_date_name: build_date_value,
                universal_num_name: universal_num_value,
                taxpayer_name: taxpayer_value,
                auth_num_name: auth_num_value,
                organ_code_name: organ_code_value,
                firm_type_name: firm_type_value,
                belong_vocation_name: belong_vocation_value,
                check_date_name: check_date_value,
                log_organ_name: log_organ_value,
                addr_name: addr_value,
                en_name: en_value,
                used_name: used_value,
                attend_amount_name: attend_amount_value,
                employee_anmount_name: employee_anmount_value,
                manage_timeout_name: manage_timeout_value,
                firm_addr_name: firm_addr_value,
                manage_range_name: manage_range_value,

            }
            return base_info


        elif len(key_log)!=0:
            print('在网页中查找到关键词:"{}"'.format(key_log[0]))
            log_info = {}
            # print('登记信息提取')

            table_lst = result.xpath("//section[@id='Cominfo']/table/tr")

            universal_num_name = table_lst[0].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 统一社会信用代码
            universal_num_value = table_lst[0].xpath('./td[2]/text()')[0].strip().replace("\n", "")

            legal_p_name = table_lst[1].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 法人/负责人
            legal_p_value = table_lst[1].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            log_amount_name = table_lst[1].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 注册资本
            log_amount_value = table_lst[1].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            build_date_name = table_lst[2].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 成立日期
            build_date_value = table_lst[2].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            log_state_name = table_lst[2].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 登记状态
            log_state_value = table_lst[2].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            social_type_name = table_lst[3].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 社会组织类型
            social_type_value = table_lst[3].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            log_organ_name = table_lst[3].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 登记机关
            log_organ_value = table_lst[3].xpath('./td[4]/text()')[0].strip().replace("\n", "")

            auth_office_name = table_lst[4].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 发证机关
            auth_office_value = table_lst[4].xpath('./td[2]/text()')[0].strip().replace("\n", "")
            cert_valid_name = table_lst[4].xpath('./td[3]/text()')[0].strip().replace("\n", "")  # 证书有效期
            cert_valid_value = table_lst[4].xpath('./td[4]/text()')[0].strip().replace("\n", "")



            manage_range_name = table_lst[5].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 业务范围
            manage_range_value = table_lst[5].xpath('./td[2]/text()')[0].strip().replace("\n", "")

            addr_name = table_lst[6].xpath('./td[1]/text()')[0].strip().replace("\n", "")  # 住所
            addr_value = table_lst[6].xpath('./td[2]/text()')[0].strip().replace("\n", "")

            log_info = {

                universal_num_name: universal_num_value,
                legal_p_name:legal_p_value,
                log_amount_name:log_amount_value,
                build_date_name:build_date_value,
                log_state_name:log_state_value,
                social_type_name:social_type_value,
                log_organ_name:log_organ_value,
                auth_office_name:auth_office_value,
                cert_valid_name:cert_valid_value,
                manage_range_name:manage_range_value,
                addr_name:addr_value,
            }

            print(log_info)
            return log_info

        else:
            print('未查找到有用信息')
            return None

    # def mongodb_build(self):
    #     for k1,v1 in DBS.items():
    #         MONGO_DB = k1 # 建立省级数据库
    #         db = client[MONGO_DB]
    #         for k2,v2 in v1.items():
    #             MONGO_TABLE = k2 # 建立市级表
    #             for item in v2:
    #                 print('正在检索{0}-{1}-{2}的信息，请稍候'.format(k1,k2,item))



    def save_to_mongo(self,result):
        if db[MONGO_TABLE].insert(result):
            print('Successfully Saved to Mongo', result)
            return True
        return False

    def write_to_file(self, file_path, content):
        with open(file_path, 'w', encoding='utf-8')as f:
            f.write(content)

@mongodb_build
def main(keyword):
    qi=Qichacha()
    # for item in keyword:
    # text = self.get_page_index_2(offset,item)
    for offset in range(1,11):
        text = qi.get_page_index_2(offset,keyword)
        tup = qi.parse_page_index(text)
        for url,title in tup:
            html = qi.get_page_detail(url)
            qi.write_to_file('{}.txt'.format(title),html)
            info=qi.parse_page_detail(html)
            firm_info={
                "公司名称：":title,
                "公司链接":url,
                "公司信息":info,
            }
            print(firm_info)
            if qi.save_to_mongo(firm_info):
                print('成功插入信息')
            else:
                print('插入信息失败')



if __name__ == '__main__':
    main()
    # qichacha = Qichacha()
    # run=qichacha.main
    # run()
    # run(10)
    # for item in range(1,11):
    #     run(item)
