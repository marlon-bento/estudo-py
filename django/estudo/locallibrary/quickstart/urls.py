from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from . import views

from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
router = routers.SimpleRouter()
router.register('books', views.Book_api_list)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'musics', views.MusicList,basename='music')
print(router.urls)


#127.0.0.1:8000/api/v1/quickstart/
urlpatterns = [
   
    #todos estudo udemy
     # path('books/', 
     #      views.book_api_list, 
     #      name = 'books_api' 
     #      ),
     # path('books/<int:pk>', 
     #      views.book_api_detail, 
     #      name = 'books_api' 
     #      ),


     #viewsets
     # path('books/', 
     #      views.Book_api_list.as_view({
     #         'get': 'list',
     #         'post': 'create', 
     #         }), 
     #         name= 'books_api'
     #      ),

     # path('books/<int:pk>', 
     #      views.Book_api_list.as_view({
     #         'get': 'retrieve',
     #         'patch': 'partial_update', 
     #         'delete': 'destroy',
     #     }), 
     #     name= 'books_api_detail'
     #     ),


     #jwt 
     path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
     ),
     path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
     ),
     path(
        'token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
     ),
    
     path('', include(router.urls)),
] 

