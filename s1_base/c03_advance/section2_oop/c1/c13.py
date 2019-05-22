import requests

url='http://www.baidu.com/'
url2='https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1549934921&di=f808a830620de5341ab3c77d1914c259&src=http://hbimg.b0.upaiyun.com/54ebececeda0217648263cc944d6cfd413a17cdf2cc6-MGHS0y_fw658'
url3='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1549945007526&di=0ba85528dcca5a5e12d6884098b73c34&imgtype=0&src=http%3A%2F%2Fwww.xiaopi.com%2Fgame%2Fuploadfile%2F2016%2F0303%2F20160303051652118.png'
ret=requests.get(url3)
if ret.status_code==200:
    ret.encoding=ret.apparent_encoding
    with open('timg2.png','wb') as f:
        f.write(ret.content)