# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
# 选择浏览器
driver = webdriver.Chrome()
# driver = webdriver.Edge()

# 进入百度网站
driver.get('https://www.baidu.com')
# 通过find_element定位输入框
driver.find_element(By.ID,'kw').send_keys('哔站')

from time import sleep
sleep(30)
# 关闭浏览器
driver.quit()

