from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser # It used to create extra fields like role, date_of_birth and so on while User moder w/c is the default has fixed fields (first_n, last_n email, username and pw) 

from django.conf import settings

# settings.AUTH_USER_MODEL
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name




class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


# class UserProfile(models.Model):
#     ROLE_CHOICES=(
#         ("admin","Admin"),
#         ("librarian" , "Librarian"),
#        ( "member" , "Member"),
#     )
#     user= models.OneToOneField(User, on_delete=models.CASCADE)
#     role=models.CharField(max_length=30, choices=ROLE_CHOICES, default="member")
    
#     def __str__(self):
#         return self.role


# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be ser")
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user    
   
# # Create normal and super users

# def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self.create_user(username, email, password, **extra_fields)
# class CustomUser(AbstractUser):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     date_of_birth = models.DateField()
#     profile_photo = models.ImageField()
#     objects = UserManager()

#     def __str__(self):
#         return self.user