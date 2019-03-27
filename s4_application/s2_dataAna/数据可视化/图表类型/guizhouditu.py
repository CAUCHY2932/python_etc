#-*- coding:utf-8 -*-  
from pyecharts import Map  
  
value = [95, 70, 30, 45, 80,  
         10, 25, 40, 5]  
attr = [u'贵阳市', u'遵义市',  u'六盘水市', u'安顺市', u'毕节市',   
        u'铜仁市', u"黔东南苗族侗族自治州", u"黔南布依族苗族自治州",  
        u"黔西南布依族苗族自治州"]  
map = Map(u"贵州地图示例", width=1200, height=600)  
map.add("", attr, value, maptype=u'贵州',  
        is_visualmap=True, visual_text_color='#000')  
map.show_config()  
map.render()  