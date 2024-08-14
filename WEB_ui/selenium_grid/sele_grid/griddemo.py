from selenium import webdriver
import selenium.webdriver.chrome.options as chrome_options

# 创建 ChromeOptions 对象
options = chrome_options.Options()

# 配置浏览器参数（可选）
# options.add_argument('headless')  # 无头模式
# options.add_argument('window-size=1920x1080')  # 设置窗口大小

# 创建 WebDriver 实例
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444',
    options=options
)

# 访问网站
driver.get('https://www.baidu.com')

# 执行其他操作...

# 关闭浏览器
driver.quit()


