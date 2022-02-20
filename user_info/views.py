# Create your views here.
import logging
import uuid

from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView

from user_info.helper import ding_talk_client
from user_info.models import UserInfo, RoomOrder
from user_info.serializers import RoomOrderSerializers, CreateRoomOrderSerializers

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()


class Serializer(serializers.Serializer):
    @property
    def object(self):
        return self.validated_data


class JSONWechatTokenSerializer(Serializer):
    """
    通过小程序post请求发送code, 经JSONWechatTokenSerializer验证后返回
    openid和session_key.
    使用用户标识openid生成一个user实例, 方便视图对用户权限的管理.
    """

    def __init__(self, *args, **kwargs):
        super(JSONWechatTokenSerializer, self).__init__(*args, **kwargs)
        self.fields['code'] = serializers.CharField()

    @property
    def username_field(self):
        return get_username_field()

    @staticmethod
    def _get_or_create_user(userid):
        try:
            user = User.objects.get(username=userid)
            return user
        except Exception as e:
            print(e)
            user = User.objects.create(username=userid, password=uuid.uuid4())
            return user

    def validate(self, attrs):
        code = attrs.get('code')
        # print(code,'code')
        userid = ding_talk_client.get_user_id(code)
        # userid = {'errcode': 0, 'sys_level': 2, 'is_sys': True, 'name': '李珍义', 'errmsg': 'ok',
        #           'deviceId': 'da8c9a9fde68bb19c0ea642208721930', 'userid': '01080703585126353642'}
        # if userid
        if userid:
            user = self._get_or_create_user(userid['userid'])
            # userinfo = ding_talk_client.get_user_info(userid['userid'])
            # print(userinfo, 'userinfo')
            # user_info = json.dumps(userid)
            # print(user_info, 'userinfo')
            # user_info = json.loads(userid)
            try:
                _user_info = UserInfo.objects.filter(user=user)
                logging.info(_user_info, '_user_info')
                if _user_info.exists():
                    logging.info('userinfo exists')
                    _user_info.update(**userid)
                else:
                    logging.info('userinfo not exists')
                    UserInfo.objects.create(user=user, **userid)
            except Exception as e:
                # pprint(locals())  # 打出当前函数变量
                import traceback
                traceback.print_exc()
                print(e)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "code" ')
            # msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


class ObtainJSONWebToken(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWechatTokenSerializer


obtain_jwt_token = ObtainJSONWebToken.as_view()


class RoomOrderViewSet(viewsets.ModelViewSet):
    """
    客房订单
    """
    queryset = RoomOrder.objects.all()
    serializer_class = RoomOrderSerializers

    def get_queryset(self) -> QuerySet:
        if self.action == 'list':
            return RoomOrder.objects.filter(user=self.request.user)
        return RoomOrder.objects.filter()

    # change get_serializer_class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateRoomOrderSerializers
        return RoomOrderSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# def hello_world(request):
#     # for django users
#     data = request.dict()
#     # for rest_framework users
#     data = request.data
#
#     signature = data.pop("sign")
#
#     # verification
#     success = alipay.verify(data, signature)
#     if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
#         print("trade succeed")
#     return 'Hello, World!'
