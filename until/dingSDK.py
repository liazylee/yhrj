#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/30/21 2:48 PM
# @Author  : liazylee
# @File    : dingSDK.py
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
import dingtalk
from django.core.cache import cache

from yhrj import settings


class DingTalk_SDK:

    def __init__(self, appkey, appsecret):
        self.appsecret = appsecret
        self.appkey = appkey

    def get_access_token(self):
        req = dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
        req.appkey = self.appkey
        req.appsecret = self.appsecret
        try:
            resp = req.getResponse()
            print(
                resp)  # {'errcode': 0, 'access_token': 'b223e03818fd3546879ed707db6dd743', 'errmsg': 'ok', 'expires_in': 7200}
            if resp:
                access_token = resp.get('access_token', '')
                expires_in = resp.get('expires_in', 1)
                if access_token:
                    cache.set('access_token', access_token, expires_in - 10)
                    return access_token
        except Exception as e:
            print(e)
            return None
        # todo 会返回None

    def cache_access_token(self):
        if cache.has_key('access_token'):
            return cache.get('access_token')
        else:
            return self.get_access_token()

    def get_userid(self, code):
        req = dingtalk.api.OapiUserGetuserinfoRequest("https://oapi.dingtalk.com/user/getuserinfo")
        req.code = code
        req.access_token = self.cache_access_token()
        try:
            resp = req.getResponse()
            if resp.get('errmsg') == 'ok':
                userid = resp.get('userid', '')
                return userid
        except Exception as e:
            print(e)

    # def


dingtalk_sdk = DingTalk_SDK(appkey=settings.AppKey, appsecret=settings.AppSecret)
