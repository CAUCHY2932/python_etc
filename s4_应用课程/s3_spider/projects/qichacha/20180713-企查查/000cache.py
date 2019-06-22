keyword='成都高新区'

MONGO_URL = 'localhost'
MONGO_DB = 'QiChaCha'
# MONGO_TABLE = 'test_beta'
MONGO_TABLE = 'chengdu'
# 四川各市县辖区
# kw_s=['成都市锦江区','成都市青羊区','成都市金牛区','成都市武侯区','成都市成华区','成都市龙泉驿区','成都市青白江区','成都市新都区','成都市温江区','都江堰市','彭州市','邛崃市','崇州市','成都市金堂县','成都市双流县','成都市郫县','成都市大邑县','成都市蒲江县','成都市新津县']

# 四川下辖市
si_chuan=['成都市','自贡市','攀枝花市','泸州市','德阳市','绵阳市','广元市','遂宁市','内江市','乐山市','南充市','眉山市','宜宾市','广安市','达州市','雅安市','巴中市','资阳市','阿坝藏族羌族自治州','甘孜藏族自治州','凉山彝族自治州']
# 河南下辖市
he_nan=['郑州','开封','洛阳','平顶山','安阳','鹤壁','新乡','焦作','濮阳','许昌','漯河','三门峡','南阳','商丘','信阳','周口','驻马店']
# hu_bei=[]
# GROUP_START = 1
# GROUP_END = 20
# KEYWORD='街拍'



# for item in 
# 设置表结构，同时建立区县级单位

# chengdu={'jinjiang':jinjiang,'qingyang':qingyang,}
chengdu=['成都市锦江区','成都市青羊区','成都市金牛区','成都市武侯区','成都市成华区','成都市龙泉驿区','成都市青白江区','成都市新都区','成都市温江区','都江堰市','彭州市','邛崃市','崇州市','成都市金堂县','成都市双流县','成都市郫县','成都市大邑县','成都市蒲江县','成都市新津县']
# 四川下辖市
sichuan={'chengdu':chengdu,'zigong':zigong,}

DBS={'sichuan':sichuan,'henan':henan,}

# for key in chengdu.keys()
# 开始遍历
# for key in chengdu.values():
    
for k1,v1 in DBS.items():
    
    MONGO_DB = k1 # 建立省级数据库
    for k2,v2 in v1.items():
        MONGO_TABLE = k2 # 建立市级表
        for item in v2:
            print('正在检索{0}-{1}-{2}的信息，请稍候'.format(k1,k2,item))
    
    

