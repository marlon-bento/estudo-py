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

@api_view(http_method_names=['get', 'post'])
@permission_classes([AllowAny]) 
def book_api_list(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('title') 
        #serializer = BookSerializer(instance=books, many=True)  
        serializer =  BookModelSerializer(instance= books, many= True) 

    
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookModelSerializer(data =request.data)
        if serializer.is_valid():
            return Response(
                {'criei aqui maluco'}, 

                status = status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status = status.HTTP_400_BD_REQUEST)
@api_view()
@permission_classes([AllowAny]) 
def book_api_detail(request, pk):
    book = get_object_or_404(Book , pk = pk)  
    serializer = BookSerializer(instance=book)  
    return Response(serializer.data)

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
    


