import requests
import pprint


link = ''
app_code = 'amazon'
timestamp = ''
check_word_result = ''
page_num = '1'
apply_time_start = '2019-07-25'
apply_time_end = '2019-07-25'

data = {"appCode": app_code,
        "timestamp": timestamp,
        "checkWord": check_word_result,
        "pageIndex": page_num,
        "applyTimeStart": apply_time_start,
        "applyTimeEnd": apply_time_end}


resp = requests.post(link, json=data) 
# resp = requests.post(link, data=data)  # 请求会有问题，因为是表单post，这里必须使用json来post
if resp.status_code == 200:
    # print(resp.json())
    pprint.pprint(resp.json())
# print('请求出错')