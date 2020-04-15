from apiTest.test_weichat.apis.weichat_accesstoken import WeChat_AccessToken


class TestGetToken:
    corpsecret = "vMrcjC8gjHVqTJYTGhEtJvvTQN6gNMxcbZi89nuIJ1k"

    @classmethod
    def setup_class(cls) -> str:
        token = WeChat_AccessToken.wechat_token(cls.corpsecret)
        return token

    def test_newToken(self):
        response = WeChat_AccessToken.get_access_token(self.corpsecret)
        # print(response["access_token"])
        assert response["errcode"] == 0

    def test_exist_token(self):
        response = WeChat_AccessToken.wechat_token(self.corpsecret)
        # print(response[self.corpsecret])
        assert self.corpsecret in response.keys()
