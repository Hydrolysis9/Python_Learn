from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

wd = webdriver.Edge()
wd.get('https://cn.bing.com/search?q=%E7%99%BD%E7%BE%BD%E9%BB%91%E6%9C%88&gs_lcrp=EgRlZGdlKgcIAxBFGMIDMgcIABBFGMIDMgcIARBFGMIDMgcIAhBFGMIDMgcIAxBFGMIDMgcIBBBFGMIDMgcIBRBFGMIDMgcIBhBFGMIDMgcIBxBFGMID0gELMzQwMzkzOWowajGoAgiwAgE&FORM=ANSPA1&PC=HCTS')

# 创建实例对象
ac = ActionChains(wd)

# 鼠标悬停
ac.move_to_element(wd.find_element(By.CSS_SELECTOR,'#b_results > li:nth-child(4) > div.b_imgcap_altitle.b_imgcap_nosc > div > div > div > a > img')).perform()
pass