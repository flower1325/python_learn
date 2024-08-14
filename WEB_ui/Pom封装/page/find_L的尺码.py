from selenium import webdriver
from selenium.webdriver.common.by import By


class FindSize:
    def __init__(self):
        self.driver = webdriver.Chrome()  # 初始化 WebDriver 实例

    def find_element_by_size(self, size):
        # 找到包含尺码信息的 div
        size_divs = self.driver.find_elements(By.XPATH, '//div[@class="theme-options sku-items"]')

        for size_div in size_divs:
            # 找到 div 内的 li 元素，这些元素包含尺码信息
            size_elements = size_div.find_elements(By.XPATH, './/li')

            for size_element in size_elements:
                # 检查每个 li 元素的 data-value 属性是否为 "L"
                if size_element.get_attribute('data-value') == size:
                    # 获取元素的 XPath
                    xpath = self.get_xpath(size_element)
                    print(xpath)  # 在此处打印出 XPath
                    return xpath
        return None  # 如果未找到返回 None

    def get_xpath(self, element):
        # 递归构建元素的 XPath
        components = []
        child = element
        while child.tag_name != "html":
            parent = child.find_element(By.XPATH, "..")
            siblings = parent.find_elements(By.XPATH, child.tag_name)
            if len(siblings) > 1:
                count = 1
                for sibling in siblings:
                    if sibling == child:
                        break
                    count += 1
                components.append(f"{child.tag_name}[{count}]")
            else:
                components.append(child.tag_name)
            child = parent
        components.reverse()
        return "/" + "/".join(components)

    def test_find_element(self):
        # 打开网页
        self.driver.get('http://shop-xo.hctestedu.com/index.php?s=/index/goods/index/id/11.html')

        # 查找尺码为 'L' 的元素
        self.find_element_by_size('L')


# 使用 FindSize 类进行测试
if __name__ == "__main__":
    finder = FindSize()
    finder.test_find_element()
