import pytest
import yaml
import os

yaml_file_path =os.path.dirname(__file__) +"/data.yml"
# 通过os.path.dirname获取/data.yml文件所在目录路径

from pythoncode.calculator import Calculator

# 打开yaml文件，并获取key值对应列表
with open(yaml_file_path)as f:
    datas=yaml.safe_load(f)
    add_datas=datas["add"]
    sub_datas=datas["sub"]
    mul_datas=datas["mul"]
    div_datas=datas["div"]

# 声明fixture，返回add,sub,mul,div 值
@pytest.fixture(scope="module",params=add_datas)
def add_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(scope="module",params=sub_datas)
def sub_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(scope="module",params=mul_datas)
def mul_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

@pytest.fixture(scope="module",params=div_datas)
def div_datas(request):
    print("开始计算")
    data = request.param
    yield data
    print("结束计算")

#获取Calculator对象
@pytest.fixture(scope="class")
def get_cal():
    cal = Calculator()
    return cal
