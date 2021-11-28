import time

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from hotel.models import HotelRooms, RoomPhoto


# User = get_user_model()


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info', verbose_name='用户')
    nickname = models.CharField(max_length=20, null=True, blank=True, verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    unionid = models.CharField(max_length=100, null=True, blank=True, verbose_name='钉钉unionid')
    openId = models.CharField(max_length=100, null=True, blank=True, verbose_name='钉钉openid')
    email = models.CharField(max_length=20, null=True, blank=True, verbose_name='邮箱')
    avatar = models.CharField(max_length=200, null=True, blank=True, verbose_name='头像')
    errcode = models.IntegerField(null=True, blank=True, verbose_name='错误码')
    sys_level = models.IntegerField(null=True, blank=True, verbose_name='系统级别')
    is_sys = models.BooleanField(null=True, blank=True, verbose_name='是否系统用户')
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='姓名')
    deviceId = models.CharField(max_length=100, null=True, blank=True, verbose_name='设备id')
    userid = models.CharField(max_length=100, null=True, blank=True, verbose_name='用户id')
    errmsg = models.CharField(max_length=200, null=True, blank=True, verbose_name='错误信息')
    managerUserid = models.CharField(max_length=20, null=True, blank=True, verbose_name='管理员用户id')
    hiredDate = models.DateField(null=True, blank=True, verbose_name='入职日期')
    tel = models.CharField(max_length=20, null=True, blank=True, verbose_name='座机')
    remark = models.CharField(max_length=200, null=True, blank=True, verbose_name='备注')
    workPlace = models.CharField(max_length=200, null=True, blank=True, verbose_name='工作地点')
    position = models.CharField(max_length=200, null=True, blank=True, verbose_name='职位')
    mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name='手机')
    stateCode = models.CharField(max_length=20, null=True, blank=True, verbose_name='工作状态')
    orgEmail = models.CharField(max_length=100, null=True, blank=True, verbose_name='组织邮箱')
    isSenior = models.BooleanField(null=True, blank=True, verbose_name='是否高级')
    jobnumber = models.CharField(max_length=100, null=True, blank=True, verbose_name='工号')
    active = models.BooleanField(default=True, verbose_name='是否激活')
    extattr = models.CharField(max_length=200, null=True, blank=True, verbose_name='扩展属性')
    unionEmpExt = models.JSONField(null=True, blank=True, verbose_name='联合管理员扩展属性')
    exclusiveAccount = models.BooleanField(default=False, null=True, blank=True, verbose_name='独立账号')
    roles = models.JSONField(max_length=200, null=True, blank=True, verbose_name='角色')
    isLeaderInDepts = models.CharField(max_length=200, null=True, blank=True, verbose_name='是否为组织主管')
    isBoss = models.BooleanField(null=True, blank=True, verbose_name='是否为老板', default=False)
    department = models.JSONField(max_length=200, null=True, blank=True, verbose_name='部门')
    orderInDepts = models.CharField(max_length=200, null=True, blank=True, verbose_name='部门中的排序')
    isAdmin = models.BooleanField(null=True, blank=True, verbose_name='是否为管理员', default=False)
    tags = models.JSONField(max_length=200, null=True, blank=True, verbose_name='标签')
    isHide = models.BooleanField(null=True, blank=True, verbose_name='是否隐藏', default=False)
    realAuthed = models.BooleanField(null=True, blank=True, verbose_name='是否实名认证', default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        # db_table = 'user_info'


class RoomOrder(models.Model):
    """
    Model for RoomOrder
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order', verbose_name='用户')
    order_id = models.CharField(max_length=128, blank=True, null=True, unique=True, verbose_name='订单号')
    room = models.ForeignKey(HotelRooms, on_delete=models.CASCADE, related_name='room_order',
                             related_query_name='room_order', verbose_name='房间')
    # room picture foreign key
    order_num = models.IntegerField(default=1, verbose_name='订单房间数量')
    user_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='用户名')
    email = models.EmailField(blank=True, null=True, verbose_name='邮箱')
    phone = models.CharField(max_length=128, blank=True, null=True, verbose_name='手机号')
    check_in = models.DateTimeField(verbose_name='入住时间')
    check_out = models.DateTimeField(verbose_name='退房时间')
    is_paid = models.BooleanField(default=False, verbose_name='是否支付')
    is_paid_time = models.DateTimeField(blank=True, null=True, verbose_name='支付时间')
    is_canceled = models.BooleanField(default=False, verbose_name='是否取消')
    is_canceled_time = models.DateTimeField(blank=True, null=True, verbose_name='取消时间')
    is_completed = models.BooleanField(default=False, verbose_name='是否完成')
    is_completed_time = models.DateTimeField(blank=True, null=True, verbose_name='完成时间')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    days = models.IntegerField(default=0, verbose_name='入住天数')
    extra_server = models.CharField(max_length=128, blank=True, null=True, verbose_name='其他服务')
    # 金额
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='总价')

    def __str__(self) -> str:
        return f'{self.user.username}-{self.room.name}'

    def get_days(self) -> int:
        return (self.check_out - self.check_in).days

    # 生成订单号
    def generate_order_id(self) -> str:
        return '{}{}{}'.format(self.user.id, self.room.id, int(time.time() * 1000))

    def save(self, *args, **kwargs) -> None:
        self.days = self.get_days()
        if not self.order_id:
            self.order_id = self.generate_order_id()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '预定房间'
        verbose_name_plural = '预定房间'


class HotelService(models.Model):
    """
    Model for HotelService
    """
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name='服务名称')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='价格')
    description = models.TextField(blank=True, null=True, verbose_name='描述')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # 服务数量
    # num = models.IntegerField(default=0, verbose_name='数量')

    class Meta:
        verbose_name = '酒店服务'
        verbose_name_plural = '酒店服务'

    def __str__(self):
        return f'{self.name}-{self.price}'


class HotleServiceOrder(models.Model):
    """
    Model for HotelService Order
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_service_order', verbose_name='用户')
    order_id = models.CharField(max_length=128, blank=True, null=True, unique=True, verbose_name='订单号')
    service = models.ForeignKey(HotelService, on_delete=models.CASCADE, related_name='service_order',
                                related_query_name='service_order', verbose_name='服务')
    room_order = models.ForeignKey(RoomOrder, on_delete=models.CASCADE, related_name='service_order',
                                   verbose_name='订单')
    order_num = models.IntegerField(default=1, verbose_name='订单服务数量')

    class Meta:
        verbose_name = '酒店服务订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.user}-{self.service}'
