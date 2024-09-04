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
            {
                'title': 'Attack on Titan',
                'author': 'Hajime Isayama',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'In a world on the brink of extinction, humanity’s last survivors live within walled cities to protect themselves from giant humanoid creatures known as Titans, who devour people. The story follows Eren Yeager and his friends as they join the military to fight the Titans after a devastating personal tragedy. As the battle for survival intensifies, dark secrets about the Titans’ origins and humanity’s true enemy begin to unravel.',
                'isbn': '9781612620244'
            },
            {
                'title': 'Bleach',
                'author': 'Tite Kubo',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Ichigo Kurosaki, a high school student, accidentally acquires the powers of a Soul Reaper—beings who guide souls to the afterlife and protect the living from evil spirits known as Hollows. Thrust into a world of supernatural battles, Ichigo must learn to harness his new abilities while protecting his loved ones and uncovering the truth behind his newfound powers.',
                'isbn': '9781591164418'
            },
            {
                'title': 'Naruto',
                'author': 'Masashi Kishimoto',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Naruto Uzumaki is a young ninja with dreams of gaining the recognition of his peers and becoming the Hokage, the leader of his village. Born with the Nine-Tailed Fox, a powerful demon, sealed inside him, Naruto faces prejudice and loneliness but remains determined to achieve his goals. Along the way, he forms powerful bonds, faces dangerous enemies, and discovers the true meaning of strength and friendship.',
                'isbn': '9781569319000'
            },
            {
                'title': 'One Piece',
                'author': 'Eiichiro Oda',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Monkey D. Luffy, a young pirate with the ability to stretch his body like rubber after eating a mysterious Devil Fruit, sets out on an epic quest to find the legendary treasure known as the One Piece. His goal is to become the Pirate King. Along the way, he forms a diverse crew of misfits, battles dangerous enemies, and uncovers the mysteries of the world’s oceans.',
                'isbn': '9781591160571'
            },
            {
                'title': 'Dragon Ball',
                'author': 'Akira Toriyama',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Goku, a young boy with extraordinary strength and a monkey-like tail, embarks on a quest to find the seven Dragon Balls, mystical orbs that can summon a dragon to grant any wish. Along the way, Goku makes lifelong friends, battles powerful foes, and discovers his true origins as he strives to protect the Earth from various threats.',
                'isbn': '9781569319208'
            },
            {
                'title': 'Hunter x Hunter',
                'author': 'Yoshihiro Togashi',
                'genres': ['Adventure', 'Drama'],
                'summary': 'Gon Freecss, a young boy living on Whale Island, discovers that his long-lost father, Ging, is a legendary Hunter—an elite member of humanity capable of tracking down secret treasures, rare beasts, or even other individuals. Determined to follow in his father’s footsteps, Gon leaves his home to take the rigorous Hunter Exam, making friends and encountering dangerous adversaries along the way as he seeks to understand why his father left him behind.',
                'isbn': '9781421514680'
            },
            {
                'title': 'Sailor Moon',
                'author': 'Naoko Takeuchi',
                'genres': ['Fantasy', 'Romance'],
                'summary': 'Usagi Tsukino, an ordinary teenage girl, discovers that she is the reincarnation of a moon princess destined to protect Earth from dark forces. With the help of her fellow Sailor Guardians, magical warriors who represent different celestial bodies, Usagi transforms into Sailor Moon and embarks on a journey to find the legendary Silver Crystal and save the world from evil.',
                'isbn': '9781892213011'
            },
            {
                'title': 'Berserk',
                'author': 'Kentaro Miura',
                'genres': ['Fantasy', 'Drama'],
                'summary': 'Guts, a lone mercenary with a tragic past, embarks on a brutal quest for vengeance against the demonic forces that have cursed him. Wielding a massive sword, he battles his way through a dark, medieval world filled with horror and betrayal. As he seeks revenge against his former friend turned mortal enemy, Guts struggles to maintain his humanity while facing the unrelenting darkness around him.',
                'isbn': '9781593070229'
            },
            {
                'title': 'Fushigi Yugi',
                'author': 'Yuu Watase',
                'genres': ['Fantasy', 'Romance'],
                'summary': 'Miaka Yūki, an ordinary high school girl, is transported into an ancient Chinese novel called "The Universe of the Four Gods" where she must become the priestess of Suzaku, one of the four gods, to save the kingdom of Konan. Along with her best friend Yui, who is also pulled into the book, Miaka must navigate dangerous trials, romantic entanglements, and betrayals to fulfill her destiny and find her way back home.',
                'isbn': '9781591161196'
            },
            {
                'title': 'Cardcaptor Sakura',
                'author': 'CLAMP',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Sakura Kinomoto, a young girl, accidentally releases a set of magical cards known as Clow Cards from a mysterious book. Each card has a unique ability, and it is Sakura’s responsibility to retrieve them before they cause harm. With the help of her friends and the guardian beast Keroberos, Sakura must capture all the cards and learn to harness their powers, all while balancing her everyday life as a schoolgirl.',
                'isbn': '9781892213974'
            },
            {
                'title': 'Inuyasha',
                'author': 'Rumiko Takahashi',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Kagome Higurashi, a modern-day schoolgirl, is transported back in time to Japan’s feudal era where she meets Inuyasha, a half-demon searching for the powerful Shikon Jewel. Together, they must gather the shattered pieces of the jewel before it falls into the hands of evil demons and other malevolent forces. Along the way, they encounter various allies and enemies, and Kagome discovers her own spiritual powers.',
                'isbn': '9781591160571'
            },
            {
                'title': 'Death Note',
                'author': 'Tsugumi Ohba',
                'genres': ['Mystery', 'Drama'],
                'summary': 'Light Yagami, a highly intelligent high school student, stumbles upon a mysterious notebook known as the Death Note. The notebook grants him the power to kill anyone by writing their name in it. Believing he can rid the world of evil, Light begins a campaign to eliminate criminals, but his actions attract the attention of a brilliant detective known only as L, leading to a deadly game of cat and mouse.',
                'isbn': '9781421501680'
            },
            {
                'title': 'Bakuman',
                'author': 'Tsugumi Ohba',
                'genres': ['Drama', 'Romance'],
                'summary': 'Moritaka Mashiro, a talented artist, and Akito Takagi, a gifted writer, team up to create manga with the dream of getting their work serialized in the prestigious Weekly Shōnen Jump magazine. As they navigate the competitive world of manga publishing, they face numerous challenges, including rival creators, editorial decisions, and the pressures of meeting deadlines. Through their journey, they also experience personal growth and romantic relationships.',
                'isbn': '9781421535135'
            },
            {
                'title': 'Akira',
                'author': 'Katsuhiro Otomo',
                'genres': ['Science Fiction', 'Drama'],
                'summary': 'In a dystopian future Tokyo, the government conducts secret experiments on children to develop psychic abilities. When a young biker named Kaneda’s friend Tetsuo gains incredible psychic powers, he becomes the focus of a government conspiracy. As Tetsuo’s powers grow uncontrollably, threatening to destroy the city, Kaneda must stop him while uncovering the truth behind the enigmatic figure known as Akira.',
                'isbn': '9781935429012'
            },
            {
                'title': 'Rurouni Kenshin',
                'author': 'Nobuhiro Watsuki',
                'genres': ['Adventure', 'Romance'],
                'summary': 'Set in the Meiji era of Japan, the story follows Kenshin Himura, a former assassin known as Battosai, who has vowed never to kill again. Now a wandering swordsman, Kenshin uses his reverse-blade sword to protect the innocent and uphold justice. As he tries to atone for his past sins, Kenshin encounters old enemies, new allies, and a romantic interest in Kaoru Kamiya, all while struggling with his inner demons.',
                'isbn': '9781591169208'
            },
            {
                'title': 'Gantz',
                'author': 'Hiroya Oku',
                'genres': ['Science Fiction', 'Adventure'],
                'summary': 'Kei Kurono and Masaru Kato, two high school students, are killed in a train accident but find themselves resurrected in a mysterious room with a black orb known as Gantz. They, along with others who have recently died, are forced to participate in a deadly game where they must hunt down and kill aliens to earn points and the chance to return to their normal lives. As the game progresses, they uncover disturbing truths about their existence and the purpose of Gantz.',
                'isbn': '9781593079710'
            },
            {
                'title': 'Neon Genesis Evangelion',
                'author': 'Yoshiyuki Sadamoto',
                'genres': ['Science Fiction', 'Drama'],
                'summary': 'In a post-apocalyptic world, the remnants of humanity are threatened by mysterious beings known as Angels. To combat this threat, the organization NERV enlists teenagers, including the reluctant Shinji Ikari, to pilot giant bio-mechanical robots called Evangelions. As they fight to protect Earth, the pilots struggle with their own emotional traumas, uncovering dark secrets about the true nature of the Evangelions and the intentions of those in power.',
                'isbn': '9781591164004'
            },
            {
                'title': 'Tokyo Ghoul',
                'author': 'Sui Ishida',
                'genres': ['Fantasy', 'Drama'],
                'summary': 'Ken Kaneki, a shy college student, is attacked by a ghoul, a creature that feeds on human flesh, but survives the encounter after receiving an organ transplant from the ghoul. Now a half-ghoul, Kaneki must adapt to his new life, balancing his human side with his ghoul instincts. As he navigates the dangerous world of ghouls, he discovers the dark and brutal reality of the society he once knew.',
                'isbn': '9781421580364'
            },
            {
                'title': 'Fairy Tail',
                'author': 'Hiro Mashima',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Lucy Heartfilia, a young celestial wizard, joins the Fairy Tail guild, a group of powerful and eccentric wizards known for their destructive tendencies and fierce loyalty to one another. Together with her new friends, including the fire dragon slayer Natsu Dragneel, Lucy embarks on thrilling quests, battles dark forces, and uncovers the mysteries of her own past, all while strengthening the bonds of friendship that define Fairy Tail.',
                'isbn': '9781612622767'
            },
            {
                'title': 'Claymore',
                'author': 'Norihiro Yagi',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'In a world plagued by shape-shifting demons known as Yoma, the only hope lies with the Claymores, female warriors who are part-human, part-Yoma. Clare, a low-ranking Claymore, seeks revenge against the Yoma who killed her loved ones. As she battles powerful enemies and uncovers the truth about the organization that created the Claymores, Clare grapples with her own humanity and the monstrous power within her.',
                'isbn': '9781421506203'
            },
            {
                'title': 'Black Clover',
                'author': 'Yūki Tabata',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'In a world where magic is everything, Asta, a boy born without any magical power, dreams of becoming the Wizard King, the strongest mage in the land. Despite his lack of magic, Asta’s determination and physical prowess make him a formidable fighter. Alongside his rival and adoptive brother Yuno, who is a magical prodigy, Asta embarks on a journey to prove his worth and achieve his dream, facing powerful enemies and uncovering dark secrets along the way.',
                'isbn': '9781421587189'
            },
            {
                'title': 'Blue Exorcist',
                'author': 'Kazue Katō',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Rin Okumura, a teenager who discovers that he is the son of Satan, decides to defy his demonic heritage by becoming an exorcist. Along with his twin brother Yukio, Rin enrolls in True Cross Academy, a school for exorcists, where he learns to control his demonic powers while fighting against the forces of darkness. As Rin struggles with his identity and the expectations of others, he must confront the threat posed by his father and the demons that seek to destroy humanity.',
                'isbn': '9781421540320'
            },
            {
                'title': 'Fullmetal Alchemist',
                'author': 'Hiromu Arakawa',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'After a failed alchemical experiment to bring their mother back to life, brothers Edward and Alphonse Elric pay a heavy price: Edward loses an arm and a leg, and Alphonse’s soul is bound to a suit of armor. The brothers set out on a journey to find the Philosopher’s Stone, a powerful alchemical artifact that could restore their bodies. Along the way, they uncover dark secrets about the government, the military, and the true nature of alchemy itself.',
                'isbn': '9781591169208'
            },
            {
                'title': 'D.Gray-man',
                'author': 'Katsura Hoshino',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'Allen Walker, a young exorcist, joins the Black Order, an organization dedicated to protecting the world from Akuma, demons created from the souls of the dead. With the help of Innocence, a divine substance that grants exorcists their powers, Allen battles the forces of the Millennium Earl, a mysterious figure who seeks to destroy humanity. As Allen struggles with his own cursed past and the darkness within him, he learns the true meaning of sacrifice and the cost of fighting for a just cause.',
                'isbn': '9781421506227'
            },
            {
                'title': 'My Hero Academia',
                'author': 'Kohei Horikoshi',
                'genres': ['Fantasy', 'Adventure'],
                'summary': 'In a world where nearly everyone possesses a superpower known as a Quirk, Izuku Midoriya is one of the few born without one. Despite this, he dreams of becoming a professional hero like his idol, All Might. When All Might recognizes Izuku’s potential, he passes on his own Quirk to the boy, who enrolls in U.A. High School, a prestigious academy for heroes-in-training. Izuku must navigate the challenges of hero training, confront dangerous villains, and discover what it truly means to be a hero.',
                'isbn': '9781421582696'
            },
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