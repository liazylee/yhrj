#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/30/21 2:28 PM
# @Author  : liazylee
# @File    : helper.py
# @Software: PyCharm

# code is far away from bugs with the god animal protecting
""" I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""
import json

import requests
from alibabacloud_dingtalk.oauth2_1_0 import models as dingtalkoauth_2__1__0_models
from alibabacloud_dingtalk.oauth2_1_0.client import Client as dingtalkoauth2_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from django.core.cache import cache

from dingtalk import AppKeyClient
from dingtalk.client.api import User as DingTalkUser
from yhrj import settings

client = AppKeyClient(settings.CorpId, settings.AppKey, settings.AppSecret)


class DingTalkAcessToken(object):
    def __init__(self, app_key, app_secret):
        self.app_key = app_key
        self.app_secret = app_secret
        self.client = DingTalkAcessToken.create_client()
        self.get_access_token_request = dingtalkoauth_2__1__0_models.GetAccessTokenRequest(
            app_key=app_key,
            app_secret=app_secret
        )

    def get_access_token(self):
        if cache.get('access_token'):
            return cache.get('access_token')
        resp = self.client.get_access_token(self.get_access_token_request)
        if resp:
            resp = resp.body
            access_token = getattr(resp, 'access_token', '')
            expires_in = getattr(resp, 'expires_in', 1)
            if access_token:
                cache.set('access_token', access_token, expires_in - 10)
                return access_token

    @staticmethod
    def create_client() -> dingtalkoauth2_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkoauth2_1_0Client(config)


class DingTalkClient(object):

    def get_user_id(self, code) -> dict:
        user_id_info = DingTalkUser(client=client).getuserinfo(code=code)
        return user_id_info

    def get_user_info(self, user_id) -> dict:
        user_info = DingTalkUser(client=client).get(user_id)
        return user_info


ding_talk_client = DingTalkClient()


# 钉钉机器人
class DingTalkRobot(object):

    def __init__(self, access_token):
        self.access_token = access_token

    def send_text(self, content):
        url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(self.access_token)
        data = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            # "at": {
            #     "atMobiles": [
            #         "13588888888"
            #     ],
            "isAtAll": True
        }

        headers = {'Content-Type': 'application/json; charset=utf-8'}
        try:
            response = requests.post(url=url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(e)
            return None


ding_talk_robot = DingTalkRobot(access_token=settings.DingTalkRobotAccessToken)
