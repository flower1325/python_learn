import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# 全局driver的声明，在session开始和结束时会被销
driver = None


# pytest的session scope保证在session开始和结束时执行fixture
@pytest.fixture(scope="session")
def browser():
    global driver
    if driver is  None:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
    yield driver
    # session结束时，关闭driver
    driver.quit()
