import requests
# from urllib.request import urlopen
response=requests.get('https://www.baidu.com')
response.encoding='utf-8'
print(response.text)