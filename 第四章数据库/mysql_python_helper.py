
from mysql_helper import MysqlHelper

Help = MysqlHelper('localhost', 3306, 'test1', 'root', 'mysql', 'utf8')
print("-------")
Help.fetchone('select * from students')
#Help.insert('insert into students values(%s,%s,%s,%s,%s)',[0,'南帝','1990-10-1',1,1])
print('22222')
Help.fetchall('select * from students')