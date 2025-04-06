from django.test import TestCase
from django.contrib.auth.models import User
from .models import LibraryUser

# Create your tests here.

def create_test_user():
    # Create a regular user
    user, created = User.objects.get_or_create(username='test_user', email='test_user@example.com')
    if created:
        user.set_password('password123')
        user.save()
        LibraryUser.objects.get_or_create(user=user)
        print("Test user created successfully.")
    else:
        print("Test user already exists.")
