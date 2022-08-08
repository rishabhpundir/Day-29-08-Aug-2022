from django.urls import path, include
from apiapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('singers', views.SingerViewset, basename='singers')
router.register('songs', views.SongViewset, basename='songs')

urlpatterns = [
    path('', include(router.urls)),
    path('get_token', obtain_auth_token),
]
