# -*- coding=utf-8 -*-

import urllib
import urllib2

url ="http://www.renren.com/966909627/profile"
headers = {
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "anonymid=jjjh4exx-xim7ec; depovince=GW; _r01_=1; ick_login=ee409cc1-4bc9-4ccb-86f6-4e1dfb0edc00; __utma=151146938.507282392.1531455634.1531455634.1531455634.1; __utmc=151146938; __utmz=151146938.1531455634.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ick=a76012ac-6eeb-4cd4-926f-d3d7fdc62d9b; __utmb=151146938.3.10.1531455634; jebecookies=17304011-38c8-4357-9f83-7d0a2776d79c|||||; _de=78040E07E1774B5CD57018AC73E28DA1; p=a721c4a186b3290ab26e5bc62557992a7; first_login_flag=1; ln_uact=15274782328; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=cebcc232e976e8899a89ee42ca5d0e817; societyguester=cebcc232e976e8899a89ee42ca5d0e817; id=966909627; xnsid=6e19754e; loginfrom=syshome; jebe_key=82fb750e-cc4b-440a-a718-3c3d5ee0ba56%7Cd51bdfbd32525f8984d76f470d8c2751%7C1531456176569%7C1%7C1531456181381; wp_fold=0; XNESSESSIONID=7549c807e971; BAIDU_SSP_lcr=https://www.baidu.com/link?url=aivJ4luwg7jwimUltklA7AOwa-ZICZxdp6zYp3JlkXa&wd=&eqid=f894cf3b000051d7000000065b482870",
    # "Host": "www.renren.com",
    "Referer": "http://zhibo.renren.com/top",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

request = urllib2.Request(url, headers=headers)

print urllib2.urlopen(request).read()

