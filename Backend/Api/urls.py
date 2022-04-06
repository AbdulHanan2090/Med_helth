from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from .views import Contactviewset,Login
from .views import Customerviewset,Otp,Check
router=DefaultRouter()
router.register('Contact',Contactviewset,basename='Contact')
router.register('Customer',Customerviewset,basename='Customer')

# http://192.168.1.16/api/Otp/+923090389688/1122
urlpatterns = [
    path('api/',include(router.urls)),
    path('api/Login/<str:data>/<str:password>', Login.as_view(), name='Login'),
    path('api/Otp/<str:data>/<int:otp>', Otp.as_view(), name='Otp'),
    path('api/Check/<str:data>', Check.as_view(), name='Check'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
