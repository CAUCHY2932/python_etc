# import urllib, urllib2, sys
# import ssl
import urllib.request
def get_token():

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的AK】&client_secret=【官网获取的SK】'
    # request = urllib2.Request(host)
    request=urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    # response = urllib2.urlopen(request)
    response = urllib.request.urlopen(request)

    content = response.read()
    if (content):
        print(content)
        return content
    return None







