import urllib2
import ssl


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36"}

context = ssl._create_unverified_context()

# url = "https://www.12306.cn/mormweb"
# url = "https://www.baidu.com/"
url = "https://www.12306.cn/mormhweb"

request = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(request, context=context)

with open("12306.html", "w") as f:
    f.write(response.read())
# print response.read()
