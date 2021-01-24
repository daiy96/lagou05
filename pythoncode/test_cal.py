import pytest
import yaml

from pythoncode.calculator import Calculator

# 打开yaml文件，并获取key值对应列表
with open("data.yml")as f:
    datas=yaml.safe_load(f)
    add_datas=datas["add"]
    sub_datas=datas["sub"]
    mul_datas=datas["mul"]
    div_datas=datas["div"]

# 声明fixture，返回add,sub,mul,div 数据
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

class Test_cal:
    def test_add(self,get_cal,add_datas):
        # 调用add函数,返回的结果保存在result里面
        result = get_cal.add(add_datas[0],add_datas[1])
        # 判断result结果是否等于期望的值
        assert result == add_datas[2]

    def test_sub(self, get_cal, sub_datas):
        # 调用sub函数,返回的结果保存在result里面
        result = get_cal.sub(sub_datas[0], sub_datas[1])
        # 判断result结果是否等于期望的值
        assert result == sub_datas[2]
    def test_mul(self, get_cal, mul_datas):
        # 调用mul函数,返回的结果保存在result里面
        result = get_cal.mul(mul_datas[0], mul_datas[1])
        # 判断result结果是否等于期望的值
        assert result == mul_datas[2]
    def test_div(self, get_cal, div_datas):
        # 调用div函数,返回的结果保存在result里面
        result = get_cal.div(div_datas[0], div_datas[1])
        # 判断result结果是否等于期望的值
        assert result == div_datas[2]