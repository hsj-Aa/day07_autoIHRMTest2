import logging
import unittest
from api.loginApi import LoginApi
from api.empApi import EmpApi
import app
from utils import assert_utils


class TestEmp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        cls.emp_api = EmpApi()
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test01_login(self):
        # 调用登陆接口
        response = self.login_api.login("13800000002", "123456")
        # 获取token
        token = response.json().get("data")
        # headers
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        # 把获取到的Headers放在全局变量HEADERS中
        app.HEADERS = {"Content-Type": "application/json", "Authorization": "Bearer " + token}

    def test02_add_emp(self):
        # 调用添加员工接口
        respone = self.emp_api.add_emp("乔布斯323123", "15388882323")
        logging.info("添加员工接口返回的值为： {}".format(respone))
        # 需要传入哪些参数？
        # 调用登陆接口，获取token，把token组合成Bearer xxx
        # requests.post(url, json=jsonData, headers=headers)
        assert_utils (self,response, 200, True, 10000, "操作成功")

        #保存员工ID到全局变量（app.py）
        jsonData = respone.json()
        id = jsonData.get("data").get("id")
        #实现保存员工ID到全局变量
        app.ID = id

    def test03_query_emp(self):
        #调用查询员工接口
        response = self.emp_api.query_emp()
        #断言
        assert_utils(self,response,200,True,10000,"操作成功")