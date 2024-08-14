from time import sleep

from lxml import etree
from selenium.webdriver.common.by import By

from Pom封装.base操作.BasePage import BasePage


class LoginPage_base2(BasePage):  # 继承
    html_content = '''
        <ul>
            <li class="sku-line  sku-line-images" data-type-value="尺码" data-value="M" data-type-images="http://shop-xo.hctestedu.com/static/upload/images/goods/2019/01/14/1547455907486857.jpg">
                <img src="http://shop-xo.hctestedu.com/static/upload/images/goods/2019/01/14/1547455907486857.jpg">
                M<i></i>
            </li>
            <li class="sku-line  sku-line-images" data-type-value="尺码" data-value="L" data-type-images="http://shop-xo.hctestedu.com/static/upload/images/goods/2019/01/14/1547455907256518.jpg">
                <img src="http://shop-xo.hctestedu.com/static/upload/images/goods/2019/01/14/1547455907256518.jpg">
                L<i></i>
            </li>
            <li class="sku-line  sku-line-images" data-type-value="尺码" data-value="XL" data-type-images="http://shop-xo.hctestedu.com/static/upload/images/goods/2019/01/14/1547455601528614.jpg">
                <img src="http://shop-xo.hctestedu.com/static/upload/images/goods/2019/01/14/1547455601528614.jpg">
                XL<i></i>
            </li>
        </ul>
    '''
    root = etree.HTML(html_content)

    shop_user = (By.XPATH, "//input[@name='accounts']")
    shop_pass = (By.XPATH, "//input[@name='pwd']")
    shop_loginbtn = (By.XPATH,"//div[@class='am-form-group am-form-group-refreshing am-margin-top-lg']//button[@type='submit']")
    # shop_logoutbtn = (By.XPATH, "//div[@class='m-baseinfo']//a[@class='member-logout']")
    shop_logoutbtn = (By.XPATH, "//div[@class='menu-hd']//a[contains(text(),'退出')]")

    index_btn = (By.XPATH, "//a[@title='首页']")
    shop_image = (By.XPATH, "//img[@alt='夏季复古ins风格网红SP同款 短袖大圆领香槟色蕾丝绣花钉珠连衣裙']")
    # goods_size = (By.XPATH, "")
    shop_car = (By.XPATH, "//button[@title='加入购物车']")

    # 写这个页面的操作:登录/退出
    def do_login(self, username, password):
        self.send_keys(self.shop_user, username)
        self.send_keys(self.shop_pass, password)
        self.click(self.shop_loginbtn)

    def index_click(self):
        self.click(self.index_btn)

    def add_shop_car(self):
        self.click(self.shop_image)
        sleep(15)
        # self.click(self.goods_size)
        # self.click(self.shop_car)

    def logout(self):
        self.click(self.shop_logoutbtn)


