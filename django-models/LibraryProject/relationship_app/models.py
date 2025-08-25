from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser # It used to create extra fields like role, date_of_birth and so on while User moder w/c is the default has fixed fields (first_n, last_n email, username and pw) 
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


class UserProfile(models.Model):
    ROLE_CHOICES=(
        ("admin","Admin"),
        ("librarian" , "Librarian"),
       ( "member" , "Member"),
    )
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=30, choices=ROLE_CHOICES, default="member")
    
    def __str__(self):
        return self.role


    
   