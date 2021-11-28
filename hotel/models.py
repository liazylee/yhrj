from django.db import models


# Create your models here.

class RoomTags(models.Model):
    """
    RoomTags model
    """
    name = models.CharField(max_length=255, verbose_name='标签')
    description = models.TextField(blank=True, help_text='描述')
    icon = models.ImageField(upload_to='room_tags', blank=True, null=True)
    is_icon = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.icon:
            self.is_icon = True
        super(RoomTags, self).save()

    class Meta:
        verbose_name = '房间标签'
        verbose_name_plural = verbose_name


class RoomFeatures(models.Model):
    """
    RoomFeatures model
    """
    name = models.CharField(max_length=255, verbose_name='特色')
    description = models.TextField(blank=True, help_text='描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '房间特色'
        verbose_name_plural = verbose_name


class Hotel(models.Model):
    """
    Hotel model
    """
    name = models.CharField(max_length=255, verbose_name='酒店名称')
    description = models.TextField(blank=True)
    address = models.TextField(blank=True, verbose_name='地址')
    phone = models.CharField(max_length=255, blank=True, verbose_name='电话')
    email = models.CharField(max_length=255, blank=True, verbose_name='邮箱')
    latitude = models.FloatField(blank=True, null=True, verbose_name='纬度')
    longitude = models.FloatField(blank=True, null=True, verbose_name='经度')
    city = models.CharField(max_length=255, blank=True, verbose_name='城市')
    state = models.CharField(max_length=255, blank=True, verbose_name='省份')
    zipcode = models.CharField(max_length=255, blank=True, verbose_name='邮编')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '酒店'
        verbose_name_plural = verbose_name


class HotelRooms(models.Model):
    """
    Model for HotelRoom
    """
    room_features = models.ManyToManyField(RoomFeatures, blank=True, verbose_name='特色')
    # 可住人数
    max_occupancy = models.IntegerField(default=2, verbose_name='最大入住人数')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=128, )
    description = models.TextField(verbose_name='描述', blank=True, null=True, default='')
    room_tags = models.ManyToManyField(RoomTags, blank=True, related_name='rooms', related_query_name='room')
    # 原价
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='原价')
    # 现价
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='现价')
    # price = models.FloatField(verbose_name='Price per night', default=0.0, blank=True, null=True,
    #                           help_text='Price per night')
    #
    # room_photo = models.ForeignKey('RoomPhoto', on_delete=models.CASCADE, blank=True, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True, help_text='Photo of the room')
    # photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True, help_text='Photo of the room')
    # photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True, help_text='Photo of the room')
    # photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True, help_text='Photo of the room')
    # photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    list_date = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=5, verbose_name='库存', help_text='库存')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '酒店房间'
        verbose_name_plural = '酒店房间'


class RoomPhoto(models.Model):
    """
    Model for HotelRoomPhotos
    """
    hotel_room = models.ForeignKey(HotelRooms, on_delete=models.CASCADE)
    caption = models.CharField(max_length=128, blank=True, verbose_name='标题')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_main = models.BooleanField(default=False, verbose_name='是否为主图')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    list_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = '酒店房间照片'
        verbose_name_plural = '酒店房间照片'

# 客服服务
