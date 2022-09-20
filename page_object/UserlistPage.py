#用户列表相关元素定位
#作者：张旭东
from selenium.webdriver.common.by import By
from utils.Driverunit import Driver
from time import sleep

class User_Add_Page_Locator(object):
    """用户列表-添加用户"""
    def __init__(self):
        self.driver = Driver.get_driver()
        #用户管理导航栏元素定位
        self.banner = (By.XPATH,"//i[@class='el-icon-user-solid']/following-sibling::span")
        #用户列表元素定位
        self.user_list = (By.XPATH,"//li[@class='el-submenu is-opened']/ul/li/span")
        #添加用户按钮元素定位
        self.add_user = (By.XPATH,"//span[text()='添加用户']")
        #用户名输入框元素定位
        self.new_user = (By.XPATH,"//label[@for='username']/following-sibling::div/div/input")
        #密码输入框元素定位
        self.password = (By.XPATH,"//input[@type='password']")
        #邮箱输入框元素定位
        self.email = (By.XPATH,"//label[@for='email']/following-sibling::div/div/input")
        #状态选项元素定位
        self.status = (By.XPATH,"//div[@class='el-select']/div/input")
        #正常选项元素定位
        self.normal = (By.XPATH,"//span[text()='正常']")
        #禁用选项元素定位
        self.forbidden = (By.XPATH, "//span[text()='禁用']")
        #添加用户弹框-确定按钮元素定位
        self.confirm = (By.XPATH,"//div[@aria-label='添加分类']/div[3]/span/button[2]/span")
        #添加用户弹框-取消按钮元素定位
        self.cancel = (By.XPATH,"//div[@aria-label='添加分类']/div[3]/span/button[1]/span")
        #添加用户成功提示信息元素定位
        self.user_succee = (By.XPATH,"//p[text()='添加用户成功']")

    def user_add_banner(self):
        return self.driver.find_element(self.banner[0],self.banner[1])
    def user_add_userlist(self):
        return self.driver.find_element(self.user_list[0],self.user_list[1])
    def user_add_user(self):
        return self.driver.find_element(self.add_user[0],self.add_user[1])
    def user_new_user(self):
        return self.driver.find_element(self.new_user[0],self.new_user[1])
    def user_password(self):
        return self.driver.find_element(self.password[0],self.password[1])
    def user_email(self):
        return self.driver.find_element(self.email[0],self.email[1])
    def user_status(self):
        return self.driver.find_element(self.status[0],self.status[1])
    def user_normal(self):
        return self.driver.find_element(self.normal[0],self.normal[1])
    def user_forbidden(self):
        return self.driver.find_element(self.forbidden[0],self.forbidden[1])
    def user_confirm(self):
        return self.driver.find_element(self.confirm[0],self.confirm[1])
    def user_cancel(self):
        return self.driver.find_element(self.cancel[0],self.cancel[1])
    def user_add_succee(self):
        return self.driver.find_element(self.user_succee[0],self.user_succee[1])


class User_Add_Page_Handle(object):
    """用户列表页，添加用户操作"""
    def __init__(self):
        self.user_add_page_locator = User_Add_Page_Locator()
    #点击用户管理
    def user_add_click_banner(self):
        self.user_add_page_locator.user_add_banner().click()
    #点击用户列表
    def user_add_click_userlist(self):
        self.user_add_page_locator.user_add_userlist().click()
    #点击添加用户按钮
    def user_add_click_button(self):
        self.user_add_page_locator.user_add_user().click()
    #输入用户名
    def user_add_input_usename(self,username):
        self.user_add_page_locator.user_new_user().clear()
        self.user_add_page_locator.user_new_user().send_keys(username)
    #输入密码
    def user_add_input_password(self,password):
        self.user_add_page_locator.user_password().clear()
        self.user_add_page_locator.user_password().send_keys(password)
    #输入邮箱
    def user_add_input_email(self,email):
        self.user_add_page_locator.user_email().clear()
        self.user_add_page_locator.user_email().send_keys(email)
    #点击状态选项
    def user_add_click_status(self):
        self.user_add_page_locator.user_status().click()
    #选择正常选项
    def user_add_choice_normal(self):
        self.user_add_page_locator.user_normal().click()
    #选择禁用选项
    def user_add_choice_forbidden(self):
        self.user_add_page_locator.user_forbidden().click()
    #点击弹框的确定按钮
    def user_add_click_confirm(self):
        self.user_add_page_locator.user_confirm().click()
    #点击弹框的取消按钮
    def user_add_click_cancel(self):
        self.user_add_page_locator.user_cancel().click()

class User_Add_Page_Task(object):
    """用户管理列表，添加用户业务"""
    def __init__(self):
        self.user_add_task = User_Add_Page_Handle()
    def user_add(self,username,password,email):
        self.user_add_task.user_add_click_banner()
        sleep(2)
        self.user_add_task.user_add_click_userlist()
        sleep(2)
        self.user_add_task.user_add_click_button()
        sleep(2)
        self.user_add_task.user_add_input_usename(username)
        sleep(2)
        self.user_add_task.user_add_input_password(password)
        sleep(2)
        self.user_add_task.user_add_input_email(email)
        sleep(2)
        self.user_add_task.user_add_click_confirm()
        sleep(2)


