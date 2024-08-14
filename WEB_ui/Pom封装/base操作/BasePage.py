# selenium进行浏览器的操作
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


# pom的本质就是把重复的操作的提取出去
# 封装操作基础类，提供基础的driver操作
class BasePage(object):
    def __init__(self,browser):
        # self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = browser
        self.driver.set_window_size(1550, 1000)

    def get_url(self, url):
         self.driver.get(url)
    def quit_browser(self):
         self.driver.quit()

    def send_keys(self,selector, context ):
         self.driver.find_element(*selector).send_keys(context)

    def click(self,selector):
        self.driver.find_element(*selector).click()
