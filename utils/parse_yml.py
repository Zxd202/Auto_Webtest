import yaml
import os

#封装读取配置文件yml的类
class ParseYML():
    def parse_yml(file,key):
        f = open(file,encoding='utf-8')
        file_data = f.read()
        res = yaml.load(file_data,Loader=yaml.FullLoader)
        return res.get(key)