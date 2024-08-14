from  config.browser_driver import Browser_drivcer
from  selenium.webdriver.common.by import By
from  selenium.webdriver import ActionChains
from  selenium.webdriver.support.ui import WebDriverWait
from time import sleep



driver = Browser_drivcer().deriver_init()
driver.get("https://layui.dev/docs/2/laydate/")
# 点击开始时间
wait = WebDriverWait(driver,10)

driver.set_window_position(1900,200)
driver.set_window_size(1550,1000)

# 年份的时间选择器
ul = driver.find_element(By.ID,"layui-laydate60")
ActionChains(driver).scroll_to_element(ul).perform()

year_locator = (By.XPATH,"//span[@lay-type='year']")
sleep(3)

driver.find_element(*year_locator).click()
sleep(2)

year_option_locator = (By.XPATH,"//li[@lay-ym='2031']")
sleep(2)

driver.find_element(*year_option_locator).click()







# 小时的时间选择器
#
# ul = driver.find_element(By.ID,"layui-laydate61")
# # 操作鼠标
# ActionChains(driver).scroll_to_element(hour_elements).perform()
#
# # 查找包含 "时" 的 li 元素
# hour_list = driver.find_element(By.XPATH, "//li[p='时']/ol")
#
# # 查找所有小时的 li 元素
# hour_elements = hour_list.find_elements(By.XPATH, "./li")
#
# # 打印所有小时
# for hour in hour_elements:
#     print(hour.text)
#
# # 选择当前选中的小时
#
#
#
# # 暂停30秒以观察结果
# sleep(30)
# print(f'selected_hour', {selected_hour})
#
#
#

