from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics
from .models import Music
from .serializers import MusicSerializer
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

#curso udemy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from catalog.models import Book
from .serializers import BookSerializer, BookModelSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size= 2
class book_api_list(viewsets.ViewSet):
    queryset = Book.objects
    serializer_class = BookSerializer
    pagination_class = BookPagination


@api_view(http_method_names=['get', 'post'])
@permission_classes([AllowAny]) 
def book_api_list(request):
     if request.method == 'GET':
         books = Book.objects.all().order_by('title') 
        #serializer = BookSerializer(instance=books, many=True)  
         serializer =  BookModelSerializer(instance= books, many= True) 

    
         return Response(serializer.data)
     elif request.method == 'POST':
         serializer = BookModelSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)

         serializer.save()
         return Response(
             serializer.data,
             status=status.HTTP_201_CREATED
         )
        
        
@api_view(['get', 'patch','delete'])
@permission_classes([AllowAny]) 
def book_api_detail(request, pk):
    book = get_object_or_404(Book , pk = pk)  

    if request.method == 'GET':
        serializer = BookModelSerializer(instance=book)  
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = BookModelSerializer(
            instance=book, 
            data=request.data,
            partial=True
            )  

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(
            serializer.data
        )

    elif request.method == 'DELETE':
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MusicList(viewsets.GenericViewSet, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):

    queryset = Music.objects.all().order_by('title')
    serializer_class = MusicSerializer
    


