#用户列表-添加用户测试用例
#作者：张旭东
from config import conf
from page_object.LoginPage import Login_Page_Task
from utils.ScreenUtil import insert_img
from utils.readjsonUtil import ReadJson
from page_object.UserlistPage import User_Add_Page_Task
from utils.Driverunit import Driver
from utils.save_log import Logger
from selenium.common.exceptions import NoSuchElementException
import os
import pytest


#读取测试数据
test_file = os.path.join(conf.get_data_path(),"user_add.json")
data = ReadJson()
username = data.get_json_value("username",test_file)
password = data.get_json_value("password",test_file)
email = data.get_json_value("email",test_file)

#用户列表添加用户测试用例
class Test_User_add(object):
    def setup_class(self):
        self.driver = Driver.get_driver()
        self.user_add = User_Add_Page_Task()
        self.login = Login_Page_Task()
        self.login.login("admin","123456")
    def teardown_class(self):
        Driver.quit_driver()
    def test_user_add(self):
        """正常添加用户"""
        Logger().info("user add success")
        try:
            self.user_add.user_add(username, password, email)
        except NoSuchElementException:
            Logger().error("user_add no find element")
        #assert
        insert_img("user_add_normal.png")



if __name__ == '__main__':
    pytest.main(["-s","test_001_user_add.py"])