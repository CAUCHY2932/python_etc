from pyecharts import Bar
attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[10, 20, 30, 40, 50, 60]
v2 =[25, 20, 15, 10, 60, 33]

bar =Bar("标记线和标记点示例")
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.render() 

from pyecharts import Bar
bar =Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
bar.render() 