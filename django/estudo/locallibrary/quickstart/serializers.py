from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Music
from catalog.models import Genre
from catalog.models import Author
from catalog.models import Book


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'




class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title' , 'author_id', 'author_name', 'summary', 'isbn', 'genres']
        
    author_id = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all(),
    )

    author_name = serializers.StringRelatedField( source = 'author')
    
    genres = GenreSerializer(
        many = True,
        source = 'genre'
    )

#fazendo na mão
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    #author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    
    #author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    
    #author_complete_name = serializers.SerializerMethodField()
    
    author_id = serializers.PrimaryKeyRelatedField(
        queryset = Author.objects.all(),
    )

    author_name = serializers.StringRelatedField( source = 'author')

    #author_complete_name = serializers.CharField(source ='author')
    #author = serializers.StringRelatedField()

    summary = serializers.CharField(max_length=1000)
    isbn = serializers.CharField(max_length=13)

    #retorna os generos com os nomes mas pode mudar o slug para id por exemplo
    """genre = serializers.SlugRelatedField(
        many=True,
        slug_field='name',  # Exibe o nome dos gêneros
        queryset=Genre.objects.all()
    )"""

    #retorna os ids dos generos
    """genre = serializers.PrimaryKeyRelatedField(
        queryset = Genre.objects.all(),
        many=True,
        
    )"""
    #retorna os generos que defini para serializar id e name
    genres = GenreSerializer(
        many = True,
        source = 'genre'
    )

    def get_author_complete_name(self, book):
        return f'{book.author}'