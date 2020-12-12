import allure
import requests
from api.apiLogin import ApiLogin
from api.apiOrder import ApiOrder
from api.apiPay import ApiPay

class TestPay:
    def setup_class(self):
        # 获取session对象
        self.session = requests.session()
        # 调用成功的登录接口
        ApiLogin().login_success(self.session)
        # 调用下订单接口
        ApiOrder().order(self.session)
        # 创建支付对象
        self.pay_obj = ApiPay()

    @allure.title('支付成功的测试用例')
    @allure.feature('支付成功功能')
    def test_pay(self):
        '''
        测试用例
        :return:
        '''
        resp_pay = self.pay_obj.pay(self.session)
        # 断言
        assert '支付成功' in resp_pay.text
