
import pymysql

class MysqlHelper(object):

    def __init__(self, host, port, db, user, passwd, charset):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset)

    def update(self, sql, params):
        return self.__cur(sql, params)

    def insert(self, sql, params):
        return self.__cur(sql, params)

    def delete(self, sql, params):
        return self.__cur(sql, params)

    def __cur(self, sql, params):
        cs = self.conn.cursor()
        try:
            cs.execute(sql, params)
            self.conn.commit()
            cs.close()
            self.conn.close()
            print('done')
        except Exception as e:
            print(e)
            self.conn.rollback()

    def fetchall(self, sql, params=[]):
        cs = self.conn.cursor()
        try:
            cs.execute(sql,params)
            raw = cs.fetchall()
            cs.close()
            self.conn.close()
            print(raw)
            #return raw
            for element in raw:
                print(element)

        except Exception as e:
            print(e)

    def fetchone(self, sql, params=[]):
        cs = self.conn.cursor()
        try:
            cs.execute(sql,params)
            raw = cs.fetchone()
            cs.close()
            self.conn.close()
            print(raw)
            print('done')

            return raw
            #for element in raw:
            #    print(element)

        except Exception as e:
            print(e)

#help = MysqlHelper('localhost', 3306, 'test1', 'root', 'mysql', 'utf8')
#help.fetchone('select * from students')
