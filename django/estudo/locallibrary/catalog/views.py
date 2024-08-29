
from django.shortcuts import render
from django.views import generic
# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
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





class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 7
class BookDetailView(generic.DetailView):
    model = Book



class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 7
class AuthorDetailView(generic.DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 7

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    
class AllLoanedBooksListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    permission_required = "catalog.i_am_librarian"
    model = BookInstance
    template_name ='catalog/bookinstance_list_all_borrowed.html'
    paginate_by = 7

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')