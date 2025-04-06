from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, LibraryUser
from .serializers import BookSerializer, LibraryUserSerializer

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LibraryUserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer
