from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.get('https://www.byhy.net/cdn2/files/selenium/sample1.html')

elements_list = wd.find_elements(By.CSS_SELECTOR,'.animal')
for element in elements_list:
    print(element.text)

# 选择子元素与后代元素
elements_list = wd.find_elements(By.CSS_SELECTOR,'#container > div')
for element in elements_list:
    print(element.text)
    pass

# 根据属性值查找
elements_list = wd.find_elements(By.CSS_SELECTOR,'[href="http://www.miitbeian.gov.cn"]')
for element in elements_list:
    print(element.get_attribute('href'))

wd.quit()
