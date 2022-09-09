#浏览器对象的方法
#作者：张旭东
from selenium import webdriver
from time import sleep
import os
from utils.parse_yml import ParseYML


current_path = os.path.realpath(__file__)
one_path = os.path.dirname(os.path.dirname(current_path))
yml_file = os.path.join(one_path,'config','conf.yml')
ip = ParseYML.parse_yml(yml_file,'ipaddress')
url = 'http://{}/'.format(ip)

class Driver(object):
    #浏览器对象变量初始化
    __driver = None
    #获取浏览器对象方法
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.option = webdriver.ChromeOptions()
            cls.option.add_argument("--window-size=1920,1050")
            # 无头模式
            cls.option.add_argument('headless')
            # 沙盒模式运行
            cls.option.add_argument('no-sandbox')
            # 大量渲染时候写入/tmp而非/dev/shm
            cls.option.add_argument('disable-dev-shm-usage')
            # 指定驱动路径
            cls.__driver = webdriver.Chrome(options=cls.option)
            cls.__driver = webdriver.Chrome()
            cls.__driver.get(url)
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    #退出浏览器对象的方法
    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            sleep(3)
            cls.__driver.quit()

if __name__ == '__main__':
    Driver.get_driver()
    Driver.quit_driver()



