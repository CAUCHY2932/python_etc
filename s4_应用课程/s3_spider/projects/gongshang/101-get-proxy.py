import requests
import random

def get_proxy():
    # return requests.get('http://123.207.35.36:5010/get/').content
    # return requests.get("http://127.0.0.1:5010/get/").content
    return requests.get("http://127.0.0.1:5010/get/").text


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


# ret=get_proxy()
# print(ret)
# print(type(ret))
# ret2=ret.split(':')
# print(ret2[0])
# print(type(ret2[0]))
# print(ret2[1])
# print(type(ret2[1]))
# ip_addr=ret2[0]
# print(ip_addr)
# ip_port=int(ret2[1])
# print(ip_port)
def get_random_proxy():
    return requests.get("http://127.0.0.1:5010/get_all/").text

ret=get_random_proxy()
print(type(ret))
print(ret)
# ret2=list(ret)
# print(type(ret2))
# print(ret2)
# ret3=ret.split('[').split(']')
# ret4=ret[0]
# print(ret4)
ret5=ret[1:][:-2]
print(ret5)
print(type(ret5))
ret7=[]
ret6=ret5.split(',')
for item in ret6:
    item=item[1:][:-2]
    ret7.append(item)
print(ret7)
print(type(ret7))
ret8=random.choice(ret7)
print(ret8)


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies
