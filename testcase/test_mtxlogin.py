# 导包
import allure
import pytest
import requests

from api.apiLogin import ApiLogin
from tools.readData import ReadData
data_li = ReadData().get_yaml('login_data','test_login')
# data_li = ReadData().get_yaml1('test_login')
# print(data_li)

class TestLogin:
    # 在所有的测试用例之前做创建session，实例化登录接口对象  测试用例类不能有init方法->setup_class
    def setup_class(self):
        # 获取session对象
        self.session = requests.Session()
        # 实例化登录接口对象
        self.login_object = ApiLogin()

    @pytest.mark.parametrize('dic',data_li)
    @allure.title('登录的测试用例')
    @allure.feature('登录功能')
    @allure.story('登录的参数:正向和逆向')
    def test_login(self, dic):
        '''
        data_li是列表套字典的形式用这个测试用例里面的写法
        :param dic:
        :return:
        '''
       # 读取数据，进行构造data,然后发起请求
        data = {'accounts':dic['accounts'],'pwd':dic['pwd']}
        # requests基本库中的一些内容
        res = self.login_object.login(self.session,data).json()
        # 做断言，业务层
        assert res['msg'] == dic['exp']



