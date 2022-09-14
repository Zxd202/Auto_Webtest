#登录页面元素定位
#作者：张旭东
from selenium.webdriver.common.by import By
from utils.Driverunit import Driver
from time import sleep

class Login_Page_Locator(object):
    """登录页元素定位"""
    def __init__(self):
        self.driver = Driver.get_driver()
        self.username = (By.XPATH, '//input[@placeholder="请输入用户名"]')
        self.password = (By.XPATH, '//input[@placeholder="请输入密码"]')
        self.submit = (By.XPATH,'//span[text()="登录"]')
    def login_username(self):
        return self.driver.find_element(self.username[0],self.username[1])
    def login_password(self):
        return self.driver.find_element(self.password[0],self.password[1])
    def login_submit(self):
        return self.driver.find_element(self.submit[0],self.submit[1])

class Login_Page_Handle(object):
    """登录页操作"""
    def __init__(self):
        self.login_page_locator = Login_Page_Locator()
    def login_input_username(self, username):
        self.login_page_locator.login_username().clear()
        self.login_page_locator.login_username().send_keys(username)
    def login_input_password(self,password):
        self.login_page_locator.login_password().clear()
        self.login_page_locator.login_password().send_keys(password)
    def login_click_submit(self):
        self.login_page_locator.login_submit().click()

class Login_Page_Task(object):
    """登录页业务"""
    def __init__(self):
        self.login_handle = Login_Page_Handle()
    def login(self,username,password):
        self.login_handle.login_input_username(username)
        sleep(2)
        self.login_handle.login_input_password(password)
        sleep(2)
        self.login_handle.login_click_submit()
        sleep(2)







