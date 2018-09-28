import urllib.request

url = 'http://www.baidu.com'
ua_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 \
    Chrome/65.0.3325.181 Safari/537.36'}

request = urllib.request.request(url, headers=ua_headers)
response = urllib.request.urlopen(request)

html = response.read()

print(response.getcode())
