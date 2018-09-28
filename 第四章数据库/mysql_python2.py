

import pymysql

try:
    conn = pymysql.connect(host='localhost', port=3306, user='root', db='test1', passwd='mysql', charset='utf8')
    cs1 = conn.cursor()
    user = input('请输入姓名')
    udate = input('请输入出生年月日')
    ugender = input('请输入性别')
    sql= 'update students set name=%s,birthday=%s,gender=%s where id=%s'
    params = [user, udate, int(ugender), 5]
    op = cs1.execute(sql, params)
    conn.commit()
    cs1.close()
    conn.close()
    print('done')

except Exception as e:
    print(e)