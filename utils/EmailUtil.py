import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os


#发送邮件报告
def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver='smtp.qq.com'
    user='892927017@qq.com'
    password='mvwetpykwlejbdge'

    sender='892927017@qq.com'
    receives='zxd_20210330@163.com'

    subject='web selenium 自动化测试报告'

    msg = MIMEText(mail_content,'html','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)

    smtp.sendmail(sender,receives,msg.as_string())
    smtp.quit()

#查找最新报告
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    file = os.path.join(report_dir, lists[-1])
    return file