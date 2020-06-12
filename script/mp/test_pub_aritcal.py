import pytest

from config import BASE_ARITCAL_TITLE
from page.mp.home_page import HomePorxy
from page.mp.pubilsh_page import PubPorxy
from utils import DriverUtils, element_is_exist


@pytest.mark.run(order=3)
class TestPubAeitical:
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.home_proxy = HomePorxy()
        self.pub_proxy = PubPorxy()

    def teardown_class(self):
        DriverUtils.quit_mp_driver()

    def test_pub_aritical(self):
        title = BASE_ARITCAL_TITLE
        content = "可是今天还要上课啊！！！！"
        option = "数码产品"
        self.home_proxy.to_publish_page()
        self.pub_proxy.test_pub_aritcal(title, content, option)
        is_suc = element_is_exist(self.driver, text="新增文章成功")
        assert is_suc
