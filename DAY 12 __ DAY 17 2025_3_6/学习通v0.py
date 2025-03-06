from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# 生成一个驱动对象
wd = webdriver.Edge()
# 发起命令，打开指定网址
wd.get('https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com')

# 模拟输入间隔
def send_keys(num):
    keys = list(f'{num}')
    for key in keys:
        element_user.send_keys(key)
        time.sleep(random.random() / 2)

# 寻找元素是否存在并返回布尔值
def check_element_presence(driver, by, value, timeout=0.1):

    try:
        WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located((by, value)))
        return True
    except:
        return False

# 时间计算
def time_caculator(time_str):
    parts = time_str.split(':')
    if len(parts) == 3:
        dt = datetime.strptime(time_str,'%H:%M:%S')
        return dt.hour * 3600 + dt.minute * 60 + dt.second
    if len(parts) == 2:
        dt = datetime.strptime(time_str,'%M:%S')
        return dt.minute * 60 + dt.second

# 等待元素出现
wd.implicitly_wait(10)
# 用户名
for _ in range(2):
    element_user = wd.find_element(By.ID,'phone')
    send_keys('请输入账号')
    pass
# 密码及登录
    element_user = wd.find_element(By.ID,'pwd')
    send_keys('请输入密码')
    pass
# 确认登录
    load_in = wd.find_element(By.ID,'loginBtn')
    load_in.click()
    time.sleep(random.randrange(1,5))
pass
# 选择课程
# 切换至iframe
wd.switch_to.frame('frame_content')
# 生成正在进行的网课的列表
courses_selenium = wd.find_elements(By.CSS_SELECTOR,'#courseList > #stuNormalCourseListDiv  div.course-info a')
courses_dict = {course.text:course.get_attribute('href') for course in courses_selenium for course in courses_selenium}

pass
wd.switch_to.default_content()
# 要刷的网课
aim_course = '毛概（新版）'
# 切换至网课界面
for course_name,course_web in courses_dict.items():
    if course_name == aim_course:
        wd.get(courses_dict[aim_course])
        break
time.sleep(random.random())
pass
# 章节选择
chapter = wd.find_element(By.CSS_SELECTOR,'#boxscrollleft > div > ul > li:nth-child(4) > a')
chapter.click()
time.sleep(random.randrange(2,5)) # 模拟人工选择
pass
# 待完成的章节
# 切换至iframe
wd.switch_to.frame('frame_content-zj')
to_be_completed = wd.find_element(By.XPATH,'//*[@class="catalog_points_yi"]/ancestor::div[4]')
to_be_completed.click()
wd.switch_to.default_content()

# 开始播放
wd.switch_to.frame('iframe')
wd.switch_to.frame(wd.find_element(By.TAG_NAME,'iframe'))
wd.find_element(By.CSS_SELECTOR,'#ext-gen1049 > div.main.clearfix > div.prev_video_left > div.sp_function > div.writeNote_vid.fr > div > div > div.writeNote_vid_bnt > a').click()
wd.find_element(By.XPATH,'//*[@id="video"]/button').click()
time.sleep(1)

pass
# 这里留个坑位给倍速选择
# 由于进入页面时“写笔记”弹窗会遮挡“倍速”键，而此弹窗在frame之外，处理较为麻烦
# 使用 JavaScript 点击可以绕过遮挡，直接触发点击事件，但容易被反爬机制监测
# 既然是自动化，那不倍速也还能接受
# 以后有合理方法再更新

# 屏幕监测：未知时刻的答题弹窗,当视频开始时开始监测，视频播放完成停止监测
# 获取总时长
total_time = time_caculator(wd.find_element(By.CSS_SELECTOR,'#video > div.vjs-control-bar > div.vjs-duration.vjs-time-control.vjs-control > span.vjs-duration-display').text)
#获取当前时长
displayed_time = time_caculator(wd.find_element(By.CSS_SELECTOR,'#video > div.vjs-control-bar > div.vjs-current-time.vjs-time-control.vjs-control > span.vjs-current-time-display').text)

pass

while  True:
    while displayed_time < total_time:
        while True and displayed_time < total_time:
            try:
                popup = WebDriverWait(wd,30).until(
                    expected_conditions.presence_of_element_located((By.CLASS_NAME,"tkTopic_title")))
                break
            except:
                time.sleep(random.random())
                displayed_time = time_caculator(wd.find_element(By.CSS_SELECTOR,'#video > div.vjs-control-bar > div.vjs-current-time.vjs-time-control.vjs-control > span.vjs-current-time-display').text)
                if displayed_time == None:
                    displayed_time = 0
                else:continue

        # 答题逻辑
        if displayed_time < total_time:
            is_answer = True
            # 确定题目类型
            quiz_type = wd.find_element(By.CLASS_NAME,'tkTopic_title').text
            # 获取选项
            opt = wd.find_elements(By.CLASS_NAME,'tkRadio')
            # 提交
            submit = wd.find_element(By.CSS_SELECTOR,'#videoquiz-submit')
            if quiz_type in  ['单选题','判断题']:
                for element in opt:
                    actions = ActionChains(wd)
                    actions.move_to_element_with_offset(element, random.randint(-3, 3), random.randint(-3, 3))
                    time.sleep(random.uniform(2, 3))
                    actions.click().perform()
                    pass
                    actions.move_to_element_with_offset(submit, random.randint(-3, 3), random.randint(-3, 3))
                    time.sleep(random.uniform(2, 3))
                    actions.click().perform()
                    time.sleep(random.random())
                    is_answer = check_element_presence(wd,By.CSS_SELECTOR,'#spanNot')
                    '''元素不存在，说明回答正确'''
                    if not is_answer:
                        break
                    else:time.sleep(random.uniform(1,2))
                    pass
            elif quiz_type == '多选题':
            # 选项集合
                answer2 = set()
                answer3 = set()
            # 若多选题有两个答案，则总答案组数为6
                while len(answer2) < 6:
                    answer2.add(tuple(random.sample(opt,2)))
                while len(answer3) < 4:
                    answer3.add(tuple(random.sample(opt, 3)))
                answers = answer2 | answer3
                sort = 0
                for _ in list(answers):
                    item = list(answers)[sort]
                    for the_item in item:
                        the_item.click()
                    submit.click()
                    is_answer = check_element_presence(wd, By.CSS_SELECTOR, '#spanNot')
                    if not is_answer: # 回答正确
                        break
                    else: # 回答错误，继续循环
                        '''清空选项'''
                        for the_item in item:
                            the_item.click()
                        sort += 1
                        time.sleep(random.random())
    pass
    # 自动切换课程
    wd.switch_to.default_content()
    try:
        to_be_completed = wd.find_element(By.XPATH, '//*[@class="catalog_points_yi prevTips"]/..')
        to_be_completed.click()
    except NoSuchElementException:
        print("无待完成任务")
    time.sleep(random.random())
    wd.switch_to.frame('iframe')
    wd.switch_to.frame(wd.find_element(By.TAG_NAME, 'iframe'))
    wd.find_element(By.XPATH, '//*[@id="video"]/button').click()
    time.sleep(1)
    total_time = time_caculator(wd.find_element(By.CSS_SELECTOR,
                                                '#video > div.vjs-control-bar > div.vjs-duration.vjs-time-control.vjs-control > span.vjs-duration-display').text)
    displayed_time = 0
