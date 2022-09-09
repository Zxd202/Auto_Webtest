#登录测试用例
#作者：张旭东
from selenium.common.exceptions import NoSuchElementException
from utils.save_log import *
from utils.Driverunit import Driver
from page_object.LoginPage import Login_Page_Task
from utils.ScreenUtil import insert_img
from utils.readjsonUtil import ReadJson
import allure
import pytest
import os
from config import conf

#测试数据文件路径
test_file = os.path.join(conf.get_data_path(),"login_data.json")
data = ReadJson()
username = data.get_json_value("username",test_file)
password = data.get_json_value("password",test_file)

@allure.suite("登录测试用例")
@allure.feature("登录一级用例")
class Test_Login(object):
    def setup_class(self):
        self.driver = Driver.get_driver()
        self.loginpage = Login_Page_Task()
    def teardown_class(self):
        Driver.quit_driver()

    def setUp(self):
        self.driver.get('http://43.138.61.199:8899/#/login')
    def tearDown(self):
        pass

    @allure.story("登录用例")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login1_normal(self):
        """username and passwd is normal"""
        Logger().info('test_login success')
        try:
            self.loginpage.login(username, password)
        except NoSuchElementException:
            Logger().error('login no find element')
        assert username == "admin"
        insert_img("login_normal.png")

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])









