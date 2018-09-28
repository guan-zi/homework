#-*- coding=utf-8 -*-
from mysqlhelper import *
from hashlib import sha1

try:
    uname = input('请输入用户名')
    upwd = input('请输入密码')

    s1 = sha1()
    s1.update(upwd.encode())
    upwd2 = s1.hexdigest()

    redis = RedisHelper()
    upwd3 = redis.get(uname)

    if upwd3 != None:
        if upwd2 == upwd3:
            print('ok')
        else:
            print('ok')

    else:
        mysql = mysqlhelper()
        sql = 'select upwd from users where uname=%s'
        params = [uname]
        result = mysql.fetchone(sql, params)

        if result == None:
            print('用户名不存在')
        elif result[0] == upwds:
            print('ok')
        else:
            print('密码错误')

except Exception as e:
    print(e)
