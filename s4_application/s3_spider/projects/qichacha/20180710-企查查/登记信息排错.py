import requests
# from lxml import etree
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

# url = "https://www.qichacha.com/search_index?key=%25E6%2588%2590%25E9%2583%25BD%25E9%25AB%2598%25E6%2596%25B0%25E5%258C%25BA&ajaxflag=1&p={}&"

# url_list = [url.format(i) for i in range(1,10)]
# print(url_list)
# for url in url_list:
#     data = requests.get(url=url,headers=Request_headers,cookies=cookies).content.decode()
#     html = etree.HTML(data)
#     data_lsit = html.xpath("//table[@class='m_srchList']/tbody/tr")
#     for i in data_lsit:
#         print(i.xpath("./td[2]/a/text()"))


url='https://www.qichacha.com/firm_s1dd204af499130b6eac9b90d972b520.html'
data = requests.get(url=url,headers=Request_headers,cookies=cookies).content.decode()
with open('qiye.html','w')as f:
    f.write(data)



