from pyecharts import Line
attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]
line =Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.show_config()
line.render() 

line =Line("折线图-阶梯图示例")
line.add("商家A", attr, v1, is_step=True, is_label_show=True)
line.show_config()
line.render() 