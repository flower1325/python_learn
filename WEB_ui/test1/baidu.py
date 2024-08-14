"""
打开浏览器
让浏览器打开页面
操作页面
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(30)
driver.quit()
"""




# 进阶版：
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://www.baidu.com')
from time import sleep
sleep(30)
"""

from config.browser_driver import Browser_drivcer
from selenium.webdriver.common.by import By
from time   import sleep

driver = Browser_drivcer.deriver_init()
driver.get('http://www.baidu.com')
driver.find_element(By.ID,"kw").send_keys("哔站")
driver.find_element(By.ID,"su").click()
sleep(10)
