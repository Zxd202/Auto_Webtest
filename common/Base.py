from config.conf import ConfigYaml
from utils.EmailUtil import SendEmail
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

#发送邮件
def send_mail(report_html_path="",content="",title="测试"):
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path
    )
    email.send_mail()

