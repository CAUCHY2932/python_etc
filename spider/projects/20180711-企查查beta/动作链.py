

# https://www.cnblogs.com/alpha-go/p/6957298.html

# 1.ActionChains基本用法

# 首先需要了解ActionChains的执行原理，当你调用ActionChains的方法时，不会立即执行，而是会将所有的操作按顺序存放在一个队列里，当你调用perform()方法时，队列中的时间会依次执行。

# 这种情况下我们可以有两种调用方法：

# 链式写法

# menu = driver.find_element_by_css_selector(".nav")
# hidden_submenu =  driver.find_element_by_css_selector(".nav #submenu1")

# ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

# 分步写法

# menu = driver.find_element_by_css_selector(".nav")
# hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
 
# actions = ActionChains(driver)
# actions.move_to_element(menu)
# actions.click(hidden_submenu)
# actions.perform()



# 2.ActionChains方法列表

# click(on_element=None) ——单击鼠标左键

# click_and_hold(on_element=None) ——点击鼠标左键，不松开

# context_click(on_element=None) ——点击鼠标右键

# double_click(on_element=None) ——双击鼠标左键

# drag_and_drop(source, target) ——拖拽到某个元素然后松开

# drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开

# key_down(value, element=None) ——按下某个键盘上的键

# key_up(value, element=None) ——松开某个键

# move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标

# move_to_element(to_element) ——鼠标移动到某个元素

# move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置

# perform() ——执行链中的所有动作

# release(on_element=None) ——在某个元素位置松开鼠标左键

# send_keys(*keys_to_send) ——发送某个键到当前焦点的元素

# send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素 




action = ActionChains(driver)

# nc_1_n1z
# width: 308px;
# 348
dragger = driver.find_element_by_id('nc_1_n1z') # 被拖拽元素

action.click_and_hold(dragger).move_by_offset(400, 348).release().perform()


dragger = driver.find_element_by_id('dragger') # 被拖拽元素
item1 = driver.find_element_by_xpath('//div[text()="Item 1"]') # 目标元素1
item2 = driver.find_element_by_xpath('//div[text()="Item 2"]') # 目标2
item3 = driver.find_element_by_xpath('//div[text()="Item 3"]') # 目标3
item4 = driver.find_element_by_xpath('//div[text()="Item 4"]') # 目标4

action = ActionChains(driver)
action.drag_and_drop(dragger, item1).perform() # 1.移动dragger到目标1


Actions action = new Actions(driver);
action.moveToElement(bodyImgEle, x + 2, y - 34).click().perform();