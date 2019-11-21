import requests
import app


class EmpApi:

    def __init__(self):
        self.add_emp_url = "http://182.92.81.159/api/sys/user"
        self.headers = app.HEADERS
        # self.headers = {"Content-Type":"application/json", "Authorization":"Bearer "}
        pass

    def add_emp(self, username, mobile):
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-11-01",
            "formOfEmployment": 1,
            "workNumber": "33333222",
            "departmentName": "测试部",
            "correctionTime": "2019-11-18T16:00:00.000Z"
        }
        print("self.HEADERS", app.HEADERS)
        return requests.post(self.add_emp_url, json=jsonData, headers=headers)

    def query_emp(self):
        headers = app.HEADERS
        id = app.ID
        url = self.query_emp_url +"/" + id
        print("查询员工的url为：{}".format(url))
        return requests.get(url,headers=headers)
