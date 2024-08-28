
from django.shortcuts import render
from django.views import generic
# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

# Pega um valor de sessão baseado na sua chave (ex.:'my_car'), disparando um KeyError se a chave não for encontrada.
#my_car = request.session['my_car']

# Pega o valor da sessão, seta o valor padrão ('mini') se a chave não estiver presente.
#my_car = request.session.get('my_car', 'mini')

# Seta o valor da sessão
#request.session['my_car'] = 'mini'

# Deleta o valor da sessão
#del request.session['my_car']

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()


    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable.
    return render(request, 'index.html', context=context)





class BookListView(generic.ListView):
    model = Book
    paginate_by = 7
class BookDetailView(generic.DetailView):
    model = Book



class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 7
class AuthorDetailView(generic.DetailView):
    model = Author
