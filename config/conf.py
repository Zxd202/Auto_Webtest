#文件路径
#作者：张旭东
import os


#获取当前项目的绝对路径
current = os.path.abspath(__file__)
#返回到上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(current))

_data_path = BASE_DIR + os.sep + "test_data"
#定义测试数据路径方法
def get_data_path():
    return  _data_path