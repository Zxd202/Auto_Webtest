#该文件作用：封装的数据库工具类
#作者 : 张旭东
import pymysql
from utils.save_log import Logger

#封装数据库工具类
class Mysql:
    def __init__(self,host,user,passwd,database,charset="utf8",port=3306):
        self.log = Logger()
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            database=database,
            charset=charset
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    #创建查询（单个查询，多个查询），执行的方法
    def fetchone(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    def fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self,sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                #提交修改，因为pymysql 模块默认是启用事务的，sql语句 如果不提交 相当于没有执行
                self.conn.commit()
        except Exception as ex:
            #当执行错误时数据库进行回滚
            self.conn.rollback()
            self.log.error("mysql 执行失败")
            self.log.error(ex)
            return False
        return True

    #关闭链接数据库对象，关闭光标对象
    def __del__(self):
        if self.conn is not None:
            self.conn.close()
        if self.cursor is not None:
            self.cursor.close()


if __name__ == '__main__':
    mysql = Mysql(
        "43.138.61.199",
        "root",
        "123456",
        "authority",
        charset="utf8",
        port=9506
    )
    res = mysql.fetchone("SELECT * FROM `user` WHERE username='admin'")
    #res = mysql.exec("update policy_info set State='4' where PolicyCode='222'")
    print(res)

