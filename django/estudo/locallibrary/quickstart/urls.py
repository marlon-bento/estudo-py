from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'musics', views.MusicList,basename='music')


#127.0.0.1:8000/api/v1/quickstart/
urlpatterns = [
   
    #todos estudo udemy
    path('books/', 
         views.book_api_list, 
         name = 'books_api' 
         ),
    path('books/<int:pk>', 
         views.book_api_detail, 
         name = 'books_api' 
         ),
    
    path('', include(router.urls)),
] 

