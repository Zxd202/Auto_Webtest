'''
用于创建目录，存放文件（截图）
'''
import os
from utils.mydate import currentDate,currentTime

#截图路径
def createDir():
    #获取当前路径
    filedir=os.path.abspath(__file__)
    #返回上一级路径
    currentpath=os.path.dirname(filedir)
    #返回上一级路径
    currentpath1 = os.path.dirname(currentpath)
    #拼接
    filepath=currentpath1+'/report/screenshot/'
    mydate = currentDate()
    datedir = os.path.join(filepath,mydate)
    datedir1=datedir.replace('\\','/')
    #创建第一层目录
    if not os.path.exists(datedir1):
        os.mkdir(datedir1)

    #创建第二层的目录
    now = currentTime()
    timedir=os.path.join(datedir1,now)
    timedir1=timedir.replace('\\','/')
    if not os.path.exists(timedir1):
        os.mkdir(timedir1)


if __name__ == '__main__':
    createDir()