import requests

class Httper:
    def __init__(self):
        pass

    def _fetch_content(url,headers):
        r=requests.get(url,headers)
        if r.status_code==200:
            r.encoding=r.apparent_encoding
            return r
        return None
        
    def _fetch_text(resp):
        if resp:
            return resp.text
        return None

    def _fetch_binary(resp):
        if resp:
            return resp.content
        return None

    def _fetch_json():
        if resp:
            return resp.json
        return None

    

class Spider_netease:
    def __init__:
        self.keyword=''
        self.songs=[] # 由元组组成的列表



 
    def _analysis():
        pass

    def _persistent():
        pass


    def go_crawl():
        pass



if __name__=="__main__":
    pass