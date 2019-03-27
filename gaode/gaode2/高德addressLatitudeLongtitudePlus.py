# -*- conding: utf-8 -*-
# @Author:暗香彻骨.沐之杰 Hugo
# @Contact : qyx01@qq.com 
# @Time: 2018/11/5 14:30
# @Software： PyCharm
# @File: addressLatitudeLongtitude.py
# Description:

import requests
import json

serialNumber = 0  # 序号
with open("amap_address.txt", "r", encoding="utf-8") as fr:
    with open("amap_address_result.txt", "w", encoding="utf-8") as fw:
        for line in fr.readlines():
            try:
                # 去除换行符
                line = line.strip('\n').replace('#', ' ')
                # 去除特殊字符
                # line1 = line.replace('#', ' ').replace('/',' ')
                indexNumber = line.find("（")
                indexNumber1 = line.find(",")
                indexNumber2 = line.find("，")
                indexNumber3 = line.find("。")
                indexNumber4 = line.find("酒店")
                indexNumber5 = line.find("饭店")
                indexNumber6 = line.find("、")
                if indexNumber != -1:
                    line1 = line[:line.index("（")]
                elif indexNumber1 != -1:
                    line1 = line[:line.index(",")]
                elif indexNumber2 != -1:
                    line1 = line[:line.index("，")]
                elif indexNumber3 != -1:
                    line1 = line[:line.index("。")]
                elif indexNumber4 != -1:
                    line1 = line[:line.index("酒店")]
                elif indexNumber5 != -1:
                    line1 = line[:line.index("饭店")]
                elif indexNumber6 != -1:
                    line1 = line[:line.index("、")]
                else:
                    line1 = line.replace('#', ' ').replace('/', ' ')
                # 地址获取经纬度
                baiduUrl = "https://restapi.amap.com/v3/geocode/geo?address=%s&output=json&key" \
                           "=" % (line1)

                # req = requests.get(baiduUrl)
                # content = req.text
                # content = content.replace("renderOption&&renderOption(", "")
                # content = content[:-1]
                # baiduAddr = json.loads(content)
                # lng = baiduAddr["result"]["location"]["lng"]
                # lat = baiduAddr["result"]["location"]["lat"]
                # # 经纬度获取城市
                # baiduUrl = "http://api.map.baidu.com/geocoder/v2/?ak=&callback" \
                #            "=renderReverse&location=%s,%s&output=json&pois=0" % (
                #                lat, lng)
                # print(baiduUrl)
                req = requests.get(baiduUrl)
                content = req.text
                # content = content.replace("renderReverse&&renderReverse(", "")
                # content = content[:-1]
                # baiduAddr = json.loads(content)
                result_json = json.loads(content)
                # print(result_json["geocodes"][0]['formatted_address'])
                # print(type(result_json["geocodes"][0]))
                formatted_address = result_json["geocodes"][0]["formatted_address"]
                # print(formatted_address)
                province = result_json["geocodes"][0]['province']
                city = result_json["geocodes"][0]['city']
                district = result_json["geocodes"][0]['district']
                # 写入AddressResult.txt文件
                new_line = line + "+" + formatted_address + "+" + province + "+" + city + "+" + district
                fw.write(new_line)
                fw.write("\n")
                # 打印输出序号
                serialNumber += 1
                print(serialNumber, new_line)  # 打印
            except KeyError:
                pass
                new_line = line + '+' + 'Failure'
                fw.write(new_line)
                fw.write("\n")
                # 打印输出序号
                serialNumber += 1
                print(serialNumber, new_line)  # 打印
            except IndexError:
                pass
                new_line = line + '|' + 'Failure'
                fw.write(new_line)
                fw.write("\n")
                # 打印输出序号
                serialNumber += 1
                print(serialNumber, new_line)  # 打印
            except TypeError:
                pass
                new_line = line + '|' + 'Failure'
                fw.write(new_line)
                fw.write("\n")
                # 打印输出序号
                serialNumber += 1
                print(serialNumber, new_line)  # 打印
            # continue
    print("End")
