from django.core.management.base import BaseCommand
from catalog.models import Book, Author, Genre, BookInstance
import uuid
from datetime import date, timedelta
import random
from django.contrib.auth.models import User
# Rodar esse comando para popular o bd ./manage.py populate_db
class Command(BaseCommand):
    help = 'Popula o banco de dados com autores, livros e gêneros'

    def handle(self, *args, **kwargs):
        genres = {
            'Fantasy': Genre.objects.get_or_create(name='Fantasy')[0],
            'Adventure': Genre.objects.get_or_create(name='Adventure')[0],
            'Drama': Genre.objects.get_or_create(name='Drama')[0],
            'Science Fiction': Genre.objects.get_or_create(name='Science Fiction')[0],
            'Mystery': Genre.objects.get_or_create(name='Mystery')[0],
            'Romance': Genre.objects.get_or_create(name='Romance')[0],
        }

        authors = {
            'Hajime Isayama': Author.objects.get_or_create(first_name='Hajime', last_name='Isayama', date_of_birth='1986-08-29')[0],
            'Tite Kubo': Author.objects.get_or_create(first_name='Tite', last_name='Kubo', date_of_birth='1977-06-26')[0],
            'Masashi Kishimoto': Author.objects.get_or_create(first_name='Masashi', last_name='Kishimoto', date_of_birth='1974-11-08')[0],
            'Eiichiro Oda': Author.objects.get_or_create(first_name='Eiichiro', last_name='Oda', date_of_birth='1975-01-01')[0],
            'Akira Toriyama': Author.objects.get_or_create(first_name='Akira', last_name='Toriyama', date_of_birth='1955-04-05')[0],
            'Yoshihiro Togashi': Author.objects.get_or_create(first_name='Yoshihiro', last_name='Togashi', date_of_birth='1966-04-27')[0],
            'Naoko Takeuchi': Author.objects.get_or_create(first_name='Naoko', last_name='Takeuchi', date_of_birth='1967-03-15')[0],
            'Kentaro Miura': Author.objects.get_or_create(first_name='Kentaro', last_name='Miura', date_of_birth='1966-07-11')[0],
            'Yuu Watase': Author.objects.get_or_create(first_name='Yuu', last_name='Watase', date_of_birth='1970-03-05')[0],
            'CLAMP': Author.objects.get_or_create(first_name='CLAMP', last_name='(Group)', date_of_birth='1970-03-05')[0],
            'Rumiko Takahashi': Author.objects.get_or_create(first_name='Rumiko', last_name='Takahashi', date_of_birth='1957-10-10')[0],
            'Tsugumi Ohba': Author.objects.get_or_create(first_name='Tsugumi', last_name='Ohba', date_of_birth='1970-03-05')[0],
            'Takeshi Obata': Author.objects.get_or_create(first_name='Takeshi', last_name='Obata', date_of_birth='1969-02-11')[0],
            'Katsuhiro Otomo': Author.objects.get_or_create(first_name='Katsuhiro', last_name='Otomo', date_of_birth='1954-04-14')[0],
            'Nobuhiro Watsuki': Author.objects.get_or_create(first_name='Nobuhiro', last_name='Watsuki', date_of_birth='1970-05-26')[0],
            'Hiroya Oku': Author.objects.get_or_create(first_name='Hiroya', last_name='Oku', date_of_birth='1967-09-16')[0],
            'Yoshiyuki Sadamoto': Author.objects.get_or_create(first_name='Yoshiyuki', last_name='Sadamoto', date_of_birth='1962-01-29')[0],
            'Sui Ishida': Author.objects.get_or_create(first_name='Sui', last_name='Ishida', date_of_birth='1970-03-05')[0],
            'Hiro Mashima': Author.objects.get_or_create(first_name='Hiro', last_name='Mashima', date_of_birth='1977-05-03')[0],
            'Norihiro Yagi': Author.objects.get_or_create(first_name='Norihiro', last_name='Yagi', date_of_birth='1968-06-06')[0],
            'Yūki Tabata': Author.objects.get_or_create(first_name='Yūki', last_name='Tabata', date_of_birth='1970-03-05')[0],
            'Kazue Katō': Author.objects.get_or_create(first_name='Kazue', last_name='Katō', date_of_birth='1980-07-20')[0],
            'Hiromu Arakawa': Author.objects.get_or_create(first_name='Hiromu', last_name='Arakawa', date_of_birth='1973-05-08')[0],
            'Katsura Hoshino': Author.objects.get_or_create(first_name='Katsura', last_name='Hoshino', date_of_birth='1980-04-21')[0],
            'Kohei Horikoshi': Author.objects.get_or_create(first_name='Kohei', last_name='Horikoshi', date_of_birth='1986-11-20')[0],
        }

        books = [
            {'title': 'Attack on Titan', 'author': 'Hajime Isayama', 'genres': ['Fantasy', 'Adventure'], 'summary': 'Humanity fights for survival against giant humanoid creatures.', 'isbn': '9781612620244'},
            {'title': 'Bleach', 'author': 'Tite Kubo', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A high school student becomes a Soul Reaper and battles evil spirits.', 'isbn': '9781591164418'},
            {'title': 'Naruto', 'author': 'Masashi Kishimoto', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A young ninja seeks recognition from his peers and dreams of becoming the Hokage.', 'isbn': '9781569319000'},
            {'title': 'One Piece', 'author': 'Eiichiro Oda', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A pirate embarks on a quest to find the One Piece and become the Pirate King.', 'isbn': '9781591160571'},
            {'title': 'Dragon Ball', 'author': 'Akira Toriyama', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A young boy with extraordinary strength searches for the Dragon Balls.', 'isbn': '9781569319208'},
            {'title': 'Hunter x Hunter', 'author': 'Yoshihiro Togashi', 'genres': ['Adventure', 'Drama'], 'summary': 'A young boy becomes a Hunter to find his father.', 'isbn': '9781421514680'},
            {'title': 'Sailor Moon', 'author': 'Naoko Takeuchi', 'genres': ['Fantasy', 'Romance'], 'summary': 'A teenage girl transforms into the magical warrior Sailor Moon to save the world.', 'isbn': '9781892213011'},
            {'title': 'Berserk', 'author': 'Kentaro Miura', 'genres': ['Fantasy', 'Drama'], 'summary': 'A lone swordsman battles demons and seeks revenge.', 'isbn': '9781593070229'},
            {'title': 'Fushigi Yugi', 'author': 'Yuu Watase', 'genres': ['Fantasy', 'Romance'], 'summary': 'A girl is transported into a mysterious book where she must become a priestess.', 'isbn': '9781591161196'},
            {'title': 'Cardcaptor Sakura', 'author': 'CLAMP', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A young girl must capture magical cards to prevent disaster.', 'isbn': '9781892213974'},
            {'title': 'Inuyasha', 'author': 'Rumiko Takahashi', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A girl travels back in time and teams up with a half-demon to collect magical shards.', 'isbn': '9781591160571'},
            {'title': 'Death Note', 'author': 'Tsugumi Ohba', 'genres': ['Mystery', 'Drama'], 'summary': 'A student discovers a notebook that allows him to kill anyone by writing their name.', 'isbn': '9781421501680'},
            {'title': 'Bakuman', 'author': 'Tsugumi Ohba', 'genres': ['Drama', 'Romance'], 'summary': 'Two students team up to create manga and achieve their dreams.', 'isbn': '9781421535135'},
            {'title': 'Akira', 'author': 'Katsuhiro Otomo', 'genres': ['Science Fiction', 'Drama'], 'summary': 'In a dystopian future, a young biker gains incredible psychic powers.', 'isbn': '9781935429012'},
            {'title': 'Rurouni Kenshin', 'author': 'Nobuhiro Watsuki', 'genres': ['Adventure', 'Romance'], 'summary': 'A wandering samurai with a dark past protects the innocent in Meiji-era Japan.', 'isbn': '9781591169208'},
            {'title': 'Gantz', 'author': 'Hiroya Oku', 'genres': ['Science Fiction', 'Adventure'], 'summary': 'Two students are resurrected by a mysterious black orb and forced to participate in a deadly game.', 'isbn': '9781593079710'},
            {'title': 'Neon Genesis Evangelion', 'author': 'Yoshiyuki Sadamoto', 'genres': ['Science Fiction', 'Drama'], 'summary': 'Teenagers pilot giant robots to protect Earth from mysterious beings.', 'isbn': '9781591164004'},
            {'title': 'Tokyo Ghoul', 'author': 'Sui Ishida', 'genres': ['Fantasy', 'Drama'], 'summary': 'A college student becomes a half-ghoul and must navigate his new life as a monster.', 'isbn': '9781421580364'},
            {'title': 'Fairy Tail', 'author': 'Hiro Mashima', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A young wizard joins a powerful guild and goes on epic quests with her new friends.', 'isbn': '9781612622767'},
            {'title': 'Claymore', 'author': 'Norihiro Yagi', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A group of female warriors battle against shape-shifting demons.', 'isbn': '9781421506203'},
            {'title': 'Black Clover', 'author': 'Yūki Tabata', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A boy born without magic power dreams of becoming the Wizard King.', 'isbn': '9781421587189'},
            {'title': 'Blue Exorcist', 'author': 'Kazue Katō', 'genres': ['Fantasy', 'Adventure'], 'summary': 'The son of Satan enrolls in an exorcist school to fight demons.', 'isbn': '9781421540320'},
            {'title': 'Fullmetal Alchemist', 'author': 'Hiromu Arakawa', 'genres': ['Fantasy', 'Adventure'], 'summary': 'Two brothers use alchemy to search for the Philosopher’s Stone.', 'isbn': '9781591169208'},
            {'title': 'D.Gray-man', 'author': 'Katsura Hoshino', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A young exorcist battles dark forces to save the world.', 'isbn': '9781421506227'},
            {'title': 'My Hero Academia', 'author': 'Kohei Horikoshi', 'genres': ['Fantasy', 'Adventure'], 'summary': 'A boy born without superpowers enrolls in a hero academy to become a professional hero.', 'isbn': '9781421582696'},
        ]

        for book in books:
            book_obj = Book.objects.create(
                title=book['title'],
                author=authors[book['author']],
                summary=book['summary'],
                isbn=book['isbn']
            )
            book_obj.genre.add(*[genres[genre] for genre in book['genres']])

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))


        for book in books:
            book_obj = Book.objects.get(title=book['title'])
            
            num = random.randrange(0, 3)
            
            if num == 0:
                try:
                    user = User.objects.get(username='adm')
                except User.DoesNotExist:
                    raise ValueError("Usuário 'adm' não encontrado.")
            elif num == 1:
                try:
                    user = User.objects.get(username='bib')
                except User.DoesNotExist:
                    raise ValueError("Usuário 'adm' não encontrado.")
            else:
                try:
                    user = User.objects.get(username='marlon157')
                except User.DoesNotExist:
                    raise ValueError("Usuário 'adm' não encontrado.")
            num = random.randrange(-10, 31)
            # Primeira instância
            BookInstance.objects.create(

                id=uuid.uuid4(),
                book=book_obj,
                imprint='Imprint 1',

                borrower=user,
                due_back=date.today() + timedelta(num),
                status='o'
            )
            
            # Segunda instância
            BookInstance.objects.create(
                id=uuid.uuid4(),
                book=book_obj,
                imprint='Imprint 2',
                due_back=date.today() + timedelta(days=60),
                status='a'
            )

        self.stdout.write(self.style.SUCCESS('Instâncias de livros criadas com sucesso!'))