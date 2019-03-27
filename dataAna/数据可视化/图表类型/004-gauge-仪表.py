from pyecharts import Gauge
gauge =Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.show_config()
gauge.render()