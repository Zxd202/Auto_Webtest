#封装yaml读取方法封装
#作者：张旭东
import os
import yaml


class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None

    #单个文档读取
    def data(self):
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data = yaml.safe_load(f)
        return self._data

    # 多个文档读取
    def data_all(self):
        if not self._data_all:
            with open(self.yamlf, "rb") as f:
               self._data_all = list(yaml.safe_load_all(f))
        return self._data_all