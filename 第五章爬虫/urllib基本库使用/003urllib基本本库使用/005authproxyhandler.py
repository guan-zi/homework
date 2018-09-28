# -*- coding=utf-8 -*-

import urllib2
import os

# 获取系统环境变量的授权代理的账户和密码

proxyuser = os.environ.get("proxyuser")
proxypasswd = os.environ.get("proxypasswd")

# 授权的代理账户密码拼接

authproxy_handler = urllib2.ProxyHandler({"http": proxyuser+":"+proxypasswd+"@114.215.104.49:16816"})

opener = urllib2.build_opener(authproxy_handler)

request = urllib2.Request("http://www.baidu.com")

response = opener.open(request)
print response.read()

