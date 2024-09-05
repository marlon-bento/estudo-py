from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'musics', views.MusicList,basename='music')

#127.0.0.1:8000/api/v1/
urlpatterns = [
   
    path('', include(router.urls)),
  
] 

