from django.urls import path, include
from apiapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singers', views.SingerViewset, basename='singers')
router.register('songs', views.SongViewset, basename='songs')

urlpatterns = [
    path('', include(router.urls)),
]
