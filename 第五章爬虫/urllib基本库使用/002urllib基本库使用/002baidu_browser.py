import urllib2
import urllib

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36"}
url = "http://www.baidu.com/s"
keyword = raw_input("pleas input keywords")
wd = {"kw": keyword}

kw = urllib.urlencode(wd)
# print kw
fullurl = url + '?'+ kw

request = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(request)

print response.read()


