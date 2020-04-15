import pytest
import json
from apiTest.test_weichat.apis.weiChat_departments import WeiChat_Departments


class TestDepartment():

    @classmethod
    def setup_class(cls):
        cls.departments = WeiChat_Departments()

    gets_data_ids = [(3, "广州研发中心update", "update"), (2, "name", "for new test"), (0, 'order', 100000000),
                     ('sss', "order", 111)]

    @pytest.mark.parametrize("data_id,checkParam,exceptValue", gets_data_ids)
    def test_get_departments(self, data_id, checkParam, exceptValue):
        r = self.departments.get_departments(data_id)
        print(r)
        # r = json.dumps(r, indent=2)
        # print(r)
        assert r['errmsg'] == "ok"
        for i in range(0, len(r['department'])):
            if r['department'][i][checkParam] == exceptValue:
                assert True
                break
            assert False

    add_data = [("", ""), ("广州研发中心4", "2")]

    @pytest.mark.parametrize("name,parentid", add_data)
    def test_add_department(self, name, parentid):
        new_company_data = {
            "name": name,
            "parentid": parentid
        }
        r = self.departments.add_department(new_company_data)
        print(r)
        assert r["errmsg"] == "created"

    update_date = [(3, '3 test update'), (4, '4 test update'), ("0", 'test update')]

    @pytest.mark.parametrize("id,name", update_date)
    def test_update_department(self, id, name):
        update_data = {
            "id": id,
            "name": name
        }
        r = self.departments.update_departments(update_data)
        print(r)
        assert r["errmsg"] == "updated"

    @pytest.mark.parametrize("id", [4])
    def test_delete_department(self, id):
        id = id
        r = self.departments.delete_departments(id)
        assert r["errmsg"] == "deleted"
