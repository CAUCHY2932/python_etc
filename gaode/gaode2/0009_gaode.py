# coding: utf-8
# author: young
# datetime: 20190621

import requests
import json
# import time
import pandas as pd


order = "10"


def request_from_gaode(addr):
    payload = {
        "key": "",
        "output": "json",
        "address": addr,
    }
    base_gaode_url = ""
    resp = requests.get(base_gaode_url, payload)

    return resp.text if resp.status_code == 200 else ""


def parse_addr_json(addr):
    addr_json = json.loads(addr)
    try:
        if addr_json["status"] == "1":
            adcode = addr_json["geocodes"][0]["adcode"]
            citycode = addr_json["geocodes"][0]["citycode"]
            province = addr_json["geocodes"][0]["province"]
            city = addr_json["geocodes"][0]["city"]
            district = addr_json["geocodes"][0]["district"]
            lat_lng = addr_json["geocodes"][0]["location"]
            return 1, adcode, citycode, province, city, district, lat_lng
        return 0, "行政编码", "城市编码", "省", "市", "区", "经纬度"
    except Exception as e:
        print(e)
        return 0, "行政编码", "城市编码", "省", "市", "区", "经纬度"
        pass


def process(chunk):
    # chunk.to_csv(r'D:\0621\new_records.csv', mode='a', header=False)
    with open('./datasets/success_{}.csv'.format(order), 'a', encoding="utf-8") as f:
        # f.write()

        for index, item in chunk.iterrows():
            # print(type(item["banquet_addr"]))
            # print(item["banquet_addr"], item["banquet_id"])
            addr = request_from_gaode(item["banquet_addr"])
            parsed_addr_json = parse_addr_json(addr)
            status_code, parsed_addr = parsed_addr_json[0], parsed_addr_json[1:]
            try:

                banquet_addr_handled = item["banquet_addr"].split(",")[0]
            except Exception as e:
                print(e)
                banquet_addr_handled = item["banquet_addr"]
                pass
            content_str = '{},{},{},{},{},{},{},{}\n'.format(
                item["banquet_id"],
                parsed_addr[0],
                parsed_addr[1],
                parsed_addr[2],
                parsed_addr[3],
                parsed_addr[4],
                parsed_addr[5],
                banquet_addr_handled)
            # print("{},{},{}".format(item["banquet_id"], parsed_addr, item["banquet_addr"]))
            print(index, content_str)
            # content_str = ", ".join(*parsed_addr) + "\n"
            if status_code == 1:
                f.write(content_str)
            else:
                with open("./datasets/error_{}.csv".format(order), "a", encoding="utf-8")as f_error:
                    f_error.write(content_str)
            # if parsed_addr["parse_status"] == "1":
            #     f.write(",".join(list(parse_addr_json.values()).append())+ "\n")
    # print(chunk)
    pass


def split_chunk_read(file_name, usecols=None, chunk_size=100):
    # item = 10
    for chunk in pd.read_csv(file_name, usecols=usecols, header=None, chunksize=chunk_size):
        chunk.columns = ['banquet_id', 'banquet_addr']  # banquet_id 宴会单号, banquet_addr 宴会地址
        process(chunk)
        # item = item + 1
        # if item>10:
        #     break
        print('-' * 50)
        # time.sleep(3)


def request_from_gaode_test():
    # addr = "泉州市,惠安县螺阳镇达利世纪酒店,3楼世纪厅"
    addr = ''
    addr = request_from_gaode(addr)
    print(addr)


def go():
    split_chunk_read("./datasets/addr_2017_{}.csv".format(order))
    pass


if __name__ == '__main__':
    # request_from_gaode_test()
    go()
