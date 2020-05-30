import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

#浏览器头--无头
ch_options = Options()
ch_options.add_argument("--headless")
driver = webdriver.Chrome(options=ch_options)

#服务大厅地址
url = "https://ehall.jlu.edu.cn/jlu_portal/index"
driver.get(url)

#登录问题判断
flag = driver.find_elements_by_xpath("//a[@href='/jlu_portal/login']")
if len(flag) == 1:
    driver.find_element_by_xpath("//a[@href='/jlu_portal/login']").click()
    driver.find_element_by_name("username").send_keys("#你的用户名")
    driver.find_element_by_name("password").send_keys("#你的邮箱")
    driver.find_element_by_name("login_submit").click()

time.sleep(2)

#登录完毕，点击”本科生健康填报“按钮
button_1 = driver.find_element_by_id("cont_one_1")
button_url = button_1.find_elements_by_xpath('li')
Atype = button_url[3].find_element_by_tag_name('a')
href = Atype.get_attribute('href')
driver.get(href)

time.sleep(2)

#点击我要填报
driver.find_element_by_class_name("guide_title_center")
driver.find_element_by_class_name("bt_2").click()

time.sleep(3)

#切换网页，填报按钮在另一个标签页
handles = driver.window_handles
driver.switch_to.window(handles[1])

checkbox = driver.find_element_by_id("V1_CTRL82").is_selected()
if checkbox == False:
    driver.find_element_by_id("V1_CTRL82").click()
    time.sleep(1)
    driver.find_element_by_class_name("command_button_content").click()
else:
    driver.find_element_by_class_name("command_button_content").click()

time.sleep(2)

#点击"好"
driver.find_element_by_xpath("//*[contains(text(),'好')]/../button ").click()



