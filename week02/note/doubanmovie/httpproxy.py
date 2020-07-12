# 从配置文件中读取两个设置项
# 设置到代理中
import base64
from urllib.parse import unquote,urlunparse
from urllib.request import getproxies,proxy_bypass,_parse_proxy

from scrapy.exceptions import NotConfigured
from scrapy.utils.httpobj import urlparse_cached
from scrapy.utils.python import to_bytes

class RandomHttpProxyMiddleware(HttpProxyMiddleware):
    def __init__(self,auth_encoding='utf-8',proxy_list = None):
        self.proxies = defaultdict(list)
        for proxy in proxy_list:
            parse = urlparse(proxy)
            self.proxies[parse.scheme].appende(proxy)
    
    @classmethod
    def from_crawler(cls,crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        auth_encoding = crawler.setting.get('HTTPPROXY_AUTH_ENCODING')
        return cls(auth_encoding)

    def _basic_auth_header(self,username,password):

    def _get_proxy(self,url,orig_type) :

    def process_request(self,request,spider):
        
    def _set_proxy(self,request,scheme):
        creds,proxy = self.proxies
        print(self.proxies)
        request.meta['proxy'] = proxy
        print(proxy)
        if creds:
            request.headers['Proxy-Authorization'] = b'Basic' + creds