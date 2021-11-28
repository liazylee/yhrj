#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/31/21 10:53 AM
# @Author  : liazylee
# @File    : signals.py
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

# @receiver(post_save, sender=User)
# def create_user_info(sender, instance, created, **kwargs):
#     from user_info.models import UserInfo
#     user_id = instance.username
#     user_info = ding_talk_client.get_user_info(user_id)
#     if created:
#         UserInfo.objects.create(user=instance, **user_info)
#     else:
#         UserInfo.objects.get(user_id=user_id).update(**user_info)
from django.db.models.signals import post_save
from django.dispatch import receiver

from user_info.helper import ding_talk_robot
from user_info.models import RoomOrder


@receiver(post_save, sender=RoomOrder)
def transfer_room_order(sender, instance, created, **kwargs):
    if created:
        message = f'订单编号：{instance.order_id},客户姓名是{instance.user_name},手机号是{instance.phone}，房间为{instance.room.name},' \
                  f'房间数量{instance.order_num}间，入住时间为{instance.check_in.strftime("%Y-%m-%d")},' \
                  f'离开时间为{instance.check_out.strftime("%Y-%m-%d")},总入住天数为{instance.days}晚，期间需要的服务是{instance.extra_server}，总价{instance.total_price}'
        ding_talk_robot.send_text(message)
        print('created')
    else:
        print('updated')
