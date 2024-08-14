
from config.browser_driver import Browser_drivcer
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from  Pom封装.LoginPage import Login
class dl(object):
    def 登录test_001(self):
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
        login_button = driver.find_element(By.XPATH,"//div[@class='am-form-group am-form-group-refreshing am-margin-top-lg']//button[@type='submit']")
        login_button.click()
        time.sleep(15)

        # 点击首页
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='doc-topbar-collapse']/ul[@class='am-nav am-nav-pills am-topbar-nav']")))
        driver.find_element(By.XPATH, "//a[@title='首页']").click()

        #  查询输入框
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='floor1']/div[@class='am-g am-g-fixed floor']/div[@class='am-u-sm-3 aggregation']/div[@class='word']")))
        man_sheet = driver.find_element(By.XPATH,"//a[contains(text(), '男装')]")
        man_sheet.click()

        # # 等待搜索按钮加载，并点击搜索按钮
        # search_button = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//button[@id='ai-topsearch']/span[.='搜索']")))
        # search_button.click()


        login_quit = driver.find_element(By.XPATH,"//div[@class='m-baseinfo']//a[@class='member-logout']")
        login_quit.click()
        time.sleep(15)

if __name__ == "__main__":
    dl().登录test_001()

