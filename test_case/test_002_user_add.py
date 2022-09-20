#用户列表-添加用户测试用例
#作者：张旭东
from config import conf
from utils.ScreenUtil import insert_img
from utils.readjsonUtil import ReadJson
from page_object.UserlistPage import User_Add_Page_Task,User_Add_Page_Locator
from utils.save_log import Logger
from selenium.common.exceptions import NoSuchElementException
from common.Base import init_db
import os
import pytest
import allure


#读取测试数据
test_file = os.path.join(conf.get_data_path(),"user_add.json")
data = ReadJson()
username = data.get_json_value("username",test_file)
password = data.get_json_value("password",test_file)
email = data.get_json_value("email",test_file)


@allure.suite("用户列表添加用户测试用例")
class Test_User_add(object):
    user_add = User_Add_Page_Task()
    def setup_class(self):
        pass
    def teardown_class(self):
        SQL = init_db('db_authority')
        sql = "DELETE FROM user WHERE username='test20220915'"
        SQL.exec(sql)
    @allure.story("正常添加用户")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_add(self):
        """正常添加用户"""
        Logger().info("user add success")
        try:
            self.user_add.user_add(username, password, email)
        except NoSuchElementException:
            Logger().error("user_add no find element")
        text = User_Add_Page_Locator().user_add_succee().text
        assert "添加用户成功" == text
        insert_img("user_add_normal.png")



if __name__ == '__main__':
    pytest.main(["-s","test_002_user_add.py"])