from apiTest.test_weichat.apis.weichat_accesstoken import WeChat_AccessToken
import requests


class WeiChat_Departments(WeChat_AccessToken):
    corpsecret = "vMrcjC8gjHVqTJYTGhEtJvvTQN6gNMxcbZi89nuIJ1k"

    def get_departments(self, id="") -> str:
        '''
        根据ID 获取department的有数据, 如果ID 为空返回所有
        :param id: department ID
        :return: department 的response json
        '''
        departmentUrl = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        token = self.wechat_token(self.corpsecret)
        params = {}
        params["access_token"] = token[self.corpsecret]
        params["id"] = id
        r = requests.get(departmentUrl, params=params)
        json_data = r.json()
        # self.format(r)
        return json_data

    def add_department(self, new_company_data) -> str:
        '''
        新增department
        :param new_company_data: 新department的数据, 词典类型
        :return: 调用接口返回的response
        '''

        add_department_URL = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        token = self.wechat_token(self.corpsecret)
        r = requests.post(add_department_URL, params={"access_token": token[self.corpsecret]}, json=new_company_data)
        # print(r.json())
        return r.json()

    def update_departments(self, update_data) -> str:
        '''
        更新通讯录
        :param update_data: 需要更新的数据
        :return: update 接口返回的response JSON
        '''
        update_department_URL = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        token = self.wechat_token(self.corpsecret)

        r = requests.post(update_department_URL,
                          params={"access_token": token[self.corpsecret]},
                          json=update_data)
        return r.json()

    def delete_departments(self, id) -> str:
        '''
        删除指定ID department
        :param id: 指定的department ID
        :return:
        '''
        delete_department_URL = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        token = self.wechat_token(self.corpsecret)
        params_data = {}
        params_data["access_token"] = token[self.corpsecret]
        params_data["id"] = id

        r = requests.get(delete_department_URL, params=params_data)

        return r.json()
