from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, LibraryUser, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LibraryUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = LibraryUser
        fields = ['id', 'date_of_membership', 'is_active', 'username', 'email', 'password']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        library_user = LibraryUser.objects.create(user=user, **validated_data)
        return library_user

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'