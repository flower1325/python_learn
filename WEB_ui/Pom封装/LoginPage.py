from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.browser_driver import Browser_drivcer
class Login:
    def do_login(self):
        # # 初始化浏览器驱动
        driver = Browser_drivcer().deriver_init()
        # 打开网页
        driver.get("http://shop-xo.hctestedu.com/")

        # 等待登录链接元素加载，并点击登录链接
        login_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='member-login']//a[@class='am-btn-primary btn am-fl']")))
        login_link.click()

        # 等待用户名输入框加载，并输入用户名
        driver.find_element(By.NAME, "accounts").send_keys("huace_tester")

        # 等待密码输入框加载，并输入密码
        driver.find_element(By.NAME, "pwd").send_keys("huace_tester")

        # 等待登录按钮加载，并点击登录按钮
        # 使用XPath定位登录按钮
        login_button = driver.find_element(By.XPATH,  "//div[@class='am-form-group am-form-group-refreshing am-margin-top-lg']//button[@type='submit']")
        login_button.click()
        time.sleep(15)

