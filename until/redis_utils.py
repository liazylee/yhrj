#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/31/21 1:56 PM
# @Author  : liazylee
# @File    : redis_utils.py
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

# 记录酒店房间的库存量
from redis import StrictRedis, ConnectionPool

from yhrj import settings


class ScenenRedis(object):
    def __init__(self):
        if not hasattr(ScenenRedis, 'pool'):
            ScenenRedis.create_pool()
        self._connection = StrictRedis(connection_pool=ScenenRedis.pool)

    @staticmethod
    def create_pool():
        url = settings.CACHES['default']['LOCATION']
        ScenenRedis.pool = ConnectionPool.from_url(
            url=url
        )
    # 一个月的库存
  