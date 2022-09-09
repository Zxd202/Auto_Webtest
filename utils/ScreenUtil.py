#封装截屏的方法
#作者：张旭东
from utils.Driverunit import Driver
import os


driver = Driver.get_driver()
#截图
def insert_img(filename):
    func_path=os.path.dirname(__file__)
    base_dir=os.path.dirname(func_path)

    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/Website')[0]

    filepath=base+'/test_report/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)