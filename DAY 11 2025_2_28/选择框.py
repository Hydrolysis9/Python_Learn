from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.get('https://www.byhy.net/cdn2/files/selenium/test2.html')

# radio选择框
teacher_choose = wd.find_element(By.CSS_SELECTOR,'#s_radio > input[type=radio]:nth-child(3)')
teacher_choose.click()
print('现在选中的是' + teacher_choose.get_attribute('value'))

# checkbox选择框
teachers_choose = wd.find_elements(By.CSS_SELECTOR,'#s_checkbox input[checked = "checked"]')
for teacher in teachers_choose:
    teacher.click()
wd.find_element(By.CSS_SELECTOR,'#s_checkbox > input[type=checkbox]:nth-child(3)').click()
pass

# select选择框
from selenium.webdriver.support.ui import Select
select = Select(wd.find_element(By.ID,'ss_multi'))
pass

select.deselect_all()
select.select_by_visible_text('小雷老师')
select.select_by_visible_text('小凯老师')
pass