from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, LibraryUser, Transaction
from .serializers import BookSerializer, LibraryUserSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['copies_available']
    search_fields = ['title', 'author', 'isbn']

    @action(detail=True, methods=['post'])
    def check_out(self, request, pk=None):
        book = self.get_object()
        user = request.user.libraryuser

        if book.copies_available < 1:
            return Response({"error": "No copies available."}, status=status.HTTP_400_BAD_REQUEST)

        if Transaction.objects.filter(user=user, book=book, return_date__isnull=True).exists():
            return Response({"error": "You have already checked out this book."}, status=status.HTTP_400_BAD_REQUEST)

        Transaction.objects.create(user=user, book=book)
        book.copies_available -= 1
        book.save()

        return Response({"message": "Book checked out successfully."}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        book = self.get_object()
        user = request.user.libraryuser

        transaction = Transaction.objects.filter(user=user, book=book, return_date__isnull=True).first()
        if not transaction:
            return Response({"error": "No active transaction found for this book."}, status=status.HTTP_400_BAD_REQUEST)

        transaction.return_date = timezone.now()
        transaction.save()

        book.copies_available += 1
        book.save()

        return Response({"message": "Book returned successfully."}, status=status.HTTP_200_OK)

class LibraryUserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer
