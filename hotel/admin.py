from django.contrib import admin

# Register your models here.
from hotel.models import (Hotel, RoomFeatures, RoomTags, HotelRooms, RoomPhoto)
# 修改admin界面的默认样式
from user_info.models import HotelService

admin.site.site_header = '运河人家酒店管理系统'
admin.site.site_title = '运河人家酒店管理系统'
admin.site.index_title = '运河人家酒店管理系统'


class RoomPhotoModelInline(admin.StackedInline):
    model = RoomPhoto
    extra = 4
    # exclude = ('caption', 'photo', 'is_main', 'is_published', 'create_datetime')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zipcode',)


# @admin.register(RoomPhoto)
# class RoomPhotoAdmin(admin.ModelAdmin):
#     list_display = ('hotel_room', 'photo',)
#     list_filter = ('hotel_room', 'photo',)
#     search_fields = ('hotel_room', 'photo',)


@admin.register(RoomFeatures)
class RoomFeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(RoomTags)
class RoomTagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('name', 'description',)
    search_fields = ('name', 'description',)
    exclude = ('is_icon',)


@admin.register(HotelRooms)
class HotelRoomsAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'original_price', 'price', 'name', 'description',)
    inlines = [RoomPhotoModelInline, ]


@admin.register(HotelService)
class HotelServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('name', 'description',)
    search_fields = ('name', 'description',)
