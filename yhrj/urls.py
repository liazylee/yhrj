"""yhrj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from hotel.views import HotelViewSet, HotelRoomsViewSet, ServiceViewSet
from user_info.views import obtain_jwt_token, RoomOrderViewSet
from yhrj import settings

router = DefaultRouter()
router.register('hotel_list', HotelViewSet, basename='酒店')
router.register('hotel_room', HotelRoomsViewSet, basename='房间')
router.register('order_hotel', RoomOrderViewSet, basename='酒店订单')
router.register('hotel_server', ServiceViewSet, basename='酒店服务')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hotel/', include(router.urls)),
    path('api/auth/login', obtain_jwt_token),
    # path('docs', include('rest_framework_docs.urls')),
]
schema_view = get_schema_view(
    openapi.Info(

        title="API文档",
        default_version='v1',
        description="Welcome to Carbon_Cloud",
        terms_of_service="",
        contact=openapi.Contact(email="li233111@gmail.com"),
        license=openapi.License(name="mimi科技有限公司"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=urlpatterns
)
if not settings.DEBUG:
    urlpatterns += [path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
                    path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT}), ]

if settings.DEBUG:
    urlpatterns += [
        path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
        path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT}),
        # path(r'^api/v1/swagger', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        # 对测试人员更友好
        path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        # 对开发人员更友好
        path('api/v1/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    ]
