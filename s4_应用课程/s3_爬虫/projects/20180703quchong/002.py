import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
def get_page_index(base_url):
    data={

    }
    headers={

    }
    url=base_url+urlencode(data)
    response=requests.get(url)
    if response.status_code==200:
        print(response.text)
        return response.text
    # if re
    return None
