from selenium.webdriver.common.by import By

from Pom封装.base操作.BasePage import BasePage


class IndexPage(BasePage):

    index_btn = (By.XPATH, "//a[@title='首页']")
    shop_image = (By.XPATH, "//img[@alt='夏季复古ins风格网红SP同款 短袖大圆领香槟色蕾丝绣花钉珠连衣裙']")
    goods_size = (By.XPATH, "//ul[@xpath='1']/li[@data-value='M']")
    shop_car = (By.XPATH, "//button[@title='加入购物车']")


    def add_shop_car(self):
        self.click(self.shop_image)
        self.click(self.goods_size)
        self.click(self.shop_car)

    def index_click(self):
        self.click(self.index_btn)




