"""
URL configuration for library_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, CustomLoginView, RegisterView, ProfileView, ProfileUpdateView, custom_logout_view, BorrowingHistoryView, AdminDashboardView, TransactionListView, CheckOutView, ReturnBookView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='root'),  
    path('admin/', admin.site.urls),
    path('books/list/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('borrowing-history/', BorrowingHistoryView.as_view(), name='borrowing-history'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('books/<int:pk>/checkout/', CheckOutView.as_view(), name='book-checkout'),
    path('transactions/<int:pk>/return/', ReturnBookView.as_view(), name='book-return'),
]
