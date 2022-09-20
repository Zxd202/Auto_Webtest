#文件路径
#作者：张旭东
import os
from utils.parse_yml import YamlReader


#获取当前项目的绝对路径
current = os.path.abspath(__file__)
#返回到上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(current))

_data_path = BASE_DIR + os.sep + "test_data"
_config_path = BASE_DIR + os.sep + "config"
_config_file = _config_path + os.sep + "conf.yml"
_db_conf_file = _config_path + os.sep + "db_conf.yml"
#定义测试数据路径方法
def get_data_path():
    return  _data_path
def get_config_file():
    return _config_file
def get_db_config_file():
    return _db_conf_file

class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()

    #根据db_alias获取该名称下的数据库信息
    def get_db_conf_info(self,db_alias):
        return self.db_config[db_alias]
    # 获取邮件配置相关信息
    def get_email_info(self):
        return self.config["email"]
    def get_url(self):
        return self.config["ipaddress"]

if __name__ == '__main__':
    conf_read = ConfigYaml()
    print(conf_read.get_url())