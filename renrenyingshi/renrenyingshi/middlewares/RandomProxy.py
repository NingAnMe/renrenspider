# coding:utf-8
import random
import base64
"""
这个类主要用于产生随机代理
"""
class RandomProxy(object):

    def __init__(self, http_proxy, user_pass):  # 初始化一下数据库连接
        self.http_proxy = http_proxy
        self.user_pass = user_pass
        self.proxy_auth = self.proxy_authorization(self.user_pass)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('HTTP_PROXY'),
                   crawler.settings.get('PROXY_USER_PASSWOED'))


    def process_request(self, request, spider):
        """
        在请求上添加代理
        :param request:
        :param spider:
        :return:
        """
        # 使用普通代理
        # p = random.choice(self.proxy_list)
        # proxy = r'http://%s:%s' %(p[0],p[1])
        # request.meta['proxy'] = proxy

        # 使用隧道代理
        proxy = "http://http-dyn.abuyun.com:9020"
        request.meta['proxy'] = proxy
        request.headers["Proxy-Authorization"] = self.proxy_auth

    def proxy_authorization(self, user_pass):
        """产生隧道代理的Proxy-Authorization
        """
        proxy_auth = 'Basic %s' % base64.b64encode(user_pass)
        return proxy_auth
