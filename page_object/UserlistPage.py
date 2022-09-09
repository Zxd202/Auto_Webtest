#用户列表相关元素定位
#作者：张旭东
from selenium.webdriver.common.by import By
from utils.Driverunit import Driver
from time import sleep


class User_Page_Locator(object):
    def __init__(self):
        self.driver = Driver.get_driver()
        #添加用户按钮元素定位
        self.add_user_button = (By.XPATH,"//span[text()='添加用户']")
        #用户名输入框元素定位
        self.new_user_input = (By.XPATH,"//*[@id='app']/section/section/main/div/div[3]/div/div[2]/form/div[1]/div/div[1]/input")
        #密码输入框元素定位
        self.password_input = (By.XPATH,"//input[@type='password']")
        #邮箱输入框元素定位
        self.email_input = (By.XPATH,"//*[@id='app']/section/section/main/div/div[3]/div/div[2]/form/div[3]/div/div[1]/input")
        #状态选项元素定位
        self.status_option = (By.XPATH,"//*[@id='app']/section/section/main/div/div[3]/div/div[2]/form/div[4]/div/div/div/input")
        #正常选项元素定位
        self.normal_option = (By.XPATH,"//span[text()='正常']")
        #禁用选项元素定位
        self.forbidden_option = (By.XPATH, "//span[text()='禁用']")