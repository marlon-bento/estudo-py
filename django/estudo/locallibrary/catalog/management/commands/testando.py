from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from catalog.models import Book, BookInstance
class Command(BaseCommand):
    help = 'Comando para teste'

    def handle(self, *args, **options):
        # Step 1: Obter o usuário "adm"
        try:
            user = User.objects.get(username='adm')
        except User.DoesNotExist:
            raise ValueError("Usuário 'adm' não encontrado.")

        # Step 2: Obter o livro "Naruto"
        try:
            book = Book.objects.get(title='Naruto')
        except Book.DoesNotExist:
            raise ValueError("Livro 'Naruto' não encontrado.")

        # Step 3: Criar uma nova instância de BookInstance
        book_instance = BookInstance.objects.create(
            book=book,
            imprint='First Edition',
            borrower=user,
            status='o'  
        )

        # Agora `book_instance` foi criado e salvo no banco de dados.
        print(f'BookInstance criado: {book_instance}')
