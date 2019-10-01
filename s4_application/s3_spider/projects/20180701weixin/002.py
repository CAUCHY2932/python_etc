import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError


base_url='http://weixin.sogou.com/weixin?'
keyword='风景'
def get_html(url):
    headers={
        'Cookie': 'IPLOC=CN5101; SUID=5699B86E1E20910A000000005B38B609; SUV=1530443272216316; SNUID=834D6DBBD5D0BB3ACD21934ED530BC47; ld=hlllllllll2bnaYslllllV7cHADlllllbrABqkllll9llllllylll5@@@@@@@@@@; LSTMV=253%2C76; LCLKINT=3118; ABTEST=0|1530443316|v1; JSESSIONID=aaag6DI_D-sqG8AJqdgrw; weixinIndexVisited=1; sct=2; ppinf=5|1530443954|1531653554|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0Ok5VTEx8Y3J0OjEwOjE1MzA0NDM5NTR8cmVmbmljazo0Ok5VTEx8dXNlcmlkOjQ0Om85dDJsdUFJeDN3d3JpaTBjdnlnRF9NQW5EWG9Ad2VpeGluLnNvaHUuY29tfA; pprdig=XtCOT3-DT99h7En_0KVQM3Gzw15Wb3v4IwgKiWKr2lj32OkV-H2S9yNByQh77yDlu_FKO8H0iWTaMOoGWJ2tdUEF70tyVkYh2D-lVaT8vOUr6bXF7BzCdRZINHMZH6IO7Bul0gN8tgp4VKDIKGIHu_-1sBFEhRyfhbPhAfw6GfE; sgid=21-35814663-AVs4uLJ1I46khm4plsuDAFA; ppmdig=1530443954000000b0ae62d59a6293d43513d5c5d37a0eb1',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    }
    try:
        response=requests.get(url,allow_redirects=False,headers=headers)
        if response.status_code==200:
            response.encoding='utf-8'
            return response.text
        else:
            print('*'*100)
        # if response==302:
        #     # need proxy
        #     print('*'*150)
        #     print('302')
    except ConnectionError as e:
        print('请求出错',e)

        return get_html(url)

def get_index(keyword,page):
    data={
        'query':keyword,
        'type':2,
        'page':page,
        'ie':'utf-8',
    }
    query=urlencode(data)
    url=base_url+query
    html=get_html(url)
    # print(html)
    return html
def main():
    for i in range(1,101):
        html=get_index(keyword,i)
        print(html)



if __name__ == '__main__':
    main()
