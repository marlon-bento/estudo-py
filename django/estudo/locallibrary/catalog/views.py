
import datetime
from django.shortcuts import render
from django.views import generic
# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewBookForm
from django.db.models import RestrictedError


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


@permission_required('catalog.i_am_librarian')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 3
   
    
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
    



class AuthorCreate(PermissionRequiredMixin, CreateView):
    permission_required = "catalog.i_am_librarian"
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = "catalog.i_am_librarian"
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "catalog.i_am_librarian"
    model = Author
    success_url = reverse_lazy('authors')
    def form_valid(self, form):
        try:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except RestrictedError:
            return HttpResponseRedirect(reverse('author-has-book') )
def author_has_book(request):  
    error_message = "Author já possui livro registrado, e não pode ser exclúido."   
    redirect = reverse_lazy('authors')
    context = {
        'error_message': error_message,
        'redirect': redirect,
    }
   
    return render(request, 'error.html', context= context )