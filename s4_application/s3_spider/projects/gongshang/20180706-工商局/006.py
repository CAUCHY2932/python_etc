import re

def join_url(url):
    pattern=re.compile(r'../..(.*)')
    result=re.search(pattern,url).group(1)
    base_url='http://search.saic.gov.cn'
    url=base_url+result
    return url
url='../../auto3743/auto3744/201802/t20180222_272431.html'
url=join_url(url)
print(url)