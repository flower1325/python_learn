from selenium.webdriver.common.by import By


class LoginPage_base:

    shop_user = (By.XPATH, "//input[@name='accounts']")
    shop_pass = (By.XPATH, "/input[@name='pwd']")
    shop_loginbtn = (By.XPATH, "//button[@type='submit']")
    shop_logoutbtn = (By.XPATH, "//div[@class='m-baseinfo']//a[@class='member-logout']")

    # 写这个页面的操作:登录/退出
    def do_login(self, username, password):
        self.sendkeys(self.shop_user, username)
        self.sendkeys(self.shop_pass, password)
        self.click(self.shop_loginbtn)

    def logout(self):
        self.click(self.shop_logoutbtn)


