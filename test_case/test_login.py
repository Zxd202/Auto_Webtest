import pytest
from page_object.LoginPage import *
from selenium.common.exceptions import NoSuchElementException
from utils.save_log import *
import allure
import sys

sys.path.append(r"F:\Auto_Webtest")

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

    def test_login1_normal(self):
        """username and passwd is normal"""
        Logger().info('test_login success')
        try:
            self.loginpage.login('admin', '123456')
        except NoSuchElementException:
            Logger().error('login no find element')
        #self.assertEqual(po.type_loginPass_hint(),'zhangxudong222')
        #function.insert_img(self.driver,"sx_login_normal.jpg")


if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])









