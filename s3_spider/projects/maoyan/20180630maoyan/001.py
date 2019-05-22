import requests
import re
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

def parse_one_page(html):
    pattern=re.compile(r'<dd>.*?<i class="board-index board-index-.*?">(\d+)</i>.*?<img data-src="(.*?)"'
                       +r'.*?name"><a.*?>(.*?)</a>.*?class="star">(.*?)</p>'
                        +r'.*?releasetime">(.*?)</p>.*?class="integer">(.*?)</i>'
                         +r'.*?class="fraction">(.*?)</i></p>',re.S)
    # pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>',re.S)
    ret=re.findall(pattern,html)
    # print(ret)
    for item in ret:
        num=item[0]
        src=item[1]
        name=item[2]
        actor=item[3].strip()
        time=item[4]
        score=item[5]+item[6]
        print("%s\t\t%s\t%s\t%s\t%s\t%s"%(num,src,name,actor,time,score))
    # print(len(ret))
    # for item in ret:
    #     print(item.group(1)[0])
    #     print(item.group(2)[0])
    #     print(item.group(3)[0])
    # for item in ret:
    #     print(item[0])
    #     print(item[1])
    #     print(item[2])


def main():
    url='http://maoyan.com/board/4?offset=0'
    html=get_one_page(url)
    parse_one_page(html)
    # print(html)

if __name__ == "__main__":
    main()
