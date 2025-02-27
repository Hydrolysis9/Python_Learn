from selenium import webdriver
from selenium.webdriver.common.by import By

# 生成一个驱动对象
wd = webdriver.Edge()
wd.implicitly_wait(10)
# 发起命令，打开指定网址
wd.get('https://baidu.com')
main_window = wd.current_window_handle
# 根据id选择元素
element_user = wd.find_element(By.ID,'kw')

# 键入搜索，对页面元素进行操作
element_user.send_keys('南方医科大学')

# 点击搜索
search_click = wd.find_element(By.ID,'su')
search_click.click()

# 打开新窗口
search_click = wd.find_element(By.CSS_SELECTOR,r'#\33  > div > div:nth-child(1) > div:nth-child(3) > div.c-row.c-gap-top-middle > div.c-span3 > a > div > div > span')
search_click.click()

# handles
print(wd.window_handles)
pass

# 窗口切换
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if handle.title() == '南方医科大学':
        break

# 切换回原窗口
wd.switch_to.window(main_window)

pass

