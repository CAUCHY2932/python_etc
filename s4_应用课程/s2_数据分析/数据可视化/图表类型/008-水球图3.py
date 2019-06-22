from pyecharts import Liquid
liquid =Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
liquid.show_config()
liquid.render()