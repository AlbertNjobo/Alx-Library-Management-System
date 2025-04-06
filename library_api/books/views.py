from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from .models import Book, Transaction
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

@login_required
def custom_logout_view(request):
    if request.method == 'GET' or request.method == 'POST':
        logout(request)
        return redirect('/login/')

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    paginate_by = 6  # Display 6 books per page

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(isbn__icontains=query)
            )
        available = self.request.GET.get('available')
        if available == '1':
            queryset = queryset.filter(copies_available__gt=0)
        return queryset

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'isbn', 'published_date', 'copies_available']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'isbn', 'published_date', 'copies_available']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

class CustomLoginView(LoginView):
    template_name = 'books/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'books/logout.html'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class RegisterView(FormView):
    template_name = 'books/register.html'
    form_class = UserCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'books/profile.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'books/profile_update.html'
    success_url = '/profile/'

    def get_object(self):
        return self.request.user

class BorrowingHistoryView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'books/borrowing_history.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        library_user = self.request.user.libraryuser  # Get the associated LibraryUser instance
        return Transaction.objects.filter(user=library_user).order_by('-check_out_date')

@method_decorator(staff_member_required, name='dispatch')
class AdminDashboardView(TemplateView):
    template_name = 'books/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_count'] = Book.objects.count()
        context['user_count'] = User.objects.count()
        context['transaction_count'] = Transaction.objects.count()
        return context

@method_decorator(staff_member_required, name='dispatch')
class TransactionListView(TemplateView):
    template_name = 'books/transaction_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.all().order_by('-check_out_date')
        return context

class CheckOutView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        if book.copies_available > 0:
            library_user = request.user.libraryuser
            Transaction.objects.create(user=library_user, book=book)
            book.copies_available -= 1
            book.save()
            return HttpResponseRedirect(reverse('borrowing-history'))
        return HttpResponseRedirect(reverse('book-detail', args=[pk]))

class ReturnBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        transaction = Transaction.objects.get(pk=pk, user=request.user.libraryuser, return_date__isnull=True)
        transaction.return_date = timezone.now()
        transaction.save()

        book = transaction.book
        book.copies_available += 1
        book.save()

        return HttpResponseRedirect(reverse('borrowing-history'))
