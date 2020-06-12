"""
文章发布页面
"""
import time

from selenium.webdriver.common.by import By
from dase.mp.base_page import BasePage, BaseHandle
from utils import DriverUtils, select_option


# 对象库层


class PulPage(BasePage):
    # 定义初始化方法
    def __init__(self):
        super().__init__()
        # 文章标题
        self.title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # frame元素
        self.frame = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 文章内容
        self.aritcal_content = (By.CSS_SELECTOR, "body")
        # 封面元素
        self.aritcal_cover = (By.XPATH, "//*[text()='自动']")
        # 下拉框
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 下拉框选项
        self.channel_option = (By.XPATH, "//*[text()='区块链']")
        # 发表
        self.publish_btn = (By.XPATH, "//*[text()='发表']")

    # 定义找到所有元素实例方法
    def find_title(self):
        return self.find_elt(self.title)

    def find_frame(self):
        return self.find_elt(self.frame)

    def find_artical_content(self):
        return self.find_elt(self.aritcal_content)

    def find_artical_cover(self):
        return self.find_elt(self.aritcal_cover)

    def find_channel(self):
        return self.find_elt(self.channel)

    def find_channel_option(self):
        return self.find_elt(self.channel_option)

    def find_publish_btn(self):
        return self.find_elt(self.publish_btn)


# 操作层
class PubHandle(BaseHandle):

    def __init__(self):
        self.pub_page = PulPage()
        self.driver = DriverUtils.get_mp_driver()

    # 输入文章标题
    def input_title(self, title):
        self.input_text(self.pub_page.find_title(), title)

    # 输入文章内容
    def input_content(self, content):
        # 切换iframe
        self.driver.switch_to.frame(self.pub_page.find_frame())
        self.input_text(self.pub_page.find_artical_content(), content)
        self.driver.switch_to.default_content()

    # 封面元素
    def check_cover(self):
        self.pub_page.find_artical_cover().click()

    def check_channel(self, option):
        # # 下拉框
        # self.pub_page.find_channel().click()
        # # 下拉框选项
        # self.pub_page.find_channel_option().click()
        select_option(self.driver, "请选择", option)

    # 发表
    def click_publish(self):
        self.pub_page.find_publish_btn().click()


# 业务层
class PubPorxy:
    def __init__(self):
        self.pub_handle = PubHandle()

    # 操作方法
    def test_pub_aritcal(self, title, content, option):
        self.pub_handle.input_title(title)
        self.pub_handle.input_content(content)
        self.pub_handle.check_cover()
        self.pub_handle.check_channel(option)
        time.sleep(3)
        self.pub_handle.click_publish()
