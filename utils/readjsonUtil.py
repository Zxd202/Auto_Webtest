#封装读取json文件，json文件中字段的方法
#作者：张旭东
import json


class ReadJson:
    #读取json文件
    def read_json_file(self,file_name):
        if file_name == None:
            file_path = ""
        else:
            file_path = file_name
        try:
            with open(file_path,encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception:
            print("未找到json文件")
            return {}

    #读取json文件里具体的字段值
    def get_json_value(self,key,file_name):
        if file_name == None:
            return ""
        else:
            with open(file_name,mode='r',encoding='utf-8') as f:
                jsonData=json.load(f)
        if key == None:
            getJsonValue = ""
        else:
            getJsonValue = jsonData.get(key)
        return getJsonValue



