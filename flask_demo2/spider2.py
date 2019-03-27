import requests
import pprint


url = 'http://127.0.0.1:5006/'
data = dict(time='niaho')


resp = requests.post(url=url, json=data)
if resp.status_code == 200:
    pprint.pprint(resp.json())
