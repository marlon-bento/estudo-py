from django.contrib.auth.models import Group, User
from .models import Music
from .serializers import MusicSerializer
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

#curso udemy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions, viewsets, generics

from catalog.models import Book, Author, BookInstance


from .serializers import BookSerializer, BookModelSerializer, AuthorModelSerializer,LoanedBooksByUserListSerializer
from django.shortcuts import get_object_or_404

from django.db.models import RestrictedError

class BookPagination(PageNumberPagination):
    page_size= 7

class Book_api_list(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title') 
    serializer_class = BookModelSerializer
    pagination_class = BookPagination
    permission_classes = [IsAuthenticatedOrReadOnly,]
    http_method_names = ['get', 'head', 'options','patch', 'delete', 'post']


class Author_api_list(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('first_name') 
    serializer_class = AuthorModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    http_method_names = ['get', 'head', 'options','patch', 'delete', 'post']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            # Tenta deletar o autor
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except RestrictedError:
            return Response(
                {"detail": "Este autor possui livros registrados e não pode ser deletado."},
                status=status.HTTP_400_BAD_REQUEST
            )

class LoanedBooksByUserListView(viewsets.ModelViewSet):
    
    serializer_class = LoanedBooksByUserListSerializer
    permission_classes = [IsAuthenticated,]
    http_method_names = ['get', 'head', 'options']
    def get_queryset(self):
        user = self.request.user
        return BookInstance.objects.filter(borrower=user).filter(status='o').order_by('due_back')

# @api_view(http_method_names=['get', 'post'])
# @permission_classes([AllowAny]) 
# def book_api_list(request):
#      if request.method == 'GET':
#          books = Book.objects.all().order_by('title') 
#         #serializer = BookSerializer(instance=books, many=True)  
#          serializer =  BookModelSerializer(instance= books, many= True) 

    
#          return Response(serializer.data)
#      elif request.method == 'POST':
#          serializer = BookModelSerializer(data=request.data)
#          serializer.is_valid(raise_exception=True)

#          serializer.save()
#          return Response(
#              serializer.data,
#              status=status.HTTP_201_CREATED
#          )
        
        
# @api_view(['get', 'patch','delete'])
# @permission_classes([AllowAny]) 
# def book_api_detail(request, pk):
#     book = get_object_or_404(Book , pk = pk)  

#     if request.method == 'GET':
#         serializer = BookModelSerializer(instance=book)  
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = BookModelSerializer(
#             instance=book, 
#             data=request.data,
#             partial=True
#             )  

#         serializer.is_valid(raise_exception=True)

#         serializer.save()
#         return Response(
#             serializer.data
#         )

#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)










# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class MusicList(viewsets.GenericViewSet, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):

#     queryset = Music.objects.all().order_by('title')
#     serializer_class = MusicSerializer
    


