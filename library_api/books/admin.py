from django.contrib import admin
from .models import Book, LibraryUser, Transaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'copies_available')
    search_fields = ('title', 'author', 'isbn')

@admin.register(LibraryUser)
class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_membership', 'is_active')
    search_fields = ('user__username', 'user__email')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'check_out_date', 'return_date')
    search_fields = ('user__user__username', 'book__title')
