from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.get('https://www.byhy.net/cdn2/files/selenium/test4.html')
# alert
wd.find_element(By.CSS_SELECTOR,'#b1').click()
wd.switch_to.alert.accept()
pass

# confirm
wd.find_element(By.CSS_SELECTOR,'#b2').click()
wd.switch_to.alert.dismiss()
pass

# prompt
wd.find_element(By.CSS_SELECTOR,'#b3').click()
wd.switch_to.alert.send_keys('selenium')
wd.switch_to.alert.accept()
pass