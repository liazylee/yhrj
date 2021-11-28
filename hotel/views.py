# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from hotel.models import Hotel, HotelRooms
from hotel.serializers import HotelSerializer, HotelRoomsSerializer
from user_info.models import HotelService
from user_info.serializers import HotelServiceSerializers


class HotelViewSet(ReadOnlyModelViewSet):
    """
    酒店接口
    经纬度，位置，联系电话
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [AllowAny]


class HotelRoomsViewSet(ReadOnlyModelViewSet):
    """
    酒店房间接口
    """
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomsSerializer
    permission_classes = [AllowAny]


# 客服服务接口只读
class ServiceViewSet(ReadOnlyModelViewSet):
    serializer_class = HotelServiceSerializers
    queryset = HotelService.objects.all()
    permission_classes = [AllowAny]
