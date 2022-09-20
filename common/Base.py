from config.conf import ConfigYaml
from utils.mysqlUtil import Mysql

def init_db(db_alias):
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host=db_info["db_host"]
    user=db_info["db_user"]
    password=db_info["db_password"]
    db_name=db_info["db_name"]
    db_charset=db_info["db_charset"]
    port=int(db_info["db_port"])
    #初始化mysql对象
    conn = Mysql(host,user,password,db_name,db_charset,port)
    return conn


