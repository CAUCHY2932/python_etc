from pyecharts import Scatter
scatter =Scatter("散点图示例")
v1, v2 =scatter.draw("../images/pyecharts-0.png")
scatter.add("pyecharts", v1, v2, is_random=True)
scatter.show_config()
scatter.render()