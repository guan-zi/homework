import random
import base64

from settings import USER_AGENTS
from settings import PROXIES

class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent',useragent)


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        
        if proxy['user_passwd'] is None:
            request.meta['proxy'] = 'http://' + proxy['ip_port']

        else:
            base64_userpasswd = base64.bs64encode(proxy['user_passwd'])
            request.headers['Proxy-Authorization'] = 'Basic' + base64_userpasswd
            request.meta['proxy'] = 'http://' + proxy['ip_port']
