'''
前提：依赖于登录接口
下订单的所有场景
step1:先调用登录接口
step2.下订单接口测试
宗旨:设计测试用例的时候，接口调用之间没有依赖关系的(降到最低)
举例：存在依赖关系的接口，登录接口失败了，并不会影响下订单接口
'''
import allure
import requests

from api.apiLogin import ApiLogin
from api.apiOrder import ApiOrder


class TestOrder:
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 创建order对象
        self.order_obj = ApiOrder()
        # 调用成功的登录接口
        ApiLogin().login_success(self.session)

    @allure.title('下订单的测试用例')
    @allure.feature('下订单功能')
    def test_order(self):
        '''
        测试用例
        :return:
        '''
        resp_order = self.order_obj.order(self.session)
        # 断言
        assert resp_order.json().get('msg') == '提交成功'
