import pytest
from Pom封装.page.LoginPage_base2 import LoginPage_base2
from Pom封装.page.IndexPage import IndexPage
from  time import sleep

"""
pytest整合页面的操作
"""
def test_01(browser):
    lp = LoginPage_base2(browser)
    lp.get_url("http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html")
    lp.do_login("huace_tester","huace_tester")
    lp.index_click()
    lp.add_shop_car()
    sleep(30)

def test_02():
    pass

def test_03(browser):
    index = IndexPage(browser)
    index.get_url("http://shop-xo.hctestedu.com/")
    # index.index_click()
    index.add_shop_car()
    sleep(30)

if __name__ == "__main__":
    pytest.main(["-v","-s"])