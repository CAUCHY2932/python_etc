# coding:utf-8


import requests


# class Http:
#     """"""
#     def get(self, url, return_json=True):
#         r =requests.get(url)
#         if r.status_code == 200:
#             if return_json:
#                 return r.json()
#             else:
#                 return r.text
#         else:
#             if return_json:
#                 return {}
#             else:
#                 return ''
class Http:
    """
    利用requests进行数据请求
    """
    @staticmethod
    def get(url, return_json=True):
        r =requests.get(url)
        if r.status_code == 200:
            return r.json() if return_json else r.text
        else:
            return {} if return_json else ''
