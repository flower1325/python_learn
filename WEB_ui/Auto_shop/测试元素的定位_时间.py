from  config.browser_driver import Browser_drivcer
from  selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as ec

driver = Browser_drivcer().deriver_init()
driver.get("https://layui.dev/docs/2/laydate/")

# 点击开始时间
wait = WebDriverWait(driver,10)
located = (By.XPATH,'//input[@id="ID-laydate-demo"]')
wait.until(ec.visibility_of_element_located(located)).send_keys("2024-06-28")
sleep(30)
