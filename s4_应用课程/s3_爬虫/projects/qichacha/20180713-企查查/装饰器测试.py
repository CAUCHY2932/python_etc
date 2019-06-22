# def mongodb_build(func):
#     def wrapper(self):
#         for k1,v1 in DBS.items():
#             MONGO_DB = k1 # 建立省级数据库
#             db = client[MONGO_DB]
#             for k2,v2 in v1.items():
#                 MONGO_TABLE = k2 # 建立市级表
#                 for item in v2:
#                     print('正在检索{0}-{1}-{2}的信息，请稍候'.format(k1,k2,item))
#                     keyword=item
#                     func(self,keyword)
#     return wrapper


# class Qi:
#     @mongodb_build
#     def main(self,keyword):
#         for offset in range(1,11):
#             text = self.get_page_index_2(offset,keyword)



def m_deco(func):
    def wrapper(self):
        for item in range(3):
            keyword=item
            func(self)
    return wrapper

class Qi:
    @m_deco
    def main(self):
        for offset in range(1,11):
            # text = self.get_page_index_2(offset,keyword)
            print(offset,keyword)

Qi().main()

              