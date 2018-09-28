

import pymysql

try:
    #conn = pymysql.connect(host='localhost', port=3306, db='test1', user='root', passwd='mysql', charset='utf8')
    conn = pymysql.connect(host='127.0.0.1', port=3306, db='test1', user='root', passwd='mysql', charset='utf8')
    cs1 = conn.cursor()
    raw = cs1.execute('select * from students')
    print(raw)
    #table = cs1.fetchone()
    #fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
    #print(table)

    table = cs1.fetchall()
    cs1.close()
    conn.close()
    #执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
    for raw1 in table:
        print(raw1)

except Exception as e:
    print(e)