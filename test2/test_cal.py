import pytest


class Test_cal:
    @pytest.mark.run(order=1)
    # 设置案例执行顺序
    def test_add(self,get_cal,add_datas):
        # 调用add函数,返回的结果保存在result里面
        result = get_cal.add(add_datas[0],add_datas[1])
        # 判断result结果是否等于期望的值
        assert result == add_datas[2]

    @pytest.mark.run(order=4)
    def test_div(self, get_cal, div_datas):
        # 调用div函数,返回的结果保存在result里面
        result = get_cal.div(div_datas[0], div_datas[1])
        # 判断result结果是否等于期望的值
        assert result == div_datas[2]

    @pytest.mark.run(order=2)
    def test_sub(self, get_cal, sub_datas):
        # 调用sub函数,返回的结果保存在result里面
        result = get_cal.sub(sub_datas[0], sub_datas[1])
        # 判断result结果是否等于期望的值
        assert result == sub_datas[2]

    @pytest.mark.run(order=3)
    def test_mul(self, get_cal, mul_datas):
        # 调用mul函数,返回的结果保存在result里面
        result = get_cal.mul(mul_datas[0], mul_datas[1])
        # 判断result结果是否等于期望的值
        assert result == mul_datas[2]
# D:\test_pytest\lagou05\test2\test_cal.py