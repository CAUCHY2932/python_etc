import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException

def get_one_page(offset,keyword):
    data={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',

    }
    url='https://www.toutiao.com/search_content/?'+urlencode(data)
    print(url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def main():
    html=get_one_page(0,'街拍')
    print(html)

if __name__ == "__main__":
    main()