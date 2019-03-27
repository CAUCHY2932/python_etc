import requests
# from bs4 import BeautifulSoup
# import sys
from urllib.parse import urlencode

from lxml import etree
from config import *
from requests.exceptions import ConnectionError
import pymongo
# from multiprocessing import Pool



client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]


class Qichacha(object):
    def __init__(self):
        pass

    def get_page_index(self, offset, keyword):
        data={
            'key':keyword,
        }
        # url='https://www.qichacha.com/search?'+urlencode(data)+'#p:{offset}&'.format( offset=offset)

        url='https://www.qichacha.com/search?'+urlencode(data)+'#p:{offset}'.format( offset=offset)


        # url = 'https://www.qichacha.com/search?key={keyword}#p:{offset}&'.format(keyword=keyword, offset=offset)
        # url = 'https://www.qichacha.com/search?key={keyword}#p:{offset}&'.format(keyword=keyword, offset=offset)

        print(url)
        Request_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'UM_distinctid=1648246e3e2105-0f286da990ab8f-77256752-e1000-1648246e3e3398; CNZZDATA1254842228=1244370978-1531191327-https%253A%252F%252Fwww.baidu.com%252F%7C1531283479;zg_did=%7B%22did%22%3A%20%221648246e8d516b-0371e8373d8f25-77256752-e1000-1648246e8d6d6%22%7D;zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201531285720963%2C%22updated%22%3A%201531288555140%2C%22info%22%3A%201531194042592%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2206a8dc6ba11a66c6d46b58838cf2e7ae%22%7D; _uab_collina=153119431866858685479222;_umdata=85957DF9A4B3B3E842A8332BD23FA48FC95A90703E91E47F3332796D13B36E2E77C3B8FF6DE6C244CD43AD3E795C914CDBDBE4360F720A87C3642A67715540D9; PHPSESSID=803obe1eqjt93q0ougkijv5lu1; acw_tc=AQAAAP0U0nhyYwYA9TiUtrZGujp7C7EL',
            'Host': 'www.qichacha.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }
        try:
            response = requests.get(url, headers=Request_headers)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                print(response.text)
                return response.text
            return None
        except ConnectionError:
            print('Error occurred')
            return None

    def parse_page_index(self, text):
        result = etree.HTML(text)
        tr_lst = result.xpath('/html/body/div/div/div/div/section/table/tbody/tr')
        for item in tr_lst:
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

        if '工商信息' in html:
            base_info = {}
            print('工商信息提取')
            result = etree.HTML(html)
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
            # print(base_info)
            return base_info


        elif '登记信息' in html:
            log_info = {}
            print('登记信息提取')

            result = etree.HTML(html)
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





            base_info = {

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

            # pass
        else:
            print('未查找到有用信息')
            return None

    def turn_page(self):
        pass

    def save_to_mongo(self,result):
        if db[MONGO_TABLE].insert(result):
            print('Successfully Saved to Mongo', result)
            return True
        return False

    def write_to_file(self, file_path, content):
        with open(file_path, 'w', encoding='utf-8')as f:
            f.write(content)

    def main(self, offset):
        text = self.get_page_index(offset, keyword)
        tup = self.parse_page_index(text)
        # cnt=1
        for url,title in tup:
            # print(url)
            html = self.get_page_detail(url)
            # self.write_to_file(str(cnt)+'.txt',html)
            # cnt+=1
            info=self.parse_page_detail(html)
            firm_info={
                "公司名称：":title,
                "公司链接":url,
                "公司信息":info,
            }
            print(firm_info)
            if self.save_to_mongo(firm_info):
                print('成功插入信息')
            else:
                print('插入信息失败')



if __name__ == '__main__':
    qichacha = Qichacha()
    qichacha.main(7)
