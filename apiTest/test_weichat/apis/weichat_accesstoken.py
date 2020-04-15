import requests
from apiTest.entity.common_tool import Common_Tools


class WeChat_AccessToken():
    """这是一个调用企业微信API 获取tooken的类"""
    token_URL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww4d32ffac234f3c2a"
    corpsecret = None
    token = dict()
    currentTime = ""
    corpsecret_time = None

    @classmethod
    def wechat_token(cls, corpsecret=corpsecret) -> dict:
        '''
        根据传入的corpsercet 生成access token,
        将 corpseret 和 accress_token 生成键值对, 存入 token 词典里面. 如果 token[corpsecret]不存在, 就生成一个.
        :param corpsecret: 特定工具的token
        :return: token [corpsecret: access_token]
        '''
        format_date = Common_Tools()
        if corpsecret not in cls.token.keys():
            cls.token = cls.generate_token_time(corpsecret)
        else:
            # print('corpseret is existing value is: \n ' + cls.token[corpsecret])
            cls.currentTime = format_date.format_date()
            for key in cls.token.keys():
                if corpsecret + "_" in key:
                    cls.corpsecret_time = key
                    break
            if int(cls.currentTime) - int(cls.token[cls.corpsecret_time]) > 20000:
                # 当前时间和存储的 corpsecret_time 相比较, 大于 2小时就 生成新token, 新 token 时间
                print("need generate new token")
                cls.token = cls.generate_token_time(corpsecret)

        return cls.token

    @classmethod
    def get_access_token(cls, corpsecret) -> str:
        '''
        根据传入的corpsercet 生成access token
        :param corpsecret: 特定工具的token
        :return: JSON 格式的response
        '''
        r = requests.get(cls.token_URL, params={"corpid": cls.corpid, "corpsecret": corpsecret})
        return r.json()

    @classmethod
    def generate_token_time(cls, corpsecret):
        format_date = Common_Tools()
        response = cls.get_access_token(corpsecret)
        cls.token[corpsecret] = response["access_token"]
        cls.currentTime = format_date.format_date()
        cls.corpsecret_time = corpsecret + '_' + cls.currentTime
        print(cls.corpsecret_time)
        cls.token[cls.corpsecret_time] = cls.currentTime
        return cls.token
