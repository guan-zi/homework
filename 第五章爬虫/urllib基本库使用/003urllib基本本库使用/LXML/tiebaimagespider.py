# usr/bin/env python3
# -*- coding=utf-8 -*-

import urllib.request
import urllib.parse


if __name__ == '__main__':
    kw = input("请输入要爬取的贴吧：")
    kw = urllib.parse.urlencode({"kw": kw})
    bg_pg = int(input("请输入"))