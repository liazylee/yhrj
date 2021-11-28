#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/28/21 10:30 PM
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

from hotel.models import Hotel, HotelRooms, RoomTags, RoomFeatures, RoomPhoto


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelRoomsSerializer(serializers.ModelSerializer):
    rooms_pic = serializers.SerializerMethodField()

    class Meta:
        model = HotelRooms
        fields = ('__all__')
        depth = 1

    def get_rooms_pic(self, obj):
        room_phote_queryset = RoomPhoto.objects.filter(hotel_room_id=obj.id)
        room_phote_serializer = RoomPhotoSerializer(room_phote_queryset, many=True,
                                                    context={'request': self.context['request']})
        return room_phote_serializer.data


class RoomsTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTags
        fields = ('__all__')


class RoomFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFeatures
        fields = ('__all__')


class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = ('__all__')
