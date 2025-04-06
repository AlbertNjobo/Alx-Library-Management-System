from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def custom_logout_view(request):
    if request.method == 'GET' or request.method == 'POST':
        logout(request)
        return redirect('/login/')

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'

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
