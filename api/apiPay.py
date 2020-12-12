import setting

from tools.logger import GetLogger
logger = GetLogger().get_logger()

class ApiPay:
    def __init__(self):
        logger.info('开始获取pay的url地址')
        self.url = setting.JUMP_URL

    def pay(self,session):
        # 对302接口禁止重定向allow_redirects = False
        logger.info('发起pay请求，将重定向设置为不重定向')
        resp = session.get(self.url, allow_redirects = False)
        # 提取响应头的location,对location后面的地址发起请求，然后获取响应，以便testcase中做断言
        resp_pay = session.get(resp.headers['location'])
        return resp_pay

