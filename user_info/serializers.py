#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/31/21 11:16 AM
# @Author  : liazylee
# @File    : serializers.py
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

from rest_framework import serializers

from user_info.models import UserInfo, RoomOrder, HotelService, HotleServiceOrder


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class RoomOrderSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RoomOrder
        fields = '__all__'
        depth = 1
        # read_only_fields = fields


class CreateRoomOrderSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RoomOrder
        fields = (
            'user', 'room', 'user_name', 'phone', 'check_in', 'check_out', 'extra_server', 'total_price', 'order_num')

    # 验证数据
    def validate(self, attrs):
        # 判断入住日期是否大于当前日期
        # if attrs['check_in'] < datetime.now().date():
        #     raise serializers.ValidationError('入住日期不能小于当前日期')
        # 退房日期不能小于入住日期
        # if attrs['check_out'] < attrs['check_in']:
        #     raise serializers.ValidationError('退房日期不能小于入住日期')
        return attrs


# def validated_data(self):
#     # 确定每天的房间数量
#     # room_num = self.validated_data['room'].stock
#     # 判断入住期间库存是否足够
#     # if room_num < self.validated_data['order_num']:
#     #     raise serializers.ValidationError('库存不足')
#     # 判断日期是否大于当前日期
#     if self.data['check_in'] < datetime.now().date():
#         raise serializers.ValidationError("入住日期不能小于当前日期")
#     if self.data['check_out'] < self.data['check_in']:
#         raise serializers.ValidationError("退房日期不能小于入住日期")
#     # 返回数据
#     return self.data
class HotelServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelService
        fields = '__all__'
        # read_only_fields = fields


class HotelServiceOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotleServiceOrder
        fields = '__all__'
