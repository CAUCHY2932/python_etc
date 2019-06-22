import requests
import re
import json
from multiprocessing import Pool
from requests.exceptions import  RequestException

def get_one_page(url):
    headers={
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 67.0.3396.62 Safari/537.36'
    }
    try:

        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def write_to_file(content):
    with open("log4.txt",'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        # f.write(content+'\n')


def parse_one_page(html):
    pattern=re.compile(r'<dd>.*?<i class="board-index board-index-.*?">(\d+)</i>.*?<img data-src="(.*?)"'
                       +r'.*?name"><a.*?>(.*?)</a>.*?class="star">(.*?)</p>'
                        +r'.*?releasetime">(.*?)</p>.*?class="integer">(.*?)</i>'
                         +r'.*?class="fraction">(.*?)</i></p>',re.S)
    # pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>',re.S)
    ret=re.findall(pattern,html)
    # print(ret)
    for item in ret:
        yield{
            "num":item[0],
            "src":item[1],
            "name":item[2],
            "actor":item[3].strip()[3:],
            "time":item[4][5:],
            "score":item[5]+item[6],
        }




def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

    # print(html)

if __name__ == "__main__":
    for i in range(10):
        main(i*10)
