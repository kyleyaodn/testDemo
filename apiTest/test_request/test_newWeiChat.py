import requests
import json


class Test_WeiChat():
    token_URL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww4d32ffac234f3c2a"
    corpsecret = "vMrcjC8gjHVqTJYTGhEtJvvTQN6gNMxcbZi89nuIJ1k"

    @classmethod
    def get_access_token(cls) -> str:
        '''获取access token'''
        r = requests.get(cls.token_URL, params={"corpid": cls.corpid, "corpsecret": cls.corpsecret})
        # print(r.json()["access_token"])
        return r.json()["access_token"]

    def test_get_departments(self):
        departmentUrl = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        accessToken = self.get_access_token()
        r = requests.get(departmentUrl, params={"access_token": accessToken})
        json_data = r.json()

        print(json.dumps(json_data, indent=4))

        assert r.status_code == 200

    def test_add_departments(self):
        '''新增通讯录'''
        '''坑: API通讯录同步助手未开启, 需要设置打开'''
        add_department_URL = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        access_token = self.get_access_token()
        new_company_data = {
            "name": "广州研发中心",
            "parentid": 1
        }
        r = requests.post(add_department_URL, params={"access_token": access_token}, json=new_company_data)

        print(r)
        print(r.json())
        assert r.json()["errmsg"] == "created"

    def test_update_departments(self):
        '''更新通讯录'''
        update_department_URL = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        access_token = self.get_access_token()
        update_data = {
            "id": 3,
            "name": "广州研发中心"
        }
        r = requests.post(update_department_URL,
                          params={"access_token": access_token},
                          json=update_data)
        assert r.json()["errmsg"] == "updated"

    def test_delete_departments(self):
        '''删除指定ID department'''
        delete_department_URL = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        access_token = self.get_access_token()
        params_data = {
            "access_token": access_token,
            "id": 3
        }

        r = requests.get(delete_department_URL, params=params_data)

        assert r.json()["errmsg"] == "deleted"
