import requests


class Test_WeiChat:
    token_URL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww4d32ffac234f3c2a"
    corpsecret = "vMrcjC8gjHVqTJYTGhEtJvvTQN6gNMxcbZi89nuIJ1k"

    def test_get_accessToken(self):
        r = requests.get(self.token_URL, params={"corpid": self.corpid, "corpsecret": self.corpsecret})
        print(r.json())
        # print(r.json()["access_token"])
        print(r.status_code)

        assert r.status_code == 200
