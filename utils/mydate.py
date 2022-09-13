#获取当前时间
#作者：张旭东
from datetime import datetime


#获取当前时间的方法
def now_time():
    curr_time = datetime.now()
    today = (curr_time.strftime("%Y-%m-%d %H:%M:%S"))
    return today
