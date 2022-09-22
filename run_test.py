#执行所有测试用例文件
#作者：张旭东
import pytest
import os
import time

if __name__ == '__main__':
    pytest.main(['-s',"--alluredir=test_report/result"])
    time.sleep(2)
    os.system("allure generate ./test_report/result -o ./test_report/html  --clean")

