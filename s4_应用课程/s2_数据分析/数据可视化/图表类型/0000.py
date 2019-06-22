#-*- coding:utf-8 -*-  
from pyecharts import Map  
value =[2, 60, 2, 6, 80, 2, 5, 2, 1, 4, 5, 1,  
        4, 1, 5, 2, 2, 5, 4, 1, 1, 10, 2]  
attr =["安徽", "北京", "福建", "广东", "贵州", "海南", "河北", "河南", "黑龙江",  
       "湖北", "湖南", "吉林", "江苏", "辽宁", "山东", "山西", "陕西", "上海",  
       "四川", "天津", "云南", "浙江", "重庆"]  
map=Map("各省微信好友分布", width=1200, height=600)  
map.add("", attr, value, maptype='china', is_visualmap=True,  visual_text_color='#000')  
map.show_config()  
map.render()  