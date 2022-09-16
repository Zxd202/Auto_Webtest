from page_object.LoginPage import Login_Page_Task
from utils.Driverunit import Driver
import pytest

@pytest.fixture(scope="session",autouse=True)
def start_driver():
    driver = Driver.get_driver()
    loginpage = Login_Page_Task()
    loginpage.login("admin", "123456")
    yield
    driver.quit()