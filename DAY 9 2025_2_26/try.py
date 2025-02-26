from selenium import webdriver
from selenium.webdriver.common.by import By
# 生成一个驱动对象
wd = webdriver.Edge()
# 发起命令，打开指定网址
wd.get('https://baidu.com')

# 根据id选择元素
element_user = wd.find_element(By.ID,'kw')

# 键入搜索，对页面元素进行操作
element_user.send_keys('南方医科大学')

# 点击搜索
search_click = wd.find_element(By.ID,'su')
search_click.click()


