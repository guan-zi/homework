# -*- coding=utf-8 -*-
# !usr/bin/env python

import pymysql

try:
    conn = pymysql.connect(host='localhost', port=3306, db='test1', user='root', passwd='mysql', charset='utf8')
    cs1 = conn.cursor()

    count = cs1.execute('insert into students values(0,"周博通","1960-01-01",1,0);')
    print(count)
    conn.commit()
    cs1.close()
    conn.close()

except Exception as e:
    print(e)


