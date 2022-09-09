#封装日志方法
#作者：张旭东
import logging
from logging import handlers

#封装日志的类
class Logger(object):
    lever_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'critical':logging.CRITICAL
    }

    def __init__(self,fp='F:\\Auto_Webtest\\log\\test.log',level='debug'):
        #创建日志等级
        self.lever = self.lever_relations.get(level)
        #创建一个logger
        self.logger = logging.getLogger(fp)
        #设置日志级别
        self.logger.setLevel(self.lever)
        #定义日志的输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        th = handlers.TimedRotatingFileHandler(fp)
        th.setFormatter(formatter)
        th.setLevel(self.lever)
        #添加一个handler处理者,用于写入日志文件
        self.logger.addHandler(th)

    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warning(self,msg):
        self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    log = Logger('abc.log','debug')
    log.info('info')
    log.critical('critical')