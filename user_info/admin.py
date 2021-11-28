from django.contrib import admin

# Register your models here.
from user_info import models
from user_info.models import HotleServiceOrder


@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', ]
    search_fields = ['username', 'email']
    list_per_page = 10
    ordering = ['id']


@admin.register(models.RoomOrder)
class RoomOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_id', 'user', 'check_in', 'check_out', 'is_paid']
    list_per_page = 10
    ordering = ['id']


@admin.register(HotleServiceOrder)
class HotleServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_id', 'service', 'room_order', 'order_num')
